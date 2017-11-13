function initMap() {
	var map = new google.maps.Map(document.getElementById('map'), {
	   	zoom: 7,
	    center: {lat: -43.980198, lng: -68.275580 },
	    mapTypeId: google.maps.MapTypeId.SATELLITE,  
	});
	var markers = []
	var url = '/obtener_puntos/';
	$.get(url,function(data){
		for(var i = 0; i < data.length; i ++){
			pos = new google.maps.LatLng(data[i]["fields"]["posLatitud"],data[i]["fields"]["posLongitud"]);
			contentString = '<b>'+data[i]["fields"]["nombre"]+'</b><br><i>'+data[i]["fields"]["posLatitud"]+', '+data[i]["fields"]["posLongitud"]+'</i>';
			infowindow = new google.maps.InfoWindow({
		    content: contentString
		});
		marker = new google.maps.Marker({
			map:map,
			position:pos,
		});


		google.maps.event.addListener(marker,'click',(function(marker,contentString,infowindow){
			return function(){
				
				infowindow.setContent(contentString);
				infowindow.open(map,marker);
			};
		})(marker,contentString,infowindow));
		    markers.push(marker);
		}

		var markerCluster = new MarkerClusterer(map, markers,
	        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
	});
}

//------------------------Script que acciona el select------------------------
$(document).ready(function() {
	$('select').material_select();
});
  