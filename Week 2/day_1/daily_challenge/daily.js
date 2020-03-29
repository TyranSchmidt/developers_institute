let array = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log(array);
array.splice(0, 1);
console.log(array);
array.sort();
console.log(array);
array.push("kiwi");
console.log(array);
array.splice(0, 1);
console.log(array);
array.reverse();
console.log(array);

let array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let orange = array2[1][1]
console.log(orange)