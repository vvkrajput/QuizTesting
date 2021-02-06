from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.db.models import Q


from . import models

@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
	search_fields = ['author', 'title']
	list_display=['id', 'title', 'author', 'created_at']
	list_filter = ['author']

class QuizQuestionFilter(admin.SimpleListFilter):
	title = 'quiz'
	parameter_name = 'quiz'

	def lookups(self, request, model_admin): # create clickable links on right hand side 
		quizzes = models.Quiz.objects.all()
		lookups = ()
		for quiz in quizzes:
			lookups += ((quiz.title, quiz.title),)
		return lookups

	def queryset(self, request, queryset): # return all the ojbects that fit parameter that we set
		if self.value(): # why is self.value() containing the year?
			quiz_title = self.value()
			return queryset.filter(Q(quiz__title=quiz_title))

@admin.register(models.Question)
class QuestionAdmin(ImportExportModelAdmin):
    
	fields = [
		'questions',
		'quiz',
		'option1',
		'option2',
		'option3',
		'option4',
		'correct_option',
		'difficulty'
	]
	list_display=['id', 'questions', 'quiz','option1','option2','option3','option4','correct_option','difficulty']
	list_filter=[QuizQuestionFilter, 'difficulty']
	search_fields=['quiz', 'title']





class AnswerQuestionFilter(admin.SimpleListFilter):
	title = 'quiz'
	parameter_name = 'quiz'

	def lookups(self, request, model_admin): # create clickable links on right hand side 
		quizzes = models.Quiz.objects.all()
		lookups = ()
		for quiz in quizzes:
			lookups += ((quiz.title, quiz.title),)
		return lookups

	def queryset(self, request, queryset): # return all the ojbects that fit parameter that we set
		if self.value(): # why is self.value() containing the year?
			quiz_title = self.value()
			return queryset.filter(Q(question__quiz__title=quiz_title))


@admin.register(models.Quizer)
class QuizerAdmin(admin.ModelAdmin):
	list_display=['username','password']
	
@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
	list_display=['exam','section1','section2','section3']

@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
	list_display=['username','name','email','subject','messages']

@admin.register(models.QuizTaker)
class QuizTakerAdmin(admin.ModelAdmin):
    list_display=['user', 'quiz','score','completed','date_finished']
    list_filter = ['user','quiz','completed']

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display=['user','quiz','level_1','level_2','level_3']

