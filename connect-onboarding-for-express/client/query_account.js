function codeAddress() {
    fetch("http://localhost:4242/update-account-status", {
		method: "POST",
		headers: {
		  "Content-Type": "application/json"
		}
	})
	.then(response => response.json())
	.then(data => {
		console.log(data)
		if (data.details_submitted)	{
			document.getElementById("account-status").innerHTML = "Account Details Submitted: True";
		}
		else	{
			document.getElementById("account-status").innerHTML = "Account all details not submitted";
		}
	});
}

window.onload = codeAddress;