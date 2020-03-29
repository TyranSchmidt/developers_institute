let addressNumber = 12;
let addressStreet = "Yitshak Sadeh";
let country = "Israel";

let global_adress = "I live in " + addressStreet + addressNumber +  ", in " + country;

console.log(global_adress);

let birth = 1998;
let future = 2024;

let future_age =  (future - birth);

console.log("I will be " + future_age + " in " + future);

let pets = ["cat", "dog", "fish", "rabbit", "cow"]
console.log(pets[1])
pets.splice(3, 1, "horse")
console.log(pets)
console.log(pets.length)