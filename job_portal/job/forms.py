from django import forms 
from .models import Tag, Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "description", "location", "min_salary", "max_salary", "tags"]

    def save(self, commit = True, company=None):
        instance = super().save(commit=False)
        if company:
            instance.company = company
        if commit:
            instance.save()
        return instance
