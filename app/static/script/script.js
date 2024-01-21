document.getElementById("locationBtn").addEventListener("click", function () {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        const userLocation = {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
        };

        findNearestHospitals(userLocation.latitude, userLocation.longitude);
      },
      function (error) {
        console.error("Error getting location:", error.message);
      }
    );
  } else {
    console.error("Geolocation is not supported by this browser");
  }
});

function calculateDistance(userLocation, hospitalLocation) {
  // this is the radius of the aerth in km lol

  // alot of math was used!!!!!!!
  const earthRadius = 6371;
  const lat1 = userLocation.latitude;
  const lon1 = userLocation.longitude;
  const lat2 = hospitalLocation.latitude;
  const lon2 = hospitalLocation.longitude;

  const dLat = toRadians(lat2 - lat1);
  const dLon = toRadians(lon2 - lon1);

  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(toRadians(lat1)) *
      Math.cos(toRadians(lat2)) *
      Math.sin(dLon / 2) *
      Math.sin(dLon / 2);

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  const distance = earthRadius * c;

  return distance;
}

function toRadians(degrees) {
  return degrees * (Math.PI / 180);
}

function findNearestHospitals(latitude, longitude) {
  const hospitals = [
    { name: "VGH", latitude: 49.26236, longitude: -123.12422 },
    { name: "Richmond", latitude: 49.16882, longitude: -123.1468 },
    { name: "St. Paul", latitude: 49.28072, longitude: -123.12855 },
    { name: "Lions", latitude: 49.32087, longitude: -123.06771 },
    { name: "Mt. St. Joseph", latitude: 49.25815, longitude: -123.096 },
    { name: "UBC", latitude: 49.26412, longitude: -123.24543 },
    { name: "BC Child", latitude: 49.24468, longitude: -123.12534 },
    { name: "Sechelt", latitude: 49.47564, longitude: -123.74928 },
    { name: "Abbotsford", latitude: 49.03686, longitude: -122.31188 },
    { name: "Burnaby", latitude: 49.24946, longitude: -123.01563 },
    { name: "Chilliwack", latitude: 49.16654, longitude: -121.9628 },
    { name: "Delta", latitude: 49.08573, longitude: -123.06164 },
    { name: "Eagle", latitude: 49.28549, longitude: -122.82341 },
    { name: "Langley", latitude: 49.09285, longitude: -122.61252 },
    {
      name: "Peace Arch Hospital",
      latitude: 48.998999,
      longitude: -122.740968,
    },
    {
      name: "Ridge Meadows Hospital",
      latitude: 49.21487,
      longitude: -122.630951,
    },
    {
      name: "Squamish General Hospital",
      latitude: 49.69755,
      longitude: -123.14132,
    },
    {
      name: "Surrey Memorial Hospital",
      latitude: 49.17645,
      longitude: -122.84278,
    },
    {
      name: "Royal Columbian Hospital",
      latitude: 49.22657,
      longitude: -122.89157,
    },
    {
      name: "qathet General Hospital",
      latitude: 49.85083,
      longitude: -124.51847,
    },
    {
      name: "Pemberton Health Centre",
      latitude: 50.32115,
      longitude: -122.80478,
    },
    {
      name: "Surrey Whalley UPCC",
      latitude: 49.17798,
      longitude: -122.84232,
    },
    {
      name: "Ridge Meadows UPCC",
      latitude: 49.21798,
      longitude: -122.59781,
    },
    { name: "Port Moody UPCC", latitude: 49.2788, longitude: -122.8415 },
    { name: "Metrotown UPCC", latitude: 49.23007, longitude: -123.00277 },
    { name: "Edmonds UPCC", latitude: 49.21873, longitude: -122.95125 },
  ];

  const sortedHospitals = hospitals
    .map((hospital) => ({
      name: hospital.name,
      distance: calculateDistance({ latitude, longitude }, hospital),
    }))
    .sort((a, b) => a.distance - b.distance);

  const nearestHospitalsContainer = document.getElementById("nearestHospitals");
  nearestHospitalsContainer.innerHTML = "<h2>Nearest Hospitals:</h2>";

  sortedHospitals.slice(0, 5).forEach((hospital, index) => {
    nearestHospitalsContainer.innerHTML += `<p>Hospital ${index + 1}: ${
      hospital.name
    } - Distance: ${hospital.distance.toFixed(2)} km</p>`;
  });
}
