// base

$(document).ready(function() {
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });
});


function post(path,parameter) {

	var element = document.getElementById("postField");
	//alert(parameter);
	element.setAttribute("value",parameter);

	var form = document.getElementById("postForm");
	form.setAttribute("action",path);

	form.submit();

};


function getObject(jsonString) {
	//returns the object assoicated with the given JSON string

	if ((jsonString.length < 1)||(typeof(jsonString) != "string"))  {
		return [50.935531, -1.396047];
	};

	var sanitisedJASONString = jsonString.replace(/'/g, '"');
	return JSON.parse(sanitisedJASONString);
};

//nightout_user_base.js

var map; 
var drawingManager;
var shape;
var volume;
var markerTitles = ["Home","Takeoff","Landing","Next"];
var markerSelect = 0;

var DELAY = 200
var DEFAULT_SHAPE_FORMAT = {
		editable: true,
		strokeColor : "#FFFFFF",
		strokeOpacity : 0.8,
		strokeWeight : 2,
		fillColor : "#FFFFFF",
		fillOpacity : 0.35
	};
var DEFAULT_MARKER_FORMAT = {
	draggable : true,
	flat : true
};

function setMarkerListeners(marker) {
	//setupd the functions that will be called when the marker has been dragged to location

	google.maps.event.addListener(marker, 'dragend', function() {
		markerLocation = this.getPosition();
    	updateMarker(this);
	});
};



function updateMarker(marker) {
	//function to take the marker object and post the update

	position = marker.getPosition();
	title = marker.getTitle()

	console.log(title)

	if (typeof(title) == "undefined") {
		title = markerTitles[markerSelect];
		newTitle = markerTitles[markerSelect+1];
		toggleHelp(newTitle.toLowerCase());
		markerSelect ++;
		if (markerSelect > 2){
			markerSelect = 0;
		};
	};

	console.log(title)

	markerData = {"title":title,"position":position};
	markerData = JSON.stringify(markerData);

	$.post( "post_marker",{"postField":markerData}, function(data){
		update(data);
	} ,"json");

};


function addMarker(title,position) {

	if (title == "Home"){
		//TODO clear all markers
	};

	var point = new google.maps.LatLng(position[0],position[1]);
	console.log(point);
	var marker = new google.maps.Marker({
		draggable : true,
		position: point,
		map: map,
		title : title
	});

	marker.setMap(map);
	setMarkerListeners(marker)
};

function drawMap(mapCenter,drawingModesSelector) {

	var myOptions = {
		center : new google.maps.LatLng(mapCenter[0],mapCenter[1]),
		zoom : 16,
		mapTypeId : google.maps.MapTypeId.MAP
	};

	map = new google.maps.Map(document.getElementById('map_canvas'), myOptions); 

	setDrawingManager(drawingModesSelector)

	google.maps.event.addListener(drawingManager, 'markercomplete', function(marker) {
		updateMarker(marker);
		setMarkerListeners(marker);
		shape = marker;
	});

	google.maps.event.addListener(drawingManager, 'polygoncomplete', function(polygon) {
		if (typeof(shape) != "undefined") {
			shape.setMap(null);
		};
		complexPath = polygon.getPath();
		path = complexPath["b"];
		updatePolygon(path);
		setPolygonListeners(polygon);
		shape = polygon;
	});

	google.maps.event.addListener(drawingManager, 'rectanglecomplete' , function(rectangle) {
		if (typeof(shape) != "undefined") {
			shape.setMap(null);
		};
		var path = rectangle.getBounds()
		updateRectangle(path)
		setRectangleListeners(rectangle);
		shape = rectangle;
	});

};


function setDrawingManager(drawingModesSelector) {

	var allDrawingModes = {
		"marker" : google.maps.drawing.OverlayType.MARKER,
		"polygon" : google.maps.drawing.OverlayType.POLYGON,
		"circle" : google.maps.drawing.OverlayType.CIRCLE,
		"rectangle" : google.maps.drawing.OverlayType.RECTANGLE
	};

	drawingModes = [];
	for (var i = 0; i < drawingModesSelector.length; i++) {
		drawingModes.push(allDrawingModes[drawingModesSelector[i]]);
	};

	drawingManager = new google.maps.drawing.DrawingManager({
		drawingMode : null,
		drawingControl : true,
		drawingControlOptions : {
			position : google.maps.ControlPosition.TOP_CENTER,
			drawingModes : drawingModes
		},
		markerOptions : DEFAULT_MARKER_FORMAT,
		rectangleOptions : DEFAULT_SHAPE_FORMAT,
		polygonOptions : DEFAULT_SHAPE_FORMAT
	});
	drawingManager.setMap(map);
};