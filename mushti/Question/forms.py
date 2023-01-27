from dataclasses import fields
from django import forms
from .models import Question

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['id','question','option1','option2','answer']
       
        
        
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {
            'placeholder': f'{str(field)}',
            'class': 'form-control'
            }
                
        )
    
