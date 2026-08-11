#chris, 1234

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import Site

def index(request):
    sites = list(Site.objects.values("site_num", "latitude", "longitude","site_name"))
    context = {
        "sites": sites
    }
    return render(request, "index.html", context)

def about_us(request):
    return render(request, "about_us.html")

def collocation(request):
    return render(request, "collocation.html")

def contact_us(request):
    return render(request, "contact_us.html")

def downloads(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            site_num = form.cleaned_data["site_num"]
            site_loc = form.cleaned_data["site_loc"]
            date = form.cleaned_data["date"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            issue = form.cleaned_data["issue"]
            other_issue = form.cleaned_data["other_issue"]
            message = form.cleaned_data["message"]

            issue_text = ", ".join(issue)
            send_mail(
                subject=f"Contact form from {name}",
                message=f"""
            Site number: {site_num}
            Site location: {site_loc}
            Date: {date}
            Name: {name}
            Email: {email}
            Phone: {phone}
            Issue: {issue_text}
            Other issue: {other_issue}
            Message:
            {message}
            """,
                from_email=email,
                recipient_list=["you@company.com"],
            )

            messages.success(request, "Thank you for contacting us. Your message has been sent.")
            return redirect("downloads")

    else:
        form = ContactForm()

    return render(request, "downloads.html", {"form": form})

def towers(request):
    sites = list(Site.objects.values("site_num", "latitude", "longitude","site_name"))
    context = {
        "sites": sites
    }

    return render(request, "towers.html", context)

def towers_list(request):
    sites = Site.objects.all()

    context = {
        "sites":sites,
    }
    return render(request, "towers_list.html",context)

def towers_bystate(request, address_state):
    sites = Site.objects.filter(address_state=address_state)
    context = {
        "sites":sites,
        "state":address_state
    }
    return render(request, "towers_list.html",context)

def tower_page(request, site_name):
    site = Site.objects.get(site_name=site_name)
    photos_for_page = []  
    photos = site.photos.all()
    for photo in photos:
        readable_name = photo.image.name[13:].partition(".")[0].replace("-"," ")
        photos_for_page.append({
            "photo":photo,
            "name":readable_name,
        })
    context = {
        "site":site,
        "photos_for_page":photos_for_page
    }
    return render(request, "tower_page.html",context)

def state_list(request):
    states = Site.objects.values("address_state").distinct()
    context = {
        "states":states
    }
    return render(request, "state_list.html",context)

