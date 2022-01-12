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

    def clean_number(self):
        number = self.cleaned_data['number']
        if number < 10 or number > 99:
            raise forms.ValidationError(
                'Неправильный ввод. Необходимо загадать двузначное число.'
            )
        return number
