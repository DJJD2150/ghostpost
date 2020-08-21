from django import forms
from ghostpost_app.models import BoastsAndRoasts

# Got help from Sohail Aslam in study hall.
class BoastsAndRoastsForm(forms.Form):
    CHOICES = [(True, 'roast'), (False, 'boast')]
    isroast = forms.ChoiceField(choices=CHOICES)
    post_content = forms.CharField(max_length=280)
