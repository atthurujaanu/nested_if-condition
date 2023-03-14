from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':5500,'b':500,'c':1000}
    return render(request,'conditions.html',context=d)