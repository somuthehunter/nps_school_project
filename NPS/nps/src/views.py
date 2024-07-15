from django.shortcuts import render
from .forms import studetPayment
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import razorpay

def student_payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        stu_class = request.POST.get('class')
        amount= int(request.POST.get('amount')) * 100
        #create Razorpay client 
        client = razorpay.Client(auth=('rzp_test_wFREsmnp7V1lQX','43kdOjXtmUDU1sExdYovP8aF'))

        #create an order 
        payment = client.order.create(dict(amount = amount,
                                                     currency = 'INR',)
                                                    )
        dbs = StudentsPayment(name = name , amount = amount , razorpay_payment_id = payment['id'])

    
        
        print(payment)
        print(name,stu_class,amount)
        return render(request,'student_payment.html' , {'payment':payment})
    return render(request,'student_payment.html')

@csrf_exempt
def payment_status(request):
    if request.method == "POST":
        a = request.POST
        order_id= ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
    student = StudentsPayment.objects.filter(payment_id =order_id).first()
    student.paid = True
    student.save()
    return render(request, 'payment_status.html')