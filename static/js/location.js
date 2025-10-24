let map, marker;
function initMap() {
  const lat = parseFloat(document.getElementById("lat").value) || 32.6546;
  const lng = parseFloat(document.getElementById("lng").value) || 51.668;

  const defaultLocation = { lat: lat, lng: lng };
  map = new google.maps.Map(document.getElementById("map"), {
    center: defaultLocation,
    zoom: 13,
  });

  marker = new google.maps.Marker({
    position: defaultLocation,
    map: map,
    draggable: true,
  });

  function updateInputs(latLng) {
    document.getElementById("lat").value = latLng.lat();
    document.getElementById("lng").value = latLng.lng();
  }

  marker.addListener("dragend", function (event) {
    updateInputs(event.latLng);
  });

  map.addListener("click", function (event) {
    marker.setPosition(event.latLng);
    updateInputs(event.latLng);
  });
}
