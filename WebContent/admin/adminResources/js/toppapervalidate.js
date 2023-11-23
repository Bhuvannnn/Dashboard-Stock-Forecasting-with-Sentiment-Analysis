$().ready(function() {
	$("#toppapervalidate").validate({
		rules : {
			topPaperBundleNumber: {
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
			topPaperBundleNumber : {
				required : "Please Enter a Top Paper Bundle Number",
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