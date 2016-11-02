from django import forms


class LogIn(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=50)
    password = forms.CharField(label='Password', max_length=32)


class SignUp(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=32)
    image = forms.ImageField(required=False, label='Select a file')


class PostAdd(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    text = forms.CharField(label='text', widget=forms.Textarea)
    picture = forms.ImageField(required=False, label='Select a file')


class PostEdit(PostAdd):

    def __init__(self, post):
        super(PostEdit, self).__init__()
        self.post = post
        self.fields['title'].widget = forms.TextInput(attrs={
            'value': '{}'.format(self.post.title)})
        self.fields['text'].widget = forms.Textarea(attrs={
            'cols': 140, 'rows': 10,
            'placeholder': '{}'.format(self.post.text)})


class TagAdd(forms.Form):
    tag = forms.CharField(label='title', max_length=20)

