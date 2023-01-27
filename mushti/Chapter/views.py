from django.http import Http404

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.db.models import Q
from .forms import *
# Create your views here.

def Chapter_create_update_view(request,*args, **kwargs):
    Chapter=None
    msg = "Create Chapter"
    Chapter_id = kwargs.get('id')
    if not Chapter_id is None:
        Chapter = Chapter.objects.get(id=Chapter_id)
        msg = "Update Chapter"

    form = ChapterCreateForm(request.POST or None,instance=Chapter)
    if request.POST:
        if form.is_valid():
            Chapter =form.instance
            Chapter.user = request.user
            form.save()
            return redirect (form.instance.get_detail_url())             
    context = {
            'form':form,
            'object':Chapter,
            'msg':msg

        }      
    return render(request,'Chapter/create.html',context)   
def Chapter_deactivate_view(request):
    if request.POST:
        id = request.POST.get('Chapter_id')
        Chapter = Chapter.objects.get(id=id)
        Chapter.is_active = False
        Chapter.modified_by = request.user
        Chapter.save()
        return redirect('Chapter:list_view')

def Chapter_detail_view(request,id,*args, **kwargs):
    chapter = get_object_or_404(Chapter,id=id,is_active = True)
 
    context ={
        'object':chapter,
    }
    
    return render(request,'Chapter/detail.html',context)


def Chapter_list_view(request,*args, **kwargs):
    q= request.GET.get('q')
    qs = Chapter.objects.get_all_active_Chapters()
    if not q is None:
  #TODO: add search Parameters below:
        search_param =  Q(id__icontains =q )| Q( name__icontains = q)
        qs = qs.filter(search_param)
    context ={
        'object_list': qs
    }
    return render(request,'Chapter/list.html',context)
