from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserSignupForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm  # استيراد النموذج المخصص
from .utils import send_welcome_email  # استيراد الوظيفة

def signup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # تسجيل الدخول بعد التسجيل
            messages.success(request, "Account created successfully!")

            # إرسال البريد الإلكتروني الترحيبي
            send_welcome_email(user.email, user.username)

            return redirect('library:home')  # التوجيه إلى الصفحة الرئيسية
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})

# def signup_view(request):
#     if request.method == "POST":
#         form = UserSignupForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)  # تسجيل الدخول بعد التسجيل
#             messages.success(request, "Account created successfully!")
#             return redirect('library:home')  # التوجيه إلى الصفحة الرئيسية
#     else:
#         form = UserSignupForm()

#     return render(request, 'signup.html', {'form': form})

# def login_view(request):
#     if request.method=='POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, "You have successfully logged in.")
#             return redirect('library:home')  # التوجيه إلى الصفحة الرئيسية
#         else:
#             messages.error(request, "Invalid username or password")
#     else:
#         form = AuthenticationForm()

#     return render(request, 'login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)  # استخدام النموذج المخصص
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('library:home')  # التوجيه إلى الصفحة الرئيسية
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = CustomLoginForm()  # استخدام النموذج المخصص

    return render(request, 'login.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('accounts:update_profile')  # توجيه المستخدم إلى صفحة الملف الشخصي بعد التحديث
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'update_profile.html', {'form': form})


def logout_view(request):
    logout(request)  # يقوم بتسجيل الخروج من النظام
    messages.success(request, "You have successfully logged out.")
    return redirect('library:home')