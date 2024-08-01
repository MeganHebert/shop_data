from faker import Faker
from faker.providers import DynamicProvider

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

    print(f'Category: {product_category}, Payment Type: {payment_type}, Quantity: {quantity}, Price: {price}, Failure Reason: {failure_reason}')

# Run main function
if __name__ == "__main__":
    main()

