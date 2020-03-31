// let fav_colors = ["red", "blue", "green"];

// console.log("My 1st choice is " + fav_colors[0]+ "."
// + " My 2nd choice is " + fav_colors[1] + "." 
// + " My 3rd choice is " + fav_colors[2] + ".")

// let number =prompt("Give me a number")
// if (!isNaN(number)) {
// 	while (number < 10) {
// 		number = prompt("Give me a new number")
// 		if (isNaN(number)){
// 			alert("Don't try to trick me!")
// 		}
// 	}
// } 
// else if (isNaN(number)) {
// 	alert("Next time give a number, refresh to try again.")
// } 

let people = ["Greg", "Mary", "Devon", "James"];

for (y of people) {
	console.log(y)
}

people.shift()
console.log(people)

people.splice(2, 1, "Jason")
console.log(people)

people.push("Tyran")
console.log(people)

for (y of people) {
	console.log(y)
	if (y === "Mary") {
		break;
	}
}

let some_people = people.slice(1, 3)
console.log(some_people)

console.log(people.indexOf("Mary"))

console.log(people.indexOf("Foo"))

let last = people.length - 1;
last = people.slice(last)
console.log(last)

let age = [20,5,12,43,98,55];

let total = age[0] + age[1] + age[2] + age[3] + age[4] + age[5]
console.log(total)

for (y of age) {
	if (y % 2 == 0) {
		console.log(y)
	}
}

age.sort();
console.log(age.slice(age.length - 1))