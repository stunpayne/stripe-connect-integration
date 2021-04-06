
window.addEventListener("load", function(){

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
			document.getElementById("account-status").innerHTML = "Account Details Submitted Check: True";
		}
		else	{
			document.getElementById("account-status").innerHTML = "All account details not submitted";
		}
	});
});



