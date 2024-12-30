from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_number']


    def save(self, commit=True, user=None):
        """Custom company save method to save the current user as owner."""
        instance = super().save(commit=False)
        if user:
            instance.owner = user
        if commit:
            instance.save()

        return instance
