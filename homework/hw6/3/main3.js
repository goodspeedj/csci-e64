
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
    	var pop = json[i].POPULATION;

    	if (pop > 119553334) {
    		changeColor(json[i].COUNTRY, "#BD0026");
    	}
    	else if (pop > 95706668 && pop <= 119553334) {
    		changeColor(json[i].COUNTRY, "#F03B20");
    	}
    	else if (pop > 71860002 && pop <= 95706668) {
    		changeColor(json[i].COUNTRY, "#FD8D3C");
    	}
    	else if (pop > 48013336 && pop <= 71860002) {
    		changeColor(json[i].COUNTRY, "#FECC5C");
    	}
    	else if (pop > 24166670 && pop <= 48013336) {
    		changeColor(json[i].COUNTRY, "#FECC5C");
    	}
    	else {
    		changeColor(json[i].COUNTRY, "#FFFFB2");
    	}
    }
}