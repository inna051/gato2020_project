from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = ''

        if self['username'].value() or self.data.get('username'):
            self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['password1'].help_text = ''

        if self['password1'].value() or self.data.get('password1'):
            self.fields['password1'].error_messages = {
                'password_too_short': 'Your password must contain at least 8 characters.',
                'password_entirely_numeric': 'Your password can’t be entirely numeric.',
                'password_common': 'Your password can’t be a commonly used password.',
                'password_similar': 'Your password can’t be too similar to your other personal information.',
            }

        self.fields['password2'].help_text = ''

        if self['password2'].value() or self.data.get('password2'):
            self.fields['password2'].error_messages = {
                'password_mismatch': 'The two password fields didn’t match.',
            }


