let age = prompt("How old are you?")

if (age < 18) {
	alert("Sorry, you are too young to drive this car. Powering off.")
} else if (age == 18) {
	alert("Congratulations on your first year of driving. Enjoy the ride!")
} else {
	alert("Powering On. Enjoy the ride!")
}


var a = 2 + 2; //makes 4 

switch (a) { //if a = 3 then do this
  case 3:
    alert( 'Too small' );
    break;
  case 4: //if a = 4 then do this
    alert( 'Exactly!' );
    break;
  case 5: //if a = 5 then do this
    alert( 'Too large' );
    break;
  default: //if none of the above are true do this
    alert( "I don't know such values" );
}


var a = 2 + 2; //a = 4

switch (a) { //if a = 4 do this
  case 4:
    alert('Right!');
    break; 

  case 3: //if a = 3 or 5 do this
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default: //if none of the above do this
    alert('The result is strange. Really.');
}