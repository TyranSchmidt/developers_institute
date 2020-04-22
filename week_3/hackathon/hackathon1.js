let form_up = document.getElementsByTagName("form")[0];
let input_up_name = form_up.children[2];
let input_up_email = form_up.children[3];
let input_up_password = form_up.children[4];
let input_up_btn = form_up.children[5];

let form_in = document.getElementsByTagName("form")[1];
let input_in_name = form_in.children[2];
let input_in_password = form_in.children[3];
let input_in_btn = form_in.children[4];

let name_value;
let email_value;
let password_value;

input_up_btn.addEventListener("click", sign_up);
function sign_up() {
	if(input_up_name.value != "" && input_up_email.value != "" && input_up_password.value != "") {
		name_value = input_up_name.value;
		email_value = input_up_email.value;
		password_value = input_up_password.value;
		input_up_name.value = "";
		input_up_email.value = "";
		input_up_password.value = "";
	} else {
		alert("Please fill out all the required fields.")
	}
};

input_in_btn.addEventListener("click", sign_in);
function sign_in(){
	if(name_value == input_in_name.value && password_value == input_in_password.value){
		location.href = "hackathon1p2.html";
	}
	else{
		alert("Please enter valid details");
		input_in_name.value = "";
		input_in_password.value = "";

	};

};
