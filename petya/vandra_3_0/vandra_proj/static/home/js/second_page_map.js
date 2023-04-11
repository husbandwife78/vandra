
var map = L.map('map_trip').setView([53.8946, 27.5583], 6);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
             maxZoom: 19,
             attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
             }).addTo(map);

let post_points = JSON.parse(document.getElementById('post_points_json').textContent)

post_points.forEach(point => {
    var marker = L.marker([point.latitude, point.longitude]).addTo(map)

    marker.bindPopup("This is the Transamerica Pyramid").openPopup();
})