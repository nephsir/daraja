from urllib import request
from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json

from accounts.serializer import LoanSerializer
from accounts.serializer import MpesaSerializer
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment
from .models import mpesa_response
from rest_framework.decorators import api_view
from accounts.models import Loan
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import datetime


#STK PUSH


def getAccessToken(request):
    consumer_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
    consumer_secret = '2nHEyWSD4VjpNh2g'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254706594653
        ,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254706594653,  # replace with your phone number to get stk push
        "CallBackURL": "https://darajambili.herokuapp.com/express-payment",
        "AccountReference": "Nephat",
        "TransactionDesc": "Testing stk push"

    }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse(response)
    

































# @api_view(["GET","POST"])
# def test(response):
#     response = lipa_na_mpesa_online()
#     # mpesa_response = json.loads(response)
#     # ResponseCode = mpesa_response.get('ResponseCode')
#     # __init__(self,mpesa_response):


    
               
#     # a = mpesa_response.object.get(ResponseCode=ResponseCode)
#     # a.save()
#     print(mpesa_response)
#     # return HttpResponse(response)
#     # mpesa_response = json.loads(response)
#     # resp_serializer = MpesaSerializer(mpesa_response, many=True)
#     # return Response({'mpesa_response':resp_serializer.data})
    


#     # return HttpResponse(response)
#     #saving json in models
#     # json_data = request.data
#     # stream = io.BytesIO(json_data)
#     # python_data = JSONParser().parse(stream)
#     # serializer = MpesaSerializer(data=python_data)
#     # if serializer.is_valid():
#     #     serializer.save()
#     #     res = {'msg':'DATA CREATED'}
#     #     json_data = JSONRenderer().render(res)
#     #     return HttpResponse(json_data, content_type='application/json')

# #saving json in models






# def sum(x,y):
#     total=x+y
#     print(total)

# def add():
#     x='THis is good'
#     y=820.0
#     sum()











# #C2B

# @csrf_exempt
# def register_urls(request):
#     access_token = MpesaAccessToken.validated_mpesa_access_token
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     options = {"ShortCode": LipanaMpesaPpassword.Business_short_code,
#                "ResponseType": "Completed",
#                "ConfirmationURL": "https://91563395.ngrok.io/api/v1/c2b/confirmation",
#                "ValidationURL": "https://91563395.ngrok.io/api/v1/c2b/validation"}
#     response = requests.post(api_url, json=options, headers=headers)

#     return HttpResponse(response.text)




# @csrf_exempt
# def validation(request):

#     context = {
#         "ResultCode": 0,
#         "ResultDesc": "Accepted"
#     }
#     return JsonResponse(dict(context))


# @csrf_exempt
# def confirmation(request):
#     mpesa_body =request.body.decode('utf-8')
#     mpesa_payment = json.loads(mpesa_body)

#     payment = MpesaPayment(
#         first_name=mpesa_payment['FirstName'],
#         last_name=mpesa_payment['LastName'],
#         middle_name=mpesa_payment['MiddleName'],
#         description=mpesa_payment['TransID'],
#         phone_number=mpesa_payment['MSISDN'],
#         amount=mpesa_payment['TransAmount'],
#         reference=mpesa_payment['BillRefNumber'],
#         organization_balance=mpesa_payment['OrgAccountBalance'],
#         type=mpesa_payment['TransactionType'],

#     )
#     payment.save()

#     context = {
#         "ResultCode": 0,
#         "ResultDesc": "Accepted"
#     }

#     return JsonResponse(dict(context))

# #C2B










# #POSTMAN TESTS

# @api_view(["POST"])
# def view_loans(request):
#     loans = Loan.objects.all()
#     loans_serializer = LoanSerializer(loans, many=True)
#     return Response({'loans':loans_serializer.data})


# @api_view(["POST"])
# def deposit_to_account_callbacks(request):
#     # print(request.data)
#     ReceivingAccount = request.data.get('total', None)
#     print(ReceivingAccount)

#     return Response({'loans':'loans_serializer.data'})


# # def test(request):
# #     data =requests.get('http://  ')
            
# #     json_object = json.loads(data.MpesaReceiptNumber)
# #     return HttpResponse((json.dumps(json_object, indent = 1)))


# @api_view(["POST"])
# def test_callback(request):
#     sample_data = request.data

#     transaction_id = sample_data.get('TransID')
#     print(transaction_id)
#     return Response(transaction_id)

#     # callback_details = MpesaCallbacks.objects.get(transaction_id=transaction_id)
#     # loan_ref = callback_details.loan_ref 
#     # actual_loan = Loans.objects.get(loan_ref=loan_ref)
#     # actual_loan.repay()

# {
#     "TransactionType":"Pay Bill",
#     "TransID":"CeSVIJFe9AqbWBmawbPTP31qKdQmQV22NepsDhRpidlI9reJMvaQhBJzk5zIXqZU9138ddf7d12790503709db6c2f4bbb76",
#     "TransTime":"20191122063845",
#     "TransAmount":"10",
#     "BusinessShortCode":"600638",
#     "BillRefNumber":"254708374149",
#     "InvoiceNumber":"",
#     "OrgAccountBalance":"49197.00",
#     "ThirdPartyTransID":"",
#     "MSISDN":"254708374149",
#     "FirstName":"John",
#     "MiddleName":"",
#     "LastName":"Doe"
#      }