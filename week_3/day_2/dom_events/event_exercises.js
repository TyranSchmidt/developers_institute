// exercise 1

function insert_Row() {
	let table = document.getElementById("sampleTable")
	let row = table.insertRow();
	let cell1 = row.insertCell(0);
	let cell2 = row.insertCell(1);
	cell1.innerText = "new cell1"
	cell2.innerText = "new cell2"
}

//exercise 2

// e.target.style
// this.style

let btn = document.getElementById("jsstyle");

btn.addEventListener("click", OnClick);
btn.addEventListener("mouseover", OnMouseOver)

function OnClick(e) {
	e.target.style.color = "red";
}

function OnMouseOver(e) {
	e.target.style.backgroundColor = "lightblue";
}