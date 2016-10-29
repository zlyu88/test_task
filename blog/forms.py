from django import forms


class LogIn(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Password', max_length=32)


class SignUp(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=20)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=32)
    picture = forms.ImageField(required=False)

    def clean_picture(self):
        return None
