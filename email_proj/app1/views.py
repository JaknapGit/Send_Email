from django.shortcuts import render
from .serializer import Account, AccountSerial
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .util import EmailThread
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger('mylogger')

class AccountView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            post = Account.objects.all()
            serializer = AccountSerial(post, many=True)
            logger.info('Get method executed successfully.')
            return Response(data=serializer.data, status=200)
        except:
            logger.error('Get called and had an error')
            return Response('Bad request', status=400)

    
    def post(self, request):
        try:
            subject = 'Gratitude Mail'
            message = 'Welcome to App Family, Your account created successfully'
            serialized = AccountSerial(data=request.data)
            user_email = request.data.get('email')
            logger.info('post executed and details fetched successfully.')
            if serialized.is_valid():
                serialized.save()
                if user_email:
                    EmailThread(
                        subject=subject,
                        message=message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user_email,]
                    ).start()
                    logger.info('post started thread successfully...')
                return Response('User Created Successfully.')
        except:
            logger.error('post called and had error.')
            return Response('Bad request', status=400)