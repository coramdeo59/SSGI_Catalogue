from django.shortcuts import render, redirect
from django.contrib import messages

import http.client
import json
import random
import urllib

from .forms import PaymentForm

def PaymentFormView(request):
    passed_amount = request.GET.get('price', '')
    download_url = request.GET.get('download_url', '')
    form = PaymentForm(initial={'download_url': download_url,'amount': passed_amount})
    field = form.fields['download_url']
    field.widget = field.hidden_widget()
    return render(request, 'payments/payment-form.html', {'form': form, 'price': passed_amount})

def send_payment_request(request):
    if request.method == 'POST':
        try:
            amount = request.POST['amount']
        except:
            messages.error(request, 'Please enter Amount.')
            form = PaymentForm(request.POST)
            return render(request, 'payments/payment-form.html', {'form': form})
        email = None
        first_name = None
        last_name = None
        phone_number = None
        try:
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']
        except:
            pass
        conn = http.client.HTTPSConnection("api.chapa.co")
        num = random.random()
        download_url = request.POST['download_url']
        download_url = urllib.parse.quote(download_url[14:])
        payload = json.dumps({
            "amount": amount,
            "currency": "ETB",
            "tx_ref": "chewatatest-"+str(num),
            "callback_url" :  "http://localhost:8000/download_zip/?dir_path=" + download_url,
            "return_url": 'http://localhost:8000',
            "customization[title]": "SSGI Catalog",
            "customization[description]": "Payment for SSGI Catalog."
        })

        headers = {
            'Authorization': 'Bearer CHASECK_TEST-bR1U56EcHeKWnUPT0bqtuATCtz535umB',
            'Content-Type': 'application/json'
        }

        conn.request("POST", "/v1/transaction/initialize", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode('utf-8'))
        print(data)
        if data['status'] == 'success':
            checkout_url = data['data']['checkout_url']
            return redirect(checkout_url)

def callback_view(request):
    # Process callback data and determine if payment was successful
    payment_status = request.GET.get('status', '')
    download_url = request.GET.get('link', '')

    if payment_status == 'success':
        # Redirect to the download URL after successful payment
        return redirect(download_url)
    else:
        # Handle failed payment (optional)
        return HttpResponse("Payment failed or was not successful.")
