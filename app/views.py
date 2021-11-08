from django.shortcuts import render , redirect
from django.urls import reverse
from .models import Group , Post
from .forms import GroupForm , UserRegistrationForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def homepage(request):
	q = request.GET.get('q') if request.GET.get('q',None) else '' 
	if not q:
		groups = Group.objects.all() 
	else:
		groups = Group.objects.filter(
				Q(name__icontains = q) |
				Q(description__icontains = q)
			)

	group_count = groups.count()

	data = { 'groups':groups , 'group_count': group_count }
	return render(request,'home/index.html',data)


def group(request,group_id):
	group = Group.objects.get( id = group_id )
	posts = Post.objects.filter(group = group)
	return render(request,'group/index.html',{'group':group , 'posts': posts })

@login_required(login_url='/user/login')
def create_group(request):
	form = GroupForm()
	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home-page')
	return render(request,'group/create-group.html',{'form':form})

@login_required(login_url='/user/login')
def update_group(request,group_id):
	group = Group.objects.get( id = group_id )
	form = GroupForm(instance = group)
	if request.method == 'POST':
		form = GroupForm(request.POST , instance = group)
		if form.is_valid():
			form.save()
			return redirect(reverse('group-page',kwargs={'group_id': group_id }))
	return render(request,'group/create-group.html',{'form':form})

@login_required(login_url='/user/login')
def delete_group(request,group_id):
	group = Group.objects.get(id = group_id)
	if request.method == 'POST' and group is not None:
		group.delete()
		return redirect(reverse('home-page'))
	return render(request,'group/delete-group.html', {'group':group})

def login_user(request):
	if request.user.is_authenticated:
		return redirect('home-page')

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		try:
			user = User.objects.get(username = username)
		except:
			messages.error(request, 'User is not registered')
		
		user = authenticate(request , username = username , password = password)
		
		if user is not None:
			login(request , user)
			return redirect('home-page')
		else:
			messages.error(request, 'Username or Password Incorrect')
	return render(request,'user/login.html')

def logout_user(request):
	logout(request)
	return redirect('home-page')

def signup_user(request):
	form = UserRegistrationForm()
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request , user)
			messages.success(request , "Registration Successful")
			return redirect('home-page')
		messages.error(request,"Registration failed")
	return render(request,'user/signup.html',{ 'signup_form':form })

def view_post(request,post_id,post_slug):
	post = get_object_or_404(Post, pk = post_id)
	return render(request,'post/index.html',{'post':post})