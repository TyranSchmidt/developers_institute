let div = document.querySelector("div");
div.style.fontSize = "20px";

function banner() {
	div.innerText = "The sales end in 10min!";
	div.style.fontSize = "40px";
	div.style.backgroundColor = "red";
}

setTimeout(banner, 5000);

let id;
let time = 11;
// div.innerText = "The sales end in " + time + "sec!";

id = setInterval(countdown, 1000);
	
function countdown() {
	if (time > 0) {
		time = time - 1;
		div.innerText = "The sales end in " + time + "sec!";
	} else {
		clearInterval(id);
		div.innerText = "You just missed our sales!";
		div.style.backgroundColor = "orange";
	};
}
