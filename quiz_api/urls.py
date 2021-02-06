
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers

from quiz_api import views



router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

router.register('question', views.QuestionViewSet)
router.register('exam', views.ExamViewSet)

router.register('Quiz', views.QuizViewSet)
 
urlpatterns = [
        path('', include(router.urls)),
        path('quizer/',views.quizerUser,name="quizer"),
        path('quiz_question/',views.quiz_question,name="quiz_question"),
        path('easy_question/',views.easy_question,name="easy_question"),
        path('medium_question/',views.medium_question,name="medium_question"),
        path('hard_question/',views.hard_question,name="hard_question"),
        path('save_answer/',views.save_answer,name="save_answer"),
        path('feedback/',views.feedback,name="feedback"),
       # path('section/',views.section,name="section"),
]