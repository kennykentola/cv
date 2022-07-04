var objpeople =[{
	username:"san",
	password:"password25"
},
{
	username:"matt",
	password:"password88",
},
{
	username:"chris",
	password:"password3"
}]

function myFunction(){
		
		var username = document.getElementById("username").value
		var password =document.getElementById("password").value

		for (var i = 0; i < objpeople.length; i++) {
			if (username==objpeople[i].username && password==objpeople[i].password){
			

				console.log(username + " is logged in !!!")
				return
			}
				//beginning of welcome page
		var un= document.forms["myForm"]["uname"].value;
		var pw =document.forms["myForm"]["pass"].value;
		if(un=="objpeople" && pw=="objpeople"){
			window.location.href="welcome.html";
		}
		else{
			alert("invalid userName and password");
			return
		}
		//end of welcome page
		}
	
		
		//erro if username and password do not match
		console.log("incorrect username or password")
	}

	function registerUser(){
		var registerUser = document.getElementById("newUser").value
		var registerPassword =document.getElementById("newPassword").value
		var newUser ={
			username:registerUser,
			password:registerPassword
		}
		for ( i = 0; i < objpeople.length; i++) {
			if (registerUser ==objpeople[i].username){
				alert("that username is already in use,please choose another")
				return}else if(registerPassword.length<8){
					alert("that password is too short, include 8 or more characters")
					return
				}
		}
		objpeople.push(newUser)
		console.log(objpeople)
	}
