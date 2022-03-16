from django.urls import path, include
from . import views



urlpatterns = [
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    # register, confirmation, validation and callback urls
    # path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    # path('c2b/confirmation', views.confirmation, name="confirmation"),
    # path('c2b/validation', views.validation, name="validation"),
    # # path('c2b/callback', views.callback, name="call_back"),
    # path('c2b/test', views.test, name="validation"),
    # path('c2b/deposit', views.deposit_to_account_callbacks, name="prints deposit"),
    # path('c2b/test_callback', views.test_callback, name="prints ref"),


]