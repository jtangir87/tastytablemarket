from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import send_mail
from django.http import JsonResponse

from .forms import ContactUsForm

# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/home.html"


def contact_us(request):
    data = dict()
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]

            context = {
                "name": name,
                "email": email,
                "phone": form.cleaned_data["phone"],
                "subject": subject,
                "message": form.cleaned_data["message"],
            }
            ### SEND EMAIL ###

            template = get_template("pages/emails/contact_us.txt")
            content = template.render(context)
            send_mail(
                subject,
                content,
                "{}<{}>".format(name, email),
                ["chad@exteriordd.com"],
                fail_silently=False,
            )

            data["html_success_message"] = render_to_string(
                "pages/includes/partial_contact_success.html", request=request,
            )
            data["form_is_valid"] = True

        else:
            data["form_is_valid"] = False
    return JsonResponse(data)
