let zoomLatitude = JSON.parse(document.getElementById('zoomLat').textContent)
let zoomLongitude = JSON.parse(document.getElementById('zoomLong').textContent)

console.log(zoomLat)

var map = L.map('map_trip').setView([zoomLatitude, zoomLongitude], 12);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
             maxZoom: 19,
             attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
             }).addTo(map);

let post_points = JSON.parse(document.getElementById('post_points_json').textContent)

post_points.forEach(point => {
    var marker = L.marker([point.latitude, point.longitude]).addTo(map)

    marker.bindPopup("This is the Transamerica Pyramid").openPopup();
})