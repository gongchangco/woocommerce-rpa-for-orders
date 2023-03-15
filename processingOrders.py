import os
import pandas as pd
from woocommerce import API
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from WooCommerce
wcapi = API(
    url             =   os.getenv('WOOCOMMERCE_URL'),
    consumer_key    =   os.getenv('WOOCOMMERCE_API_KEY'),
    consumer_secret =   os.getenv('WOOCOMMERCE_API_SECRET'),
    wp_api          =   True,
    version         =   'wc/v3',
    timeout         =   20
)

# Start on the first page
page = 1

# Get all orders that are on processing status
orders = wcapi.get( "orders", params= {"per_page": 30, "status": 'processing', "page": page} ).json()

# Create empty array for specific data for each order
orderNum    = []
orderName   = []
orderStatus = []
orderID     = []

# Loop through each order
for row in orders:
    orderNum.append(row['id'])
    orderName.append(row['billing']['first_name'] + ' ' + row['billing']['last_name'])
    orderStatus.append(row['status'])
    orderID.append(row['transaction_id'])

# Create a dataframe for each order
df = pd.DataFrame(
    {
        'Order Number': orderNum,
        'Order Name': orderName,
        'Order Status': orderStatus,
        'Order ID': orderID
    }
)

# print(df)

# Add empty column for Tracking Id
df['Tracking ID'] = ''

# Export the dataframe to a xlsx file
df.to_excel('orderProcessing/processingOrders.xlsx', index=False)

print("Processing orders exported successfully!")
