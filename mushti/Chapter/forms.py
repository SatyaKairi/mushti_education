from dataclasses import fields
from django import forms
from .models import Chapter

class ChapterCreateForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['id','name','subjectid','content']
       
        
        
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {
            'placeholder': f'{str(field)}',
            'class': 'form-control'
            }
                
        )
    
