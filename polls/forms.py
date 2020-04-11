from django import forms
from .models import *
from django.contrib.auth.models import User

class Page1Form(forms.ModelForm):

	question = forms.ChoiceField(label='How was the Event?',choices=(('E', 'Excellent'), ('G', 'Good'), ('A', 'Average'), ('P', 'Poor')), widget=forms.RadioSelect)
	card = forms.ChoiceField(label='Which card do You use?',choices=(('V', 'Visa'), ('M', 'MasterCard'), ('P', 'Paypal')), widget=forms.RadioSelect)

	class Meta():
		model=Page1
		fields=['card','question']

class Page1Form1(forms.ModelForm):
    question = forms.ChoiceField(label='Campus',choices=(('E', 'Excellent'), ('G', 'Good'), ('A', 'Average'), ('P', 'Poor')), widget=forms.RadioSelect)
    question1 = forms.ChoiceField(label='Infrastructure',choices=(('E1', 'Excellent'), ('G1', 'Good'), ('A1', 'Average'), ('P1', 'Poor')), widget=forms.RadioSelect)
    question2 = forms.ChoiceField(label='Canteen',choices=(('E2', 'Excellent'), ('G2', 'Good'), ('A2', 'Average'), ('P2', 'Poor')), widget=forms.RadioSelect)
    question3 = forms.ChoiceField(label='Faculty',choices=(('E3', 'Excellent'), ('G3', 'Good'), ('A3', 'Average'), ('P3', 'Poor')), widget=forms.RadioSelect)
    review = forms.CharField(label='Overall Review',widget = forms.TextInput())
    
    class Meta():
        model=vcet
        fields=['question','question1','question2','question3']



class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Confirm Password...'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password

        #card_type = forms.ChoiceField(choices=(('V', 'Visa'), ('M', 'MasterCard'), ('P', 'Paypal')), widget=forms.RadioSelect)
    
class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

# class UserProctorForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = (
#             'name',
#             'email_id',
#             'contact_no',
            
#         )



# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = (
#             'name',
#             'email_id',
#             'contact_no',
            
#         )
