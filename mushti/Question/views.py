from django.http import Http404

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.db.models import Q
from .forms import *
# Create your views here.

def Question_create_update_view(request,*args, **kwargs):
    Question=None
    msg = "Create Question"
    Question_id = kwargs.get('id')
    if not Question_id is None:
        Question = Question.objects.get(id=Question_id)
        msg = "Update Question"

    form = QuestionCreateForm(request.POST or None,instance=Question)
    if request.POST:
        if form.is_valid():
            Question =form.instance
            Question.user = request.user
            form.save()
            return redirect (form.instance.get_detail_url())             
    context = {
            'form':form,
            'object':Question,
            'msg':msg

        }      
    return render(request,'Question/create.html',context)   
def Question_deactivate_view(request):
    if request.POST:
        id = request.POST.get('Question_id')
        Question = Question.objects.get(id=id)
        Question.is_active = False
        Question.modified_by = request.user
        Question.save()
        return redirect('Question:list_view')

def Question_detail_view(request,id,*args, **kwargs):
    question = get_object_or_404(Question,id=id,is_active = True)
 
    context ={
        'object':question,
    }
    
    return render(request,'Question/detail.html',context)


def Question_list_view(request,*args, **kwargs):
    q= request.GET.get('q')
    qs = Question.objects.get_all_active_Questions()
    if not q is None:
  #TODO: add search Parameters below:
        search_param =  Q(id__icontains =q )| Q( question__icontains = q)
        qs = qs.filter(search_param)
    context ={
        'object_list': qs
    }
    return render(request,'Question/list.html',context)
