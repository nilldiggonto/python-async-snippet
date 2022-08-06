from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_email_task
# Create your views here.
class SendMailView(APIView):
    def post(self,request):
        title   =   request.data['title']
        email   =   request.data['email']
        content =   request.data['content']

        send_email_task.delay(title,email,content)
        return Response({'status':"mail sent"})

        
