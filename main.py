from faker import Faker
from faker.providers import DynamicProvider
import csv
from datetime import datetime


def getProductCategoryProvider():
    product_category_provider = DynamicProvider(
        provider_name = 'category',
        elements = ['Beauty', 'Books', 'Electronics', 'Fine Art', 'Health & Personal Care', 
                        'Home & Garden', 'Music & DVD', 'Musical Instruments', 'Office Products', 
                        'Outdoors', 'Pet Supplies', 'Software', 'Sports', 'Toys & Games', 'Video Games', 
                        'Video & Blu-ray', 'Watches'],
    )
    return product_category_provider

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

def main():
    print("Running application...")
    with open(f"GenerateData-{datetime.now().strftime('%Y-%m-%d %H:%M')}.csv", "w", newline='') as csvfile:
        gen_data_csv_writer = csv.writer(csvfile)

        fields = ["order_id", "customer_id", "customer_name", "product_id", "product_name",
                       "product_category", "payment_type", "qty", "price", "datetime", "country", "city",
                       "ecommerce_website_name", "payment_txn_id", "payment_txn_success", "failure_reason"]
        gen_data_csv_writer.writerow(fields)

        fake = Faker()
        for i in range(14000):

            # Add the product category provider
            fake.add_provider(getProductCategoryProvider())
            fake.add_provider(getPaymentProvider())
            fake.add_provider(getFailureProvider())


            product_category = fake.category()
            payment_type = fake.payment_type()
            quantity = fake.pyint(min_value=1, max_value=20)
            price = round(fake.pyfloat(min_value=1.00, max_value=200.00), 2)
            failure_reason = fake.failure_reason()

            row = []        #TODO: put the faker generated variables here to be written to the csv file
            gen_data_csv_writer.writerow(row)


# Run main function
if __name__ == "__main__":
    main()

