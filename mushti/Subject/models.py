from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from Classes.models import Classes


class SubjectManager(models.Manager):
    def get_all_active_Subjects(self):
        return Subject.objects.filter(is_active=True)


class Subject(models.Model):

    name = models.TextField(max_length=100)
    session = models.TextField(max_length=50)
    classid = models.ForeignKey(Classes, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="modified_Subject_user")
    is_active = models.BooleanField(default=True)
    objects = SubjectManager()
# Urls

    def __str__(self):
        return self.name

    def get_detail_url(self, **kwargs):
        return reverse('subject:detail_view', kwargs={'id': self.id})

    def get_update_url(self, **kwargs):
        return reverse('subject:update_view', kwargs={'id': self.id})
    