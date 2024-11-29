from django.shortcuts import render, redirect
from .models import Project, Skill, Contact, Endorsement
from .forms import ProjectForm, SkillForm, EndorsementForm, CommentForm, QuestionForm, CountryForm, ContactForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')

    skills = Skill.objects.filter(body='')
    form = ContactForm()
    endorsement = Endorsement.objects.filter(approved=True)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully')

    context = {'projects': projects, 'skills': skills,
               'detailedSkills': detailedSkills,
               'form': form,
               'endorsement': endorsement}
    return render(request, 'base/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    count = project.comment_set.count()
    comments = project.comment_set.all().order_by('-created')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request, 'Comment sent successfully')

    context = {'project': project, 'count': count,
               'comments': comments, 'form': form}

    return render(request, 'base/project.html', context)


def AddProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def EditProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/project_form.html', context)


'''
def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadCount': unreadCount}
    return render(request, 'base/inbox.html', context)
'''


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,)
        if form.is_valid():
            print('the form is valid')
            name = request.cleaned_data['name']
            email = request.cleaned_data['email']
            body = request.cleaned_data['body']

            email_message = EmailMessage(
                subject=f'Contact Form from {name}',
                body=body,
                from_email=email,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],)
            email_message.send(fail_silently=False),
            form.save()
            messages.success(
                request, "Thank you for your message! We'll get back to you shortly.")
            print(email)
            return render(request, 'base/home.html')
    else:
        form = ContactForm()

    context = {'form': form, }
    return render(request, 'base/home.html', context)


'''
def messagePage(request, pk):
    form = MessageForm
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message,
               'form': form}
    return render(request, 'base/message.html', context)
'''


def addSkill(request):
    skill = SkillForm
    if request.method == 'POST':
        form = SkillForm(request.POST)
        form.save()
        messages.success(request, 'Skill saved successfully')
    context = {'skill': skill}
    return render(request, 'base/skill_form.html', context)


def addEndorsement(request):
    form = EndorsementForm
    if request.method == 'POST':
        form = EndorsementForm(request.POST)
        form.save()
        messages.success(
            request, 'Thank you! Your comment was submitted and is pending approval from Juani.')
        return redirect('endorsement-form')
    context = {'form':  form}

    return render(request, 'base/endorsement_form.html', context)


def chartPage(request):
    Questionform = QuestionForm()
    Countryform = CountryForm()

    if request.method == 'POST':
        if 'Questionform' in request.POST:
            Questionform = QuestionForm(request.POST)
            if Questionform.is_valid():
                Questionform.save()
                messages.success(request, 'Thank you for your vote!')
                return redirect('chart')

        if 'Countryform' in request.POST:
            Countryform = CountryForm(request.POST)
            if Countryform.is_valid():
                Countryform.save()
                messages.success(
                    request, 'Thank you for your vote in country!')
                return redirect('chart')

    return render(request, 'base/chart.html', {'Countryform': Countryform, 'Questionform': Questionform})
