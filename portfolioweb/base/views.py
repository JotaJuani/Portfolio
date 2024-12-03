from django.shortcuts import render, redirect
from .models import Project, Skill, Endorsement
from .forms import ProjectForm, SkillForm, EndorsementForm, CommentForm, QuestionForm, CountryForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')

    skills = Skill.objects.filter(body='')
    
    endorsement = Endorsement.objects.filter(approved=True)

    context = {'projects': projects, 'skills': skills,
               'detailedSkills': detailedSkills,
               
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
               'comments': comments, 'form': form,}

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

    return render(request, 'base/chart.html', {'Countryform': Countryform, 'Questionform': Questionform,})
