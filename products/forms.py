from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm, \
    AuthenticationForm
from django.core.exceptions import PermissionDenied

from blog.models import Blog, Comment
from products.models import Product
from users.models import User
from version_app.models import Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['view_count', 'owner', 'published']


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'description', 'published',)


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['view_count', 'published', 'owner']

    def clean(self):
        """
        Проверяет все текстовые поля формы и проверяет на наличие запрещенных слов
        :return:
        """
        banned_words_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                             'радар', 'фурри']
        fields_list = []

        cleaned_data = super().clean()

        for field_name, field in self.fields.items():
            if isinstance(field, forms.CharField):
                fields_list.append(field_name)

        for field_data in fields_list:
            field_data = cleaned_data.get(field_data)
            for word in banned_words_list:
                if word in field_data.lower():
                    raise forms.ValidationError('Нельзя использовать запрещенные слова')

        return cleaned_data


class BlogContentMenedgerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('published',)


class CommentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserResetPasswordForm(StyleFormMixin, PasswordResetForm):
    pass


class UserPasswordResetConfirmForm(StyleFormMixin, SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = forms.HiddenInput()


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    pass
