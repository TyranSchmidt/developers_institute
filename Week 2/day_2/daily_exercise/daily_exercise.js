let str = "This dinner is not that bad!"

let not = (str.search("not"))
let bad = (str.search("bad"))
let sub = str.substring(not)
console.log(sub)
console.log(bad)
console.log(not)


if (not < bad && not > -1) {
	str = str.slice(0, not) 
	str = str + "good"
	console.log(str)
}