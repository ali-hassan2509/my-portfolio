from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import About, Skill, Project

def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')

        if name and email and subject and message_body:
            try:
                full_message = f"Message from: {name} ({email})\n\n{message_body}"
                send_mail(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully! Thank you.')
            except Exception as e:
                messages.error(request, f'An error occurred: {e}. Please try again.')
        else:
            messages.error(request, 'Please fill out all the fields in the contact form.')
        
        return redirect(reverse('home') + '#contact')

    about = About.objects.first()
    
    # Get skills and projects
    all_skills = Skill.objects.order_by('-level')
    frontend_skills = all_skills.filter(category='FRONTEND')
    backend_skills = all_skills.filter(category='BACKEND')
    projects = Project.objects.all().order_by('display_order')

    context = {
        'about': about,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'projects': projects,
    }
    return render(request, 'main/home.html', context)
