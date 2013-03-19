
/*
 * Set the fill color of a SVG element
 */
function changeColor(id, color) {
    document.getElementById(id).setAttribute("fill", color);
}


/*
 * Iterate over the countries and set the color
 */
function iterate() {
	var data_json  = document.getElementById("data").value;
	var json       = JSON.parse(data_json);

    for (var i = 0; i < json.length; i++) {
    	changeColor(json[i].COUNTRY, "green");
    }
}