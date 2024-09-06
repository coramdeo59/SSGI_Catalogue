const showSearchFormField = document.querySelector('#searchButton');
const searchContainer = document.querySelector('#searchFormContainer');
// const resultButton=document.querySelector('#resultButton');
// const resultFormContainer=document.querySelector('#resultFormContainer');
const submitButton=document.querySelector('#submitButton');

const chooseFromMapButton=document.querySelector('#chooseFromMapButton');
var inputFieldsContainer = document.getElementById('coordinateFieldsContainer');

var coordinateForm = document.getElementById('coordinateForm');
coordinateForm.style.backgroundColor = 'rgba(211, 211, 211,0.9)';
var searchGeocoder=document.getElementById('#searchGeocoder')

addCoordinate=document.querySelector('#addCoordinate')

var input_lat;
var input_long;


 

const flag_value = document.getElementById('flag_id');
const lat_long_flag_value = document.getElementById('lat_long_flag');
const showresultContainer= document.getElementById('resultButton');
const resultFormContainer=document.querySelector('#resultFormContainer');
var flag=flag_value.innerHTML;
var file_flag=lat_long_flag_value.innerHTML
// const showGeocoderContainer= document.getElementById('tab1-tab');
// const GeocoderContainer=document.querySelector('#searchGeocoder');

// const showsearchShapefile= document.getElementById('tab2-ta');
// const searchShapefile=document.querySelector('#searchShapefile');
 


console.log(file_flag);
var val=lat_long_val.innerHTML;
var arr = val.split(", ");
   
console.log(arr);






// if(file_flag=='True') {
  
//  var count=0;
//  var lat_val=0;
//  var long_val=0;
// for (var i = 0; i < arr.length; i++) {
// lat_val+=(parseFloat(arr[i].split(',')[0].trim()));
// long_val+=(parseFloat(arr[i].split(',')[1].trim()));
// console.log(lat_val+""+long_val);


// const coordinate = L.latLng(lat_val, long_val);
//   polygonPoints.push(coordinate);
  
//   // Plot the coordinate on the map
//   const marker = L.marker(coordinate).addTo(map_folium);
//   marker.on('click', latLngPop);
//   count++;
//   }
//   updateLinesAndShadedArea()


// input_lat=(lat_val/=count).toFixed(4);
// input_long=(long_val/=count).toFixed(4);


// document.getElementById("Latitude").value=input_lat
// document.getElementById("Longitude").value=input_long


// map_folium.setView([input_lat,input_long])
// }




if(flag=='True'){
  console.log(flag);
  resultFormContainer.style.display='block';
  searchContainer.style.display = 'none';
  searchGeocoder.className='show'
}

// const handleTab1Toggle = () => {
//   if (GeocoderContainer.style.display == 'none' ) {
//     GeocoderContainer.style.display='60%';
//     GeocoderContainer.style.display='block';
//     searchShapefile.style.display = 'none';
//     searchShapefile.style.width = '90%';
 
//   } else {
//     GeocoderContainer.style.display = 'none';
//   }
 
//  };
//  showGeocoderContainer.addEventListener('click', handleToggle);





//  const handleTab2Toggle = () => {
//   if (searchShapefile.style.display == 'none' ) {
//     searchShapefile.style.display = 'block';
//     searchShapefile.style.width = '90%';
//     GeocoderContainer.style.display = 'none';
//     GeocoderContainer.style.width = '90%';
 
//   } else {
//     searchShapefile.style.display = 'none';
//   }
 
//  };
//  showsearchShapefile.addEventListener('click', handleToggle);





const handleToggle = () => {
 if (resultFormContainer.style.display == 'none' && flag =='True') {
   resultFormContainer.style.display='60%';
   resultFormContainer.style.display='block';
   searchContainer.style.display = 'none';
   searchContainer.style.width = '90%';

 } else {
   resultFormContainer.style.display = 'none';
   
 }

};
showresultContainer.addEventListener('click', handleToggle);

  // var result_value = "{{ result_value }}";  

  // if (result_value) {
  //   console.log("found your result");
  //   document.getElementById("resultFormContainer").style.display = "block";
  // }else{
  //   console.log("sorry");
  // }





