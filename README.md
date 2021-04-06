# stripe-connect-integration
Notes on a sample Stripe Connect integration

# Executive Summary
<ins>User Persona:</ins>  
I am assuming the persona of a startup's technical co-founder, one who can code, looking to integrate with a payment gateway for processing transactions on his platform app.


<ins>Top user needs from a payment processor:</ins>  
- Accepting payments from customers
- Transferring funds to businesses within defined SLAs with reliability
- Quick & easy integration
- Easy generation of invoices for customers
- Dashboard for sellers to debit funds to my platform
- Periodic reporting of sales and customer acquisition performance
- Security & Compliance out of the box


<ins>Flows I tried:</ins>  
- Create and link connected account
- Accept payment from customer
- Transfer funds to connected account during charge
- Transfer funds to connected account later (Separate charges and transfers)
- Send invoice from dashboard
- Top up from bank account to Stripe balance
- Generate reports



<ins>Connect Flows I didn't try:</ins>  
- Disputes, Reviews
- Refunds



<ins>What worked well:</ins>  
1. Most of the <ins>integration was smooth and easy</ins>. Anyone who knows how to code will easily understand the APIs and get onboarded quickly.
2. Examples of firms using various APIs helps the user <ins>find the right product and documentation</ins> and gain confidence in the system
3. Documentation is comprehensive and <ins>builds confidence in Stripe's capabilities</ins>
4. Documentation helps to understand not only Stripe APIs but also payment flows generally and also <ins>acts as a tutorial on building a seamless payment customer experience</ins>
5. Code samples were fairly <ins>copy-pastable</ins> and immensely helpful


<ins>Improvements: </ins>  
1. Stripe CLI-generated code doesn't work out of the box leading to frustration in integration  
    * Solution: The code can be simplified to require less setup (such as env variables) from the developer. Regular testing of the sample codes with external developers (and by the Stripe Connect PM and dev teams) will improve reliability of the code. The goal should be to have the code functioning out of the box in 100% of cases.
2. Incorrect dates at multiple places make the user question whether Stripe's reports will be accurate  
    * Solution: Correct all dates facing the user. Add automation testing for front end to ensure long-term reliability.
3. Platforms shouldn't have to switch to manual payouts to add funds for transfers
    * Solution: Although I would like to investigate this further, my current hypothesis is that allowing platforms to add funds even on an automated payout schedule should not be an issue.
4. Payout schedule only has periodic (daily/weekly/monthly) options which could lead to high transaction costs for Stripe  
    * Solution: An option to trigger payouts when the balance reaches a threshold amount (and nudging users to adopt this option) will reduce transaction costs for Stripe
5. 'Payout' term used for multiple operations (move funds to own bank, transfer to sellers) leading to confusion - even the document heading says "Collect payments then pay out"  
    * Solution: Since 'Transfers' is the API for moving funds to sellers, ensure that this is the term used for this action throughout the documentation.
