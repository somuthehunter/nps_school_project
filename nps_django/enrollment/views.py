from django.shortcuts import render , HttpResponse , redirect
from .models import Enrollment

# Create your views here.

def success_view(request):
    return render(request,'enrollment/success.html')


def enroll(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        student_class = request.POST.get('class')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        question = request.POST.get('question')
    
        Enrollment.objects.create(
            student_name = student_name , 
            father_name = father_name,
            student_class = student_class,
            email = email,
            mobile = mobile, 
            question = question
        )
        return render(request,'enrollment/success.html')


    return render(request , "enrollment/enroll.html")