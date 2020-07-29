from urllib import request

from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User

from .models import Request, JuryApproved, AwardNewParticipant


class AwardRequestForm(forms.ModelForm):
    """Форма заявки на премию"""
    class Meta:
        model = Request
        exclude = ('approved_by_jury', 'jurys_nomination', 'vote', 'to_edit_notification', 'public')

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'required': '',
                    'placeholder': 'Фамилия Имя Отчество *'
                }
            ),

            'company': forms.TextInput(
                attrs={
                    'id': 'company',
                    'required': '',
                    'placeholder': 'Компания *'
                }
            ),

            'professional': forms.TextInput(
                attrs={
                    'id': 'professional',
                    'required': '',
                    'placeholder': 'Ваша должность *'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'required': '',
                    'placeholder': 'Email *'
                }
            ),

            'project_name': forms.TextInput(
                attrs={
                    'id': 'project_name',
                    'required': '',
                    'placeholder': 'Название проекта *'
                }
            ),

            'nomination': forms.Select(
                attrs={
                    'id': 'nomination',
                    'required': '',
                    'placeholder': 'Название проекта *',
                    'class': 'browser-default custom-select'
                }
            ),

            'phone': forms.NumberInput(
                attrs={
                    'id': 'phone',
                    'required': '',
                    'placeholder': 'Номер телефона *'
                }
            ),

            'video': forms.TextInput(
                attrs={
                    'id': 'video',
                    'required': ''
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

            'avatar': forms.FileInput(
                attrs={
                    'id': 'avatar',
                    'required': '',
                    'class': 'custom-file-input',
                    'lang': 'ru'
                }
            ),

            'presentation': forms.FileInput(
                attrs={
                    'id': 'presentation',
                    'required': '',
                    'class': 'custom-file-input',
                    'lang': 'ru'
                }
            ),

            'description': CKEditorWidget(
                attrs={
                    'required': '',
                    'id': 'description',
                    'placeholder': 'Описание проекта'
                }
            ),

            'project_appoints': CKEditorWidget(
                attrs={
                    'required': '',
                    'id': 'project_appoints'
                }
            ),

            'results': CKEditorWidget(
                attrs={
                    'required': '',
                    'id': 'results'
                }
            ),
        }


class JuryApprovedForm(forms.ModelForm):
    """Форма оценки жюри"""
    class Meta:
        model = JuryApproved
        fields = ('name', 'approved', 'recommendation', 'vote', 'nomination_jury', 'project')


class AwardNewParticipantForm(forms.ModelForm):
    """Форма оценки жюри"""
    class Meta:
        model = AwardNewParticipant
        fields = ('name', 'company', 'email', 'phone')
