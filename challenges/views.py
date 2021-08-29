from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "ICE BUCKET CHALLENGE",
    "february": "FOOD CHALLENGE",
    "march": "CINNAMON  CHALLENGE",
    "april": "RAW ONION CHALLENGE",
    "june": "THE WASABI CHALLENGE",
    "july": "HOT PEPPER CHALLENGE",
    "august": "WARHEAD CHALLENGE",
    "september": "LEMON CHALLENGE",
    "october": "LIME CHALLENGE",
    "november": "CHUBBY BUNNY CHALLENGE",
    "december": "PIZZA CHALLENGE"
}


# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month!")

    redirect_month = months[month-1]
    return HttpResponseRedirect('/challenges/'+redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This Month is not supported!!!!!')
