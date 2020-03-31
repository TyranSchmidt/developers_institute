let number = prompt("Give me a number.")

if (isNaN(number)) {
	alert("error 303: number not found")
}
else if (number % 2 == 0) {
	alert(number + ' is an even Number');
} else{
	alert(number + ' is an odd Number');
}

let x = 11
let y = 120

if (x > y) {
	alert(x + " is bigger than " + y)
} else {
	alert(y + " is bigger than " + x)
}

let language = prompt("What language do you speak?")

switch (language) {
	case "French":
	alert("Bonjour");
	break;
	case "English":
	alert("Hello");
	break;
	case "Hebrew":
	alert("Shalom");
	break;
	default:
	alert(":)")
}

let grade = Number(prompt("What is your grade?"))

switch (true) {
	case  (grade >= 90):
		alert("A");
		break;
	case (grade < 90 && grade >= 80):
		alert("B"); 
		break;
	case (grade < 80 && grade >= 70):
		alert("C"); 
		break;
	case (grade < 70):
	    alert("D"); 
	    break;
}