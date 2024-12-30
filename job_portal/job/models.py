from django.db import models
from django.core.exceptions import ValidationError
from company.models import Company

class Tag(models.Model):
    """
    Stores a Single Tag entry.
    """
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

class Job(models.Model):
    """
    Stores a single Job entry, related to :model `company.Company`
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='jobs')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")

    def clean(self):
        """Constraint for taking salary range."""
        if self.min_salary > self.max_salary:
            raise ValidationError("minimum salary should be less than maximum salary.")

    def __str__(self):
        return self.title
