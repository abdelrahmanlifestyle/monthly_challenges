from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenges(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = ' ICE BUCKET CHALLENGE'
    elif month == 'february':
        challenge_text = ' FOOD CHALLENGE'
    elif month == 'march':
        challenge_text = ' CINNAMON  CHALLENGE'
    elif month == 'april':
        challenge_text = ' RAW ONION CHALLENGE'
    elif month == 'june':
        challenge_text = ' THE WASABI CHALLENGE'
    elif month == 'july':
        challenge_text = ' HOT PEPPER CHALLENGE'
    elif month == 'august':
        challenge_text = ' WARHEAD CHALLENGE'
    elif month == 'september':
        challenge_text = ' LEMON CHALLENGE'
    elif month == 'october':
        challenge_text = ' LIME CHALLENGE'
    elif month == 'november':
        challenge_text = ' CHUBBY BUNNY CHALLENGE'
    elif month == 'december':
        challenge_text = ' PIZZA CHALLENGE'
    else:
        return HttpResponseNotFound('This Month is not supported!!!!!')
    return HttpResponse(challenge_text)
