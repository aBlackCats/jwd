from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import *

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("psw")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render (request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    query = request.GET.get("q")
    if query:
        data_mhs = mahasiswa.objects.filter(nim__icontains=query)
    else:
        data_mhs = mahasiswa.objects.all()

    return render(request, "dashboard.html", {
        "dt_mhs": data_mhs
    })

@login_required
def create(request):
    if request.method == "POST":
        nim = request.POST.get("nim")
        nama = request.POST.get("nama")
        email = request.POST.get("email")
        nomor = request.POST.get("no")

        mahasiswa.objects.create(
            nim = nim,
            nama = nama,
            email = email,
            nomor = nomor
        )
        return redirect("dashboard")

    return render (request, "CRUD/create.html")

@login_required
def edit(request, id):
    mhs = get_object_or_404(mahasiswa, id=id)

    if request.method == "POST":
        mhs.nim = request.POST.get("nim")
        mhs.nama = request.POST.get("nama")
        mhs.email = request.POST.get("email")
        mhs.nomor = request.POST.get("nomor")

        if "profile" in request.FILES:
            mhs.profile = request.FILES["profile"]

        mhs.save()
        return redirect("dashboard")

    return render(request, "CRUD/edit.html", {"mhs": mhs})

def hapus(request, id):
    mhs = get_object_or_404(mahasiswa, id=id)
    mhs.delete()
    return redirect('dashboard')