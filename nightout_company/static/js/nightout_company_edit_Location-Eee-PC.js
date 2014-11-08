//explore

function initialize() {

	var drawingModesSelector = ["marker"]
	var mapCenter = [50.912058,-1.404979]//getObject($("#mapCenter").val());
	//var markerData = getObject($("#markerData").val());
	drawMap(mapCenter,drawingModesSelector);
	// addMarker("Junk",[50.912098,-1.403863])
	// addMarker("Orange Rooms",[50.912288,-1.404882])
	// addMarker("The Bedford Arms",[50.911834,-1.405901])

};

google.maps.event.addDomListener(window, 'load', initialize); 