from django import forms

class TransactionForm(forms.Form):
    date = forms.CharField(label="Date")
    value = forms.CharField(label="Value")
    description = forms.CharField(label="Description")
    category = forms.CharField(label="Category")
    document = forms.CharField(label="Document")

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Arquivo')