const handleToggleInput = () => {
  if (searchContainer.style.display == 'none') {
    searchContainer.style.display = 'block';
    resultFormContainer.style.display = 'none';
    searchContainer.style.width = '60%';
   
  } else {
    searchContainer.style.display = 'none';
    GeocoderContainer.style.display = 'none';
    searchShapefile.style.display = 'none';
  }

};

showSearchFormField.addEventListener('click', handleToggleInput);
// const handleSearchFormInput = () => {

//   resultFormContainer.style.display='block';
//   searchContainer.style.display='none';

// };
// submitButton.addEventListener('click',handleSearchFormInput)
let polygonPoints = [];
let inputFieldValues=[];
let buttonClicked=false;






const addCoordinateButton = document.getElementById('addCoordinate'); // Replace 'your-button-id' with the actual ID of your button
const handleChooseFromMap = () => {

  // searchContainer.style.display = 'none';
  const dropdownValue = document.getElementById('dropdown').value;
  const existingInputFields = [...inputFieldsContainer.getElementsByClassName('input-field')];
 inputFieldValues = existingInputFields.map((field) => field.value.trim());

console.log('Existing Input Field Values:', inputFieldValues);
   

 var count=0;
 var lat_val=0;
 var long_val=0;
for (var i = 0; i < inputFieldValues.length; i++) {
lat_val+=(parseFloat(inputFieldValues[i].split(',')[0].trim()));
long_val+=(parseFloat(inputFieldValues[i].split(',')[1].trim()));
count++;
}
input_lat=(lat_val/=count).toFixed(4);
input_long=(long_val/=count).toFixed(4);

if(isNaN(input_lat)){
input_lat=''
}
if(isNaN(input_long)){
 input_long=''
  }

document.getElementById("Latitude").value=input_lat
document.getElementById("Longitude").value=input_long



  if (dropdownValue === 'circle') {
    inputFieldsContainer.innerHTML = '';
    removeMarkers();
    removeCircles();
    removeLines();
    let clickCount = 0;
    let centerPoint = null;
    let radius = 0;

    const handleClick = (e) => {
      if (clickCount === 0) {
        newMarker(e);
        centerPoint = e.latlng; // Set the first point as the center
        clickCount++;
      } else if (clickCount === 1) {
        newMarker(e);
        radius = centerPoint.distanceTo(e.latlng); // Calculate the distance between points as the radius

        // Create a circle using the center point and radius
        const circle = L.circle(centerPoint, {
          radius: radius,
          color: 'red',
          fillOpacity: 0.2
        }).addTo(map_folium);

        searchContainer.style.display = 'block'; // Show the search container after creating the circle
        searchContainer.style.width = '60%';

        map_folium.off('click', handleClick);
        map_folium.off('click', latLngPop);
      }
    };

    map_folium.off('click', newMarker);
    map_folium.off('click', latLngPop);
    map_folium.on('click', handleClick);

  }
  else if (dropdownValue === 'polygon') {

    removeCircles();
    // removeLines();
    // removeMarkers();
    const inputFields = inputFieldsContainer.getElementsByClassName('input-field');
    if (inputFields.length > 0) {
      for (let i = 0; i < inputFields.length; i++) {
        const coordinate = inputFields[i].value.trim();
        if (coordinate !== '') {
          const [lat, lng] = coordinate.split(',');
          const point = L.latLng(parseFloat(lat), parseFloat(lng));
          polygonPoints.push(point);
        }
      }
    }


    const handleClick = (e) => {
      const marker = L.marker(e.latlng).addTo(map_folium);
      marker.on('click', latLngPop);
    
      polygonPoints.push(e.latlng);
    addCoordinateButton.addEventListener('click',handleClick);
      const polygon = L.polygon(polygonPoints, {
        color: 'red',
        fillOpacity: 0.5
      }).addTo(map_folium);
    
    
    
    };
    map_folium.off('click', handleClick);
    map_folium.off('click', latLngPop);
    // map_folium.on('click', handleClick);

  }
   else {
    // Enable adding multiple points on the map
    map_folium.on('click', newMarker);
    map_folium.on('click', latLngPop);
  }

  searchContainer.style.display = 'none';
    
};


