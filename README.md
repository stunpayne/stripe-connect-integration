# stripe-connect-integration
A sample Stripe Connect integration

# Friction Log
I am assuming the persona of a startup's technical co-founder, one who can code, looking to integrate with a payment gateway for processing transactions on his platform app. The app I'm building is an online shopping marketplace which connects artisans building customized home decor with local consumers. Consumers will make payments to my platform app for items they wish to purchase. My app will take a small fixed percentage fee and relay the remaining payment to the artisan.

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

I understand that this is to reduce friction but it makes me question what the impact of delaying the verification would be. Having an explanation about that - such as "You can go ahead and get started with your Stripe Integration but would need to verify your email before going live. This is needed so that we know it's really you and can send you important information." -  would help. Nonetheless, I go ahead and verify my email which is simple enough to do.

### Change business name
I'm not a fan of the "New Business" name on my account. So I go ahead and hover over it. Seeing the "Edit" option right there with a simple way to change my name feels great!

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
