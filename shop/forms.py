from django import forms
from .models import Order, Product


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


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'category', 'description']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'ExampleTV Smart 42\''}),
            'price': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '$500'}),
            'category': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Electronics'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter your product description'}),
            'user': forms.HiddenInput(
                attrs={'id': 'user'}),
        }
