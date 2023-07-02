from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib import messages
from prsmsp.panel import Panel

from app.models import SmsPanel, Sms
from app.forms import SmsPanelForm, SmsForm

def index(request):
    smses = Sms.objects.all()
    panel_smses = SmsPanel.objects.all()
    total_sms = smses.count()
    total_sms_panel = panel_smses.count()

    return render(request, "index.html", {
        "total_sms": total_sms,
        "total_sms_panel": total_sms_panel,
    })

def add_panel(request):

    if request.method == "POST":
        form = SmsPanelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"{form.data.get('panel','')} panel added successfully")
        else:
            messages.error(request, "Invalid Form")
    else:
        form = SmsPanelForm()

    return render(request, "add_panel.html", {
        "form": form,
    })

def send_sms_with_panel(request):
    resp = ""

    if request.method == "POST":
        form = SmsForm(request.POST)

        if form.is_valid():
            form.save()
            data = form.cleaned_data
            #return JsonResponse(data["panel"].panel, safe=False)
            #panel_obj = SmsPanel.objects.get(data["panel"])
            panel_obj = data["panel"]

            if panel_obj.username and panel_obj.password:
                auth = {
                    'username': panel_obj.username,
                    'password': panel_obj.password,
                }
            else:
                auth = {
                    'api_key': panel_obj.api_key
                }

            p = Panel.initiate(panel_obj.panel, **auth)
            if data["originator"]:
                resp = p.send_sms(data["receptor"], data["message"])
            else:
                resp = p.send_sms(data["receptor"], data["message"], data["originator"])
            messages.success(request, f"sms sent to {form.data.get('receptor','')} successfully")
        else:
            messages.error(request, "Invalid Form")
    else:
        form = SmsForm()

    return render(request, "send_sms.html", {
        "form": form,
        "resp": resp or "",
    })