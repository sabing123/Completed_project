from django import forms
from django.forms import ModelForm, TextInput
from .models import PremiumCourseEnroll

class PremiumCourseForm(ModelForm):
    class Meta:
        model = PremiumCourseEnroll
        fields = '__all__'
    

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30,
                           widget=TextInput(attrs={'class': 'form-label form-label-top form-label-extended form-label-auto'}))
    email = forms.EmailField(max_length=254,
                             widget=TextInput(attrs={'class': 'form-label form-label-top form-label-extended form-label-auto'}))
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-label form-label-top form-label-extended form-label-auto'}),
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

