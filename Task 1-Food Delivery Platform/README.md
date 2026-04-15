# COMP 2090SEF Project Task1
### Food Delivert System

## GROUP 32
<ul>
<li>Liu Pinwei(13703437)</li>
<li>Tang Chao(13791501)</li>
<li>Tsoi Pak Kiu(14276156)</li>
</ul>

## project included files
<ol>
<li>account.txt (save the information of accounts)</li>
<li>restaurant_test.txt (including the name of restaurants)</li>
<li>food_order.txt (added when there is food order, used for saving pending orders)</li>
<li>restaurant_data (folder, used for containing restaurants' menus)</li>
<li>main_system.py (the core of the system, connecting customer side and restaurant side, managing the whole system)</li>
<li>customer.py (managing the part of customer, including account management and money calculation)</li>
<li>restaurant.py (managing the part of restaurant, including the restaurant menu, details information, etc.)</li>
</ol>

# System User Guide

## initial page
When user enter into the system, they will reach the initial page. In the initial page, functions are separated into customer and restaurant sides.

### 1. sign in (Customer)
User can log into their account if they have one, saved in <i>account.txt</i>.

### 2. sign up (Customer)
User can create an account for the usage of the system.

### 3. add restaurant (Restaurant)
The function is used to add restaurant into the system. User can add a restaurant with details, and its customised menu.

### 4. restaurant orders (Restaurant)
When there is(are) order(s) from the customer side, the restaurant side can choose the order and complete it with this function.

## main page
After signing in successfully, User will enter the main page.<br>
In this page, different information will be shown. Like the money in the account, restaurant list, and the username of the account.

### 1. add value
User can add value into their account, money shown on the main page will increase if money is added.

### 2. my orders
User can see the pending orders in the account. "You don't have any pending order." will be shown if no order is done by the account.

### 3. choose restaurant
User can enter the coresponding restaurant number to choose restaurant for further information.

### 4. switch restaurant list
User can enter ">" or "<" to switch the restaurant page. The restaurants shown in the main page with change.

## restaurant page
When user choose a restaurant, the restaurant page will be shown.

### 1. restaurant menu
The menu of the restaurant will be shown, with categories and corresponding dishes. User can order dishes and make payment.

### 2. restaurant details
In this function, user can find the details of the restaurant, including the address and the open hours.

# Sample of Running The Program

## STEPS:
<ol>
Create a restaurant
<li>add a restaurant (initial page: add restaurant)</li>
<li>enter details of the restaurant</li>
<li>create the menu, enter the types, dishes and price</li>
<br>
Create an account
<li>create an account (initial page: sign up)</li>
<br>
Get in the main page
<li>add value into the account (main page: add value)</li>
<li>enter the value wanted to be added</li>
<br>
Food ordering
<li>choose an restaurant (main page: choose restaurant)</li>
<li>order some dishes, money of the account will be automatically deducted (restaurant page: menu)</li>
<li>check the order (main page: my orders)</li>
<li>end the system (main page: exit)</li>
<br>
Start the system again:
<br>
Restaurant order management
<li>check the restaurant order (initial page: restaurant orders)</li>
<li>enter the order ID and complete the order</li>
<br>
Login the system
<li>login the account (initial page: sign in)</li>
<br>
Check the order
<li>check the user order list, no pending order is supposed to be shown (main page: my orders)</li>
<li>end the system (main page: exit)</li>
</ol>


# Default Data Used for Testing
## account.txt
(account name;password;money)<br>

12345678;ShuaiGe123;0<br>
87654321;HiHi1234;0<br>
12341234;Abcd1234;0<br>
12345678;Matt1234;0

## restaurant_test.txt
(restaurant ID;restaurant name;address;store image;dining image;kitchen image;license image;open hours)<br>

1;YUMYUM;Tuen Mun;store.jpg;dining.jpg;kitchen.jpg;license.jpg;10:00-22:00<br>
2;YAHYAH;Sai Kung;store.jpg;dining.jpg;kitchen.jpg;license.jpg;10:00-20:00<br>
3;HAPPY REstaurant;Causeway Bay;store.jpg;dining.jpg;kitchen.jpg;license.jpg;07:00-22:00<br>
4;RESTAURANT;Cheung Chau;store.jpg;dining.jpg;kitchen.jpg;license.jpg;00:00-23:59<br>
5;PepegaRestaurant;Kwai Chung;store.jpg;dining.jpg;kitchen.jpg;license.jpg;09:00-21:30<br>
6;PeepoClap;Tsim Sha Tsui;store.jpg;dining.jpg;kitchen.jpg;license.jpg;10:00-21:00<br>
7;SHUmitoo;Central;store.jpg;dining.jpg;kitchen.jpg;license.jpg;06:00-20:00<br>
8;Omakakakase;Ho Man Tin;store.jpg;dining.jpg;kitchen.jpg;license.jpg;09:00-02:30<br>
9;PepeLunch;Mongkok;store.jpg;dining.jpg;kitchen.jpg;license.jpg;10:00-21:30

## food_order.txt
(order ID;customer name;restaurant name;ordered dish;total value)<br>

(it is defaulted to be empty)

## restaurant data (folder)
### (restaurant name)_menu.txt
(the restaurant YUMYUM's menu is shown here)<br>
(category;dish ID;dish name;dish price; dish sales)<br>

type1;1;dish1;50;100<br>
type1;2;dish2;40;1<br>
type2;3;dish3;72;12<br>
type2;4;dish4;73;140<br>
type3;5;dish5;56;160<br>
type4;6;dish6;10;132

## <p align = "center">THE END</p>
