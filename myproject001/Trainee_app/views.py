

from django.shortcuts import render,redirect
from .models import userinput
from .forms import userinputform
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = userinputform(request.POST)
        if form.is_valid():
             #Process the user input here
            #input_data = form.cleaned_data['EmpName']
            #input_data2 = form.cleaned_data['EmpID']
            #input_data3 = form.cleaned_data['DOJ']
            #input_data3 = form.cleaned_data['TrainingDuration']
            #input_data3 = form.cleaned_data['Experience']
            form.save()

        return redirect('/index1/')
            
    else:
        form =userinputform()
    
    return render(request, 'index.html', {'form': form})        

def index1(request):
    if request.method == 'GET':
        Data = userinput.objects.all().values().order_by('-id')
        trinee_data = {
            "Datas": Data
        }
        return render(request,'index1.html',trinee_data)
     
    