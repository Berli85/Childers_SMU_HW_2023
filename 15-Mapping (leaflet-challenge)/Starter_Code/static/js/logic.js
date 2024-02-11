// grab the data
let url = `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson`;
let url2 = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json"

 // make request
 d3.json(url).then(function (data) {
   console.log(data);
   d3.json(url2).then(function (data2) {
    makeMap(data, data2);
   });
});

function makeMap(data, data2) {
  // Step 1: Define your BASE Layers

  // Define variables for our tile layers.
  let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // Step 2: Create the OVERLAY (DATA) Layers
  let markers = [];
  let circles = [];

  // Loop through the data.
  for (let i = 0; i < data.features.length; i++){

    // Set the data location property to a variable.
    let row = data.features[i];

    // Check for the location property.
    if (row.geometry) {
      let latitude = row.geometry.coordinates[1];
      let longitude = row.geometry.coordinates[0];
      let depth = row.geometry.coordinates[2];
      let location = [latitude, longitude];

      // Add a new marker to the cluster group, and bind a popup.
      let mag = row.properties.mag;
      let popup_text = `<h1>${row.properties.title}</h1><hr><a href="${row.properties.url}" target="_blank">Link</a>`;
      let marker = L.marker(location).bindPopup(popup_text);

      // for the marker layer
      markers.push(marker);

      // if statement for the color of the circle
      let color;
      if (depth < 10) {
        color = "#F2D7D5";
      } else if (depth < 30) {
        color = "#E6B0AA";
      } else if (depth < 50) {
        color = "#C0392B";
      } else if (depth < 70) {
        color = "#922B21";
      } else if (depth < 90) {
        color = "#7B241C";
      } else {
        color = "#641E16";
      }

      // radius
      let radius = 2500 * (mag**2);

      // create a new circle
      let circle = L.circle(location, {
        color: color,
        fillColor: color,
        fillOpacity: 0.5,
        radius: radius
      }).bindPopup(popup_text);

      circles.push(circle);
    }
  }

  let markerLayer = L.layerGroup(markers);
  let circleLayer = L.layerGroup(circles);
  let tectonicLayer = L.geoJSON(data2, {
    style: function (feature) {
      let mapStyle = {
        color: "dark red",
        fillColor: "dark red",
        fillOpacity: 1,
        weight: 5
      };

      return mapStyle;
    }
  });

  // Step 3: Create the MAP object

  // Create a map object, and set the default layers.
  let myMap = L.map("map", {
    center: [32.7767, -96.7970],
    zoom: 5,
    layers: [street, circleLayer, tectonicLayer]
  });

  // Step 4: Add the Layer Controls (Legend goes here too)

  // Only one base layer can be shown at a time.
  let baseMaps = {
    Street: street,
    Topography: topo
  };

  // Overlays that can be toggled on or off
  let overlayMaps = {
    Markers: markerLayer,
    Circles: circleLayer,
    Tectonic: tectonicLayer
  };

  // Pass our map layers into our layer control.
  // Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps).addTo(myMap);

  // Step 5: Legend
  // Create legend
  let legend = L.control({ position: 'topleft' });

  // Define the legend content
  legend.onAdd = function (myMap) {
    let div = L.DomUtil.create('div', 'legend');
    let colors = ["#CCCC00", "#99CC66", "#999966", "#CCCC99", "#CC9900", "#996600"];
    let labels = ["-10-10", "10-30", "30-50", "50-70", "70-90", "90+"];

    // set the title
    div.innerHTML += "<h3>Earthquake Depth</h3>";

    // Loop through the colors and labels to create the legend items
    for (let i = 0; i < colors.length; i++) {
        div.innerHTML +=
            '<i style="background:' + colors[i] + '"></i> ' + labels[i] + '<br>';
    }

      return div;
  };

  // Add the legend control to the map
  legend.addTo(myMap);
  }
