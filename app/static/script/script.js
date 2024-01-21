document.getElementById('locationBtn').addEventListener('click', function() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var userLocation = {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude
        };
        // Display user's location
        alert('User Location: Latitude ' + userLocation.latitude + ', Longitude ' + userLocation.longitude);
        
        // Call function to fetch and display nearby hospitals
        fetchNearbyHospitals(userLocation);
      }, function(error) {
        console.error('Error getting location:', error.message);
      });
    } else {
      console.error('Geolocation is not supported by this browser.');
    }
  });

  function fetchNearbyHospitals(userLocation) {
    var map = new google.maps.Map(document.createElement('div'));
    var service = new google.maps.places.PlacesService(map);

    // Specify search parameters
    var request = {
      location: new google.maps.LatLng(userLocation.latitude, userLocation.longitude),
      radius: 5000,  // Search within a 5km radius
      type: 'hospital'  // Search for hospitals
    };

    // Fetch nearby hospitals
    service.nearbySearch(request, function(results, status) {
      if (status == google.maps.places.PlacesServiceStatus.OK) {
        // Display the top 5 nearest hospitals and their distances
        for (var i = 0; i < Math.min(5, results.length); i++) {
          var hospital = results[i];
          var hospitalLocation = hospital.geometry.location;
          var distance = calculateDistance(userLocation, hospitalLocation);

          // Display hospital information
          alert('Hospital ' + (i + 1) + ': ' + hospital.name + ', Distance: ' + distance.toFixed(2) + ' km');
        }
      } else {
        console.error('Error fetching nearby hospitals:', status);
      }
    });
  }

  function calculateDistance(userLocation, hospitalLocation) {
    var R = 6371;  // Radius of the Earth in kilometers
    var lat1 = userLocation.latitude * (Math.PI / 180);
    var lon1 = userLocation.longitude * (Math.PI / 180);
    var lat2 = hospitalLocation.lat() * (Math.PI / 180);
    var lon2 = hospitalLocation.lng() * (Math.PI / 180);

    var dlat = lat2 - lat1;
    var dlon = lon2 - lon1;

    var a =
      Math.sin(dlat / 2) * Math.sin(dlat / 2) +
      Math.cos(lat1) * Math.cos(lat2) * Math.sin(dlon / 2) * Math.sin(dlon / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    var distance = R * c;  // Distance in kilometers
    return distance;
  }