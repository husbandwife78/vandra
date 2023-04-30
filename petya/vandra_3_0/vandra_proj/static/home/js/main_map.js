
var map = L.map('map').setView([53.8946, 27.5583], 6);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
             maxZoom: 19,
             attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
             }).addTo(map);

let post_markers = JSON.parse(document.getElementById('post_coordinates_json').textContent)

post_markers.forEach(post_marker => {
    var marker = L.marker([post_marker.postLatitude, post_marker.postLongitude]).addTo(map)

    marker.bindPopup("<b style='font-family: Cursive'>" + post_marker.slug.toUpperCase() + "</b>")
})

//console.log(document.location.href = '../')


