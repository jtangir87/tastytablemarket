from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(
        widget=forms.Textarea()
    )