# stripe-connect-integration
Notes on a sample Stripe Connect integration

# Executive Summary
<ins>User Persona:</ins>  
I am assuming the persona of a startup's technical co-founder, one who can code, looking to integrate with a payment gateway for processing transactions on his platform app.


<ins>Top user needs from a payment gateway:</ins>  
- Accepting payments from customers
- Transferring funds to businesses within defined SLAs with reliability
- Quick & easy integration
- Easy generation of invoices for customers
- Dashboard for sellers to debit funds to my platform
- Security & Compliance out of the box


<ins>What worked well:</ins>  
- Most of the integration was smooth and easy. Anyone who knows how to code will easily understand the APIs and get onboarded quickly.
- Documentation is comprehensive and builds confidence in the capabilities of the Stripe system
- Code samples were fairly copy-pastable and immensely helpful


<ins>Improvements: </ins>  
- Stripe CLI-generated code doesn't work out of the box leading to frustration in integration
  - Solution: The code can be simplified to require less setup (such as env variables) from the developer. Regular testing of the sample codes with external developers (and by the Stripe Connect PM and dev teams) will improve reliability of the code. The goal should be to have the code functioning out of the box in 100% of cases.
- Payout schedule only has periodic (daily/weekly/monthly) options which could lead to high transaction costs for Stripe
  - Solution: An option to trigger payouts when the balance reaches a threshold amount (and nudging users to adopt this option) will reduce transaction costs for Stripe
- 'Payout' term used for multiple operations (move funds to own bank, transfer to sellers) leading to confusion - even the document heading says "Collect payments then pay out"
  - Solution: Since 'Transfers' is the API for moving funds to sellers, ensure that this is the term used for this action throughout.
-  Some terms (destination charges, Express accounts) are left unexplained
  - Solution: Add one-line explanations with hyperlinks to detailed documentation wherever possible



# Friction Log

