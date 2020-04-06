// function checkDriverAge() {
// 	let driver_age = prompt("What is your age?")
// 	return driver_age
// }
// let age = checkDriverAge()

// if (Number(age) < 18) {
// alert("Sorry, you are too young to drive this car. Powering off");
// } else if (Number(age) > 18) {
// alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
// alert("Congratulations on your first year of driving. Enjoy the ride!");
// }

// function check_Driver_Age(your_age) {
// 	let the_age = your_age
// 	return the_age
// }

// let new_age = check_Driver_Age(92)


// if (Number(new_age) < 18) {
// alert("Sorry, you are too young to drive this car. Powering off");
// } else if (Number(new_age) > 18) {
// alert("Powering On. Enjoy the ride!");
// } else if (Number(new_age) === 18) {
// alert("Congratulations on your first year of driving. Enjoy the ride!");
// }


// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100,
// }

// function checkBasket() {	
// 	let user_item = prompt("What item do you want?")
// 		if (user_item in amazonBasket) {
// 			console.log(user_item + " is in the basket")
// 		} else {
// 			console.log(user_item + " is not in the basket")
// 		}
// }    


// checkBasket()


// let shoppingList = ["banana", "orange", "apple"]

// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10,
// } 

// function myBill() {
// 	let n = shoppingList.length;
// 	let str = Number("");
// 	for (i = 0; i < n; i++) {
// 		let word = shoppingList[i];
// 		if (shoppingList[i] in prices && stock[word] > 0) {
// 			str = prices[word] + str;
// 			stock[word] = stock[word] - 1;
// 		}
// 	}
// 	console.log(stock)
// 	console.log(str)
// }

// myBill()

let total_night = 0

function hotel_cost(nights) {
	total_night = 140 * nights 
	return total_night
}

function plane_ride_cost(city) {
	switch (city) {
		case "" :
		plane_ride_cost(prompt("enter a new city"))
	 	break;
		case "London":
		total_night = total_night + 183;
		break;
		case "Paris":
		total_night = total_night + 220;
		break; 
	 	default:
	 	total_night = total_night + 300;
	 	break;
	}
	return total_night;
}

function rental_car_cost(days) {
	total_night = total_night + 40 * days 
	return total_night
}




