//exericse 1

let body = document.querySelector("body");

let p = document.getElementsByTagName("p");
	// p is an array

	for (x of p) {
		// x.classList.add("para_article");
		// x.setAttribute("class", "para_article");
		x.className = "para_article";
	}

let article = document.querySelector("article");

let last_p = article.children[5];

article.removeChild(last_p);

let h2 = document.querySelector("h2");

h2.addEventListener("click", whenClick)

function whenClick() {
	article.removeChild(h2);
}

let n = Math.floor(Math.random() * 101) + ("px")
document.querySelector("h1").style.fontSize = n
/* adding life to a dead page (text color and background color
spam refresh a few times ;))*/
let colors = ["blue", "brown", "green"]
let v = Math.floor(Math.random() * 3)
document.querySelector("h1").style.color = colors[v]
let back_colors = ["purple", "orange", "black", "red"]
let oh = Math.floor(Math.random() * 4)
document.querySelector("h1").style.backgroundColor = back_colors[oh]

let p1 = article.children[2]
p1.addEventListener("click", newClick)
	function newClick() {
		p1.style.visibility = "hidden"
	}

let p2 = article.children[3]
console.log(p2)
p2.addEventListener("click", fadeout)
	
	function fadeout() {
	p2.style.opacity = 0;
	p2.style.transitionProperty = "opacity";
	p2.style.transitionDuration = "2s";
	}

let new_p = body.children[3];
let button = document.createElement("button")
button.innerText = "submit"
button.addEventListener("click", funky)

let input1 = document.getElementsByTagName("input")[0]
let input2 = document.getElementsByTagName("input")[1]
let table = document.createElement("table");
	let row = table.insertRow();
	let cell1 = row.insertCell(0);
	let cell2 = row.insertCell(1);
	cell1.innerText = "Name";
	cell2.innerText = "Thoughts";
new_p.insertBefore(table, new_p.childNodes[0])
new_p.insertBefore(button, new_p.childNodes[0])
	function funky() {
		row = table.insertRow();
		cell1 = row.insertCell(0);
		cell2 = row.insertCell(1);
		cell1.innerText = input1.value;
		cell2.innerText = input2.value;
	}


//exercise 2

let i = ""
let p_ex_2 = body.children[3]
let strongs = document.getElementsByTagName("strong")
let strong_words = ""

function get_bold_items() {
	for (strong of strongs) {
		strong_words = strong_words + " " + (strong.innerText)
	}
	return strong_words
}

function highlight() {
	for (strong of strongs) {
	strong.style.color = "blue";
	}	
	
}

function return_normal() {
	for (strong of strongs) {
	strong.style.color = "black";
	}
}

p_ex_2.addEventListener("mouseover", highlight)
p_ex_2.addEventListener("mouseout", return_normal)

get_bold_items()
highlight()
return_normal()
console.log(strong_words)

