
let body = document.getElementsByTagName("body");

let planetList = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

for (planets of planetList) {
	let planet = document.createElement("div");
	planet.innerHTML = planets;
	body[0].appendChild(planet);
	planet.setAttribute("class", "planet");
	planet.setAttribute("id", planets);
}

document.getElementById("Mercury").style.backgroundColor = "red";
document.getElementById("Venus").style.backgroundColor = "blue";
document.getElementById("Earth").style.backgroundColor = "green";
document.getElementById("Mars").style.backgroundColor = "yellow";
document.getElementById("Jupiter").style.backgroundColor = "pink";
document.getElementById("Saturn").style.backgroundColor = "white";
document.getElementById("Uranus").style.backgroundColor = "orange";
document.getElementById("Neptune").style.backgroundColor = "purple";