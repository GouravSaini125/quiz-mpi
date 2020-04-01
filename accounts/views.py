from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from quizApp.models import Quiz
from .models import Attempted


def register(request):
    if request.method == 'POST':
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        email = request.POST["email"].strip().lower()
        name = request.POST["name"]
        roll = request.POST["roll"]

        if password == confirm_password:
            try:
                User.objects.get(username=email)
                return render(request, 'register.html', {'error': 'User already exists.'})

            except User.DoesNotExist:
                try:
                    User.objects.create_user(username=roll, password=password, email=email, first_name=name)
                    user = auth.authenticate(username=roll, password=password)
                    auth.login(request, user)
                    return redirect('index')
                except:
                    return render(request, 'register.html', {'error': 'Something Went Wrong!'})

        else:
            return render(request, 'register.html', {'error': 'Password didn\'t match.'})

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['roll'].strip().lower(), password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(request.GET.get('next', 'index'))
        return render(request, 'login.html', {'error': 'Invalid Credentials...'})
    else:
        return render(request, 'login.html')


@login_required(login_url='/accounts/')
def logout(request):
    auth.logout(request)
    return redirect('index')


@login_required(login_url='/accounts/')
def profile(request):
    return render(request, 'profile.html', {'attempted': Attempted.objects.filter(user=request.user).order_by('-created')})


@login_required(login_url='/accounts/')
def submit(request, id):
    if request.method == 'POST':
        got = 0
        quiz = get_object_or_404(Quiz, pk=id)
        for que in quiz.questions.all():
            if que.answer == request.POST[f'{que.id}']:
                got += que.credit
        Attempted.objects.create(user=request.user, quiz=quiz, got=got)
        return redirect('profile')
    else:
        return redirect('index')
