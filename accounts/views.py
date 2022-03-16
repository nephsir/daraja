# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import User, Loan
# import requests


 

# # Create your views here.



# def add_loan_limit(request):
#     response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Bearer VkRwc2V4bE5xVERUNVk4YVZJbjhjQ0tYM2M4alhhMWo6RFRCQ0FqbXpEMXN0emxhdQ==' })
#     print(response.text.encode('utf8'))



#     # name=request.data.get('name')
#     # limit=request.data.get('loan_limit')
#     # id = request.data.get('id')
#     # user_to_update = User.objects.filter(id = id)
#     # user_to_update.loan_limit = limit
#     # user_to_update.save()
#     # response_string = f"the limit is {limit}"
#     return HttpResponse(response.text.encode('utf8')) 


# def total_loan_with_intrest(request):
#     id = request.data.get('id')
#     loan = Loan.objects.get(id=id)
#     loan_amount = loan.amount
#     total = loan_amount*0.12
    
#     response_string = f"the total amount with intrest is {total}"
#     return HttpResponse(response_string)



def signup(request):
    return render(request, 'signup.html')



from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Loan
import requests
import datetime
from base64 import b64encode 



 

# Create your views here.

def add_loan_limit(request):
    response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Bearer VkRwc2V4bE5xVERUNVk4YVZJbjhjQ0tYM2M4alhhMWo6RFRCQ0FqbXpEMXN0emxhdQ==' })
    print(response.text.encode('utf8'))
    time_now = datetime.datetime.now().strftime("%Y%m%d%H%I%S")
    s =time_now
    encoded = b64encode(s.encode('utf-8'))
    return HttpResponse(encoded)

