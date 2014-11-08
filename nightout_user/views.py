# Create your views here.

from django.shortcuts import render,redirect

from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
#from django.shortcuts import render_to_response

import json,re

@csrf_exempt
def home(request):
	"view for index of nightout_user"
	data = None
	return render(request, 'nightout_user_index.html', data)

@csrf_exempt
def promote(request):
	"view for index of nightout_user"

	events = [
	("http://img.dooyoo.co.uk/GB_EN/175/uk-ireland-guide/clubs-national/jesters-nightclub-southampton.jpg","Jesters Monday",u"\xA34"),
	("http://www.residentadvisor.net/images/events/flyer/2012/9/uk-0923-400567-front.jpg","Big Reggae Sunday",u"\xA32.50"),
	("http://listings07.skiddlecdn.co.uk/1/b/0/487476_0_mixtape-fridays-pres-maxin_400.jpg","Maxin",u"\xA33.20")
	]

	data = {"events":events}
	return render(request, 'nightout_user_promote.html', data)

@csrf_exempt
def map(request):
	"view for index of nightout_user"
	data = None
	return render(request, 'nightout_user_map.html', data)

@csrf_exempt
def nightout(request,title):
	"view for index of nightout_user"
	title = title.capitalize()

	content = {
	"drinks" : [("/static/images/martini.png","Martini","4 Locations"),("/static/images/beer.png","Beer","Everywhere")],
	"events" : [("https://www.orangerooms.co.uk/galleryimages/reg2012.jpg","Big Reggae Sunday",u"\xA32.50"),("https://www.orangerooms.co.uk/galleryimages/MAX.APRIL.jpg","Maxin",u"\xA33.20")],
	"music" : [("http://1.bp.blogspot.com/-OJQEWW6jYfk/TyFeBlSr6XI/AAAAAAAAAEk/fjbYr-py29s/s1600/House_Music_by_Labelrx.png","House","2 Events"),("http://4.bp.blogspot.com/-BTE6F20qb_c/TaPCf6LGIsI/AAAAAAAAAa4/S5b0AidFFsU/s1600/jazz.jpg","Jazz","1 Event")],
	"establishments" : [("http://www.residentadvisor.net/images/clubs/uk-the-orange-room.jpg","Orange Rooms",u"\xA36.50 Entry"),("http://providerfiles2.thedms.co.uk/eandapics/ys/2194181_1.jpg","Vodka Revs","Free Entry")]
	}

	data = {
		"title" : title,
		"content" : content[title.lower()]*3
	}

	return render(request, 'nightout_user_nightout.html', data)

@csrf_exempt
def tonight(request):
	"view for index of nightout_user"
	data = None
	return render(request, 'nightout_user_tonight.html', data)

@csrf_exempt
def past(request):
	"view for index of nightout_user"

	headers = ["Date","Main Establishment","Main Event","Total Establishments","Options"]

	rows = [
		("10/12/13","Jesters","Student Mondays","2"),
		("10/12/13","SOBAR","Student Tuesday","3"),
		("10/12/13","JUNK","Club Night","4"),
		("10/12/13","Orange Rooms","Carnage","8")
	]

	data = {
		"headers":headers,
		"rows":rows
		}
	return render(request, 'nightout_user_past.html', data) 