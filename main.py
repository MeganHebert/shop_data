from faker import Faker
from faker.providers import DynamicProvider
import products
import uuid
import csv
import math

def generateOrderId():
    return str(uuid.uuid4())

def generate_name(fake):
    return fake.name()

def getPaymentProvider():
    payment_provider = DynamicProvider (
        provider_name = 'payment_type',
        elements= ['Debit', 'Cash', 'Credit'],
    )
    return payment_provider

def getFailureProvider():
    failure_provider = DynamicProvider(
        provider_name= 'failure_reason',
        elements= ['payment failed', 'insufficient funds', 'network timeout', 'card declined'],
    )
    return failure_provider

def getEcommerceWebsiteName():
    ecommerce_website_provider = DynamicProvider(
        provider_name = 'ecommerce_website',
        elements = ["www.amazon.com", "www.ebay.com", "www.walmart.com",
                    "www.alibaba.com", "www.etsy.com", "www.shopify.com",
                    "www.target.com", "www.bestbuy.com", "www.microcenter.com",
                    "www.wayfair.com", "www.newegg.com", "www.zappos.com",
                    "www.rakuten.com", "www.overstock.com", "www.aliexpress.com",
                    "www.flipkart.com"],
    )
    return ecommerce_website_provider

def addProviders(fake):
    # Add the product category provider
    fake.add_provider(products.getProductCategoryProvider())
    fake.add_provider(getPaymentProvider())
    fake.add_provider(getFailureProvider())
    
    fake.add_provider(getEcommerceWebsiteName())


    fake.add_provider(products.getBeautyProvider())
    fake.add_provider(products.getBooksProvider())
    fake.add_provider(products.getElectronicsProvider())
    fake.add_provider(products.getFineArtsProvider())
    fake.add_provider(products.getHealthProvider())
    fake.add_provider(products.getHomeGardenProvider())
    fake.add_provider(products.getMusicProvider())
    fake.add_provider(products.getInstrumentsProvider())
    fake.add_provider(products.getOfficeProvider())
    fake.add_provider(products.getOutdoorProvider())
    fake.add_provider(products.getPetProvider())
    fake.add_provider(products.getSoftwareProvider())
    fake.add_provider(products.getSportsProvider())
    fake.add_provider(products.getToyGamesProvider())
    fake.add_provider(products.getVideoGamesProvider())
    fake.add_provider(products.getVideoProvider())
    fake.add_provider(products.getWatchProvider())

def appendGeneratedData(fake, data, count, rogue_amount):
    category_product_id = products.grab_random_category_product(fake).split(',')

    order_id = generateOrderId(fake)
    customer_id = fake.unique.random_int(min=111111, max=999999)
    customer_name = generate_name(fake)
    product_id = category_product_id[2]
    product_name = category_product_id[0]
    product_category = category_product_id[1]
    payment_type = fake.payment_type()
    quantity = fake.pyint(min_value=1, max_value=20)
    price = round(fake.pyfloat(min_value=1.00, max_value=200.00), 2)
    date_time = fake.date_time().strftime("%Y-%m-%d %H:%M")
    country = fake.country()
    city = fake.city()
    ecommerce_website = fake.ecommerce_website()
    payment_txn_id = fake.random_number(digits=5, fix_len=True)
    payment_txn_success = fake.random_element(elements=['Y', 'N'])
    failure_reason = fake.failure_reason()

    # Random data added
    if count <= rogue_amount + 1:
        city += str(fake.pyint(min_value=1, max_value=10))
        ecommerce_website += '/' + fake.catch_phrase() + '/'


    data.append({'order_id': order_id, 'customer_id': customer_id, 'customer_name': customer_name, 'product_id': product_id, 
                    'product_name': product_name, 'product_category':product_category, 'payment_type':payment_type, 'qty':quantity, 'price':price, 
                    'datetime':date_time, 'country':country, 'city':city, 'ecommerce_website_name':ecommerce_website, 'payment_txn_id':payment_txn_id,
                    'payment_txn_success': payment_txn_success, 'failure_reason': failure_reason})

def main():
    print("Running application...")
    fake = Faker()

    addProviders(fake)
    
    data = []

    counter = 1
    limit = 10001
    rogue_amount = math.ceil(limit * 0.04)

    while counter < limit:
        appendGeneratedData(fake, data, counter, rogue_amount)
        counter += 1
    
    with open('shop_data_generation.csv', 'w', newline='') as csv_file:
        fieldnames = ['order_id', 'customer_id', 'customer_name', 'product_id', 'product_name','product_category', 'payment_type', 'qty', 'price', 
                      'datetime', 'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 'payment_txn_success', 'failure_reason']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
# Run main function
if __name__ == "__main__":
    main()

