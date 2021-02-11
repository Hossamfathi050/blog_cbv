from django.shortcuts import render

# Create your views here.
def home(request):
    context={'file':FileAdmin.objects.all()}
    return render(request,'upload/home.html',context)