from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quiz_api.serializers import UserSerializer,QuizerSerializer,QuestionSerializer,\
    AnswerSerializer,ExamSerializer,FeedbackSerializer,QuizSerializer

from quiz_api.models import Quizer,Question,Answer,Exam,Feedback,Quiz,QuizTaker
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from django.db.models import Max

class UserViewSet(viewsets.ModelViewSet):
   
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer                                                        



class ExamViewSet(viewsets.ModelViewSet):
    queryset=Exam.objects.all()
    serializer_class=ExamSerializer   

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer


@api_view(['GET', 'POST'])
def quizerUser(request):
    if request.method == 'POST':
        data=request.data
        if Quizer.objects.filter(username=data['username']).exists():
            user=Quizer.objects.filter(username=data['username'])
            serializer = QuizerSerializer(user, many=True)
            return Response(serializer.data)
        
        else:
            serializer = QuizerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@api_view(['GET', 'POST'])
def quiz_question(request):
    if request.method == 'GET':
        data=request.data
        quiz = Quiz.objects.get(id=1)
        
        user=Quizer.objects.get(username='manish')
        quiz_user=QuizTaker.objects.get(user=user,quiz=quiz)
        if int(quiz_user.question_attemted)<=20:
            question=Question.objects.filter(quiz=quiz,difficulty=1)
            serializer = QuestionSerializer(question[0])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def easy_question(request):
    if request.method == 'POST':
        data=request.data
        quiz = Quiz.objects.get(id=data['items']['id'])
        user=Quizer.objects.get(username=data['username'])
        if Answer.objects.filter(user=user,quiz=quiz).exists():
            anss=Answer.objects.filter(user=user,quiz=quiz)
            que_idx=anss[0].level_1+1
            question=Question.objects.filter(quiz=quiz,difficulty=1)
            ans=Answer.objects.filter(user=user,quiz=quiz).update(level_1=que_idx)
            serializer = QuestionSerializer(question[que_idx-1])
            return Response(serializer.data)
            
        else:
            a=Answer.objects.create(user=user,quiz=quiz,level_1=0,level_2=0,level_3=0)
            a.save()
            anss=Answer.objects.filter(user=user,quiz=quiz)
            que_idx=anss[0].level_1+1
            question=Question.objects.filter(quiz=quiz,difficulty=1)
            ans=Answer.objects.filter(user=user,quiz=quiz).update(level_1=que_idx)
            serializer = QuestionSerializer(question[que_idx-1])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def medium_question(request):
    if request.method == 'POST':
        data=request.data
        quiz = Quiz.objects.get(id=data['items']['id'])
        user=Quizer.objects.get(username=data['username'])
        if Answer.objects.filter(user=user,quiz=quiz).exists():
            anss=Answer.objects.filter(user=user,quiz=quiz)
            que_idx=anss[0].level_2+1
            question=Question.objects.filter(quiz=quiz,difficulty=2)
            ans=Answer.objects.filter(user=user,quiz=quiz).update(level_2=que_idx)
            serializer = QuestionSerializer(question[que_idx-1])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'POST'])
def hard_question(request):
    if request.method == 'POST':
        data=request.data
        quiz = Quiz.objects.get(id=data['items']['id'])
        user=Quizer.objects.get(username=data['username'])
        if Answer.objects.filter(user=user,quiz=quiz).exists():
            anss=Answer.objects.filter(user=user,quiz=quiz)
            que_idx=anss[0].level_3+1
            question=Question.objects.filter(quiz=quiz,difficulty=3)
            ans=Answer.objects.filter(user=user,quiz=quiz).update(level_3=que_idx)
            serializer = QuestionSerializer(question[que_idx-1])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def save_answer(request):
    if request.method == 'POST':
        data=request.data
        user=Quizer.objects.get(username=data['username'])
       
        quiz=Quiz.objects.get(id=data['items']['id'])
        if QuizTaker.objects.filter(user=user,quiz=quiz).exists():
            QuizTaker.objects.filter(user=user,quiz=quiz).update(score=data['marks'])
            return Response(status=status.HTTP_201_CREATED)
        else:
            q=QuizTaker.objects.create(user=user,quiz=quiz,score=data['marks'],question_attemted=1,completed=False)
            q.save()
            return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def feedback(request):
    if request.method == 'POST':
        data=request.data
        print(data)
        user=Quizer.objects.get(username=data['items']['username'])
        q=Feedback.objects.create(username=user,name=data['items']['Name'],email=data['items']['email'],subject=data['items']['subject'],messages=data['items']['message'])
        q.save()
        ans=Answer.objects.filter(user=user)
        ans.delete()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)   