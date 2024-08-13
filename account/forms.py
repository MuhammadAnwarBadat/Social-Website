from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('A user with that username already exists.')
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='Username or Email')
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get("username_or_email")
        password = cleaned_data.get("password")
        
        if username_or_email and password:
            user = authenticate(username=username_or_email, password=password)
            if user is None:
                self.add_error(None, "Invalid username or password")
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
