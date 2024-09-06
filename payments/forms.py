from django import forms

class PaymentForm(forms.Form):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone_number = forms.IntegerField(required=False)
    amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={'readonly': 'readonly'})
    )
    download_url = forms.CharField()