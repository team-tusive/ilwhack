var latitude = false;
var longitude;
var queryDistanceResults;
var queryDistanceResultsReady = false;


function fillupshit(){
	var destination = document.shit.whatever.value;
	getLocation();
	queryDistance([latitude,longitude].join(),destination,'');
	return true;
}


function queryDistance(origins,destinations,addtl_args){
	//docs: https://developers.google.com/maps/documentation/distancematrix/
	//origins e.g.:41.43206,-81.38992
	//destinations e.g.:24+Sussex+Drive+Ottawa+ON|Capitola+CA
	queryDistanceResultsReady = false;
	var origins = encodeURIComponent(origin);
	var destinations = encodeURIComponent(destination);
	var sensor = "false";
	if (!addtl_args) {
		addtl_args = '';
	}
	var _xmlhttp = new XMLHttpRequest();
	_xmlhttp.onreadystatechange = function(){
		alert(_xmlhttp.readyState);
		if (_xmlhttp.readyState == 4){
			queryDistanceResultsReady = true;
			queryDistanceResults = JSON.parse(_xmlhttp.responseText);
			alert(queryDistanceResults);
			document.getElementById('shitgoeshere').value = queryDistanceResults;
		}
	}
	_xmlhttp.open("GET",
		"https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origins + "&destinations=" + destinations + "&sensor=" + sensor,
		true);
	_xmlhttp.send();
	return true;

}
function getLocation(){
	if (navigator.geolocation){
		navigator.geolocation.getCurrentPosition(showPosition);
	}
	else{
		return "Geolocation is not supported by this browser.";
	}
}
function showPosition(position){
	latitude = position.coords.latitude;
	longitude = position.coords.longitude;
	 alert("Latitude: " + position.coords.latitude + 
	 "  Longitude: " + position.coords.longitude); 
}