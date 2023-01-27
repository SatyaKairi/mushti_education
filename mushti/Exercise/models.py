from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from Chapter.models import Chapter

class ExerciseManager(models.Manager):
    def get_all_active_Exercises(self):
        return Exercise.objects.filter(is_active = True)

class Exercise(models.Model):
    
    name=models.TextField()
    chapterid=models.ForeignKey(to=Chapter,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank = True, related_name="modified_Exercise_user")
    is_active = models.BooleanField(default=True)
    objects=ExerciseManager()
# Urls
    def get_detail_url(self,**kwargs):
        return reverse ('exercise:detail_view', kwargs={'id' :self.id})
    def get_update_url(self,**kwargs):
        return reverse ('exercise:update_view', kwargs={'id' :self.id})
