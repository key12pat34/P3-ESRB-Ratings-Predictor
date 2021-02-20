// // Step 1
let map = createMap();
addBaseLayer(map);
// createBorough(map);
function createMap() {
  // Creating map object
  let map = L.map("map", {
    center: [33.776108, -84.39753],
    zoom: 10,
  });
  return map;
}

// Step 2
function addBaseLayer(map) {
  let baseLayer = L.tileLayer(
    "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
    {
      attribution:
        "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
      tileSize: 512,
      maxZoom: 18,
      zoomOffset: -1,
      id: "mapbox/streets-v11",
      accessToken:
        "pk.eyJ1IjoiZGFzc2Nvb3RlciIsImEiOiJja2pwdHZzNHoxMXlmMnhwZWZkaWp6d2xiIn0.zc1HfeVEMzRwCEm_glvbUQ",
    }
  );
  baseLayer.addTo(map);
}

// create markers for schools
d3.json("/api").then(function (data) {
  console.log(data);
  console.log(data.longitude);
  for (var i = 0; i < data.length; i++) {
    let dataquery = data[i];
    let lat = dataquery.latitude;
    let lng = dataquery.longitude;
    let schoollocation = [lat, lng];
    console.log(schoollocation);
    L.circle(schoollocation, {
      color: "red",
      fillColor: "#f03",
      fillOpacity: 0.5,
      radius: 500,
    })
      .bindPopup(
        "<h4>" +
          data[i].name +
          "</h4> <hr> <h4>" +
          data[i].type +
          "</h4> <br> <h6>Enrollment: " +
          data[i].enrollment +
          "<br>Teacher Count: " +
          data[i].teachercount
      )
      .addTo(map);
  }
});

// Realtor API Query
// Realtor API jQuery Code provided code: https://rapidapi.com/apidojo/api/realtor?endpoint=apiendpoint_e259775d-d98e-479f-8440-206d6d4fa892

//Set up the Filter Button
var button = d3.select("#filter-btn");
button.on("click", runEnter);

var clear = d3.select("#clear-btn");
clear.on("click", runClear);

function runClear() {
  //Clear current markers
  location.reload();
}

//Start Filter Function
function runEnter() {
  //Assign variables based on the filter form
  let selectedcity = d3.select("#city").property("value");
  let limit = d3.select("#limit").property("value");
  let minbed = d3.select("#minbed").property("value");
  // Use this once we have the sort radios figured out
  let sort = d3.select("input[name=radioinput]:checked");
  let minbath = d3.select("#minbath").property("value");
  let maxprice = d3.select("#maxprice").property("value");
  let maxage = d3.select("#maxage").property("value");

  //Load Realtor.com API with Filter variables assigned in the call
  const settings = {
    async: true,
    crossDomain: true,
    // Use this URL when we have the Sort Drop Down/Radial Buttons figured out
    url: `https://realtor.p.rapidapi.com/properties/v2/list-for-sale?city=
                        ${selectedcity}&limit=${limit}&offset=0&state_code=GA&beds_min=
                        ${minbed}&sort=${sort}&baths_min=${minbath}&price_max=${maxprice}
                        &age_max=${maxage}`,
    // "url": `https://realtor.p.rapidapi.com/properties/v2/list-for-sale?city=
    //         ${selectedcity}&limit=${limit}&offset=0&state_code=GA&beds_min=
    //         ${minbed}&sort=relevance&baths_min=${minbath}&price_max=${maxprice}&age_max=${maxage}`,
    method: "GET",
    headers: {
      "x-rapidapi-key": "a32cef4e7fmshe42c5a1bfdbce17p135b01jsn21abc1df2bea",
      "x-rapidapi-host": "realtor.p.rapidapi.com",
    },
  };
  //Process Realtor.com API through for loop and append listings to map markers
  $.ajax(settings).done(function (response) {
    let querydata = [response];
    var propertyquery = querydata[0].properties;
    //Start Loop, set max length based on number of properties returned in search
    for (var i = 0; i < propertyquery.length; i++) {
      var property = propertyquery[i];
      //Define variables on each property
      let lat = property.address.lat;
      let lng = property.address.lon;
      let location = [lat, lng];
      let bedcount = property.beds;
      let bathcount = property.baths;
      let pricecount = property.price;
      let weburl = property.rdc_web_url;
      let street = property.address.line;
      let city = property.address.city;
      let state = property.address.state;
      let zip = property.address.postal_code;
      //Append coordinates to map and assign property variables in the pop up
      var marker = L.marker(location)
        .bindPopup(
          "<h4>" +
            street +
            "</h4> <hr> <h4>" +
            city +
            "," +
            state +
            " " +
            zip +
            "</h4> <br> <h6>Beds: " +
            bedcount +
            "<br>Baths: " +
            bathcount +
            "<br>Price: " +
            pricecount +
            '<br><a href="' +
            weburl +
            '">See on Realtor.com</a></h6>'
        )
        .addTo(map);
    }
  });
}
