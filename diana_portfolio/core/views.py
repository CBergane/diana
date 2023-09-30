from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Biography, Service, Portfolio, Testimonial, ClientPartner



def front(request):
    return render(request, 'core/front.html')

def portfolio(request):
    # Fetch all portfolio entries
    portfolios = Portfolio.objects.all()
    return render(request, 'core/portfolio.html', {'portfolios': portfolios})

def biography(request):
    # Fetch the two biography entries.
    biography_entry_1 = Biography.objects.first()
    biography_entry_2 = Biography.objects.last()
    return render(request, 'core/biography.html', {
        'biography_1': biography_entry_1,
        'biography_2': biography_entry_2
    })


def services(request):
    # Fetch all services
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def clients(request):
    # Fetch all testimonials and client-partners
    testimonials = Testimonial.objects.all()
    clients = ClientPartner.objects.all()
    return render(request, 'core/clients.html', {'testimonials': testimonials, 'clients': clients})

@csrf_exempt
def send_contact_email(request):
    print("send_contact_email was called")
    if request.method == 'POST':
        print("POST request received")
        
        name = request.POST.get('name')
        company_name = request.POST.get('companyName')
        email = request.POST.get('email')
        phone_number = request.POST.get('phoneNumber')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=f"New contact request from {name}",
                message=f"From: {name}\nCompany: {company_name}\nEmail: {email}\nPhone: {phone_number}\n\n{message}",
                from_email=email,
                recipient_list=['destination_email@example.com'],  # Use actual recipient email
            )
            print("Email sent successfully")
            return JsonResponse({"status": "success"})
        except Exception as e:
            print(f"Error sending email: {str(e)}")  # Log the error message
            return JsonResponse({"status": "error", "error": str(e)})

    print("Not a POST request or failed to send email")
    response = JsonResponse({"status": "success"})
    print(response)  # print the response before returning it
    return response
    return JsonResponse({"status": "invalid"})
