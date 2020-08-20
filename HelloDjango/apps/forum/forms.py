from django import forms

from .models import ForumNewParticipant


class ForumNewParticipantForm(forms.ModelForm):
    """Форма оценки жюри"""
    class Meta:
        model = ForumNewParticipant
        fields = ('name', 'company', 'email', 'phone')