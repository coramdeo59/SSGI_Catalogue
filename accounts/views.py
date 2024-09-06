from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        
        try:
            firstname=data['firstname']
            middlename=data['middlename']
            lastname=data['lastname']
            username=data['username']
            email=data['email']
            password=data['password']
            country=data['country']
            sector=data['sector']
            institute=data['institute']
            usage_purposes = data['usage_purposes']
            confirmPassword=data['confirmpassword']
        except:
            return Response({'error': 'Please fill all the fields.'})

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    return Response({'error': 'Password is too short.'})
                if password!=confirmPassword:
                    return Response({'error': 'Passwords don\'t match.'})
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,middle_name=middlename,last_name=lastname,country=country,work_sector=sector,institute=institute,data_purpose=usage_purposes,is_active=True)
                    user.set_password(password)
                    user.save()
                    return Response({'success': 'An account was created successfully.'})
            else:
                return Response({'error': 'An account already exists with this email.'})
        else:
            return Response({'error': 'An account already exists with this username.'})