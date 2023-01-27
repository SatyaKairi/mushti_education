from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class ClassesManager(models.Manager):
    def get_all_active_Classess(self):
        return Classes.objects.filter(is_active = True)

class Classes(models.Model):
    
    name=models.TextField()
    image=models.ImageField(blank=True,null=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank = True, related_name="modified_Classes_user")
    is_active = models.BooleanField(default=True)
    objects=ClassesManager()
# Urls
    def get_detail_url(self,**kwargs):
        return reverse ('classes:detail_view', kwargs={'id' :self.id})
    def get_update_url(self,**kwargs):
        return reverse ('classes:update_view', kwargs={'id' :self.id})