### Table of Contents
- [Platform Introduction](#platform-introduction)
- [Sign Up and Dashboard](#sign-up-and-dashboard)


## Platform Introduction
As the startup's technical co-founder, I'm building an app for an online shopping marketplace which connects artisans building customized home decor with local consumers. Consumers will make payments to my platform app for items they wish to purchase. My app will take a fee and relay the remaining payment to the artisan, after they've delivered the order.

I've heard great things about Stripe so I log on to the website(https://stripe.com/) to check it out.

## Sign Up and Dashboard

### Website Landing
My initial thoughts are highly positive. I see the one-liner on Stripe mentions "*..startups..use Stripe.. to accept payments, send payouts, and manage their businesses online*", which encourages me. 
I like seeing the "Start now" button which provides me a good place to start - I know I have to come back to this. 
Scrolling down and seeing the logos of Instacart and Shopify provides me further confidence that Stripe would work for me.

Scrolling further down, I notice an image showing a graph of declining dispute rates. As an enthusiastic startup co-founder, I hadn't thought about having to manage disputes while conducting business but it's good to see that Stripe's got it covered.

### Trying 'Start Now'
I click on 'Start Now' and land on the Sign Up page. Seeing 'marketplaces' under "Support any business model" reaffirms my faith that Stripe will work.

<img width="484" alt="Screen Shot 2021-04-02 at 1 36 41 PM" src="https://user-images.githubusercontent.com/13269259/113443907-76b87e00-93b8-11eb-8748-918c4debd510.png">

The Sign Up is simple and easy. It makes sense that email, password, full name and country were asked - nothing out of the blue.

I've received an email to verify my email on Stripe. 
On the dashboard that appears after login, I wonder why verifying the email is the fourth step instead of the first.

<img width="904" alt="Screen Shot 2021-04-02 at 1 44 06 PM" src="https://user-images.githubusercontent.com/13269259/113444425-808eb100-93b9-11eb-9086-884408cbe70b.png">

As a user, I understand that this is to reduce friction but it makes me question what the impact of delaying the verification would be. Having an explanation about that - such as "You can go ahead and get started with your Stripe Integration but would need to verify your email before going live. This is needed so that we know it's really you and can send you important information." -  would help. Nonetheless, I go ahead and verify my email which is simple enough to do.

### Change business name
I'm not a fan of the "New Business" name on my account. So I go ahead and hover over it. Seeing the "Edit" option right there with a simple way to change my name feels great! Also, writing a generic name like that is a good way to nudge users to actually edit that info - it employs the basic necessity of humans to fix low hanging fruits they spot.

<img width="198" alt="Screen Shot 2021-04-02 at 1 49 58 PM" src="https://user-images.githubusercontent.com/13269259/113444868-52f63780-93ba-11eb-8a1a-0e82091f2c80.png">

I apply my right-brain skills and choose the name "ArtIsOn" as a pun on "artisan", feel good about myself and move on :)

### Scanning the Home Page
The 'Today' and 'Reports overview' sections pique my curiosity and I scroll down to have a look.
All the dashboards seem self-explanatory from their titles and one-line descriptions. These charts give me the impression that the dashboard will maintain and present data related to my business upfront and the Home Page will be particularly useful for snapshot info.

I try to edit the charts using the 'Edit charts' button but that doesn't work, understandably, because there is no data yet. However, I wonder why I still cannot see what different charts I can create - that should be possible in the absence of data. Here's what I propose for this:
- In case there is reason to disallow the user from editing charts in the absence of data (such as dummy charts need to be designed manually OR front end chart code logic breaks if there is no data), an error message should be shown on hovering above the 'Edit Charts' button such as "Start your integration to generate data and edit charts"
- In case there is no reason to disallow the user from doing so, the 'Edit Charts' button should be enabled.

<img width="245" alt="Screen Shot 2021-04-02 at 2 14 22 PM" src="https://user-images.githubusercontent.com/13269259/113446613-ba61b680-93bd-11eb-85eb-31b0ac586967.png">


### Scanning menus
I quickly have a look at the other menu options before I start my integration to see what all information will be available on the dashboard. Everything seems quite self-explanatory.

I notice a small bug in the order of the dates mentioned on the 'Financial reports' page. Instead of `Apr2-Mar31`, it should be `Mar31-Apr2` assuming that the last two days are what is being talked about here (unless this shows the previous year's data, in which case Apr 2 doesn't make sense as a starting point).

Lastly, I like seeing 'Read more about reporting and when your data becomes available.'. This is the kind of info I was looking for when scanning the home page above.

<img width="1018" alt="Screen Shot 2021-04-02 at 2 06 30 PM" src="https://user-images.githubusercontent.com/13269259/113446058-a23d6780-93bc-11eb-98ab-d74afbf497a2.png">


## Integration
Having explored the menu options, I begin my integration. I go to the Home Page and click on 'Explore Docs'

<img width="886" alt="Screen Shot 2021-04-02 at 2 20 24 PM" src="https://user-images.githubusercontent.com/13269259/113446972-92bf1e00-93be-11eb-8cfd-85cee48ed12a.png">

It was quite easy to spot "Multiparty payments" at the bottom. Pros: Platform, Marketplace, Two-sided business -> all helpful keywords for the target customer to find the right product. From the list of integration options below it, it was quite clear that "Collect payments then pay out" was the right approach for me to take. Although my sellers would be shipping to users on their own, I would issue payments to them only once the delivery has been initiated.

Went well: The subtitle restates my use case and reaffirms that I am on the right page  
<img width="796" alt="Screen Shot 2021-04-02 at 6 31 45 PM" src="https://user-images.githubusercontent.com/13269259/113461322-af208200-93e1-11eb-8191-6dc14f362a69.png">

Can be improved: The homeowner example on this page makes the use case being served quite clear. To make the example even clearer and reduce user read time, a simple flow diagram can be built. The connect flow can be described as -  
    User                ->                      Platform               ->                 Seller  
(Makes payment)         (Accepts payments from User, pays out to Seller)     (Receives payout from Platform)  

The example can then be described as -  
    Tenants                ->                   Kavholm               ->                 Homeowners  
(Makes payment)         (Accepts payments from Tenants, pays out to Homeowner)     (Receives payout from Kavholm)  

This would reduce the setup time for the user, help them visualize the flow and enable them to get into the tutorial more quickly.

### Prereqs

<img width="844" alt="Screen Shot 2021-04-02 at 6 45 39 PM" src="https://user-images.githubusercontent.com/13269259/113461767-a16bfc00-93e3-11eb-83cb-55995349b1bc.png">

Prereq #1 - Register your platform
Upon clicking the link for this, I was taken to this page.
<img width="1391" alt="Screen Shot 2021-04-02 at 6 46 03 PM" src="https://user-images.githubusercontent.com/13269259/113461784-ae88eb00-93e3-11eb-922c-63f01b93e87a.png">

The major issue with this page is that there was no clear call to action. Coloring the 'Get Started' and 'Find a Partner' buttons differently might make the call more explicit.
I selected Platform or Marketplace and went ahead. Upon doing that, I was taken to the home page where I was shown this:
<img width="1370" alt="Screen Shot 2021-04-02 at 6 50 00 PM" src="https://user-images.githubusercontent.com/13269259/113461916-3c64d600-93e4-11eb-8656-a29cecdd98b0.png">
This is very relevant information. In case this was shown earlier, I would have known exactly which Stripe product to use (Connect) and where to start. This will eliminate the step of finding the right documentation on my own. Additionally, it will reduce one pre-requisite in the documentation which gives the user the impression of reduced setup work. In light of this, I think that registering the platform should be done the first time the user lands on the dashboard.


Prereq #2 - Activate your account
This flow was smooth overall. I particularly liked the explanatory messages for some fields that showed up on the side. These messages appeared for exactly the fields that are less common knowledge.
<img width="739" alt="Screen Shot 2021-04-02 at 6 57 49 PM" src="https://user-images.githubusercontent.com/13269259/113462195-54892500-93e5-11eb-8de3-87243b592abd.png">

After completing Step 2, the message on the home page was back to the default "Explore docs" one, leading to an inconsistent experience. As a user, I would expect to see the Connect docs link everytime once I've registered my platform.

<img width="879" alt="Screen Shot 2021-04-02 at 7 02 32 PM" src="https://user-images.githubusercontent.com/13269259/113462337-fd378480-93e5-11eb-86da-e27355b44825.png">


Prereq #3 - Fill out your platform profile
Upon clicking the link to this prereq on the docs page, I was taken to the home page again with a link to complete the profile. Instead, since the action I was going to take was already known, I should have been taken right to the prereq step.

<img width="1379" alt="Screen Shot 2021-04-02 at 7 07 09 PM" src="https://user-images.githubusercontent.com/13269259/113462464-a0889980-93e6-11eb-8235-e0c5c0fdcae6.png">

At the end of the platform profile, I was shown recommendations for the documentation I can follow for my integration.

<img width="754" alt="Screen Shot 2021-04-02 at 7 16 26 PM" src="https://user-images.githubusercontent.com/13269259/113462724-ee51d180-93e7-11eb-86ea-4f5c50c5fe32.png">

After having gone through a page listing all docs, finding the right one and completing the prereqs, I am shown the links to the docs that Stripe believes is right for me. This experience reaffirms my earlier point that these steps should have come earlier. In doing that, there surely is a cost of asking the user to complete several steps before they can begin looking into the documentation but that would be the right thing to do as the user hasn't begun the integration yet anyway. Moreover, if the user is told that these steps will help them find the right integration and documentation, they would be more easily convinced to completing these forms.

The section below this was extremely helpful. 

<img width="1370" alt="Screen Shot 2021-04-02 at 7 20 37 PM" src="https://user-images.githubusercontent.com/13269259/113462833-8354ca80-93e8-11eb-8244-81dbf4d40a25.png">


Prereq #3 - Brand settings
Went well:
- Allowing the merchant to customize how the onboarding page looks is good for user experience. It provides their users the feeling that they're still within the context of the original website even though they've been redirected to a Stripe page for onboarding, enhancing the user's trust in the flow. Moreover, merchants would love to customize the experience at every step to have greater control of the overall user experience.

<img width="1009" alt="Screen Shot 2021-04-03 at 5 19 13 PM" src="https://user-images.githubusercontent.com/13269259/113492902-b78bc200-94a0-11eb-82e9-f5444863694e.png">


To be improved:
- The prereq bullet says "Customize your brand settings on the Connect settings page. This information is required for Connect Onboarding.". As a user, I can't put my finger on what 'Connect Onboarding' means. Are we talking about onboarding me as a business onto Connect? Or about onboarding sellers onto my platform?  
Solution: Mention clearly that this action will customize the page that sellers see while signing up on the business platform.

- Upon clicking the link, I am taken to the Connect Settings page but not directly to the section of the prereq. In order to verify the action to take here, I need to go back to the documentation page and re-read "Customize your brand settings.." and scroll down to look at all the headings on the Connect Settings page to learn that 'Branding' is the section I need to head to.  

- The 'Save branding changes' button is well named as it preserves the context of the prerequisite.

<img width="197" alt="Screen Shot 2021-04-03 at 5 23 20 PM" src="https://user-images.githubusercontent.com/13269259/113492992-4b5d8e00-94a1-11eb-9d21-39238db2637e.png">

However, upon clicking it, a loader appears to show that saving is in progress but when the save is completed, the loader disappears and the button becomes unclickable. This leaves the user wondering whether the save was successfully completed so a temporary tick mark might be more satisfactory from a UX perspective.

<img width="206" alt="Screen Shot 2021-04-03 at 5 27 17 PM" src="https://user-images.githubusercontent.com/13269259/113493052-d8a0e280-94a1-11eb-8153-6fa0c7819604.png">


For further steps  
Programming language chosen: Python 3

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
##### Express Account Explanation
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


- Tell user about test dashboard early on
- Control number of transactions and send payouts?
- Invoicing
- What do payouts really mean?

<img width="693" alt="Screen Shot 2021-04-04 at 11 54 59 AM" src="https://user-images.githubusercontent.com/13269259/113515854-95e01880-953c-11eb-8f19-00bfce6c7a6d.png">



