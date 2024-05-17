import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LoginView
from django.core.checks import messages
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from products.forms import UserRegisterForm, UserProfileForm, UserResetPasswordForm, UserPasswordResetConfirmForm, \
    UserLoginForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class CustomLoginRequiredMixin(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'redirect_to'
    # permission_denied_message = 'Доступ запрещен для неавторизованных пользователей'


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token_verification = secrets.token_hex(16)
        user.token_verification = token_verification
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token_verification}'
        send_mail(
            subject="Подверждение регистрации",
            message=f"Подтвердите регистрацию, перейдя по ссылке\n{url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=True,
        )
        return super().form_valid(form)


def email_confirm(request, token_verification):
    user = get_object_or_404(User, token_verification=token_verification)
    user.is_active = True
    user.token_verification = None
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user


class UserPasswordResetView(PasswordResetView):
    form_class = UserResetPasswordForm
    success_url = reverse_lazy('users:password_reset_done')
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserPasswordResetConfirmForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class UserLoginView(LoginView):
    form_class = UserLoginForm


def user_auto_generate_password(request):
    context = {
        'reset_message': 'Новый пароль отправлен на почту'
    }
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.get(email=email)
        new_password = secrets.token_hex(8)
        user.set_password(new_password)
        user.save()
        send_mail(
            message=f'Вот ваш новый пароль - \n{new_password}',
            subject='Новый пароль',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )

    return render(request, 'users/login.html', context)
