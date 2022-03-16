from django.urls import path
from .views import add_loan_limit

from .views import signup

urlpatterns = [
    path('add_loan_limit/', add_loan_limit, name='add_loan_limit'),
    path('signup/', signup, name='signup'),
    path('login/', signup, name='login'),
    
]
