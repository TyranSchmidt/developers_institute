let str = "swing"

let length = str.length

if (length > 2 && !str.substring("ing")) {
	console.log(str + "ing")
}
else if (length > 2 && str.substring("ing")) {
	console.log(str + "ly")
}