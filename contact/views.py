from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            amount = request.POST.get('amount', '')
            address_shop = request.POST.get('address_shop', '')
            references = request.POST.get('references', '')

            # Create the email
            email = EmailMessage(
                "Donate Crown: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["info@taobtc.es"],
                reply_to=[email]
            )

            # Send and redirect
            try:
                email.send()
                # All is good... then redirect at OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Problems, redirect at FAIL
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "contact/contact.html",{'form':contact_form})