
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib.auth.hashers import check_password, make_password
from django.views.generic import *
from .models import Category, Post
from django.contrib.auth.models import User
from django.views import *
from .forms import AddBlogForm
from django.db.models import Q


# Create your views here.
class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
           
            blog = Post.objects.filter(soft_delete= False)
            p = Paginator(blog, 3)
            page = request.GET.get('page')
            blogs = p.get_page(page)

            context = {
                'post': blog,
                'blogs': blogs,
            }
            return render(request, 'mainbody.html', context)

        else:
            return render(request, 'index.html')
    # return redirect('login')

    def post(self, request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        email = request.POST['email']
        password2 = request.POST['password2']
        if len(firstname) != 0 and len(lastname) != 0 and len(username) != 0 and len(password1) != 0 and len(
                email) != 0 and len(password2) != 0:
            if not User.objects.filter(username=username).exists():
                if password1 == password2:
                    user = User.objects.create(first_name=firstname, last_name=lastname, username=username,
                                               password=make_password(password1), email=email)
                    user.save()
                    # user.set_password(password1)
                    return redirect('MainBody')
                else:
                    messages.error(request, "Password Doesn't Match")
            else:
                messages.info(request, "Username is already taken")
        else:
            messages.info(request, "All fields are Required")
        return render(request, 'index.html')


class LogIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            blog = Post.objects.all()
            p = Paginator(blog, 3)
            page = request.GET.get('page')
            blogs = p.get_page(page)

            context = {
                'post': blog,
                'blogs': blogs,
            }
            return render(request, 'mainbody.html', context)
        else:
            return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        print(user.password)
        password_check = check_password(password, user.password)
        if password_check:
            auth.login(request, user)
            return redirect('MainBody')
        return render(request, 'login.html')


class MainBody(View):
    def get(self, request):
        if request.user.is_authenticated:
            blog = Post.objects.filter(soft_delete= False)
            p = Paginator(blog, 3)
            page = request.GET.get('page')
            blogs = p.get_page(page)

            context = {
                'post': blog,
                'blogs': blogs,
                'category_menu': Category.objects.all()
            }
            return render(request, 'mainbody.html', context)
        else:
            return redirect('login')


class DetailBlog(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            blog = Post.objects.get(id=id)
            context = {
                'post': blog,
                'category_menu': Category.objects.all()
            }
            return render(request, 'detailedblog.html', context)
        else:
            return redirect('login')



class AddBlog(View):
    def get(self,request):
        form = AddBlogForm
        return render(request, 'addblog.html',{'form':form})

    def post(self, request):
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        post_image = request.FILES['post_image']
        category_check = Category.objects.get(id=category)
        print(category)
        post = Post.objects.create(title=title, content=content, category=category_check,
                                       post_image=post_image, user = request.user)
        post.save()
        return redirect('MainBody')

class AddCategory(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'

class CategoryView(View):
    def get(self, request, catergories):
        category_posts= Post.objects.filter(category__name=catergories)
        return render(request, 'categorypage.html', {'catergories':catergories, 'category_posts':category_posts})

class Profile(View):
#userdetailView
    def get(self, request, username):
        if request.user.is_authenticated:
            user = User.objects.get(username=username)
            context = {
                'user': user,
                'category_menu': Category.objects.all()
                
            }
            return render(request, 'profile.html', context)
        else:
            return redirect('login')


class LoggedInUser(View):
    #ProfileView
    def get(self, request, username):
        if request.user.is_authenticated:
            user = User.objects.get(username=username)
            # blog = Post.objects.get(soft_delete= True)
            context = {
                'user': user,
                'category_menu': Category.objects.all(),
                
            }
            return render(request, 'loggedinprofile.html', context)
        else:
            return redirect('login')


class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('login')


# class Category(View):
#     def get(self, request):
#         return render(request, 'category.html')


# class Signup(View):
#     def get(self, request):
#         return render(request, 'index.html')


class UpdatePost(UpdateView):
    model = Post
    template_name = 'updateblog.html'
    fields = ['title','content','category','post_image']

# class DeletePost(DeleteView):
#     model = Post
#     template_name = 'deletepost.html'
#     success_url = reverse_lazy('home')

class DeletePost(View):
    def get(self,request, id):
        blog = Post.objects.get(id=id)
        blog.soft_delete = True
        blog.save()
        return redirect('MainBody')

class SearchBlog(View):
    def post(self,request):
        searched = request.POST['searched']
        blogs = Post.objects.filter(Q(title__icontains=searched) | Q(content__icontains=searched))
        return render(request,'searchblog.html',{
        'blogs':blogs})