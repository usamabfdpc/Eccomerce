from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serilizer import UserSerilizer,VarifyAccountSerilizer
from .emails import send_otp_via_email

# Create your views here.

class RegisterAPI(APIView):
    def post(self,request):
        try:
            data = request.data
            serilizer  = UserSerilizer(data = data)
            if serilizer.is_valid():
                serilizer.save()
                send_otp_via_email(serilizer.data['email'])
                return Response({
                    'status':200,
                    'message':'registration successfully check email',
                    'data':serilizer.data
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serilizer.errors
            })

        except Exception as e:
            print(e)


class VerifyOTP(APIView):
    def post(self,request):
        try:
            data = request.data
            serilizer = VarifyAccountSerilizer(data=data)
            if serilizer.is_valid():
                email = serilizer.data['email']
                otp = serilizer.data['otp']

                user = User.objects.get(email = email)

                if not user:
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'invalid Email'
                    })
                if user.otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'wrong otp'
                    })
                
                user.is_verified = True
                user.save()
                
                return Response({
                    'status': 200,
                    'message': 'User is Verified',
                    'data': {}
                })
                

                

        except Exception as e:
            print(e)


