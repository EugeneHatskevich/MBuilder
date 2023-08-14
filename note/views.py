from django.shortcuts import render, HttpResponse
from .models import Note
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def register(request):
    if request.method == 'GET':
        return render(request, 'reg.html')
    else:
        data = request.POST
        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password1 = data['password1']
        password2 = data['password2']

        if username is None:
            return HttpResponse('<h1>Enter username</h1>')
        elif first_name is None:
            return HttpResponse('<h1>Enter first_name</h1>')
        elif last_name is None:
            return HttpResponse('<h1>Enter last_name</h1>')
        elif email is None:
            return HttpResponse('<h1>Enter email</h1>')
        elif password1 is None or password2 is None:
            return HttpResponse('<h1>Enter password1 or password2</h1>')
        elif password1 != password2:
            return HttpResponse('<h1>Passwords are not equal</h1>')
        else:
            new_user = User()
            new_user.username = username
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.email = email
            new_user.set_password(password1)
            new_user.save()

            return HttpResponse('<h1>Registration success</h1>')


@csrf_protect
def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        data = request.POST
        username = data['username']
        password = data['password']

        if username is None:
            return HttpResponse('<h1>Enter username</h1>')
        elif password is None:
            return HttpResponse('<h1>Enter password</h1>')
        else:
            user = authenticate(request, username=username, password=password)

            if user is None:
                return HttpResponse('<h1>User does not exist</h1>')

            login(request, user)

            return HttpResponse('<h1>Login success</h1>')


def logout_page(request):
    print(request.user)

    logout(request)

    return HttpResponse('<h1>Logout success</h1>')


def home_page(request):
    print(request.user)

    return HttpResponse('<h1>Home page</h1>')


@csrf_protect
def add_note(request):
    if request.method == 'GET':
        return render(request, 'add_note.html')
    else:
        data = request.POST
        note_text = data['note_text']

        if not bool(note_text):
            return HttpResponse('<h1>Enter note text</h1>')

        print(request.user)

        note = Note()
        note.text = note_text
        note.user = request.user

        note.save()

        return HttpResponse('<h1>Note saved</h1>')


def notes_page(request):
    user_email = request.user.email

    notes = Note.objects.filter(user__email=user_email)
    print(notes)

    return render(request, 'notes.html', {'notes': notes})
