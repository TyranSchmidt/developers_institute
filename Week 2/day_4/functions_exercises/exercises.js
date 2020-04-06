function age(myAge) {
	let momAge = myAge * 2
	let dadAge = momAge * 1.2
	console.log("My age is " + myAge + " My mom's age is " + momAge + " My dad's age is " + dadAge)
}

age(22)


function age2(myAge2) {
	let momAge2 = myAge2 * 2
	return momAge2
}

console.log(age2(22))