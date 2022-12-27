from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import AskmeModel
from .forms import AskmeForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    allquestions = AskmeModel.objects.all().order_by('-datecreated')
    letter_list = ['a', 'b', 'c', 'd', 'e']
   
    return render(request, 'askmeapp/home.html', {'allquestions': allquestions, 'letter_list': letter_list})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'askmeapp/signupuser.html', {'form':UserCreationForm()})
    # create user
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'askmeapp/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username.'})
        else:
        # tell the user the passwords didnt match
            return render(request, 'askmeapp/signupuser.html', {'form':UserCreationForm(), 'error':'Passowrds did not match. Try again!'})

def signinuser(request):
    if request.method == 'GET':
        return render(request, 'askmeapp/signinuser.html', {'form':AuthenticationForm()})
    else:
        # create user
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'askmeapp/signinuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match. Try again!'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def signoutuser(request):
    try:
        request.method == 'POST'
        logout(request)
        return redirect('home')
    except ValueError:
        return render(request, 'askmeapp/home.html')

def allquestions(request):
    allquestions = AskmeModel.objects.all().order_by('-datecreated')
    question_names = request.GET.get('question_names')

    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j']

    if question_names != '' and question_names is not None:
        allquestions = allquestions.filter(title__icontains=question_names)

    paginator = Paginator(allquestions, 10)
    page = request.GET.get('page')
    allquestions = paginator.get_page(page)    
    return render(request, 'askmeapp/allquestions.html', {'allquestions': allquestions, 'letter_list': letter_list})


@login_required
def myquestions(request):
    mines = AskmeModel.objects.filter(user=request.user).order_by('-datecreated')
    message = 'Your question will be in public once Gaai replies. '
    return render(request, 'askmeapp/myquestions.html', {'mines': mines, 'message': message})

@login_required
def checkmines(request, mine_pk):
    mine = get_object_or_404(AskmeModel, pk=mine_pk, user=request.user)
    if request.method == 'GET':
        return render(request, 'askmeapp/checkmines.html', {'mine': mine})

@login_required
def askquestion(request):
    if request.method == 'GET':
        return render(request, 'askmeapp/askquestion.html', {'form':AskmeForm()})
    else:
        try:
            # if request.method == 'POST':
            form = AskmeForm(request.POST)
            newquestion = form.save(commit=False)
            newquestion.user = request.user
            newquestion.save()
            return redirect('myquestions')
        except ValueError:
            return render(request, 'askmeapp/askquestion.html', {'form':AskmeForm(), 'error':'Bad Data. Try again'})

@login_required
def checkdetail(request, detail_pk):
    detail = get_object_or_404(AskmeModel, pk=detail_pk)
    if request.method == 'GET':
        return render(request, 'askmeapp/checkdetail.html', {'detail': detail})

@login_required
def editquestion(request, edit_pk):
    edit = get_object_or_404(AskmeModel, pk=edit_pk, user=request.user)
    if request.method == 'GET':
        form = AskmeForm(instance=edit)
        return render(request, 'askmeapp/editquestion.html', {'edit': edit, 'form':form})
    else:
        try:
            form = AskmeForm(request.POST, instance=edit)
            form.save()
            return redirect('myquestions')
        except ValueError:
            return render(request, 'askmeapp/editquestion.html', {'edit': edit, 'form':form, 'error':'bad info'})

@login_required
def deletequestion(request, question_pk):
    question = get_object_or_404(AskmeModel, pk=question_pk, user=request.user)
    if request.method == 'POST':
        question.delete()
        return redirect('myquestions')
    elif request.method == 'GET':
        return render(request, 'askmeapp/deletequestion.html', {'question':question})





    

