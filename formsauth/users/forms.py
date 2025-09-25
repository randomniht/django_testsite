from django import forms
from django.contrib.auth import authenticate 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args,**kwargs)
    
    def clean(self):
        data = self.cleaned_data
        username = data['username']
        password = data['password']

        self.user = authenticate(self.request, username=username,password=password)

        if not self.user:
            raise forms.ValidationError('Error: incorrect password or username')
        return data
    def get_user(self):
        return self.user