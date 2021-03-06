#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""

import json
import os
import time

import stripe
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify, render_template, redirect, request, session, send_from_directory
from flask_cors import CORS

# Setup Stripe python client library
load_dotenv(find_dotenv())
stripe.api_key = os.getenv('STRIPE_SECRET_KEY', "sk_test_51IbrsAGblf4VnYbVgjsB4yh4uQ8cJMSNr0RDGDNXinjfcRvzYMtBKF7dC79grURWOai6lFId1Mtz3fwMDDUC0r9n00j7cExQ4a")
stripe.api_version = os.getenv('STRIPE_API_VERSION', '2019-12-03')

print(__file__, os.getenv("STATIC_DIR"))
static_dir = str(os.path.abspath(os.path.join(__file__ , "..", os.getenv("STATIC_DIR", "."))))
print(static_dir)
app = Flask(__name__, static_folder=static_dir,
            static_url_path="", template_folder=static_dir)
CORS(app)

# Set the secret key to some random bytes. Keep this really secret!
# This enables Flask sessions.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Testing Host
ORIGIN_LOCAL = "http://localhost:4242"

# Account ID of the created connected account. I'm using Flask for the first time and was facing issues
# with persisting the account ID as a session variable so I resorted to storing it as a local variable
# for testing purposes.
account_id = None
transfer_group_id = None

@app.route('/', methods=['GET'])
def get_example():
    return render_template('index.html')


@app.route('/onboard-user', methods=['POST'])
def onboard_user():
    account = stripe.Account.create(type='express')

    # Store the account ID.
    global account_id
    account_id = account.id

    print("Account ID", account.id)
    print("Global Account ID", account_id)

    account_link_url = _generate_account_link(account_id, ORIGIN_LOCAL)
    try:
        return jsonify({'url': account_link_url})
    except Exception as e:
        return jsonify(error=str(e)), 403


@app.route('/onboard-user/refresh', methods=['GET'])
def onboard_user_refresh():
    if 'account_id' not in session:
        return redirect('/')

    account_link_url = _generate_account_link(account_id, ORIGIN_LOCAL)
    return redirect(account_link_url)


@app.route('/update-account-status', methods=['POST'])
def update_account_status():
    print("Session Account ID", account_id)

    account = stripe.Account.retrieve(account_id)

    try:
        return jsonify({'account_id': account_id, 'details_submitted': account.details_submitted})
    except Exception as e:
        return jsonify(error=str(e)), 403


@app.route('/secret')
def secret():
    global transfer_group_id
    transfer_group_id = "ORDER" + str(int(time.time()))
    print(transfer_group_id)
    payment_intent = stripe.PaymentIntent.create(
        payment_method_types=['card'],
        amount=1000,
        currency='usd',
        transfer_group={transfer_group_id}
    )

    return jsonify(client_secret=payment_intent.client_secret)


@app.route('/transfer', methods=['POST'])
def transfer():
    print(account_id, transfer_group_id)
    # Create a Transfer to a connected account (later):
    transfer = stripe.Transfer.create(
      amount=150,
      currency='usd',
      destination=account_id,
      transfer_group=transfer_group_id,
    )

    return jsonify(transfer_id=transfer.id)


def _generate_account_link(account_id, origin):
    account_link = stripe.AccountLink.create(
        type='account_onboarding',
        account=account_id,
        refresh_url=f'{origin}/onboard-user/refresh',
        return_url=f'{origin}/success.html',
    )
    return account_link.url


if __name__== '__main__':
    app.run(port=4242)





