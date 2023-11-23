$().ready(function() {
	$("#papervalidate").validate({
		rules : {
			paperType :{
				required : true,
			},	
			

		},
		messages : {
			paperType : {
				required : "Please Enter a papertype",
				
			},
			
		}
	});

	
})