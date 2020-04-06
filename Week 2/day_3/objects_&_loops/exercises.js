let ID = {
	username : "foodisgood",
	password : "1314",
}

let database = [ID]

let newsfeed = [
	{
		username : "break",
		timeline : "2000-2020",
	},
	{
		username : "main",
		timeline : "1992-2020",
	},
	{
		username : "irrelevant",
		timeline : "1995 - 2020",
	},
]



for (i = 0; i < 16; i++) {
	if (i % 2 == 0) {
		console.log(i + " is an even number")
	} else {
		console.log(i + " is an odd number")
	}
}

let person = {
fname:"John", 
lname:"Doe", 
age:25,
friends:["Lea", "Joanna", "Mark"]
};

for (let x in person) {
	console.log(person[x])
} for (let x of person.friends) {
	console.log(x)
}

let names = ["john", "sarah", 23, "Rudolf",34]

for (let y of names) {
	if (typeof y != "string") {
		continue;
	} else if (typeof y == "string") {
		let x = y.charAt(0)
		x = x.toUpperCase()
		console.log(x + y.substring(1))
	}
}

for (let y of names) {
	if (typeof y != "string") {
		break;
	}
	else if (typeof y == "string")
		console.log(y)
}