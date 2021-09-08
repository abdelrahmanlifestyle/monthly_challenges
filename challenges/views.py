from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
from django.shortcuts import render

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
    "december": None
}


# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })

    # for month in months:
    #     capitalized__month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized__month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>invalid month!</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        # challenge_text = monthly_challenges[month]
        # resposnse_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(resposnse_data)
        challenge_text = monthly_challenges[month]
        # month_name = month.capitalize()
        month_name = month
        return render(request, "challenges/challenge.html", {
            "month_name": month_name,
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound('<h1>This Month is not supported!!!!!</h1>')
