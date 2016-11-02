from django import forms


class LogIn(forms.Form):
<<<<<<< HEAD
    user_name = forms.CharField(label='Your name', max_length=50)
=======
    user_name = forms.CharField(label='Your name', max_length=20)
>>>>>>> 4e6d4b6b6ba00630ed7df82a6b542a3c9de17484
    password = forms.CharField(label='Password', max_length=32)


class SignUp(forms.Form):
<<<<<<< HEAD
    user_name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=32)
    image = forms.ImageField(required=False, label='Select a file')
=======
    user_name = forms.CharField(label='Your name', max_length=20)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=32)
    picture = forms.ImageField(required=False)
>>>>>>> 4e6d4b6b6ba00630ed7df82a6b542a3c9de17484


class PostAdd(forms.Form):
    title = forms.CharField(label='title', max_length=50)
<<<<<<< HEAD
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

=======
    text = forms.CharField(label='text', max_length=500)
    picture = forms.ImageField(required=False)
>>>>>>> 4e6d4b6b6ba00630ed7df82a6b542a3c9de17484
