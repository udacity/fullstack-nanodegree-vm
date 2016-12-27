//list of initial locations to be added to map as markers
var initLocations = [
	{
		name: 'Doghaus',
		lat: 34.1882693,
		long: -118.6061239
	},

	{
		name: 'Hook Burger',
		lat: 34.1830901,
		long: -118.60637
	},

	{
		name: 'In N Out',
		lat: 34.1949075,
		long: -118.6063385
	},

	{
		name: 'Eatsa',
		lat: 34.1853734,
		long: -118.6053226
	},

	{
		name: 'The Stand',
		lat: 34.174956,
		long: -118.5969722
	},
];

//declare global variables
var map;
var clientID;
var clientSecret;

//properly formats phone number for display to user
function formatPhone(phonenum) {
    var regexObj = /^(?:\+?1[-. ]?)?(?:\(?([0-9]{3})\)?[-. ]?)?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (regexObj.test(phonenum)) {
        var parts = phonenum.match(regexObj);
        var phone = "";
        if (parts[1]) { phone += "+1 (" + parts[1] + ") "; }
        phone += parts[2] + "-" + parts[3];
        return phone;
    }
    else {
        //invalid phone number
        return phonenum;
    }
}

//Location class definition
var Location = function(data) {
	var self = this;
	this.name = data.name;
	this.lat = data.lat;
	this.long = data.long;
	this.URL = "";
	this.street = "";
	this.city = "";
	this.phone = "";

	this.visible = ko.observable(true);

//API with foursquare to get restaurant details
	var foursquareURL = 'https://api.foursquare.com/v2/venues/search?ll='+ this.lat + ',' + this.long + '&client_id=' + clientID + '&client_secret=' + clientSecret + '&v=20160118' + '&query=' + this.name;

	$.getJSON(foursquareURL).done(function(data) {
		var results = data.response.venues[0];
		self.URL = results.url;
		if (typeof self.URL === 'undefined'){
			self.URL = "";
		}
		self.street = results.location.formattedAddress[0];
     	self.city = results.location.formattedAddress[1];
      	self.phone = results.contact.phone;
      	if (typeof self.phone === 'undefined'){
			self.phone = "";
		} else {
			self.phone = formatPhone(self.phone);
		}
	}).fail(function() {
		alert("There was an error with the Foursquare API call. Please refresh the page and try again to load Foursquare data.");
	});

//form the string that will be shows in the google maps info window when a marker is clicked
	this.contentString = '<div class="info-window-content"><div class="title"><b>' + data.name + "</b></div>" +
        '<div class="content"><a href="' + self.URL +'">' + self.URL + "</a></div>" +
        '<div class="content">' + self.street + "</div>" +
        '<div class="content">' + self.city + "</div>" +
        '<div class="content">' + self.phone + "</div></div>";

	this.infoWindow = new google.maps.InfoWindow({content: self.contentString});

//add the location marker to the map
	this.marker = new google.maps.Marker({
			position: new google.maps.LatLng(data.lat, data.long),
			map: map,
			title: data.name
	});

//only show markers that are visible
	this.showMarker = ko.computed(function() {
		if(this.visible() === true) {
			this.marker.setMap(map);
		} else {
			this.marker.setMap(null);
		}
		return true;
	}, this);

	this.marker.addListener('click', function(){
		self.contentString = '<div class="info-window-content"><div class="title"><b>' + data.name + "</b></div>" +
        '<div class="content"><a href="' + self.URL +'">' + self.URL + "</a></div>" +
        '<div class="content">' + self.street + "</div>" +
        '<div class="content">' + self.city + "</div>" +
        '<div class="content"><a href="tel:' + self.phone +'">' + self.phone +"</a></div></div>";

        self.infoWindow.setContent(self.contentString);

		self.infoWindow.open(map, this);

		self.marker.setAnimation(google.maps.Animation.BOUNCE);
      	setTimeout(function() {
      		self.marker.setAnimation(null);
     	}, 2100);
	});

	this.bounce = function(place) {
		google.maps.event.trigger(self.marker, 'click');
	};
};

function ViewModel() {
	var self = this;

	this.searchTerm = ko.observable("");

	this.locList = ko.observableArray([]);

//create a new google map object
	map = new google.maps.Map(document.getElementById('map'), {
			zoom: 10,
			center: {lat: 34.1743246, lng: -118.6061239}
	});

// Foursquare API settings
	clientID = "RCU1UXHAM1TIQ0QJ1REZZTJI5SEQOV1ZUGQQ2EXWJM1HX3FK";
	clientSecret = "TMGCJCVRUU5QPEVDIFAJFFBOGHFT32VGGOCGPWXAXDAJH3OH";

//add the initial locations list to a ko observable list
	initLocations.forEach(function(locItem){
		self.locList.push( new Location(locItem));
	});

//filter the list of markers based upon the search term
	this.filteredList = ko.computed( function() {
		var filter = self.searchTerm().toLowerCase();
		if (!filter) {
			self.locList().forEach(function(locItem){
				locItem.visible(true);
			});
			return self.locList();
		} else {
			return ko.utils.arrayFilter(self.locList(), function(locItem) {
				var string = locItem.name.toLowerCase();
				var result = (string.search(filter) >= 0);
				locItem.visible(result);
				return result;
			});
		}
	}, self);

	this.mapElem = document.getElementById('map');
	this.mapElem.style.height = window.innerHeight - 50;
}

function startApp() {
	ko.applyBindings(new ViewModel());
}

function errorHandling() {
	alert("Google Maps has failed to load. Please check your internet connection and try again.");
}
