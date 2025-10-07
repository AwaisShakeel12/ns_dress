from django import forms
from .models import Dress, Lace

class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = [
            'brand_name', 'dress_type', 'color',
            'width', 'height', 'price', 'quantity',
            'status', 'description'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
        

class LaceForm(forms.ModelForm):
    class Meta:
        model = Lace
        fields = ['name', 'length', 'price', 'image', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }        