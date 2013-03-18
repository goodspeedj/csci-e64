
var data_json = document.getElementById("json").value;
var json      = JSON.parse(data_json);


/*
 * Set the fill color of a SVG element
 */
function changeColor(id, color) {
    document.getElementById(id).setAttribute("fill", color);
}


function iterate() {
    for (var i = 0; i < json.length; i++) {
        startX += 60;
        var y = yAxisLen - ((parseFloat(json[i].OPEN) - getYMin()) * yAxisDiv);
    }
}