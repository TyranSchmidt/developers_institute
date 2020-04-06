function insert_Row() {
	let table = document.getElementById("sampleTable")
	let row = table.insertRow();
	let cell1 = row.insertCell(0);
	let cell2 = row.insertCell(1);
	cell1.innerText = "new cell1"
	cell2.innerText = "new cell2"
}
