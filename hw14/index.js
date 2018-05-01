var $tbody = document.querySelector("tbody");

var $dateInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");

var $searchBtn1 = document.querySelector("#search1");
var $searchBtn2 = document.querySelector("#search2");
var $searchBtn3 = document.querySelector("#search3");
var $searchBtn4 = document.querySelector("#search4");
var $searchBtn5 = document.querySelector("#search5");

$searchBtn1.addEventListener("click", dateFilterClick());
$searchBtn2.addEventListener("click", cityFilterClick());
$searchBtn3.addEventListener("click", stateFilterClick());
$searchBtn4.addEventListener("click", countryFilterClick());
$searchBtn5.addEventListener("click", shapeFilterClick());

var filteredData = dataSet;
console.log(filteredData);

function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredData.length; i++) {
    var sighting = filteredData[i];
    var fields = Object.keys(sighting);
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sighting[field];
    }
  }
}

renderTable();

function dateFilterClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterUfo = $dateInput.value.trim().toLowerCase();

  filteredData = dataSet.filter(function(ufos) {
    var dateTime = ufos.datetime.toLowerCase();

    return dateTime == filterUfo;
  });
  renderTable();
}

function cityFilterClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterUfo = $cityInput.value.trim().toLowerCase();

  filteredData = dataSet.filter(function(ufos) {
    var city = ufos.city.toLowerCase();

    return city == filterUfo;
  });
  renderTable();
}

function stateFilterClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterUfo = $stateInput.value.trim().toLowerCase();

  filteredData = dataSet.filter(function(ufos) {
    var state = ufos.state.toLowerCase();

    return state == filterUfo;
  });
  renderTable();
}

function countryFilterClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterUfo = $countryInput.value.trim().toLowerCase();

  filteredData = dataSet.filter(function(ufos) {
    var country = ufos.country.toLowerCase();

    return country == filterUfo;
  });
  renderTable();
}

function shapeFilterClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterUfo = $shapeInput.value.trim().toLowerCase();

  filteredData = dataSet.filter(function(ufos) {
    var shape = ufos.shape.toLowerCase();

    return shape == filterUfo;
  });
  renderTable();
}