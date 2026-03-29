from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

from .models import Contact, Project
def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': all_projects})




from django.contrib import messages
from urllib.parse import quote

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # WhatsApp number
        phone_number = "916238031020"

        # Correct message format
        whatsapp_message = f"New Contact Message:\nName: {name}\nEmail: {email}\nMessage: {message}"
        encoded_message = quote(whatsapp_message)

        whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

        # ✅ Add success message
        messages.success(request, "Message sent successfully!")

        return redirect(whatsapp_url)

    return render(request, 'main/contact.html')