6. Some terms (destination charges, Express accounts) are left unexplained leading to unanswered questions for the user  
    * Solution: Add one-line explanations with hyperlinks to detailed documentation wherever possible (as shown in the [improvement for Express accounts](#create-express-account-and-prefill-information))


# Friction Log

### Table of Contents
- [Platform Introduction](#platform-introduction)
- [Sign Up and Dashboard](#sign-up-and-dashboard)
  - [Website Landing](#website-landing)
  - [Signing up](#signing-up)
  - [Exploring dashboard](#exploring-dashboard)
- [Integration](#integration)
  - [Prerequisites](#prereqs)
  - [Set up Stripe](#set-up-stripe)
  - [Create a connected account](#create-a-connected-account)
  - [Accept a payment](#accept-a-payment)
    - [Delayed transfers](#delayed-transfers)
- [Generate Reports](#generate-reports)
- [Top up Stripe balance](#top-up-from-bank-account-to-stripe-balance)
- [Invoicing](#invoicing)


## Platform Introduction
As the startup's technical co-founder, I'm building an app for an online shopping marketplace which connects artisans building customized home decor with local consumers. Consumers will make payments to my platform app for items they wish to purchase. My app will take a fee and relay the remaining payment to the artisan, after they've delivered the order.

I've heard great things about Stripe so I log on to the website(https://stripe.com/) to check it out.


## Sign Up and Dashboard

### Website Landing
What I did:  
Open stripe.com

What went well:  
- My initial thoughts are highly positive. Encouraging one-liner on Stripe - "*..startups..use Stripe.. to accept payments, send payouts, and manage their businesses online*"
- "Start now" button provides a good place to start - I already know I have to come back to this
- Scrolling down and seeing the logos of Instacart and Shopify provides me further confidence that Stripe would work for me.

### Signing up
What I did:  
I click on 'Start Now' and land on the Sign Up page. 

What went well:  
Seeing 'marketplaces' under "Support any business model" reaffirms my faith that Stripe will work.

<img width="484" alt="Screen Shot 2021-04-02 at 1 36 41 PM" src="https://user-images.githubusercontent.com/13269259/113443907-76b87e00-93b8-11eb-8748-918c4debd510.png">

The Sign Up is simple and easy. It makes sense that email, password, full name and country were asked - nothing out of the blue.


Can be improved:  
I've received an email to verify my email on Stripe. 
On the dashboard that appears after login, I wonder why verifying the email is the fourth step instead of the first.

<img width="904" alt="Screen Shot 2021-04-02 at 1 44 06 PM" src="https://user-images.githubusercontent.com/13269259/113444425-808eb100-93b9-11eb-9086-884408cbe70b.png">

As a user, I understand that this is to reduce friction but it makes me question what the impact of delaying the verification would be. Having an explanation about that - such as "You can go ahead and get started with your Stripe Integration but would need to verify your email before going live. This is needed so that we know it's really you and can send you important information." -  would help.

<ins>Change business name</ins>  
What I did:
Saw "New Business" name on my account and tried to change it

What went well:  
Seeing the "Edit" option right there with a simple way to change my name feels great! Also, writing a generic name like that is a good way to nudge users to actually edit that info - it employs the basic necessity of humans to fix low hanging fruits they spot.

<img width="198" alt="Screen Shot 2021-04-02 at 1 49 58 PM" src="https://user-images.githubusercontent.com/13269259/113444868-52f63780-93ba-11eb-8a1a-0e82091f2c80.png">

I apply my right-brain skills, choose the name "ArtIsOn" as a pun on "artisan", feel good about myself and move on :)

### Exploring dashboard
<ins>Scanning the Home Page</ins>  
The 'Today' and 'Reports overview' sections pique my curiosity and I scroll down to have a look.
All the dashboards seem self-explanatory from their titles and one-line descriptions. These charts give me the impression that the dashboard will maintain and present data related to my business upfront and the Home Page will be particularly useful for snapshot info.

I try to edit the charts using the 'Edit charts' button but that doesn't work, understandably, because there is no data yet. However, I wonder why I still cannot see what different charts I can create - that should be possible in the absence of data. Here's what I propose for this:
- In case there is reason to disallow the user from editing charts in the absence of data (such as dummy charts need to be designed manually OR front end chart code logic breaks if there is no data), an error message should be shown on hovering above the 'Edit Charts' button such as "Start your integration to generate data and edit charts"
- In case there is no reason to disallow the user from doing so, the 'Edit Charts' button should be enabled.

<img width="245" alt="Screen Shot 2021-04-02 at 2 14 22 PM" src="https://user-images.githubusercontent.com/13269259/113446613-ba61b680-93bd-11eb-85eb-31b0ac586967.png">


<ins>Scanning menus</ins>  
What I did:
Quickly have a look at the other menu options before I start my integration.

What went well:  
- Everything seems quite self-explanatory. Descriptions provided for each section seem to be helpful.

- I like seeing 'Read more about reporting and when your data becomes available.' in the Reports section. This is what I was looking for when scanning the home page above.

<img width="1018" alt="Screen Shot 2021-04-02 at 2 06 30 PM" src="https://user-images.githubusercontent.com/13269259/113446058-a23d6780-93bc-11eb-98ab-d74afbf497a2.png">


Can be improved:  
- I notice a small bug in the order of the dates mentioned on the 'Financial reports' page. Instead of `Apr2-Mar31`, it should be `Mar31-Apr2` assuming that the last two days are what is being talked about here (unless this shows the previous year's data, in which case Apr 2 doesn't make sense as a starting point).


## Integration
What I did:  
Having explored the menu options, I begin my integration. I go to the Home Page and click on 'Explore Docs'

<img width="886" alt="Screen Shot 2021-04-02 at 2 20 24 PM" src="https://user-images.githubusercontent.com/13269259/113446972-92bf1e00-93be-11eb-8cfd-85cee48ed12a.png">

What went well:  
- Easy to spot "Multiparty payments" at the bottom
- Platform, Marketplace, Two-sided business -> all helpful keywords for the target customer to find the right product. From the list of integration options below it, it was quite clear that "Collect payments then pay out" was the right approach for me to take. Although my sellers would be shipping to users on their own, I would issue payments to them only once the delivery has been initiated.
- The subtitle restates my use case and reaffirms that I am on the right page  
<img width="796" alt="Screen Shot 2021-04-02 at 6 31 45 PM" src="https://user-images.githubusercontent.com/13269259/113461322-af208200-93e1-11eb-8191-6dc14f362a69.png">

Can be improved:  
- The homeowner example on this page makes the use case being served quite clear. To make the example even clearer and reduce user read time, a simple flow diagram can be built. The connect flow can be described as -  
    User                ->                      Platform               ->                 Seller  
(Makes payment)         (Accepts payments from User, pays out to Seller)     (Receives payout from Platform)  

The example can then be described as -  
    Tenants                ->                   Kavholm               ->                 Homeowners  
(Makes payment)         (Accepts payments from Tenants, pays out to Homeowner)     (Receives payout from Kavholm)  

This would reduce the setup time for the user, help them visualize the flow and enable them to get into the tutorial more quickly.

### Prereqs

<img width="844" alt="Screen Shot 2021-04-02 at 6 45 39 PM" src="https://user-images.githubusercontent.com/13269259/113461767-a16bfc00-93e3-11eb-83cb-55995349b1bc.png">

Prereq #1 - Register your platform
What I did:  
Upon clicking the link for this, I was taken to this page.
<img width="1391" alt="Screen Shot 2021-04-02 at 6 46 03 PM" src="https://user-images.githubusercontent.com/13269259/113461784-ae88eb00-93e3-11eb-922c-63f01b93e87a.png">

Can be improved:  
- The major issue with this page is that there was no clear call to action. Coloring the 'Get Started' and 'Find a Partner' buttons differently might make the call more explicit.

- I selected Platform or Marketplace and went ahead. Upon doing that, I was taken to the home page where I was shown this:
<img width="1370" alt="Screen Shot 2021-04-02 at 6 50 00 PM" src="https://user-images.githubusercontent.com/13269259/113461916-3c64d600-93e4-11eb-8656-a29cecdd98b0.png">
This is very relevant information and should have been shown earlier. I would have known exactly which Stripe product to use (Connect) and where to start. This will eliminate the step of finding the right documentation on my own. Additionally, it will reduce one pre-requisite in the documentation which will give the user the impression of reduced setup work.


Prereq #2 - Activate your account
What went well:  
This flow was smooth overall. I particularly liked the explanatory messages for some fields that showed up on the side. These messages appeared for exactly the fields that are less common knowledge.
<img width="739" alt="Screen Shot 2021-04-02 at 6 57 49 PM" src="https://user-images.githubusercontent.com/13269259/113462195-54892500-93e5-11eb-8de3-87243b592abd.png">

Can be improved:  
After completing Step 2, the message on the home page was back to the default "Explore docs" one, leading to an inconsistent experience. As a user, I would expect to see the Connect docs link everytime once I've registered my platform.

<img width="879" alt="Screen Shot 2021-04-02 at 7 02 32 PM" src="https://user-images.githubusercontent.com/13269259/113462337-fd378480-93e5-11eb-86da-e27355b44825.png">


Prereq #3 - Fill out your platform profile
What went well:  
At the end of the platform profile, I was shown recommendations for the documentation I can follow for my integration.

<img width="754" alt="Screen Shot 2021-04-02 at 7 16 26 PM" src="https://user-images.githubusercontent.com/13269259/113462724-ee51d180-93e7-11eb-86ea-4f5c50c5fe32.png">

Can be improved:  
- Upon clicking the link to this prereq on the docs page, I was taken to the home page again with a link to complete the profile. Instead, since the action I was going to take was already known, I should have been taken right to the prereq step.

<img width="1379" alt="Screen Shot 2021-04-02 at 7 07 09 PM" src="https://user-images.githubusercontent.com/13269259/113462464-a0889980-93e6-11eb-8235-e0c5c0fdcae6.png">

- The section below this was extremely helpful. It shows the user key APIs to integrate with to solve their use case so they know early on which flows/docs to explore.

<img width="1370" alt="Screen Shot 2021-04-02 at 7 20 37 PM" src="https://user-images.githubusercontent.com/13269259/113462833-8354ca80-93e8-11eb-8244-81dbf4d40a25.png">


- After having gone through a page listing all docs, finding the right one and completing the prereqs, I am shown the links to the docs that Stripe believes is right for me. This experience reaffirms my earlier point that these steps should have come earlier. Telling the user that these steps will help them find the right integration and documentation would more easily convince them to complete these forms. Since there is the cost of asking the user to complete several steps before reaching the documentation, increasing onboarding friction, the user can be provided a choice between exploring docs and letting us find them the right one.


Prereq #3 - Brand settings
Went well:
- Allowing the merchant to customize how the onboarding page looks is good for user experience. It provides the platform's users the feeling that they're still within the context of the platform even though they've been redirected to a Stripe page for onboarding, enhancing the user's trust in the flow. Moreover, merchants would love to customize the experience at every step to have greater control of the overall user experience.

<img width="1009" alt="Screen Shot 2021-04-03 at 5 19 13 PM" src="https://user-images.githubusercontent.com/13269259/113492902-b78bc200-94a0-11eb-82e9-f5444863694e.png">


To be improved:
- The prereq bullet says "Customize your brand settings on the Connect settings page. This information is required for Connect Onboarding". As a user, I can't put my finger on what 'Connect Onboarding' means. Are we talking about onboarding me as a business onto Connect? Or about onboarding sellers onto my platform?  
Solution: Mention clearly that this action will customize the page that sellers/vendors see while signing up on the business platform.

- Upon clicking the link, I am taken to the Connect Settings page but not directly to the section of the prereq. In order to verify the action to take here, I need to go back to the documentation page and re-read "Customize your brand settings.." and scroll down to look at all the headings on the Connect Settings page to learn that 'Branding' is the section I need to head to.  

- The 'Save branding changes' button is well named as it preserves the context of the prerequisite. However, upon clicking it, a loader appears to show that saving is in progress but when the save is completed, the loader disappears and the button becomes unclickable. This leaves the user wondering whether the save was successfully completed so a temporary tick mark might be more satisfactory from a UX perspective.

<img width="197" alt="Screen Shot 2021-04-03 at 5 23 20 PM" src="https://user-images.githubusercontent.com/13269259/113492992-4b5d8e00-94a1-11eb-9d21-39238db2637e.png">

<img width="206" alt="Screen Shot 2021-04-03 at 5 27 17 PM" src="https://user-images.githubusercontent.com/13269259/113493052-d8a0e280-94a1-11eb-8153-6fa0c7819604.png">


_*Programming language chosen: Python 3*_

### Set up Stripe
Went well:
- This step is simple and self-explanatory. 
- Throughout the documentation, the presence of code samples in multiple languages is helpful to a wide range of developers and gives the impression of a very mature API base.

To be improved:
- The prevalent version of Python now is Python3. Anyone starting a new codebase in Python would probably use Python3. The documentation should hence be updated to include `pip3` along with `pip` for Python3 users as shown below.
 
Current:  
<img width="842" alt="Screen Shot 2021-04-03 at 5 43 06 PM" src="https://user-images.githubusercontent.com/13269259/113493342-0dae3480-94a4-11eb-9ef2-8b30a9745779.png">

Suggested:  
<img width="842" alt="Screen Shot 2021-04-03 at 5 45 44  PM" src="https://user-images.githubusercontent.com/13269259/113493385-6c73ae00-94a4-11eb-8042-cf53c885ffde.png">


### Create a connected account

#### Introduction paragraph
Went well:
- The explanation of a connected account is superb. It specifies whom the account is for, what it will be used for and links it to the home-rental example to ensure no doubts are left.

<img width="864" alt="Screen Shot 2021-04-03 at 6 42 57 PM" src="https://user-images.githubusercontent.com/13269259/113494271-6a155200-94ac-11eb-8458-3d4cbd04a3b5.png">

#### What you're building
Went well:  
The "What you're building" view is helpful as it allows the user to begin with the goal in mind.

<img width="841" alt="Screen Shot 2021-04-03 at 6 46 09 PM" src="https://user-images.githubusercontent.com/13269259/113494318-dd1ec880-94ac-11eb-8666-b58829d42fc4.png">

- The "Clone with CLI" option mentions that the user's Stripe API key will be used in configuring the button. This is helpful for the user as it avoids additional effort from their end.
 
<img width="837" alt="Screen Shot 2021-04-03 at 6 50 12 PM" src="https://user-images.githubusercontent.com/13269259/113494394-6e8e3a80-94ad-11eb-965a-f7ff3b192925.png">


To be improved:  
- The button, however, opens the link on the same page, moving the reader away from the documentation. It should, instead, open on a different page so that the user can close that window and easily come back to the documentation.


#### Create express account and prefill information
Went well:
- The code snippet shows that my test key will be used, signaling to me that all the code in the page can be directly copied - a great experience!

<img width="844" alt="Screen Shot 2021-04-03 at 7 02 04 PM" src="https://user-images.githubusercontent.com/13269259/113494577-15bfa180-94af-11eb-8c03-1148542e6e66.png">

To be improved:
- The moment I read I have to create an 'Express account', I started questioning what that meant. Since there was no explanation here, I resorted to checking out the [Accounts API Page](https://stripe.com/docs/api/accounts). From there, I followed a link to "[create and manage Express or Custom accounts](https://stripe.com/docs/connect/accounts)" that explained the difference in a table.

<img width="621" alt="Screen Shot 2021-04-03 at 7 10 49 PM" src="https://user-images.githubusercontent.com/13269259/113494699-4f44dc80-94b0-11eb-8935-22228f1c78d4.png">

&nbsp;&nbsp;I think it is natural for one to question the difference between account types. In order to assuage these concerns, it might be helpful to provide a short description of the accounts as shown below.
<img width="856" alt="Screen Shot 2021-04-03 at 7 14 20 PM" src="https://user-images.githubusercontent.com/13269259/113494729-cda17e80-94b0-11eb-8372-bca56c12488f.png">

#### Create an account link
To be improved:  
- The value of the 'account' parameter is shown in the code sample but not explained in the description above it. A sample account ID is mentioned. Due to this, the user would have to check which parameter in the Account API response corresponds to the given value. A simple explanation as below might help the dev get the answer more quickly.

<img width="748" alt="Screen Shot 2021-04-03 at 7 49 35 PM" src="https://user-images.githubusercontent.com/13269259/113495229-b9ac4b80-94b5-11eb-8d10-e34c0fec5b6e.png">

The sample code can then be changed accordingly.
<img width="742" alt="Screen Shot 2021-04-03 at 7 50 57 PM" src="https://user-images.githubusercontent.com/13269259/113495264-e9f3ea00-94b5-11eb-8c69-3772cf8eeda0.png">

#### Redirect your user to the account link URL
Went well:
- A lot of key points were mentioned in this step
  - Remember to authenticate users before redirecting
  - Redirect link contains personal information so can be used only once
  - Don't email/text the link, only redirect
  - Account becomes immutable after link generation

These points will be very helpful for any user to keep in mind.

#### Handle the user returning to your platform 

Went well:
- Including both `return_url` and `refresh_url` is a good choice. As I've learnt from experience building payment platforms, it helps merchants to have different pages to handle different scenarios and power a variety of experiences.
- The cases in which both the URLs are to be used are well laid out.
- This comment is particularly helpful in closing the loop of actions to take in every scenario for the user. 

<img width="801" alt="Screen Shot 2021-04-03 at 8 17 21 PM" src="https://user-images.githubusercontent.com/13269259/113495820-9be0e580-94b9-11eb-8c94-7413ac03c50a.png">


To be improved:  
- There should be a link on the `account.updated` webhooks bullet just as there is one on the Accounts API one

<img width="523" alt="Screen Shot 2021-04-03 at 8 16 47 PM" src="https://user-images.githubusercontent.com/13269259/113495809-853a8e80-94b9-11eb-9f01-503add970735.png">



#### Handle users that haven’t completed onboarding 

Went well:
- The action to take in the cases wherein a user coming to the `return_url` might not have been onboarded completely was unanswered and lingering at the back of my mind until this point. The explanation in this section answers this question directly and completely.

To be improved:
- One strength of Stripe's docs is that almost every heading is hyperlinked. This can be used to hyperlink API parameters such as `charges_enabled` in the below paragraph to [this link](https://stripe.com/docs/api/accounts/object#account_object-charges_enabled). This will provide the user an easy way to understand the meanings and usage of API parameters, especially in cases like this where the meaning of 'charges' may not be self explanatory.

<img width="841" alt="Screen Shot 2021-04-03 at 8 29 45 PM" src="https://user-images.githubusercontent.com/13269259/113496047-558c8600-94bb-11eb-9adb-e5fa0ef975f2.png">


#### Account link redirection URL
Went well:
- Test accounts and phone numbers in the flow were very helpful to make the process easier.

To be improved:
- The redirection from the account link to the `return_url` is a GET call which means that no information about the account is passed to the platform application. Since the next step for platforms would be to call the Accounts API, the account ID needs to be known. In practice this means that platforms will have to store the account ID from the first call before the redirection Hence, the account ID needs to be passed to the `return_url` 


Step 2 Went Well:
- Overall, the order of the steps 2.1-5 makes sense and just going through them explains what needs to be done to the user. I came out of this step with almost no questions about the actions to take in different scenarios and understood very well what I am supposed to do.


Step 2 To be improved:
- From a user's perspective, making two API calls to get an account link for redirection seems redundant. Although it makes sense from Stripe's perspective to separate the resources for Accounts and AccountLinks, as a user, I see no additional benefit of separating the API calls as there is no additional step from my end between them. 

  As can be seen from the sample server code generated by Stripe, the only thing in between the API calls is storing the account ID in the session, which can be done after the single combined API call as well, before redirection.

<img width="469" alt="Screen Shot 2021-04-04 at 11 27 25 AM" src="https://user-images.githubusercontent.com/13269259/113515216-bd34e680-9538-11eb-84a2-155b95c8a5b7.png">

The user can be informed in the documentation though that Accounts and AccountLinks are maintained as separate resources and individual APIs exist for them too.


### Accept a payment

What went well:  
- The sequence diagram clearly lays out the entire flow and makes it easy to understand how payment works.
- Code snippets provide minimal working code required for integration
- Code worked exactly as doc mentioned. Since accepting payment was the major step, this increases confidence in Stripe docs
- `client_secret` is a well named term - better than the other term I've generally heard around ('payment_token')
- Stripe CLI generates modular code, providing options for language, inclusion of webhooks etc., allowing the user to generate samples as per their integration needs and reducing effort on their end  
<img width="693" alt="Screen Shot 2021-04-04 at 11 54 59 AM" src="https://user-images.githubusercontent.com/13269259/113515854-95e01880-953c-11eb-8f19-00bfce6c7a6d.png">


Can be improved:  
1. Code generated by Stripe CLI did not work leading to frustration in integration. In such a case, a typical user journey would be as follows:
  - As a user, I would first try to resolve these issues by tweaking the CLI-generated code based on errors I see hoping that I can resolve them. 
  - If that doesn't work, I would re-read the READMEs to double-check if I had missed anything. 
  - When re-following all the steps doesn't work, I would move to writing it from scratch on my own using the code snippets
  This leads to wasted time and unnecessary frustration. When the code snippets in the documentation work so well, the user would be inclined to view Stripe CLI's samples as an unnecessary addition.
  
  Some issues in the generated code:
  - Assuming environment variables, not mentioned in README, are set in the developer's environment  
  <img width="640" alt="Screen Shot 2021-04-05 at 2 08 29 PM" src="https://user-images.githubusercontent.com/13269259/113614650-67d00680-9618-11eb-9595-eb9cd16f160a.png">
  
  - Expected `index.html` template is present in a separate folder (`client`) rather than within the `server` one, creating runtime issues. I was able to resolve this by moving the `index.html` into the server folder.


#### Delayed transfers

What I did:  
Transferred amount through `curl` command for transfer


What went well:  
- Transfer worked as expected without any issues


Can be improved:  
- Since all transactions before this were destination charges, there was no balance in my account to transfer. This led to some issues in discovering how to add funds to my account [explained here](#top-up-from-bank-account-to-stripe-balance).


### Generate Reports
What I did:  
1. Email & download report from dashboard
2. Attempt to schedule report from dashboard


Can be improved:  
- Both my actions led to unexpected failures as shown below

  Schedule report failure:  
<img width="615" alt="Screen Shot 2021-04-05 at 1 25 12 PM" src="https://user-images.githubusercontent.com/13269259/113610160-5c79dc80-9612-11eb-9435-54f128525a63.png">
 
  Email & Download report failure (after clicking 'Download results' button in email):  
<img width="1316" alt="Screen Shot 2021-04-05 at 1 35 28 PM" src="https://user-images.githubusercontent.com/13269259/113611195-cd6dc400-9613-11eb-99b0-a8ef1b991682.png">


My hypothesis is that these errors arose because of the absence of data for the report generation period (which ended before I created my first transaction). Test accounts should be given the option to view sample reports so that they can at least see what fields these reports hold and whether they satisfy their needs.



### Top up and Payout
What I did:  
1. Attempt to top up funds from bank account to Stripe balance to test separate transfers
2. Attempt to pay out to bank account from Stripe balance


What went well:  
- Test bank account made testing seamless


Can be improved:  

1. I got an error that I would have to enable manual payouts to add funds to my payout balance. At the moment, this does not make sense to me. As I see it, the platform balance account should be able to receive funds regardless of when the payouts are scheduled for - this would be just another source of funds for the account.  
<img width="441" alt="Screen Shot 2021-04-05 at 11 24 29 AM" src="https://user-images.githubusercontent.com/13269259/113597559-81b21f00-9601-11eb-88d2-0cd3483deff3.png">

2. The date of the payout to my bank account appears to be of the next day with the word "Paid" - in the past tense. This is either the case of an incorrect date or a tense misnomer.  
<img width="350" alt="Screen Shot 2021-04-05 at 11 32 33 AM" src="https://user-images.githubusercontent.com/13269259/113598349-9fcc4f00-9602-11eb-8b1d-750a7a163bfc.png">


### Invoicing
What I did:  
Although it wasn't relevant to my current platform, I tried out the no-code invoice feature as it seems useful for future use cases. Also, I believe no-code is the future and, thus, an area in which Stripe should focus its efforts on.


What went well:  
1. The invoice creation is quite exhaustive with options to create several kinds of coupons which can be applied either on the whole bill or on individual items.
2. Tax creation is also smooth as sample taxes are provided to aid the user. 



Can be improved:  
1. Creation of coupons and taxes happens in a new browser tab. Once these are created, the user may resort to a) restarting the invoicing flow in the same tab OR b) if they are sophisticated enough browser users, closing the new tab and going back to the older tab to continue the flow. In this case, the list of coupons and taxes is not immediately updated.

This can be solved by updating the list periodically if the user clicks on the option to create a new coupon or tax. Doing this will provide the user greater satisfaction through seamlessness. 




