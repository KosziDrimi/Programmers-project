from django import forms
from .models import Programmer


class ProgrammerForm(forms.ModelForm):
    class Meta:
        model = Programmer
        fields = ['name', 'surname', 'email', 'position', 'c_plus_plus_level',
                  'c_level', 'rust_level', 'python_level', 'java_level']
        

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Programmer
        fields = ['c_plus_plus_level', 'c_level', 'rust_level', 
                  'python_level', 'java_level']
        
        
