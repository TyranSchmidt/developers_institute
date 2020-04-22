// volume = 4 / 3 x math.PI x r x r x r

let form = document.getElementById("MyForm")
let radius = document.getElementById("radius")
let volume = document.getElementById("volume")
let submit = document.getElementById("submit")

submit.addEventListener("click", mathStuff)

function mathStuff() {
	radius = radius.value
	let total = (4 / 3) * (Math.PI) * radius * radius * radius
	let y = form.children[3]
	y.setAttribute("value", total)
}