from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class Contact(forms.Form):
    username = forms.CharField(label="username",max_length=100,required=True)
    email = forms.EmailField(label="email", max_length=100,required=True)
    message = forms.CharField(label="message",required=True)

class Register(forms.ModelForm):
    username = forms.CharField(label="username", max_length=100,required=True)
    email = forms.EmailField(label="email", max_length=100,required=True)
    password = forms.CharField(label="password", max_length=100,required=True)
    confirm_password = forms.CharField(label="confirm_password", max_length=100,required=True)

    class Meta:
        model = User
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password!=confirm_password:
            raise forms.ValidationError("Password mismatch")

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100,required=True)
    password = forms.CharField(label="password", max_length=100,required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username and password")

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="email", max_length=100,required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')    

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user found.")
        
class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label='new_password',min_length=8)
    confirm_new_password = forms.CharField(label='confirm_new_password',min_length=8)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password and confirm_new_password and new_password!=confirm_new_password:
            raise forms.ValidationError("Password mismatch")