from django import forms
from django.core import validators
from django.contrib.auth.models import User
from second_app.models import User1, UserProfileInfor

class FormName(forms.ModelForm):
    class Meta():
        model = User1
        fields = ('first_name', 'last_name', 'email')

    '''
clas FormName(forms.form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again:")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    '''
    # it is not a built in validation but created to understand the idea
    '''
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
    '''
    '''
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure the email match")
    '''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfo_Form(forms.ModelForm):
    class Meta():
        model = UserProfileInfor
        fields = ('portfolio_site', 'profile_pic')