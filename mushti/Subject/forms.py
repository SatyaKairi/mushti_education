from dataclasses import fields
from django import forms
from .models import Subject

class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['id','name','session','classid']
       
        
        
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {
            'placeholder': f'{str(field)}',
            'class': 'form-control'
            }
                
        )
    
