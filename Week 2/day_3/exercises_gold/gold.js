let family = {
	size : 4,
	names : ["Dean", "Tyran", "Levi", "Guy"],
}

for (let y in family) {
	console.log(y)
}

console.log(family.size)
for (let y of family.names) {
	console.log(y)
}

let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent : {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

console.log(building.number_levels)

console.log(building["number_of_apt_by_level"][1] + building["number_of_apt_by_level"][3])

console.log(building.name_of_tenants[1] + " " + building["number_of_rooms_and_rent"]["Dan"][0])

let x = building["number_of_rooms_and_rent"] 
if (x["Sarah"][1] + x["David"][1] > x["Dan"][1]) {
	console.log("The owner of this building should increase Dan's rent")
	x["Dan"][1] = 2010
	console.log(building) 
}


let person1 = {
	fullName: "Jen Marie",
	mass: 120,
	height: 1.60,
} 

let person2 = {
	fullName: "Benjamin Frey",
	mass: 190,
	height:1.85,
}

function BMI_calculator(mass, height) {
	let result = (mass / (height * height))
	return result;
}

let BMI_1 = BMI_calculator(person1.mass, person1.height)
person1.BMI = BMI_1.toFixed(2)
console.log(person1.BMI)

let BMI_2 = BMI_calculator(person2.mass, person2.height)
person2.BMI = BMI_2.toFixed(2)
console.log(person2.BMI)

function Bigger_number(num1, num2) {
	array = [Number(num1), Number(num2)];
	array = array.sort();
	return array;
}

BMI_array = Bigger_number(person2.BMI, person1.BMI);
small = BMI_array[0];
big = BMI_array[1];
console.log("Jen's BMI is " + small + " which is smaller than Benjamin's " + big + ".")


