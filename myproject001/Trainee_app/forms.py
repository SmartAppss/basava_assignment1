from django import forms
from .models import userinput

class userinputform(forms.ModelForm):
    class Meta:
        model = userinput
        fields =  ['EmpName','EmpID','DOJ','TrainingDuration','Experience']
