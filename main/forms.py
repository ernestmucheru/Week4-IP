
from django import forms
from .models import NeighbourHood
from pyuploadcare.dj.forms import ImageField
from authy.models import Profile

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')
class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)
