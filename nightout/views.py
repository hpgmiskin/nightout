from django.shortcuts import render
import os

def index(request):

	data = None

	return render(request,"index.html",data)

def login(request):

	data = None

	return render(request,"login.html",data)