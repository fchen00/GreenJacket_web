# GreenJacket_web
Website for Green Jacket


## Users
### Create:
* users can sign up for an account
* **url:** /signup
* functionality: 
  * username
  * password
  * email
  * security questions
  * company name
  * company image/logo
  * number of stores
  * addresses for stores
  * credit card/paypal info with braintree (no refunds)
  * blank menu is created for them after signup (include link to edit page)

### Read / Update:
* users can edit their account
* **url:** /settings
* functionality:
  * change everything from signup
  * link to menu page

### Delete:
* users can remove their account
* **url:** /delete_account
* "are you sure?"
* warning about no refunds

### Login:
* users use this to login
*  **url:** /login
*  functionality:
  *  username
  *  password
  *  create new account
  *  forgot your password?

### Logout:
* users use this to log-out
*  **url:** /logout

## Menus
### Create:
* user can edit their menu
* **url:** /edit_menu
* create new / edit existing section
  * set time of day section is available 
    * app will check current time and decide whether to display or not
  * is it active now?
    * for seasonal sections
  * type of food for section
    * waffle / pancake
    * fruits / vegitables / salad
    * burger
    * chicken
    * fish
    * bacon
    * other sandwich (like grilled cheese)
    * steak
    * spaghetti
    * dumplings
    * pizza
    * shrimp
    * rice
    * dessert
    * drinks (non-alcoholic)
    * drinks (alcoholic)
    * side order without meal (like just fries)
    * 
    * app will only display ones that are available 
    * for each food:
      * sides
      * drinks
      * price
      * possible variations
        * pictures showing difference
      * picture showing final decision after choice is made


### Read / Delete
* user can view menu
* **url:** /menu
* link to edit menu
* view menu for account
* button to delete menu
  * "are you sure?"

## Send data to app
### Customer app
* this is not for website users, but it sends data to mobile app
* **possible urls:** 
  * /data/customer/menu/ {unique restaurant name/id} / {optional section name/id} / {optional food name/id} / {optional keyword}
    * keywords: 
     * "sides"
     * "price"
     * "drinks"
     * "variations"
    * if optional info is not provided, send all available data
      * for example, if food not provided, send all available foods
  * /data/customer/find/ {address}
    * return restauraunts near that address

### Employee app
* not for website users, but sends data to employee mobile app
* authentication is required in POST data
* **posible urls:**
  * /data/employee/login
    * employee login
  * /data/employee/logout
    * employee logout
  * /data/employee/orders
    * send all orders that have not been dismissed
  * /data/employee/dismiss_order/{unique order id}
    * dismiss order with order id 


Inspiration from http://openweathermap.org/current
