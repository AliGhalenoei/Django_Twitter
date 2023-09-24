from typing import Any
from django import http
from django.shortcuts import render,redirect
from django.views.generic import View

# .imports...
from .models import *
from .forms import *

# Create your views here.

class HomePageView(View):
    template_name = 'content/home_page.html'

    def get(self,request):
        twits = Twit.objects.order_by('-id')
        if request.GET.get('search'):
            twits = twits.filter(user__username__contains=request.GET['search'])
        return render(request,self.template_name,{
            'twits':twits,
        })

class DetailTwitPageView(View):
    form_comment = CommentTwitForm
    template_name = 'content/detail_twit.html'

    def get(self,request,pk):
        twit = Twit.objects.get(id = pk)
        comments = CommentTwit.objects.filter(twit = pk,is_sub = False)
        return render(request,self.template_name,{
            'twit':twit,
            'comments':comments,
            'form':self.form_comment,
        })
    
    def post(self,request,pk):
        twit = Twit.objects.get(id = pk)
        form = self.form_comment(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            now = form.save(commit=False)
            now.user = request.user
            now.twit = twit
            now.save()
            return redirect('detail_twit' , twit.pk)
        return render(request,self.template_name,{'form':form})

# Comments Twit Views... 
class UpdateCommentTwitView(View):
    form_class = UpdateCommentTwitForm
    template_name = 'content/update_comment.html'

    def setup(self, request , *args , **kwargs) -> None:
        self.comment_ins = CommentTwit.objects.get(id = kwargs['pk'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args: Any, **kwargs):
        comment_user = self.comment_ins
        if not comment_user.user == request.user :
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,pk):
        comment = self.comment_ins
        form = self.form_class(instance=comment)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,pk):
        comment = self.comment_ins
        form = self.form_class(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            return redirect('detail_twit' , comment.twit.pk)
        return render(request,self.template_name,{'form':form})
    
class DeleteCommentTwitView(View):

    def get(self,request,pk):
        user_comment = CommentTwit.objects.get(id = pk)
        if user_comment.user == request.user:
            user_comment.delete()
            return redirect('detail_twit' , user_comment.twit.pk)
        else:
            return redirect('home')
        
# Relations Like Twit Views...

class LikeTwitView(View):

    def get(self,request,pk):
        twit = Twit.objects.get(id = pk)
        test = Relation.objects.filter(
            user = request.user,
            twit = twit,
        ).exists()
        if test:
            return redirect('home')
        else:
            Relation.objects.create(
                user = request.user,
                twit = twit,
            )
            return redirect('home')
        
class DisLikeTwitView(View):

    def get(self,request,pk):
        twit = Twit.objects.get(id = pk)
        test = Relation.objects.filter(
            user = request.user,
            twit = twit,
        )
        if test.exists():
            test.delete()
            return redirect('home')
        else:
            return redirect('home')
        
# Relation Save Twit Views...
class SaveTwitView(View):

    def get(self,request,pk):
        twit = Twit.objects.get(id = pk)
        test = SaveTwit.objects.filter(
            user = request.user,
            twit = twit,
        ).exists()
        if test:
            return redirect('home')
        else:
            SaveTwit.objects.create(
                user = request.user,
                twit = twit,
            )
            return redirect('home')

class UnSaveTwitView(View):

    def get(self,request,pk):
        twit = Twit.objects.get(id = pk)
        test = SaveTwit.objects.filter(
            user = request.user,
            twit = twit,
        )
        if test.exists():
            test.delete()
            return redirect('home')
        else:
            return redirect('home')
        
class ListSaveTwitView(View):
    template_name = 'content/list_save.html'

    def get(self,request,pk):
        twits = SaveTwit.objects.filter(user = pk)
        return render(request,self.template_name,{'twits':twits})
    
# CRUD Twit Views...
class CreateNewTwitView(View):
    form_class = TwitForm
    template_name = 'content/new_twit.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request):
        form = self.form_class(request.POST , request.FILES )
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('home')
        return render(request,self.template_name,{'form':form})
    
class UpdateTwitView(View):
    form_class = UpdateTwitForm
    template_name = 'content/edit_twit.html'

    def setup(self, request, *args: Any, **kwargs: Any) -> None:
        self.twit_ins = Twit.objects.get(id = kwargs['pk'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args , **kwargs ):
        twit_id = self.twit_ins
        if not twit_id.user == request.user:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,pk):
        twit_id = self.twit_ins
        form = self.form_class(instance=twit_id)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,pk):
        twit_id = self.twit_ins
        form = self.form_class(request.POST , request.FILES , instance=twit_id)
        if form.is_valid():
            form.save()
            return redirect('profile' , twit_id.user.pk)
        return render(request,self.template_name,{'form':form})
    
class DeleteTwitView(View):

    def get(self,request,pk):
        twit_id = Twit.objects.get(id = pk)
        if twit_id.user == request.user:
            twit_id.delete()
            return redirect('home')
        else:
            return redirect('home')


    
    



    

    



        

        



