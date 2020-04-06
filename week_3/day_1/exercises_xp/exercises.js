let body = document.querySelector("body")[0];

let div = document.querySelector("div");

div.setAttribute("id", "socialNetworkNavigation")

let new_li = document.createElement("li")

let new_textNode = document.createTextNode("logout")

new_li.append(new_textNode)

let ul = document.querySelector("ul")

ul.appendChild(new_li)


let ul1 = document.body.children[2]

ul1.lastElementChild.innerText = "Richard"

let ul2 = document.body.children[3]

console.log(ul2)

ul1.firstElementChild.innerText = "Tyran"

ul2.firstElementChild.innerText = "Tyran"

let paragraph = document.createTextNode("Hey students")

let paragraph2 = document.createTextNode("Hey students")

ul1.appendChild(paragraph)

ul2.appendChild(paragraph2)

ul2.children[1].remove()
