from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import ClientForm

from tutoring_website.settings import EMAIL_HOST_USER

# Create your views here.
def client_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

            # extract data from the form.
            cleaned_form_data = form.clean()
            name = cleaned_form_data.get('name')
            email = cleaned_form_data.get('email')
            grade_level = cleaned_form_data.get('grade_level')
            course = cleaned_form_data.get('subject')
            comment = cleaned_form_data.get('comment')

            # construct and send email to myself.
            subject = f'NEW TUTORING STUDENT - {name.upper()}'
            message = f'Student Name: {name}\nEmail: {email}\nGrade Level: {grade_level}\nSubject: {course}\nComment: {comment}'
            send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])

            # construct and send email to the client
            client_subject = 'Form Submitted - Mitchell Daddario Private Tutoring'
            client_message = 'Thank you,\n\nThis is confirmation that your form has been received. Mitchell will reply to this email address within 1 business day with more information!\n\nSincerely,\nMitchell Daddario'
            send_mail(client_subject, client_message, EMAIL_HOST_USER, [email])

            return redirect(reverse('tutoring:client_created'))
    else:
        form = ClientForm()

    return render(request,'tutoring/client_form.html', context={'form':form})


class ClientCreationView(TemplateView):
    template_name = 'tutoring/client_created.html'

class TestimonialView(TemplateView):
    template_name = 'tutoring/testimonials.html'

class AboutView(TemplateView):
    template_name = 'tutoring/about.html'

class PricingView(TemplateView):
    template_name = 'tutoring/pricing.html'
