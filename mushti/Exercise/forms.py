from dataclasses import fields
from django import forms
from .models import Exercise

class ExerciseCreateForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['id','name','chapterid']
       
        
        
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {
            'placeholder': f'{str(field)}',
            'class': 'form-control'
            }
                
        )
    
