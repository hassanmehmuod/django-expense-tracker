from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'date', 'category']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'category': forms.TextInput(attrs={'class': 'form-control'}),
    }