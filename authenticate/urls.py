from django.urls import path
from . import views
from .views import RegistrationView,UsernameValidationView,EmailValidationView, LoginView,LogoutView,VerificationView,FirstnameValidationView,LastnameValidationView,\
                MiddlenameValidationView,PasswordValidationView,ConfirmPasswordValidationView,CountryView,SectorView,InstituteView,DataPurposeView, ResetPasswordEmail,\
                    PasswordResetVerificationView,NewPasswordVerificationView,NewConfirmPasswordVerificationView,UpdatePassword,submit_feedback

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('submit-feedback', submit_feedback, name='submit_feedback'),   

     path('login', LoginView.as_view(), name="login"),
     path('logout', LogoutView.as_view(), name="logout"),
     path('register', RegistrationView.as_view(), name="register"),
     path('passwordresetemail',ResetPasswordEmail.as_view(), name='passwordresetemail'),
     # path('passwordreset',ResetPassword.as_view(), name='passwordreset'),
     path('newpassowrdset',UpdatePassword.as_view(), name='newpassowrdset'),
     path('validate-newpassword', csrf_exempt(NewPasswordVerificationView.as_view()),         
          name="validate-newpassword"),
     path('validate-newconfirmpassword', csrf_exempt(NewConfirmPasswordVerificationView.as_view()),         
          name="validate-newconfirmpassword"),
     path('validate-firstname', csrf_exempt(FirstnameValidationView.as_view()),         
          name="validate-firstname"),
     path('validate-middlename', csrf_exempt(MiddlenameValidationView.as_view()),         
          name="validate-middlename"),
     path('validate-lastname', csrf_exempt(LastnameValidationView.as_view()),         
          name="validate-lastname"),
     path('validate-username', csrf_exempt(UsernameValidationView.as_view()),         
          name="validate-username"),
     path('validate-email', csrf_exempt(EmailValidationView.as_view()),         
          name="validate-email"),
     path('validate-password', csrf_exempt(PasswordValidationView.as_view()),         
          name="validate-password"),
     path('validate-confirmpassword', csrf_exempt(ConfirmPasswordValidationView.as_view()),         
          name="validate-confirmpassword"),
          path('validate-country', csrf_exempt(CountryView.as_view()),         
          name="validate-country"),
          path('validate-sector', csrf_exempt(SectorView.as_view()),         
          name="validate-sector"),
          path('validate-institute', csrf_exempt(InstituteView.as_view()),         
          name="validate-institute"),
          path('validate-datapurpose', csrf_exempt(DataPurposeView.as_view()),         
          name="validate-datapurpose"),
          path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),

          path('reset/<uidb64>/<token>', PasswordResetVerificationView.as_view(), name="password_reset_confirm"),


         ]


