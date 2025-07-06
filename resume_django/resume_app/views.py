from django.shortcuts import render

# Create your views here.
"""
from resume_app.models import Resume

def resume_view(request):
    resume_=Resume.objects.first() # fetch the first resume entry
    return render(request,'resume_app/home.html',{'resume':resume_})
"""
def home(request):
    return render(request,'resume_app/home.html')

def contact(request):
    return render(request,'resume_app/contact.html')
