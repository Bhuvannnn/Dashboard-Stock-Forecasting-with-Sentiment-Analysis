$().ready(function() {
	$("#reelvalidate").validate({
		rules : {
			reelNumber : {
				required : true,
			},
			weight : {
				required : true,
			},
			gsm : {
				required : true,
			},
			bf : {
				required : true,
			},
			decal : {
				required : true,
			},
		},
		messages : {
			reelNumber : {
				required : "Please Enter a Reel Number",
			},
			weight : {
				required : "Please Enter a Reel Number",
			},
			gsm : {
				required : "Please Enter a Reel Number",
			},
			bf : {
				required : "Please Enter a Reel Number",
			},
			decal : {
				required : "Please Enter a Reel Number",
			},

		}
	});

})