function resetForMap(){
  removeCircles()
  removeMarkers()
  removeLines()
  clearInputFields()
}


// Function to remove markers
function removeMarkers() {
  drawnPoints.forEach((marker) => {
    map_folium.removeLayer(marker);
  });
  drawnPoints = [];
}

// Function to remove circles
function removeCircles() {
  map_folium.eachLayer((layer) => {
    if (layer instanceof L.Circle || layer instanceof L.Polygon) {
      map_folium.removeLayer(layer);
    }
  });
}
// Function to remove lines
function removeLines() {
  map_folium.eachLayer((layer) => {
    if (layer instanceof L.Polyline) {
      map_folium.removeLayer(layer);
    }
  });
}
function clearInputFields() {
  const inputFields = inputFieldsContainer.getElementsByClassName('input-field');
  for (let i = 0; i < inputFields.length; i++) {
    inputFields[i].value = '';
  }
}
chooseFromMapButton.addEventListener('click', handleChooseFromMap);

    
    
var map_folium = L.map(
  "map_folium",
  {
      center: [10.8, 38.5],
      crs: L.CRS.EPSG3857,
      zoom: 6.5,
      zoomControl: false,
      preferCanvas: false,
      
  }
);
L.control.zoom({
  position: 'topright'
}).addTo(map_folium);
var tile_layer_3fe8f173c999f7e7ea86cabea4f6d802 = L.tileLayer(
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
  {"attribution": "Data by \u0026copy; \u003ca target=\"_blank\" href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\"_blank\" href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
).addTo(map_folium);



var tile_layer_topo = L.tileLayer(
  "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
  {
    attribution: 'Map data &copy; <a href="https://opentopomap.org/">OpenTopoMap</a>',
    maxZoom: 17,
    tileSize: 512,
    zoomOffset: -1,
  }
);



var tile_layer_watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.jpg', {
  attribution: 'Map tiles by <a href="http://stamen.com/">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org/">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0/">CC BY SA</a>'
});


var drawnPoints = [];
function newMarker(e) {
  console.log(e.latLng);
  var new_mark = L.marker(e.latlng).addTo(map_folium);
  new_mark.dragging.enable();
  new_mark.on('dblclick', function(e) {
    map_folium.removeLayer(e.target);
    removePointFromDrawnPoints(e.target);
    updateLinesAndShadedArea();
  });

  var lat = e.latlng.lat.toFixed(4);
  var lng = e.latlng.lng.toFixed(4);
  new_mark.bindPopup("Latitude: " + e.latlng.lat.toFixed(4) +
  "<br>Longitude: " + e.latlng.lng.toFixed(4));

  // Create additional input fields
  var inputField = document.createElement('input');
  inputField.type = 'text';
  inputField.value = lat + ', ' + lng;
  inputField.className = 'input-field';
  inputField.readOnly = true;
  inputField.style.border = '1px solid #ccc';
  inputField.style.borderRadius = '5px';



// Create the 'x' button
var removeButton = document.createElement('button');
removeButton.innerHTML = 'X';
removeButton.className = 'remove-button';
removeButton.addEventListener('click', function() {
  // Find the input container associated with the remove button
  var inputContainer = this.parentNode;

  // Find the input field within the container
  var inputField = inputContainer.querySelector('.input-field');

  // Find the corresponding marker based on the input field's value
  var marker = drawnPoints.find((m) => {
    var latlng = m.getLatLng();
    return (
      latlng.lat.toFixed(4) + ', ' + latlng.lng.toFixed(4) === inputField.value
    );
  });

  // If the marker is found, remove it from the map and the drawnPoints array
  if (marker) {
    // map_folium.removeLayer(marker);
    marker.removeFrom(map_folium);

    removePointFromDrawnPoints(marker);
  }

  // Remove the input field and the associated 'x' button
  inputFieldsContainer.removeChild(inputContainer);

  // Update lines and shaded area
  updateLinesAndShadedAreaOnRemove();
  
}

);



// Create a container to hold the input field and the 'x' button
var inputContainer = document.createElement('div');
inputContainer.className = 'input-container';
inputContainer.style.display = 'flex'; // Set display property to flex
inputContainer.style.alignItems = 'center'; 
inputContainer.appendChild(inputField);
inputContainer.appendChild(removeButton);

// Append the new input container to the main container
inputFieldsContainer.appendChild(inputContainer);

  // Add the marker to the drawn points array
  drawnPoints.push(new_mark);

  // Update lines and shaded area
  updateLinesAndShadedArea();

  // Log the coordinates to the console
  console.log('Clicked:', lat, lng);

}

