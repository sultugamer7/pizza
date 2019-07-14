# Project 3

Web Programming with Python and JavaScript

This is my implementation of CS50W's Project 3: Pizza.

Short Description of the project:
    This is a web application for handling a pizza restaurant’s online orders (Pinocchio's Pizza and Subs: http://www.pinocchiospizza.net/menu.html). Users are able to browse the restaurant’s menu, add items to their cart, and confirm and place the orders. Meanwhile, the restaurant owners are able to add, update, and delete menu items, and view orders that have been placed. The special dish contains 4 unique toppings (Pepperoni, Spinach, Ham, Onions).

Description of some files:
    views.py: Holds all the Django views. It is responsible for much of the server's functionality.
    admin.py: Connects database models to Django Admin (for site administrator).
    models.py: Contains all the Django database models.
    urls.py (in the orders directory): connects views and urls.
    background.jpg: Background image.
    cart.png, favicon.ico, remove.jpg, view_order.png: To be used as icons
    script.js: Contains a JavaScript function used by the application to change the total value when extras for subs are selected/removed.
    styles.css: Contains the custom CSS used in this web app.
    db.sqlite3: Database file containing all of the tables.
    base.html: Base HTML template to be used in every other templates.
    index.html: Contains restaurant menu and forms for adding items to the shopping cart.
    login.html: Contains the login form.
    register.html: Contains the register form.
    cart.html: Contains the shopping cart and has the option to confirm and place an order.
    orders.html: Contains a table of list of orders with details which can be viewed by the admin (superuser) only.

Description of Personal Touch:
    1. Added the support to send e-mails to users after they place an order in a nice, clean, and neat way.
    2. Added some animations to alert messages for nice look and feel.
    3. Added an option to remove an item already in the cart.