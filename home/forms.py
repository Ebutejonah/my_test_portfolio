from django import forms
from .models import Review
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ReviewForm(forms.ModelForm):
    class meta:
        model= Review
        fields= ['feedback']

class RawReviewForm(forms.Form):
    feedback= forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':50, 'style':'resize:none;font-family:Barlow Condensed;font-size:1rem;background:white;'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3())
    
