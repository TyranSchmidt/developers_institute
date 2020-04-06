let allBooks = [
	{
		Title : "Goosebumps The beast from the east.",
		Author : "R.L Stine",
		Image : "https://kbimages1-a.akamaihd.net/61caa848-4bf0-407e-a1ea-a0ab4a06e792/1200/1200/False/the-beast-from-the-east-goosebumps-43.jpg",
		alreadyRead : false,
	},
	{
		Title : "The Mind Readers",
		Author : "Lori Brighton",
		Image : "https://images-na.ssl-images-amazon.com/images/I/51L-0YsMB9L._SX331_BO1,204,203,200_.jpg",
		alreadyRead : true,
	}

]

let Title1 = allBooks[0].Title 
let Author1 = allBooks[0].Author 
let Image1 = allBooks[0].Image
let alreadyRead1 = allBooks[0].alreadyRead

let Title2 = allBooks[1].Title 
let Author2 = allBooks[1].Author 
let Image2 = allBooks[1].Image
let alreadyRead2 = allBooks[1].alreadyRead

let table = document.createElement("table");
let tbody = document.createElement("tbody");

 