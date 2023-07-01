from django.shortcuts import render
from django.contrib import messages

from app.forms import SmsPanelForm, SmsForm

def index(request):
    return render(request, "index.html")

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

    if request.method == "POST":
        form = SmsForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"sms sent to {form.data.get('receptor','')} successfully")
        else:
            messages.error(request, "Invalid Form")
    else:
        form = SmsForm()

    return render(request, "send_sms.html", {
        "form": form,
    })