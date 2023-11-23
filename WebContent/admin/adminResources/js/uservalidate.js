$().ready(function(){
	 	$("#uservalidate").validate({
	 		rules:{
	 			firstName:{
	 				required:true,
	 				alphabet:true,
	 			},
	 			lastName:"required",
	 			userName:{
	 				required: true,
	 				minlength: 2
	 			},
	 			
	 			mobileNumber:{
	 				required:true,
	 				number:true,
	 				minlength:8,
	 				maxlength:10,
	 			},
	 			password:{
	 				required:true,
	 				minlength:5,
	 			},
	 			
	 		},
	 		messages:{
	 			firstName:{
	 				required:"Please Enter FirstName",
	 				alphabet:"Please enter alphabets only"
	 			},
	 			lastName:"Please Enter LastName",
	 			userName:{
	 				requried:"Please enter username",
	 				minlength:"Must be of at least 2 characters",
	 			},
	 			mobilenumber:{
	 				required:"Please enter the mobile number",
	 				number:"Just enter number",
	 				minlength:"Please Enter a valid number",
	 				maxlength:"Please Enter a valid number",
	 			},
	 			password:{
	 				required:"Please enter a password",
	 				minlength:"Password must be of 5 characters"
	 			},
	 			
	 		}
	 	});
	 	
	 	$("#userName").focus(function(){
	 		var firstName = $("#firstName").val();
	 		var lastName  = $("#lastName").val();
	 		if(firstName && lastName && !this.value){
	 			this.value = firstName + "." + lastName;
	 		}
	 	})
}
)



function validateUser(){
	
		var firstName = $("#firstName").val();
 		var lastName  = $("#lastName").val();

 		console.log(firstName);
 		console.log(lastName);
	
 		return false;
}







