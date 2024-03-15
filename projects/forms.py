from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'materials', 'steps', 'image', 'category' ]

        materials = forms.CharField(widget=RichTextWidget())
        steps = forms.CharField(widget=RichTextWidget())

        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }