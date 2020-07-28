from django import forms

from .models import HhRequest


class WorkRequestForm(forms.ModelForm):
    """Форма заявки на премию"""
    class Meta:
        model = HhRequest
        fields = ('profile', 'sphere', 'experience', 'work_request', 'resume')

        widgets = {

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
            'work_request': forms.Select(
                attrs={
                    'id': 'work_request',
                    'required': '',
                    'class': 'browser-default custom-select'
                }
            ),
            'resume': forms.FileInput(
                attrs={
                    'id': 'hh_resume',
                    'required': '',
                    'class': 'custom-file-input',
                    'lang': 'ru'
                }
            ),

        }
