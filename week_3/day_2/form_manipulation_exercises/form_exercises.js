function getvalue() {
	let a = document.forms[0].children[1].value
	let b = document.forms[0].children[4].value
	console.log(a)
	console.log(b)
}

function doStuff() {
	let c = document.getElementById("select1")
	let value = c.children[1].value
	let Work = document.createElement("option")
	
	Work.setAttribute("value", "work")
	let work_text = document.createTextNode("Job")
		Work.appendChild(work_text)
		c.append(Work)

	let primary = document.createElement("option")
	primary.setAttribute("value", "Primary School")
	let school = document.createTextNode("little school for little people")
		primary.appendChild(school)
		c.appendChild(primary)
		c.insertBefore(primary, c.firstChild)
		
	select1.options[3].selected = true
	select1.value = "banana"
	select1.selectedIndex = 3

	let body = document.querySelector("body")
	let button = document.createElement("button")
	let button_label = document.createTextNode("Click Me")
	button.appendChild(button_label)
	body.appendChild(button)
		button.addEventListener("click", buttonClick)
			function buttonClick() {
				alert(select1.value)
			}
	console.log(c)
}


doStuff()