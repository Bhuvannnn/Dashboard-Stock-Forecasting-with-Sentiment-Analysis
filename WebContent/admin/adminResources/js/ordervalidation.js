function getItemsByClient() {

	var clientname = document.getElementById("clientname");
	var clientItems = document.getElementById("clientItems");

	var htp = new XMLHttpRequest();

	htp.onreadystatechange = function() {

		if (htp.readyState == 4) {

			var jsn = JSON.parse(htp.responseText);

			if (jsn.length > 0) {

				clientItems.innerHTML = "";

				var opn = document.createElement("option");

				opn.text = "Select";
				clientItems.options.add(opn);

				for (var index = 0; index < jsn.length; index++) {

					var opn = document.createElement("option");

					opn.value = jsn[index].clientreqId
					opn.text = jsn[index].clientItems

					clientItems.options.add(opn);

				}

			}

		}
	}

	htp.open("get", "getItemsByClient?clientId=" + clientname.value, true);
	htp.send();
}

function getItemsDetailsByClientItem() {

	var clientItems = document.getElementById("clientItems");

	var htp = new XMLHttpRequest();

	htp.onreadystatechange = function() {

		if (htp.readyState == 4) {

			var jsn = JSON.parse(htp.responseText);

			if (jsn.length > 0) {

				var data = jsn[0];

				$('#length').val(data.length);
				$('#width').val(data.width);
				$('#height').val(data.height);
			}
		}
	}

	htp.open("get", "getItemsDetailsByClientItem?clientItem="
			+ clientItems.value, true);
	htp.send();

}
