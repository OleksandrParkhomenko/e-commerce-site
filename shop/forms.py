from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['items', 'name', 'email', 'address', 'city', 'state', 'zipcode', 'total']
        widgets = {
            'items': forms.HiddenInput(
                attrs={'id': 'items'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'John Smith'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'johnsmith@example.com'}),
            'address': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Example Str 12'}),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'London'}),
            'state': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'UK'}),
            'zipcode': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Zipcode'}),
            'total': forms.HiddenInput(
                attrs={'id': 'total'}),
        }
