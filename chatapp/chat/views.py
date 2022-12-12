from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
PHONE_NUMBNER = os.getenv('PHONE_NUMBNER')

client = Client(ACCOUNT_SID, AUTH_TOKEN)
conversations = {
    "PromoCode" :     """Promo Code is *EngageX2022*

THIS MUST BE APPLIED WHEN UPGRADING THEIR ACCOUNTS
Here are some instructions on how to use the promo code: https://www.twilio.com/blog/apply-promo-code""",

    "Hi": "Welcome to EngageX WorkShop 1.0", 
    "Hello": "Welcome to EngageX WorkShop 1.0",
    "How Are You": "I am Fine, What About You?",
    "Wifi":"""
    SSID: AIO-021
    Pass : AI@_0210"""
}

@csrf_exempt
def webhook(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')
    response = MessagingResponse()
    response.message(conversations.setdefault(message, "Sorry, Can you Ask me another Question"))
    return HttpResponse(str(response))
