from django import forms


class LogIn(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Password', max_length=32)


class SignUp(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=20)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=32)
    picture = forms.ImageField(required=False)


class PostAdd(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    text = forms.CharField(label='text', max_length=500)
    picture = forms.ImageField(required=False)