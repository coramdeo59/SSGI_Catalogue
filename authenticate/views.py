from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from validate_email import validate_email
from django.contrib import messages
from django.contrib import auth
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator
from django.utils.encoding import force_str
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import AbstractUser

User = get_user_model()

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        feedback = UserFeedbacks(name=name, email=email, message=message)
        feedback.save()
        
        # return JsonResponse({'message': 'Feedback saved successfully'})
        
    return render(request, 'authenticate/login.html')



def password_reset_form(request):
       return render(request, 'authenticate/passwordreset.html')
class FirstnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        firstname = data['firstname']
        if not str(firstname).isalnum():
            return JsonResponse({'firstname_error': 'First name should only contain alphanumeric characters'}, status=400)

        return JsonResponse({'firstname_valid': True})

class MiddlenameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        middlename = data['middlename']
        if not str(middlename).isalnum():
            return JsonResponse({'middlename_error': 'Middle name should only contain alphanumeric characters'}, status=400)

        return JsonResponse({'middlename_valid': True})
class LastnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        lastname = data['lastname']
        if not str(lastname).isalnum():
            return JsonResponse({'lastname_error': 'Last name should only contain alphanumeric characters'}, status=400)

        return JsonResponse({'lastname_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': ' Username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid': True})

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid': True})
    
class PasswordValidationView(View):

    def post(self, request):
        data = json.loads(request.body)
        password = data['password']
        if len(password) < 6:
            return JsonResponse({'password_error': 'Password too short'}, status=400, safe=False)

        return JsonResponse({'password_valid': True}, safe=False)

class ConfirmPasswordValidationView(View):
    def post(self, request):
        data = json.loads(request.body)

        confirmpassword = data['confirmpassword']
        password=data['password']
        print(password)

        if confirmpassword!=password :
            return JsonResponse({'confirm_password_error': "Input in the confirm password doesn't match the Password field"}, status=400, safe=False)

        return JsonResponse({'confirm_password_valid': True}, safe=False)
    
class CountryView(View):

    def post(self, request):
        data = json.loads(request.body)
        country = data['country']
        if country:
            print(country)
            return JsonResponse({'country_valid': True}, safe=False)
        return JsonResponse({'country_error': 'Please select country'}, status=400, safe=False)

class SectorView(View):
    def post(self,request):
        
        data = json.loads(request.body)
        sector = data['sector']
        if sector:
            print(sector)
            return JsonResponse({'sector_valid': True}, safe=False)
        return JsonResponse({'sector_error': 'Please select sector'}, status=400, safe=False)

class InstituteView(View):
        def post(self,request):
            data = json.loads(request.body)
            institute = data['institute']
            if institute:
                print(institute)
                return JsonResponse({'institute_valid': True}, safe=False)
            return JsonResponse({'institute_error': 'Please select institute'}, status=400, safe=False)

global_array = []
class DataPurposeView(View):
    def post(self, request):
        data = json.loads(request.body)
        usage_purposes = data.get('usage_purposes')  # Use the same variable name as sent from the client
        print(usage_purposes)
        if usage_purposes:
            # global_array.extend(usage_purposes)  # Append new values to the global array
            usage_array_length=len(usage_purposes)
            global_array.append(usage_purposes[usage_array_length-1])
            print("hisdjscn",global_array)
            return JsonResponse({'usage_purpose_valid': True}, safe=False)
        else:
            return JsonResponse({'usage_purpose_error': 'Please select at least one usage purpose'}, status=400, safe=False)

class RegistrationView(View):
    def get(self,request):

        return render(request,'authenticate/register.html')

    def post(self,request):
        # messages.success(request,"Success")
        # messages.warning(request,"Success")
        # messages.info(request,"Success")
        # messages.error(request,"Success")
        context={
            'fieldValues':request.POST #This is a context (dictionary) that contains everything that has been posted
        }
        firstname=request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        country=request.POST['country']
        sector=request.POST['sector']
        institute=request.POST['institute']
        country=request.POST['country']
        usage_purposes = global_array # Use 'usage_purpose[]' as the key to retrieve the list

        confirmPassword=request.POST['confirmpassword']
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request,"Password too short")
                    return render(request,'authenticate/register.html',context)
                if password!=confirmPassword:
                    messages.error(request,"Password doesn't match the confirm password field")
                    return render(request,'authenticate/register.html',context)
                if not (firstname and middlename and lastname and username and email and password and country and sector and institute and usage_purposes):
                    reset_global_array()
                    messages.error(request, "Please fill in all the required fields")
                    return render(request, 'authenticate/register.html',context)      
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,middle_name=middlename,last_name=lastname,country=country,work_sector=sector,institute=institute,data_purpose=usage_purposes,is_active=True)
                    user.set_password(password)
                    
                    user.is_active=True
                    user.save()
                    reset_global_array()

                domain=get_current_site(request).domain
                uidb64=urlsafe_base64_encode(force_bytes(user.pk))
                token=token_generator.make_token(user)
                link=reverse('activate',kwargs={'uidb64':uidb64,'token':token})
                activate_url='http://'+domain+link
                email_subject='Activate your account'
                email_body='Hi '+user.username+' Please use the following link to verify your account. \n'   + activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@example.com',
                    [email],
                )
                email.send(fail_silently=False)
                messages.success(request, "Account created successfully. Activate your account to login. ")
                return render(request,'authenticate/register.html')
            messages.error(request,"User exists with this email")
            return render(request,'authenticate/register.html',context)
        messages.error(request,"Username already existed. Please choose another one.")


        return render(request,'authenticate/register.html')
        



