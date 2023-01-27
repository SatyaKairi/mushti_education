from django.http import Http404

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.db.models import Q
from .forms import *
# Create your views here.

def Exercise_create_update_view(request,*args, **kwargs):
    Exercise=None
    msg = "Create Exercise"
    Exercise_id = kwargs.get('id')
    if not Exercise_id is None:
        Exercise = Exercise.objects.get(id=Exercise_id)
        msg = "Update Exercise"

    form = ExerciseCreateForm(request.POST or None,instance=Exercise)
    if request.POST:
        if form.is_valid():
            Exercise =form.instance
            Exercise.user = request.user
            form.save()
            return redirect (form.instance.get_detail_url())             
    context = {
            'form':form,
            'object':Exercise,
            'msg':msg

        }      
    return render(request,'Exercise/create.html',context)   
def Exercise_deactivate_view(request):
    if request.POST:
        id = request.POST.get('Exercise_id')
        Exercise = Exercise.objects.get(id=id)
        Exercise.is_active = False
        Exercise.modified_by = request.user
        Exercise.save()
        return redirect('Exercise:list_view')

def Exercise_detail_view(request,id,*args, **kwargs):
    exercise = get_object_or_404(Exercise,id=id,is_active = True)
 
    context ={
        'object':exercise,
    }
    
    return render(request,'Exercise/detail.html',context)


def Exercise_list_view(request,*args, **kwargs):
    q= request.GET.get('q')
    qs = Exercise.objects.get_all_active_Exercises()
    if not q is None:
  #TODO: add search Parameters below:
        search_param =  Q(id__icontains =q )| Q( name__icontains = q)
        qs = qs.filter(search_param)
    context ={
        'object_list': qs
    }
    return render(request,'Exercise/list.html',context)
