from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
import md5, os, binascii

def index(request):
	return render(request, 'myFriends/index.html')

def register(request):
	salt = binascii.b2a_hex(os.urandom(15)),
	postData = {
		'first_name': request.POST['first_name'],
		'last_name': request.POST['last_name'],
		'email': request.POST['email'],
		'password': request.POST['password'],
		'confirm_pw': request.POST['confirm_pw'],
		'encrypted_pw': md5.new(str(request.POST['password']) + str(salt)).hexdigest(),
		'salt': salt,
	}

	if not User.objects.register(postData):
		new_user_id = User.objects.create_user(postData)
		request.session['user_id'] = new_user_id
		messages.success(request, 'Successfully registered!')

		return redirect('/friends')

	for error in User.objects.register(postData):
		messages.error(request, error)

	return redirect('/')

def login(request):
	postData = {
		'email': request.POST['email'],
		'password': request.POST['password'],
	}

	if not User.objects.login(postData):
		user_id = User.objects.get(email=postData['email']).id
		request.session['user_id'] = user_id
		messages.success(request, 'Successfully logged in!')
		return redirect('/friends')

	for error in User.objects.login(postData):
		messages.error(request, error)

	return redirect('/')

def friends(request):
		first_name = User.objects.get(id=request.session['user_id']).first_name
		context = {
			'first_name': first_name,
		}

		return render(request,'myFriends/friends.html', context)

def user(request):
    return render(request, 'myFriends/user.html')
    
def create(request):
    User.objects.create(first_name=request.POST['first_name'])
    return redirect('/user')

def logout(request):
	request.session.clear()
	return redirect('/')
