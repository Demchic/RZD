from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин ", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль ", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'last_name', 'first_name', 'middle_name', 'tab_number', 'phone_number',
                  'password1', 'password2']
        labels = {
            'email': 'Корпоративная почта',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'tab_number': 'Табельный номер',
            'phone_number': 'Рабочий телефон'
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-input'}),
            'tab_number': forms.TextInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такая корпоративная почта уже существует!")
        return email

    def clean_tab_number(self):
        tab_number = self.cleaned_data.get('tab_number')
        if tab_number and get_user_model().objects.filter(tab_number=tab_number).exists():
            raise forms.ValidationError("Такой табельный номер уже существует!")
        return tab_number

class ProfileUserForm (forms.ModelForm):
    username = forms.CharField(disabled=True, label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label="Корпоративная почта", widget=forms.TextInput(attrs={'class': 'form-input'}))
    tab_number = forms.CharField(disabled=True, label="Табельный номер", widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'tab_number', 'last_name', 'first_name', 'middle_name', 'phone_number']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'phone_number': 'Рабочий телефон'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'})
        }
