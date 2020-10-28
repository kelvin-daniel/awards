from .models import Projects,Rates,Comments,Profile
from django import forms

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class PostForm(forms.ModelForm):
    class Meta:
        model=Projects
        exclude=['user','design','usability','content']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['user','pro_id']
        
class RateForm(forms.ModelForm):
    class Meta:
        model=Rates
        exclude=['user','project']



