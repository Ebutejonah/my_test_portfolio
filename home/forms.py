from django import forms
from .models import Review



class ReviewForm(forms.ModelForm):
    class meta:
        model= Review
        fields= ['feedback']

class RawReviewForm(forms.Form):
    feedback= forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':50, 'style':'resize:none;font-family:Arial, sans-serif;font-size:1rem;background:white;'}))

    
