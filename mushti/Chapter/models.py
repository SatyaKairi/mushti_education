from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from Subject.models import Subject
class ChapterManager(models.Manager):
    def get_all_active_Chapters(self):
        return Chapter.objects.filter(is_active = True)

class Chapter(models.Model):
    
    name=models.TextField()
    subjectid=models.ForeignKey(to=Subject,on_delete=models.CASCADE)
    content=models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank = True, related_name="modified_Chapter_user")
    is_active = models.BooleanField(default=True)
    objects=ChapterManager()
# Urls
    def get_detail_url(self,**kwargs):
        return reverse ('chapter:detail_view', kwargs={'id' :self.id})
    def get_update_url(self,**kwargs):
        return reverse ('chapter:update_view', kwargs={'id' :self.id})
