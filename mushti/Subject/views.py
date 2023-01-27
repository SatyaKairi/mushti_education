from django.http import Http404

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.db.models import Q
from .forms import *
# Create your views here.

def Subject_create_update_view(request,*args, **kwargs):
    Subject=None
    msg = "Create Subject"
    Subject_id = kwargs.get('id')
    if not Subject_id is None:
        Subject = Subject.objects.get(id=Subject_id)
        msg = "Update Subject"

    form = SubjectCreateForm(request.POST or None,instance=Subject)
    if request.POST:
        if form.is_valid():
            Subject =form.instance
            Subject.user = request.user
            form.save()
            return redirect (form.instance.get_detail_url())             
    context = {
            'form':form,
            'object':Subject,
            'msg':msg

        }      
    return render(request,'Subject/create.html',context)   
def Subject_deactivate_view(request):
    if request.POST:
        id = request.POST.get('Subject_id')
        Subject = Subject.objects.get(id=id)
        Subject.is_active = False
        Subject.modified_by = request.user
        Subject.save()
        return redirect('Subject:list_view')

def Subject_detail_view(request,id,*args, **kwargs):
    subject = get_object_or_404(Subject,id=id,is_active = True)
 
    context ={
        'object':subject,
    }
    
    return render(request,'Subject/detail.html',context)


def Subject_list_view(request,*args, **kwargs):
    q= request.GET.get('q')
    qs = Subject.objects.get_all_active_Subjects()
    if not q is None:
  #TODO: add search Parameters below:
        search_param =  Q(id__icontains =q )| Q( name__icontains = q)
        qs = qs.filter(search_param)
    context ={
        'object_list': qs
    }
    return render(request,'Subject/list.html',context)
