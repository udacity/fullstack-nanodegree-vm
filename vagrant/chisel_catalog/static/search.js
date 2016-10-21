function initMap() {
  //Set US map
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat:37.1892273,lng:-113.293},
    zoom: 11,
    disableDefaultUI:false
  });

  // query trails from txt file (need to replace with data from mySQL database)
  /*var xmlhttp = new XMLHttpRequest();
  var url = "utah_trails.json";
  xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      myFunction(xmlhttp.responseText);
    }
  }
  xmlhttp.open("GET", url, true);
  xmlhttp.send();

  //Parse and set marker and methods for each trail 
  function myFunction(response) {
    var arr = JSON.parse(response);
    for (var i = 0; i < arr.list.length; i++) {
      set_marker(arr.list[i]);
    };
  }
  
  function set_marker(trail){
    //Create info window
    var infoWindow = new google.maps.InfoWindow({
        //content: '<div><a href=''>'+trail.trail_name+'</a></div>'
    });

    //Create and set marker
    var marker = new google.maps.Marker({
      position: trail.trailhead,
      map: map,
      title: trail.trail_name,
      url: trail.page,
      infowindow: infoWindow
    });

    marker.addListener('click', function() {
      //Go to page link
      infoWindow.open(map, marker);
      //window.location = marker.url;


    });
  }*/

}