# Reset the global_array
def reset_global_array():
    global global_array
    global_array = []
   
class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass
        return redirect('login')

class LoginView(View):
    def get(self,request):
        return render(request,'authenticate/login.html')
    
    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']

        if username and password:
            user=auth.authenticate(username=username,password=password)
            
            
            #TODO adjust the activation
            

            if user:
                if user.is_active:
                    auth.login(request,user)
                    # messages.success(request,"Welcome, "+user.username+" You are now logged in")
                    return redirect("fill_form")

                messages.error(request,"Account not active. Check your email")
                return render(request,'authenticate/login.html')
            messages.error(request,"Invalid Credentials, Try again")
            return render(request,'authenticate/login.html')
        messages.error(request,"Fill all fields")
        return render(request,'authenticate/login.html')



class ResetPasswordEmail(View):
    def get(self,request):
        return render(request,'authenticate/passwordresetemail.html')
    def post(self,request):
        email_add = request.POST.get('email')
        request.session['email_add'] = email_add 
        try:
            user = User.objects.get(email=email_add)
        except User.DoesNotExist:
            # Email does not exist in the auth_user table
            messages.error(request, "Email does not exist. Enter an email that you have registered with before.")
            return render(request, 'authenticate/login.html')

        domain = get_current_site(request).domain
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        reset_password_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        reset_password_link = 'http://' + domain + reset_password_url

        # Create the email body as both plain text and HTML
        email_subject = 'Password Reset'
        email_text = f"Hi {user.username}, please use the following link to reset your password: {reset_password_link}"
        # email_html = render_to_string('authenticate/password_reset_email.html', {'username': user.username, 'reset_password_link': reset_password_link})

        # Send the email
        email = EmailMessage(email_subject, email_text, 'noreply@example.com', [email_add])
        # email.attach_alternative(email_html, 'text/html')
        email.send(fail_silently=False)
        messages.success(request, "Password reset email sent to "+email_add+" Check your email")
        return render(request,'authenticate/login.html')

class PasswordResetVerificationView(View):
    def get(self, request, uidb64, token):
        return render(request,'authenticate/passwordreset.html')

      
class NewPasswordVerificationView(View):
    def post(self, request):
        data = json.loads(request.body)
        newpassword = data['newpassword']
        if len(newpassword) < 6:
            return JsonResponse({'new_password_error': 'Password too short'}, status=400, safe=False)
        else:
            return JsonResponse({'new_password_valid': True}, safe=False)
    
class NewConfirmPasswordVerificationView(View):
    def post(self, request):
        data = json.loads(request.body)

        newconfirmpassword = data['newconfirmpassword']
        newpassword=data['newpassword']
        print(newpassword)

        if newconfirmpassword!=newpassword :
            return JsonResponse({'new_confirm_password_error': "Input in the confirm password doesn't match the Password field"}, status=400, safe=False)
        else:
            return JsonResponse({'new_confirm_password_valid': True}, safe=False)


class UpdatePassword(View):
    def get(self,request):
        return render(request,'authenticate/passwordreset.html')
    def post(self,request):
        context={
            'fieldValues':request.POST #This is a context (dictionary) that contains everything that has been posted
        }
        email_add = request.session.get('email_add')
        print(email_add)
        newpassword=request.POST['newpassword']
        newconfirmpassword=request.POST['newconfirmpassword']
        if newpassword == newconfirmpassword:
            user = User.objects.get(email=email_add)  # Assuming the logged-in user's username is used
            user.set_password(newpassword)
            user.save()
            messages.success(request,"Password updated successfully")
            return render(request,'authenticate/login.html')

        
class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        # messages.success(request,"You have been logged out")
        return redirect('home')