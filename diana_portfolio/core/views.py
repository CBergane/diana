from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail

from .models import Biography, Service, Portfolio, Testimonial, ClientPartner



def front(request):
    return render(request, 'core/front.html')

def portfolio(request):
    # Fetch all portfolio entries
    portfolios = Portfolio.objects.all()
    return render(request, 'core/portfolio.html', {'portfolios': portfolios})

def biography(request):
    # Fetch the biography entry, assuming you have only one.
    # If there's no entry, it defaults to None.
    biography_entry = Biography.objects.first()
    return render(request, 'core/biography.html', {'biography': biography_entry})

def services(request):
    # Fetch all services
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def clients(request):
    # Fetch all testimonials and client-partners
    testimonials = Testimonial.objects.all()
    client_partners = ClientPartner.objects.all()
    return render(request, 'core/clients.html', {'testimonials': testimonials, 'client_partners': client_partners})

def send_contact_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('companyName')
        email = request.POST.get('email')
        phone_number = request.POST.get('phoneNumber')
        message = request.POST.get('message')

        # Send email
        try:
            send_mail(
                subject=f"New contact request from {name}",
                message=f"From: {name}\nCompany: {company_name}\nEmail: {email}\nPhone: {phone_number}\n\n{message}",
                from_email=email,
                recipient_list=['destination_email@example.com'],
            )
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "error": str(e)})
    return JsonResponse({"status": "invalid"})