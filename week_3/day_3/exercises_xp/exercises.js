let animate = document.getElementById("animate")

function myMove() {
	let pos_x = 0;
	let id = setInterval(function() {
		if (pos_x == 350) {
			clearInterval(id);
		} else {
			pos_x++;
			animate.style.left = pos_x + "px";
		}
	}, 5); 
}


function allowDrop(event) {
event.preventDefault(); 
}


function allowEnter(event) {
  event.target.classList.add('over');
}


function allowLeave(event) {
  event.target.classList.remove('over');
}

function dragStart(event) {
console.log("id: ",  event.target.id )
event.dataTransfer.setData("text", event.target.id);
}

function dragDrop(event) {
console.log("event.target:",event.target) 
event.preventDefault();

let data = event.dataTransfer.getData("text");
console.log("data: ",  data) 
  
let box = document.getElementById(data)
event.target.appendChild(box);
}