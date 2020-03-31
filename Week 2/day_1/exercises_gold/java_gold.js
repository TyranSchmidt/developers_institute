
var me = ["my","favorite","color","is","blue"];

console.log(me.toString());

let first = "bam";
let second = "run";

let third = first.substring(0, 2) + second.substring(2);
let fourth = second.substring(0, 2) + first.substring(2);
let both = third + " " + fourth;
console.log(both);

let first_number = prompt("Give me your first number");
console.log("The first number is " + first_number);
let boolean1 = isNaN(first_number);
console.log("Is this a number? " + !boolean1)

if (boolean1 == true) {
	alert("Please enter a valid number")
}

else {
let second_number = prompt("Give me your second number");
console.log("The second number is " + second_number);
let boolean2 = isNaN(second_number);
console.log("Is this a number? " + !boolean2)


if (boolean2 == true) {
	alert("Please enter a valid number")
}

else {

alert("The numbers added together = " + (Number(first_number) + Number(second_number)));
alert("The numbers subtracted from eachother = " + (first_number - second_number));
alert("The numbers multiplied together = " + (first_number * second_number));
alert("The numbers divided by eachother = " + (first_number / second_number));

console.log("The numbers added together = " + (Number(first_number) + Number(second_number)));
console.log("The numbers subtracted from eachother = " + (first_number - second_number));
console.log("The numbers multiplied together = " + (first_number * second_number));
console.log("The numbers divided by eachother = " + (first_number / second_number));
}
}