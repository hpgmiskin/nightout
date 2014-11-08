# Create your views here.

from django.shortcuts import render

def home(request):
	"home of company"
	data = None
	return render(request,"nightout_company_index.html",data)

def editEstablishment(request):
	"home of company"

	fields = [ #id,name,type
		("companyName","Company Name","text"),
		("companyType","Type of Establishment","text"),
		("companyEmail","Company Email","email")
	]

	data = {"fields":fields}
	return render(request,"nightout_company_edit_establishment.html",data)

def editEvent(request):
	"home of company"

	fields = [ #id,name,type
		("eventName","Event Name","text"),
		("eventType","Type of Event","text"),
		("musicType","Type of Music","text"),
		("eventCost","Cost of Event","number"),
	]

	data = {"fields":fields}
	return render(request,"nightout_company_edit_event.html",data)

def editLocation(request):
	"company define location"
	data = None
	return render(request,"nightout_company_edit_location.html",data)

def viewEvents(request,title):
	"home of company"

	

	headers = ["Date","App User Attendance","Advertising Cost","Options"]

	month = {"past":2,"future":3}

	rows = [
		("11/{}/14".format(month[title]),"16",u"\xA36.50"),
		("13/{}/14".format(month[title]),"26",u"\xA37.50"),
		("16/{}/14".format(month[title]),"42",u"\xA323.00"),
		("24/{}/14".format(month[title]),"19",u"\xA39.20")
	]
	title = title.capitalize()
	data = {
		"title" : title,
		"headers":headers,
		"rows":rows
		}
	return render(request,"nightout_company_view_events.html",data)

def promote(request):
	"function for promoting"

	headers = ["Date","App User Attendance","Advertising Cost","Options"]


	rows = [
		("11/03/14","16",u"\xA36.50"),
		("13/03/14","26",u"\xA37.50"),
		("16/03/14","42",u"\xA323.00"),
		("24/03/14","19",u"\xA39.20")
	]

	data = {
		"headers":headers,
		"rows":rows
		}
	return render(request,"nightout_company_promote.html",data)