# woocommerce-rpa-for-orders
A skeleton template for managing WooCommerce order processing using UiPath RPA + Python. 

## Useful For:
* Clients that want to know the update on their orders, if it's shipped, and want tracking number
* Want to be efficient with time

## WP Plugins Used
1. WooCommerce using PayPal Standard (Legacy) /or PayPal Payments (WC plugin)
2. A Shipping or Order Tracking Plugin 	*For this case, using [Orders Tracking for WooCommerce](https://wordpress.org/plugins/woo-orders-tracking/)*

## Manual Way
1.  Login
2.  Go to Orders tab
3.  Click on a Processing Order
4.  Go to PayPal ID in a New Tab
5.  Get Tracking ID (if it exists)
6.  Go to Processing Order
7.  Add Tracking Number
8.  Paste Tracking ID
9.  Choose Shipping Option
10. Submit information to change Processing Order to Completed Order
11. Complete and Repeat Step 2
12. When finished with all Processing Orders, Logout

### Notes:
* Decided to hide .xlsx file due to info