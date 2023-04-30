
var zoomLatitude = JSON.parse(document.getElementById('zoomLat').textContent)
var zoomLongitude = JSON.parse(document.getElementById('zoomLong').textContent)

var map = L.map('map_trip')
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
             maxZoom: 19,
             attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
             }).addTo(map);

let post_points = JSON.parse(document.getElementById('post_points_json').textContent)

post_points.forEach(point => {
    let marker = L.marker([point.latitude, point.longitude]).addTo(map)
    marker.bindPopup("<b style='font-family: Cursive'>" + point.name.toUpperCase() + "</b>")
})

map.setView([zoomLatitude, zoomLongitude], 11);
L.control.scale().addTo(map);

