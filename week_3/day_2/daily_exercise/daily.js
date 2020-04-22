let div = document.querySelector("div")

div.addEventListener("click", click)
div.addEventListener("mouseover", mouseOver)
div.addEventListener("mouseout", mouseOut)
div.addEventListener("dblclick", dblClick)

function click() {
	div.style.opacity = 0.2;
	div.style.transitionProperty = "opacity";
	div.style.transitionDuration = "10s";
}
function dblClick() {
	div.style.opacity = 1;
	div.style.transitionProperty = "opacity";
	div.style.transitionDuration = "5s";
}
function mouseOver() {
	div.style.fontSize = "50px";
	div.style.color = "red";
}
function mouseOut() {
	div.style.fontSize = "20px";
	div.style.backgroundColor = "black";
}
