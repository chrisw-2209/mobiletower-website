#chris, 1234

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Site

def index(request):
    return render(request, "index.html")

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
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"Contact form from {name}",
                message=message,
                from_email=email,
                recipient_list=["you@company.com"],
            )

            return redirect("downloads")

    else:
        form = ContactForm()

    return render(request, "downloads.html", {"form": form})

def towers(request):
    return render(request, "towers.html")

def towers_list(request):
    sites = Site.objects.all()

    context = {
        "sites":sites
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