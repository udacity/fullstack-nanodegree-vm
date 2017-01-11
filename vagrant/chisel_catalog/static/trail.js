function initMap(trail) {


  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat:trail.lat,lng:trail.lon},
    zoom: 12,
    disableDefaultUI:false
  });

  //Create and set marker
  var marker = new google.maps.Marker({
    position: {lat:trail.lat,lng:trail.lon},
    map: map,
    title: trail.name+' trailhead',
  });

}