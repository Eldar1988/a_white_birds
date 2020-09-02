from django import forms
from .models import ServiceContactResume, ServiceContact


class ServiceContactResumeForm(forms.ModelForm):
    """Форма заявки на премию"""
    class Meta:
        model = ServiceContactResume
        fields = ('name', 'email', 'phone', 'profile', 'sphere', 'experience', 'self_request', 'resume')

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'required': '',
                    'class': 'form-group'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'required': '',
                    'class': 'form-group'
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    'id': 'phone',
                    'required': '',
                    'class': 'form-group'
                }
            ),
            'profile': forms.Select(
                attrs={
                    'id': 'profile',
                    'required': '',
                    'class': 'browser-default custom-select'
                }
            ),
            'sphere': forms.Select(
                attrs={
                    'id': 'sphere',
                    'required': '',
                    'class': 'browser-default custom-select'
                }
            ),
            'experience': forms.Select(
                attrs={
                    'id': 'experience',
                    'required': '',
                    'class': 'browser-default custom-select'
                }
            ),
            'self_request': forms.Select(
                attrs={
                    'id': 'self_request',
                    'required': '',
                    'class': 'browser-default custom-select'
                }
            ),
            'resume': forms.FileInput(
                attrs={
                    'id': 'resume',
                    'required': '',
                    'class': 'custom-file-input',
                    'lang': 'ru'
                }
            ),

        }


class RequestForm(forms.ModelForm):

    class Meta:
        model = ServiceContact
        fields = '__all__'