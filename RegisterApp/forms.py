from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category




# i am using usercreationform , its a by-defoult form in django
class SignupUser(UserCreationForm):
    first_Name = forms.CharField(max_length=100,required=True)
    last_Name  = forms.CharField(max_length=100,required=True)
    email = forms.EmailField()

    class Meta :
        model= User
        fields = ('username','first_Name','last_Name','email','password1','password2')


class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def Clean(self,*args,**kwargs):
        username = self.Clean_data.get('username')
        password = self.Clean_data.get('password')

        if username and password:
            user= authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('user is not active')
        return super(UserLoginForm,self).clean(*args,**kwargs)







