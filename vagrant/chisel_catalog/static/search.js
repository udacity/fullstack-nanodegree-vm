function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat:38.9776681,lng:-96.847185},
    zoom: 5,
    disableDefaultUI:false
  });

  //Get info via AJAX call
  $.ajax({

      url : 'http://localhost:5000/parksJSON',
      type : 'GET',
      dataType:'json',
      success : function(data) {              
          for (var i = 0; i < data.Parks.length; i++) {
            set_marker(data.Parks[i]);
          };
      },
      error : function(request,error)
      {
          alert("Request: "+JSON.stringify(request));
      }
  });

  function set_marker(park){
    // Create infoWindow
    var infoWindow = new google.maps.InfoWindow({
        content: '<div><a href=''>'+park.name+'</a></div>'
    });

    //Create and set marker
    var marker = new google.maps.Marker({
      position: {lat:park.lat,lng:park.lon},
      map: map,
      title: park.name,
      infowindow: infoWindow
    });

    marker.addListener('click', function() {
      infoWindow.open(map, marker);
      map.setZoom(10);
      map.setCenter(marker.getPosition());
      //window.location = marker.url;
    });
  }

}