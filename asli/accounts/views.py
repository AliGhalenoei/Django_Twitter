from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth import views as auth_view
from django.views.generic import View
from content.models import *
# .imports...
from .models import *
from .forms import *

# Create your views here.


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                email = cd['email'],
                password = cd['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request,self.template_name,{'form':form})

class EmailBackend:
    def authenticate(self , request , email = None , password = None):
        try:
            user = User.objects.get(username = email)
            user.check_password(password)
            if user:
                return user
            return None
        
        except User.DoesNotExist:
            return None
    
    def get_user(self,pk):
        try:
            return User.objects.get(id = pk)
        except User.DoesNotExist:
            return None
        
class UserSinginView(View):
    form_class = UserSinginForm
    template_name = 'accounts/singin.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                email= cd['email'],
                username= cd['username'],
                password= cd['password'],
            )
            
            return redirect('login')
        return render(request,self.template_name,{'form':form})
    
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
    
class UserPasswordResetView(auth_view.PasswordResetView):
    template_name='accounts/password_reset_form.html'
    success_url=reverse_lazy('password_reset_done')
    email_template_name='accounts/password_reset_email.html'

class UserPasswordResetDone(auth_view.PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'

class UserPasswordResetConfirm(auth_view.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
    success_url=reverse_lazy('password_reset_complete')

class UserPasswordResetComplete(auth_view.PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'

class UserProfilePageView(View):
    form_class = UpdateProfileForm
    template_name = 'accounts/profile_user.html'

    def get(self,request,pk):
        follwers = UserFollw_UnFollw.objects.filter(user_follwing = pk).count()
        follwing = UserFollw_UnFollw.objects.filter(user_follw = pk).count()
        twits = Twit.objects.filter(user = pk)
        user = User.objects.get(id = pk)
        form = self.form_class(instance=user)
        return render(request , self.template_name , {
            'user':user,
            'form':form,
            'follwers':follwers,
            'follwing':follwing,
            'twits':twits,
        })
    
    def post(self,request,pk):
        user = User.objects.get(id = pk)
        form = self.form_class(request.POST , request.FILES , instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile' , user.pk)
        return render(request,self.template_name,{'form':form})
    
class UserFollwView(View):
    def get(self,request,pk):
        
        user = User.objects.get(id = pk)
        test = UserFollw_UnFollw.objects.filter(user_follw = request.user , user_follwing = user).exists()
        if test:
            return redirect('home')
        else:
            UserFollw_UnFollw.objects.create(user_follw = request.user , user_follwing = user)
            
            return redirect('home')
        
class UserUnFollwView(View):
    def get(self,request,pk):
        
        user = User.objects.get(id = pk)
        test = UserFollw_UnFollw.objects.filter(user_follw = request.user , user_follwing = user)
        if test.exists():
            test.delete()
            return redirect('home')
        else:
            #UserFollw_UnFollw.objects.create(user_follw = request.user , user_follwing = user)
            return redirect('home')
        
class DeleteAccountView(View):

    def get(self,request,pk):
        user_id = User.objects.get(id = pk)
        if user_id == request.user:
            user_id.delete()
            return redirect('login')
        else:
            return redirect('login')
        
        
    
    
    