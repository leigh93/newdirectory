from django import forms
# from cloudinary.forms import CloudinaryFileField
from pyuploadcare.dj.forms import ImageField
from .models import Agent, Agency


# class AddAgentForm(forms.ModelForm):
#     name = forms.CharField(label='First Name', max_length=30)
#     re = forms.CharField(label='First Name', max_length=30)

class AddAgencyForm(forms.ModelForm):
    agencyname = forms.CharField(label='Agency Name', max_length=200)
    registration_no = forms.IntegerField(label='Registration Number')
    agency_logo = ImageField(label='Add agency')
    # agency_image = CloudinaryFileField(
    #     options = {
    #         'crop': 'thumb',
    #         'width': 200,
    #         'height': 200,
    #         'folder': 'avatars'
    #    }
    # )
    
    class Meta:
        model = Agency
        fields = (
            'agencyname',
            'registration_no',
            'agency_logo',

        )
        
class AddAgencyForm(forms.ModelForm):
    agencyname = forms.CharField(label='Agency Name', max_length=200)
    registration_no = forms.IntegerField(label='Registration Number')
    agency_logo = ImageField(label='Add agency')
    # agency_image = CloudinaryFileField(
    #     options = {
    #         'crop': 'thumb',
    #         'width': 200,
    #         'height': 200,
    #         'folder': 'avatars'
    #    }
    # )
    
    class Meta:
        model = Agency
        fields = (
            'agencyname',
            'registration_no',
            'agency_logo',

        )