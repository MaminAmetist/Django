from django import forms
from django.core.exceptions import ValidationError


def validate_age(value):
    if int(value) < 18:
        raise ValidationError('Вы должны быть старше 18.')
    return value


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:', error_messages={'required': 'Тысяча чертей!', },
                               help_text='Имя пользователя должно содержать не более 30 символов.')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Введите пароль:',
                               error_messages={'required': 'Пароль слишком короткий.', },
                               help_text='Пароль должен содержать не менее 8 символов.')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Повторите пароль:')
    age = forms.IntegerField(min_value=18, label='Введите свой возраст:', validators=[validate_age],
                             error_messages={'required': 'Вы должны быть старше 18.', }, )
    subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку.')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = ['Anna', 'Den', 'Cat']
        if ' ' in username:
            raise forms.ValidationError('Имя пользователя не должно содержать пробелы.')
        elif len(username) > 30:
            raise forms.ValidationError('Имя пользователя должно содержать не более 30 символов.')
        elif username in users:
            raise forms.ValidationError('Пользователь уже существует.')
        return username

    def clean_password(self):
        #cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')
        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError(f'Пароли не совпадают,{password, repeat_password}')
        return password, repeat_password

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if len(str(age)) > 3:
            raise forms.ValidationError('Столько не живут.')
        return age
