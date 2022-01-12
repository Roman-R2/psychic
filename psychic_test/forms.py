from django import forms


class QuestionForm(forms.Form):
    number = forms.IntegerField(
        label='Загаданное число',
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    def clean_number(self):
        number = self.cleaned_data['number']
        if number < 10 or number > 99:
            raise forms.ValidationError(
                'Неправильный ввод. Необходимо загадать двузначное число.'
            )
        return number
