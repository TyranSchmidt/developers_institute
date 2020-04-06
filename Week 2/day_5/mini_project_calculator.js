
let numbers = []
let value = ""
let set_numbers = ""
let total_value = ""

function calc(number) {
	set_numbers = set_numbers + number	
	console.log(set_numbers)	
	return set_numbers
}

function dot(spec) {
	set_numbers = set_numbers + `${spec}`	
	console.log(set_numbers)	
	return set_numbers
}

function math(sign) {
	numbers.push(set_numbers)
	set_numbers = ""
	numbers.push(sign)
	console.log(numbers.join(" "))
}

function total() {
	numbers.push(set_numbers)
	set_numbers = ""
	value = numbers.join(" ")
	total_value = eval(value)
	console.log(total_value)
	numbers = [total_value]
	return numbers
	return value
}

function refresh() {
	numbers = []
	value = ""
	set_numbers = ""
	total_value = ""
	return numbers 
	return value 
	return set_numbers 
	return total_value
}

