from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, EntryForm, CommentForm
from .models import Entry, Comment

# Create your views here.

@login_required
def home(request):
    blogs = Entry.objects.all().order_by('date_posted').reverse()   
    blog_num_comments = {}
    
    for blog in blogs:
        num_comments = Comment.objects.filter(post=blog).count()
        blog_num_comments[blog.id] = num_comments
    
    context = {
        'blogs':blogs,
        'num': blog_num_comments
        }
    return render(request, 'blog/home.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)        
        if user is not None:
            login(request, user)
            return redirect('home')        
        else:
            error = 'Nombre de usuario o contraseña incorrectos.'
            return render(request, 'registration/login.html', {'error': error})        
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)      
            return redirect('home')     
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def post_detail(request, id):
    post = get_object_or_404(Entry,pk=id)
    comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            context = {
                'post': post, 
                'comments': comments, 
                'form': form
                }
            return render(request, 'blog/post_detail.html', context)
    else:
        form_comments = CommentForm()
        context = {
            'post':post,
            'comments':comments,
            'form':form_comments
        }
        return render(request, 'blog/post_detail.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect ('home')
    else:
        form = EntryForm()
    return render(request, 'blog/create_post.html', {'form':form})
    