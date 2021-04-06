// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/account/apikeys
var stripe = Stripe('pk_test_51IbrsAGblf4VnYbVNQcMMcWGHpTSO92Ah5hqULHUKK5zdr8usGBzh12Obdj6xeQ42g33FTC2Vy45J8KgBALjeEPE00qKhpXHRo');
var elements = stripe.elements();



window.addEventListener("load", function() {
    // Set up Stripe.js and Elements to use in checkout form
    var elements = stripe.elements();
    var style = {
        base: {
            color: "#32325d",
        }
    };

    var card = elements.create("card", {
        style: style
    });
    card.mount("#card-element");

    card.on('change', function(event) {
        var displayError = document.getElementById('card-errors');
        if (event.error) {
            displayError.textContent = event.error.message;
        } else {
            displayError.textContent = '';
        }
    });

    var form = document.getElementById('payment-form');

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        console.log("Clicked");

        fetch("/secret", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                stripe.confirmCardPayment(data.client_secret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: 'Jenny Rosen'
                        }
                    }
                }).then(function(result) {
                    console.log(result)
                    if (result.error) {
                        // Show error to your customer (e.g., insufficient funds)
                        console.log(result.error.message);
                        alert(result.error.message)
                    } else {
                        // The payment has been processed!
                        if (result.paymentIntent.status === 'succeeded') {
                            alert("Payment Success!");
                            var transfer = document.getElementById("transfer-form");
                            transfer.style.display = "block";
                        }
                    }
                });
            });

    });


    var transferForm = document.getElementById('transfer-form');

    transferForm.addEventListener('submit', function(ev) {
        ev.preventDefault();
        console.log("Transfer Clicked");


        fetch("/transfer", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(result => {
                console.log(result);
                if (result.transfer_id) {
                    // Show error to your customer (e.g., insufficient funds)
                    console.log("Transfer success!");
                    alert("Transfer Success!")
                } else {
                    alert("Transfer Failed!")
                }
            });

    });



});