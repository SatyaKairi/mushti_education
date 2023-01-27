from django.http import Http404

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from django.db.models import Q
from .forms import *
# Create your views here.

def Classes_create_update_view(request,*args, **kwargs):
    Classes=None
    msg = "Create Classes"
    Classes_id = kwargs.get('id')
    if not Classes_id is None:
        Classes = Classes.objects.get(id=Classes_id)
        msg = "Update Classes"

    form = ClassesCreateForm(request.POST or None,instance=Classes)
    if request.POST:
        if form.is_valid():
            Classes =form.instance
            Classes.user = request.user
            form.save()
            return redirect (form.instance.get_detail_url())             
    context = {
            'form':form,
            'object':Classes,
            'msg':msg

        }      
    return render(request,'Classes/create.html',context)   
def Classes_deactivate_view(request):
    if request.POST:
        id = request.POST.get('Classes_id')
        Classes = Classes.objects.get(id=id)
        Classes.is_active = False
        Classes.modified_by = request.user
        Classes.save()
        return redirect('Classes:list_view')

def Classes_detail_view(request,id,*args, **kwargs):
    classes = get_object_or_404(Classes,id=id,is_active = True)
 
    context ={
        'object':classes,
    }
    
    return render(request,'Classes/detail.html',context)


def Classes_list_view(request,*args, **kwargs):
    q= request.GET.get('q')
    qs = Classes.objects.get_all_active_Classess()
    if not q is None:
  #TODO: add search Parameters below:
        search_param =  Q(id__icontains =q )| Q( name__icontains = q)
        qs = qs.filter(search_param)
    context ={
        'object_list': qs
    }
    return render(request,'Classes/list.html',context)
