from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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

def dashboard(request):
    user_id = request.user.id
    username = request.user.username
    form = PasswordChangeForm(request.user, request.POST or None)

    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('dashboard')
    return render(request, "dashboard.html", {
        "user_id": user_id,
        "username": username,
        'form': form
    })

@login_required
def ganti_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'dashboard.html', {
        'form': form
    })

@login_required
def data_mahasiswa(request):
    query = request.GET.get("q")
    if query:
        data_mhs = Mahasiswa.objects.filter(nim__icontains=query)
    else:
        data_mhs = Mahasiswa.objects.all()

    return render(request, "mahasiswa.html", {
        "dt_mhs": data_mhs
    })

# Mahasiswa
@login_required
def create(request):
    if request.method == "POST":
        nim = request.POST.get("nim")
        nama = request.POST.get("nama")
        email = request.POST.get("email")
        nomor = request.POST.get("no")

        Mahasiswa.objects.create(
            nim = nim,
            nama = nama,
            email = email,
            nomor = nomor
        )
        return redirect("dashboard")

    return render (request, "CRUD/mahasiswa/create.html")

@login_required
def edit(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)

    if request.method == "POST":
        mhs.nim = request.POST.get("nim")
        mhs.nama = request.POST.get("nama")
        mhs.email = request.POST.get("email")
        mhs.nomor = request.POST.get("nomor")

        if "profile" in request.FILES:
            mhs.profile = request.FILES["profile"]

        mhs.save()
        return redirect("dashboard")

    return render(request, "CRUD/mahasiswa/edit.html", {"mhs": mhs})

def hapus(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)
    mhs.delete()
    return redirect('dashboard')

# Prodi
def data_prodi(request):
    query = request.GET.get("q")
    if query:
        data_prd = Prodi.objects.filter(nama_prodi__icontains=query)
    else:
        data_prd = Prodi.objects.all()

    return render(request, "prodi.html", {
        "dt_prd": data_prd
    })

@login_required
def create_prodi(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        jurusan_id = request.POST.get("id_jurusan")

        Prodi.objects.create(
            nama_prodi = nama,
            id_jurusan_id=jurusan_id
        )
        return redirect("prodi")
    
    jr = Jurusan.objects.all()

    return render (request, "CRUD/prodi/create.html", {"jr": jr})

@login_required
def edit_prodi(request, id):
    prd = get_object_or_404(Prodi, id=id)

    if request.method == 'POST':
        prd.nama_prodi = request.POST.get('nama_prodi')
        prd.id_jurusan_id = request.POST.get('id_jurusan')
        prd.save()
        return redirect('prodi')
    
    jr = Jurusan.objects.all()

    return render(request, "CRUD/prodi/edit.html", {
        "prd": prd,
        "jr": jr
    })

def hapus_prodi(request, id):
    prd = get_object_or_404(Prodi, id=id)
    prd.delete()
    return redirect('prodi')

# Jurusan
def data_jurusan(request):
    query = request.GET.get("q")
    if query:
        data_jurusan = Jurusan.objects.filter(nama_jurusan__icontains=query)
    else:
        data_jurusan = Jurusan.objects.all()

    return render(request, "jurusan.html", {
        "dt_jurusan": data_jurusan
    })

@login_required
def create_jurusan(request):
    if request.method == "POST":
        nama = request.POST.get("nama_jurusan")

        Jurusan.objects.create(
            nama_jurusan = nama,
        )
        return redirect("jurusan")

    return render (request, "CRUD/jurusan/create.html")

@login_required
def edit_jurusan(request, id):
    jr = get_object_or_404(Jurusan, id=id)

    if request.method == 'POST':
        jr.nama_jurusan = request.POST.get('nama_jurusan')
        jr.save()
        return redirect('jurusan')

    return render(request, "CRUD/jurusan/edit.html", {"jr": jr})

def hapus_jurusan(request, id):
    prd = get_object_or_404(Jurusan, id=id)
    prd.delete()
    return redirect('jurusan')