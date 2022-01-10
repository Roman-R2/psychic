from django import forms

from .models import UserNumbers


class QuestionForm(forms.ModelForm):
    class Meta:
        model = UserNumbers
        fields = ('number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