function updateLinesAndShadedAreaOnRemove() {
  if (drawnPoints.length >= 3) {
    // Remove existing lines and shaded area
    map_folium.eachLayer((layer) => {
      if (layer instanceof L.Polyline || layer instanceof L.Polygon) {
        map_folium.removeLayer(layer);
      }
    });

    // Draw lines between the points
    for (var i = 0; i < drawnPoints.length - 1; i++) {
      var pointA = drawnPoints[i].getLatLng();
      var pointB = drawnPoints[i + 1].getLatLng();
      L.polyline([pointA, pointB]).addTo(map_folium);
    }

    // Shade the middle area
    var latLngs = drawnPoints.map((marker) => marker.getLatLng());
    L.polygon(latLngs, { fillOpacity: 0.3 }).addTo(map_folium);
  } else {
    // Remove existing lines and polygon
    map_folium.eachLayer((layer) => {
      if (layer instanceof L.Polyline || layer instanceof L.Polygon) {
        map_folium.removeLayer(layer);
      }
    });
  }
}

function removePointFromDrawnPoints(target) {
  var index = drawnPoints.findIndex((marker) => marker === target);
  if (index !== -1) {
    drawnPoints.splice(index, 1);
    
  }
}


function updateLinesAndShadedArea() {
  var allPoints = [...drawnPoints, ...polygonPoints];

  if (allPoints.length >= 3) {
    // Remove existing lines and shaded area
    map_folium.eachLayer((layer) => {
      if (layer instanceof L.Polyline || layer instanceof L.Polygon) {
        map_folium.removeLayer(layer);
      }
    });

    // Draw lines between the points
    for (var i = 0; i < allPoints.length - 1; i++) {
      var pointA = getLatLngFromPoint(allPoints[i]);
      var pointB = getLatLngFromPoint(allPoints[i + 1]);

      L.polyline([pointA, pointB]).addTo(map_folium);
    }

    // Shade the middle area
    var latLngs = allPoints.map((point) => getLatLngFromPoint(point));
    L.polygon(latLngs, { fillOpacity: 0.3 }).addTo(map_folium);
  }
 

  // Remove all markers from the map
  // removeMarkers();
}

function getLatLngFromPoint(point) {
  if (point instanceof L.Marker) {
    return point.getLatLng();
  }
  return point;
}

      map_folium.on('click', newMarker);
      
      
      var lat_lng_popup_2a508f1cb7ad5cc03a62b714bdbd867a = L.popup();
  function latLngPop(e) {
      lat_lng_popup_2a508f1cb7ad5cc03a62b714bdbd867a
          .setLatLng(e.latlng)
          .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
          "<br>Longitude: " + e.latlng.lng.toFixed(4))
          .openOn(map_folium);
        }
        map_folium.on('click', latLngPop);
        


var layer_control_60feae8019ef67d0b19cd93ee2680403 = {
  base_layers : {
      "openstreetmap" : tile_layer_3fe8f173c999f7e7ea86cabea4f6d802,
      "OpenTopoMap": tile_layer_topo,
      "Stamen Watercolor": tile_layer_watercolor
  },
  overlays :  {
  },
};
L.control.layers(
  layer_control_60feae8019ef67d0b19cd93ee2680403.base_layers,
  layer_control_60feae8019ef67d0b19cd93ee2680403.overlays,
  {"autoZIndex": true, "collapsed": true, "position": "topright"}
).addTo(map_folium);

