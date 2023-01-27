from dataclasses import fields
from django import forms
from .models import Classes

class ClassesCreateForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['id','name','image']
       
        
        
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {
            'placeholder': f'{str(field)}',
            'class': 'form-control'
            }
                
        )
    
