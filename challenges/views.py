from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
        return HttpResponseNotFound("<h1>invalid month!</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        resposnse_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(resposnse_data)
    except:
        return HttpResponseNotFound('<h1>This Month is not supported!!!!!</h1>')
