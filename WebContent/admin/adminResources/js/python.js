function runPython() {
    var inputVal = document.getElementById("myInput").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/updatedsenti.py");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Handle the response from the Python file
            var output = xhr.responseText;
            // Update the HTML page with the output
            document.getElementById("output").innerHTML = output;
        }
    };
    xhr.send(JSON.stringify({input: inputVal}));
}