L_NO_TOUCH = false;
L_DISABLE_3D = false;




function updateLinesAndShadedAreaForAdd() {
  // Remove existing polygon
  map_folium.eachLayer((layer) => {
    if (layer instanceof L.Polygon) {
      map_folium.removeLayer(layer);
    }
  });

  // Draw lines between the points
  for (let i = 0; i < polygonPoints.length - 1; i++) {
    const pointA = polygonPoints[i];
    const pointB = polygonPoints[i + 1];
    L.polyline([pointA, pointB]).addTo(map_folium);
  }

  // Create the polygon
  if (polygonPoints.length >= 3) {
    const polygon = L.polygon(polygonPoints, { color: 'red', fillOpacity: 0.5 }).addTo(map_folium);
  }
}


const handleAddCoordinate = () => {
  console.log("object");
  const latitudeInput = document.getElementById('Latitude');
  const longitudeInput = document.getElementById('Longitude');

  const latitude = parseFloat(latitudeInput.value.trim());
  const longitude = parseFloat(longitudeInput.value.trim());

  if (isNaN(latitude) || isNaN(longitude)) {
    // Handle invalid input
    return;
  }

  const coordinate = L.latLng(latitude, longitude);
  polygonPoints.push(coordinate);
  
  // Plot the coordinate on the map
  const marker = L.marker(coordinate).addTo(map_folium);
  marker.on('click', latLngPop);

  updateLinesAndShadedArea();

  // Create input field
  const inputField = document.createElement('input');
  inputField.type = 'text';
  inputField.value = latitude + ', ' + longitude;
  inputField.className = 'input-field';
  inputField.readOnly = true;
  inputField.style.border = '1px solid #ccc';
  inputField.style.borderRadius = '5px';

  // Create the 'x' button
  const removeButton = document.createElement('button');
  removeButton.innerHTML = 'X';
  removeButton.className = 'remove-button';
  removeButton.addEventListener('click', () => {
    // Remove the coordinate from the polygonPoints array
    const index = polygonPoints.findIndex((point) => point.equals(coordinate));
    if (index !== -1) {
      polygonPoints.splice(index, 1);
    }

    // Remove the marker from the map
    map_folium.removeLayer(marker);

    // Remove the input field and the associated 'x' button
    const inputContainer = inputField.parentNode;
    inputContainer.parentNode.removeChild(inputContainer);

    // Update lines and shaded area
  });

  // Create a container to hold the input field and the 'x' button
  const inputContainer = document.createElement('div');
  inputContainer.className = 'input-container';
  inputContainer.style.display = 'flex';
  inputContainer.style.alignItems = 'center';
  inputContainer.appendChild(inputField);
  inputContainer.appendChild(removeButton);

  // Append the new input container to the main container
  inputFieldsContainer.appendChild(inputContainer);

  // Update lines and shaded area
  updateLinesAndShadedArea();

  // Clear input fields
  latitudeInput.value = '';
  longitudeInput.value = '';
};

addCoordinateButton.addEventListener('click', handleAddCoordinate);







function mark_latlong(a,b,c,d,e,f,g,h){
lat_center=(a+c+e+g)/4;
lon_center=(b+d+f+h)/4;

 const latitudeInput=[a,c,e,g];
 const longitudeInput=[b,d,f,h];
  for(i=0;i<=3;i++){

  const latitude = parseFloat(latitudeInput[i]);
  const longitude = parseFloat(longitudeInput[i]);
  
  const coordinate = L.latLng(latitude, longitude);
  polygonPoints.push(coordinate);
  
  // Plot the coordinate on the map
  const marker = L.marker(coordinate).addTo(map_folium);
  marker.on('click', latLngPop);
  }
  updateLinesAndShadedArea()


  console.log(lat_center,lon_center);

  map_folium.setView([lat_center,lon_center])
}

// markButton.addEventListener('click',mark_latlong);

