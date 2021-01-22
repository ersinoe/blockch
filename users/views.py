from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, NoteForm, DocumentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from notechainapp.models import Note, User
import json
from datetime import datetime
from hashlib import sha256

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Hesap başarıyla oluşturuldu!")
            return redirect("users-login")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form":form})

@login_required
def profile(request):

    context = {"title": "Home"}

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profil bilgileri başarıyla güncellendi!")
            return redirect("users-profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context["u_form"] =  u_form
    context["p_form"] = p_form


    return render(request, "users/profile.html", context)

@login_required
def notes(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note.mineNote(2)
            note.save()
            messages.success(request, "Not başarıyla eklendi!")
            return redirect("users-notes")
    else:
        form = NoteForm()

    context = {"notes": Note.objects.filter(owner=request.user), "form":form}
    return render(request, "users/notes.html", context)

@login_required
def protect(request, id):
    note = Note.objects.filter(id=id)
    note.update(is_protected=True, date_protected=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    filename = "Note"+str(id)+".txt"
    content = str(note[0].owner.username) + "|" + str(note[0].title) + "|" + str(note[0].description) + "|" + str(note[0].nonce)
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)

    return response

@login_required
def checkprotection(request):
    note_owner = ""
    note_protection_date = ""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['docfile']
            content = docfile.read().decode(encoding='UTF-8')
            lis = []
            m = ""
            for char in content:
                if char == "|":
                    lis.append(m)
                    m = ""
                else:
                    m += char
            lis.append(m)
            uname = lis[0]
            tit = lis[1]
            descr = lis[2]
            nonc = lis[3]
            for note in Note.objects.all():
                if note.title == tit:
                    if note.description == descr:
                        if str(note.nonce) == nonc:
                            if str(note.owner) == uname:
                                note_owner = note.owner.username
                                note_protection_date = note.date_protected

            if note_owner != "" or note_protection_date != "":
                messages.success(request, "Bu belge, " + note_protection_date + " tarihinde " + note_owner + " tarafından korumaya alınmıştır.")
            else:
                messages.warning(request, "Bu belge, koruma altında değil veya değiştirilmiştir.")

    else:
        form = DocumentForm()

    return render(request, "users/checkprotection.html", {"form":form})

@csrf_exempt
def authenticate(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]

    for user in User.objects.all():
        if str(user.username) == username:
            if str(user.profile.secret_passcode) == password:
                return HttpResponse("Login Success")
    return HttpResponse("Login Failed")

