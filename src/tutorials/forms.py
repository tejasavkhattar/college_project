from django import forms

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	subject = forms.CharField()
	message = forms.CharField()
