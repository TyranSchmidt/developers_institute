
var me = ["my","favorite","color","is","blue"];

console.log(me.toString());

let first = "bam";
let second = "run";

let third = first.substring(0, 2) + second.substring(2);
let fourth = second.substring(0, 2) + first.substring(2);
let both = third + " " + fourth;
console.log(both);

let first_number = prompt("Give me your first number");
console.log(first_number);
let boolean1 = isNaN(first_number);
console.log(boolean1)

if (boolean1 == true) {
	alert("Please enter a valid number")
}

else {
let second_number = prompt("Give me your second number");
console.log(second_number);
let boolean2 = isNaN(second_number);
console.log(boolean2)


if (boolean2 == true) {
	alert("Please enter a valid number")
}

else {

console.log(Number(first_number) + Number(second_number));
console.log(first_number - second_number);
console.log(first_number * second_number);
console.log(first_number / second_number);
}
}