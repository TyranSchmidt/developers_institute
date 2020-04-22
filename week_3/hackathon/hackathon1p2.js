	let btn_out= document.getElementById("log_out"); //log out button

	//Set all input variables

	let form= document.getElementsByTagName("form")[0];
	let table= document.getElementById("table");
	let input_name= form.getElementsByClassName("input1")[0];
	let input_date= form.getElementsByClassName("input1")[1];
	let input_loc= form.getElementsByClassName("input1")[2];
	let input_type= form.getElementsByClassName("input1")[3];
	let input_cost= form.getElementsByClassName("input1")[4];
	let btn_add= document.getElementById("add");
	let btn_submit= document.getElementById("input_btn");

	//Set all calculation variables

	let calc_name = document.getElementsByClassName("input2")[0];
	let calc_expense = document.getElementsByClassName("input2")[1];
	// let calc_date_from = document.getElementsByClassName("input2")[2];
	// let calc_date_to = document.getElementsByClassName("input2")[3];
	let btn_calculate= document.getElementById("calculate");

	
	//add event listeners
	
	btn_submit.addEventListener("click", newRow);
	btn_add.addEventListener("click", newInput);
	btn_out.addEventListener("click", logOut);
	btn_calculate.addEventListener("click", calculate);

	//function related: newInput - add button
	//adds a new name input with the same class and text as the original
	let remove = [];
	let name_array = [];
	console.log(name_array);
	function newInput(){	
		let names = form.getElementsByClassName("input1")[0];
		name_array.push(names.value);
		names.disabled = true;
		console.log(name_array);
		let new_input_name= document.createElement("input");
		new_input_name.classList.add("input1");
		form.insertBefore(new_input_name, form.childNodes[0]);
		form.getElementsByTagName("input")[0].setAttribute("placeholder", "Enter your name");
		form.getElementsByTagName("input")[0].setAttribute("type", "text");		
		remove.push("")
	}

	//function - submit button

	function newRow(){
		//setting values to an array to be pushed into the table later
		let input= [input_name.value, input_date.value, input_loc.value, input_type.value, input_cost.value];
		if(input[0]!="" && input[1]!="" && input[2]!="" && input[3]!="" && input[4]!=""){
			//creating a new row with 5 cells with the data from the input fields
			let new_row= document.createElement("tr");
			table.appendChild(new_row);
			let cell1= new_row.insertCell(0);
			let cell2= new_row.insertCell(1);
			let cell3= new_row.insertCell(2);
			let cell4= new_row.insertCell(3);
			let cell5= new_row.insertCell(4);
			let names = form.getElementsByClassName("input1")[0];
			name_array.push(names.value);
			cell1.innerText= name_array.toString();
			cell2.innerText= input[1];
			cell3.innerText= input[2];
			cell4.innerText= input[3];
			cell5.innerText= input[4];
			new_row.append(cell1, cell2, cell3, cell4, cell5);
			//resets the input fields
			form.reset();
			name_array = [];
			// remove delets extra name input fields created by the newInput function
			for (space in remove) {
				form.getElementsByClassName("input1")[0].remove();
			}		
			form.getElementsByClassName("input1")[0].disabled = false;
			remove = [];
		};
	}

	//function - calculate button

	function calculate() {
		let cost_array = [];
		let row = table.rows.length;
		let total_cost = 0;
		let n = 0
		//checks if inputs aren't empty before running code
		if (calc_name.value != "" || calc_expense.value != "" || calc_date_from.value != "" && calc_date_to.value != "") {
			for (i = 1; i < row; i++) {
				/* searches for both name value and expense type in each row of the table and then adds the 
				cost value to an array to be calculated later */
				if(calc_name.value != "" && calc_expense.value != "") {
					let in_table = table.rows[i].cells[0].innerText;
					let in_table2 = table.rows[i].cells[3].innerText;
					if(in_table.search(calc_name.value) != -1 && in_table2.search(calc_expense.value) != -1) {
						n += Number(table.rows[i].cells[4].innerText);	
					}
				}
				/* searches for expense type in each row of the table and then adds the 
				cost value to an array to be calculated later */
				else if(calc_expense.value != "") {
					let in_table = table.rows[i].cells[3].innerText;
					if(in_table.search(calc_expense.value) != -1) {
						n += Number(table.rows[i].cells[4].innerText);	
					}
				}
				/* searches for name value in each row of the table and then adds the 
				cost value to an array to be calculated later */
				else if(calc_name.value != "") {
					let in_table = table.rows[i].cells[0].innerText;
					if(in_table.search(calc_name.value) != -1) {
						n += Number(table.rows[i].cells[4].innerText);
					}
				}
			}
			alert(n);
			calc_name.value = ""
			calc_expense.value = ""
		}
		// if all inputs are empty
		else {
			alert("Please insert something into one of the input fields.");
		}
	}
		
	function logOut(){
		location.href = "hackathon1.html";
	}
