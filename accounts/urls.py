from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    #login
    #logout
    #registration / signup
    path('login', login_view, name = 'login'),
    path('logout', logout_view, name = 'logout'),
    path('signup', signup_view, name = 'signup'),
    path('change_password/', change_password, name='change_password'),
    path('password_change_done/', password_change_done, name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset_form.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt',
            success_url='/password_reset_done/'
        ), name='password_reset'),,
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url='/password_reset_complete/'
        ), name='password_reset_confirm'),


    #path('test', test, name = 'test'),
