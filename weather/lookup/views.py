from django.shortcuts import render
import json
import requests
# Create your views here.


def home(request):
    cateogry_color = None
    categoty_description = ""

    if request.method == "POST":
        zipcode = request.POST["zipcode"]
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=5&API_KEY=E8FE32DD-3182-41AF-9E71-2C1BC86BAE2F")
        try:
            api = json.loads(api_request.content)
        except Exception as error:
            api = "Error..."
        if api[0]['Category']['Name'] == "Good":
            categoty_description = "(0-50) Air quality is satisfactory, and air pollution poses little or no risk."
            cateogry_color = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            categoty_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution"
            cateogry_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            categoty_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            cateogry_color = "unhealthyforsensitivegroups"

        elif api[0]['Category']['Name'] == "Unhealthy":
            categoty_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            cateogry_color ="unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            categoty_description = "Health alert: The risk of health effects is increased for everyone."
            cateogry_color ="veryunhealthy"

        elif api[0]['Category']['Name'] == "Hazardous":
            categoty_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            cateogry_color ="hazardous"

        return render(request, "lookup/home.html", {"api" : api, "categoty_description": categoty_description,
                                                "cateogry_color" : cateogry_color})

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=E8FE32DD-3182-41AF-9E71-2C1BC86BAE2F")
        try:
            api = json.loads(api_request.content)
        except Exception as error:
            api = "Error..."


        if api[0]['Category']['Name'] == "Good":
            categoty_description = "(0-50) Air quality is satisfactory, and air pollution poses little or no risk."
            cateogry_color = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            categoty_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution"
            cateogry_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            categoty_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            cateogry_color = "unhealthyforsensitivegroups"

        elif api[0]['Category']['Name'] == "Unhealthy":
            categoty_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            cateogry_color ="unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            categoty_description = "Health alert: The risk of health effects is increased for everyone."
            cateogry_color ="veryunhealthy"

        elif api[0]['Category']['Name'] == "Hazardous":
            categoty_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            cateogry_color ="hazardous"

        return render(request, "lookup/home.html", {"api" : api, "categoty_description": categoty_description,
                                                "cateogry_color" : cateogry_color})



def about(request):
    return render(request, "lookup/about.html", {})
