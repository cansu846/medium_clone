from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from page.views import home_view
from django.contrib import messages
from django.contrib.auth.models import User

from user_profile.models import Profile

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f"{request.user.username} Daha önceden giriş yapmışsınız...")
        return redirect("home_view_name")
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("coming_username: ", username)
        print("coming_password: ", password)

        if len(username)<3 or len(password)<3:
            messages.warning(request, "Parola veya kullanıcı adı 3 ten küçük olamaz...")
            return redirect("user_profile:login_view_name")
        
        user = authenticate(request, username=username, password=password)
        print("incoming user: ", user)
        if user is not None:
            login(request,user)
            messages.success(request, f"{request.user.username} başarıyla giriş yaptınız...")
            return redirect("/")
        else:
            messages.error(request, "Geçersiz kullanıcı adı veya parola.")

    context = dict()
    return render(request, 'user_profile/login.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, f"{request.user.username} Başarılı şekilde çıkış yapıldı...")
    return redirect("/")

def register_view(request):
    context = dict()
    if request.method=="POST":
        print(request.POST)
        post_info = request.POST
        username = post_info.get("username")
        username_confirm = post_info.get("username_confirm")
        password = post_info.get("password")
        password_confirm = post_info.get("password_confirm")
        email = post_info.get("email")
        email_confirm = post_info.get("email_confirm")
        instagram = post_info.get("instagram")

        print("password: ", password, "username: ", username)

        if username!=username_confirm:
            messages.warning(request, "Username ile Username confirm bilgisi uyuşamamaktadır...")
        if password!=password_confirm:
            messages.warning(request, "Password ile password confirm bilgisi uyuşamamaktadır...")
        if email!=email_confirm:
            messages.warning(request, "Gmail ile gmail confirm bilgisi uyuşamamaktadır...")
        

        user,created = User.objects.get_or_create(username=username)
        print(user)
        if not created:
            user = authenticate(request, username=email, password=password)
            print("authenticated_user:", user)
            if user is not None:
                messages.success(request, "Daha önce kayıt olmuşssunuz..Ana sayfaya yönlendiriliyorsunuz..")
                login(request, user)
                return redirect("/")
            messages.success(request, f"{request.user.username} Daha önce kayıt oluşturmuşsunuz..Login sayfasına yönkendiriliyorsunuz...")
            return redirect("user_profile:login_view_name")
        
        user.email = email
        user.username = username
        user.set_password(password)

        profile, created = Profile.objects.get_or_create(user=user)
        profile.instagram = instagram

        messages.success(request, f"{user.username} Sisteme kaydedildiniz...")
        user_login = authenticate(request, username=username, password=password)
        login(request, user_login)
        return redirect("home_view_name")
    
    return render(request, "user_profile/register.html", context)