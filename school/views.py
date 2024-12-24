from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_request, logout
from django.shortcuts import render , redirect 
import json
from django.http import JsonResponse
from django.contrib.auth.models import User 
from django.contrib import messages



# Create your views here.
def login(request):
    if request.user.is_authenticated:
        # Vérifie les relations utilisateur
        if hasattr(request.user, 'student_user') and request.user.student_user is not None:
            return redirect('dashboard')
        elif hasattr(request.user, 'instructor') and request.user.instructor is not None:
            return redirect('dashboard')
        else:
            # Redirige vers /admin si aucune relation spécifique
            return redirect('/admin/')
    else:
        # Affiche la page de connexion pour les invités
        return render(request, 'pages/guest-login.html', {})







def signup(request):
    if request.user.is_authenticated:
        # Rediriger les utilisateurs déjà connectés
        if hasattr(request.user, 'student_user'):
            return redirect('index_student')
        elif hasattr(request.user, 'instructor'):
            return redirect('dashboard')
        else:
            return redirect('/admin/')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not name or not email or not password or not password2:
            messages.error(request, "Tous les champs sont requis.")
            return redirect('guests_signup')

        if password != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('guests_signup')

        if User.objects.filter(username=name).exists():
            messages.error(request, "Un utilisateur avec ce nom existe déjà.")
            return redirect('guests_signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Un utilisateur avec cet email existe déjà.")
            return redirect('guests_signup')

        # Création de l'utilisateur
        try:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            messages.success(request, "Inscription réussie. Vous pouvez vous connecter.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Erreur lors de l'inscription : {e}")
            return redirect('guests_signup')
    
    # Rendre la page d'inscription si méthode GET
    return render(request, 'pages/guest-signup.html', {})
 



def forgot_password(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    return redirect('dashboard')
        except:
            print("3")
            return redirect("/admin/")
    else:
        datas = {

        }
        return render(request, 'pages/guest-forgot-password.html', datas)



def islogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login_request(request, user)
            try:
                if hasattr(user, 'student_user'):
                    return redirect('index_student')
                elif hasattr(user, 'instructor'):
                    return redirect('dashboard')
                else:
                    return redirect('/admin/')
            except Exception as e:
                print(f"Erreur lors de la redirection après connexion : {e}")
                messages.error(request, "Erreur interne. Veuillez réessayer.")
        else:
            messages.error(request, "Vos identifiants ne sont pas corrects.")
    else:
        messages.error(request, "Méthode non autorisée.")
    return redirect('login')


    
def deconnexion(request):
    logout(request)
    return redirect('login')