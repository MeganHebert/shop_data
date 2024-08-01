from faker import Faker
from faker.providers import DynamicProvider

def main():
    print("Running application...")
    fake = Faker()
    # Add the product category provider
    fake.add_provider(getProductCategoryProvider())
    fake.add_provider(getPaymentProvider())
    fake.add_provider(getFailureProvider())


    product_category = fake.category()
    payment_type = fake.payment_type()
    quantity = fake.pyint(min_value=1, max_value=20)
    price = round(fake.pyfloat(min_value=1.00, max_value=200.00), 2)
    failure_reason = fake.failure_reason()

    print('Category: {0}, Payment Type: {1}, Quantity: {2}, Price: {3}, Failure Reason: {4}'.format(product_category, payment_type, quantity, price, failure_reason))

def getProductCategoryProvider():
    product_category_provider = DynamicProvider(
        provider_name = 'category',
        elements = ['Beauty', 'Books', 'Electronics', 'Fine Art', 'Health & Personal Care', 
                        'Home & Garden', 'Music & DVD', 'Musical Instruments', 'Office Products', 
                        'Outdoors', 'Pet Supplies', 'Software', 'Sports', 'Toys & Games', 'Video Games', 
                        'Video, & Blu-ray', 'Watches'],
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

# Run main function
if __name__ == "__main__":
    main()

