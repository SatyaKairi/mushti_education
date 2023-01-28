from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from Exercise.models import Exercise

class QuestionManager(models.Manager):
    def get_all_active_Questions(self):
        return Question.objects.filter(is_active = True)

class Question(models.Model):
    
    question=models.TextField()
    question_image = models.ImageField(null=True,blank=True)
    option1=models.CharField(max_length=200, null=True, blank = True)
    option2=models.CharField(max_length=200, null=True, blank = True)
    option3=models.CharField(max_length=200, null=True, blank = True)
    option4=models.CharField(max_length=200, null=True, blank = True)
    answer=models.TextField()
    answer_image = models.ImageField(null=True, blank=True)
    
    ExerciseID = models.ForeignKey(to=Exercise,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank = True, related_name="modified_Question_user")
    is_active = models.BooleanField(default=True)
    objects=QuestionManager()
# Urls
    def get_detail_url(self,**kwargs):
        return reverse ('question:detail_view', kwargs={'id' :self.id})
    def get_update_url(self,**kwargs):
        return reverse ('question:update_view', kwargs={'id' :self.id})
