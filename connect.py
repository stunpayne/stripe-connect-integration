import stripe as stripe

# Stripe API Key
stripe.api_key = "sk_test_51IbrsAGblf4VnYbVgjsB4yh4uQ8cJMSNr0RDGDNXinjfcRvzYMtBKF7dC79grURWOai6lFId1Mtz3fwMDDUC0r9n00j7cExQ4a"

account = stripe.Account.create(
  type='express',
)

print(f"Account ID: {account.id}")


# Create Account Link
account_links = stripe.AccountLink.create(
  account=account.id,
  refresh_url='https://example.com/reauth',
  return_url='https://example.com/return',
  type='account_onboarding',
)

print(f"Account Link: {account_links}")