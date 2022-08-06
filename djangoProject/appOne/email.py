from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from  django.conf import  settings

def send_email(name,email,content):
    context ={'name':name,'email':email,'content':content}
    email_subject = "test message"
    email_body = render_to_string('mail.txt',context)
    email = EmailMessage(email_subject,email_body,settings.DEFAULT_FROM_EMAIL,[email,])
    return email.send(fail_silently=False)
