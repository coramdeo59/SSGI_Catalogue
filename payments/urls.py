from django.urls import path

from .views import PaymentFormView, send_payment_request, callback_view

urlpatterns = [
    path('payment-form/', PaymentFormView, name='payment-form'),
    path('pay/', send_payment_request, name='payment-request'),
    path('callback/', callback_view, name='callback_view'),
]