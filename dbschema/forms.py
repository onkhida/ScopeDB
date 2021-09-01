from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'institute', 'dburl', 'description', 'samples')

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Project Name',
                'class': 'w-full px-5 py-1 text-gray-700 bg-gray-200 rounded',
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Project Description',
                'class': '',
            })

        }
