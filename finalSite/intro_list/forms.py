from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control'})
    )

    email = forms.CharField(
        max_length=150,
        label='Email',
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'type': 'email',
            'class': 'form-control'})
    )

    phonenumber = forms.CharField(
        max_length=50,
        label='Phone Number',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'tel',})
    )
    content = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control'})
    )
