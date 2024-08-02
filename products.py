from faker import Faker
from faker.providers import DynamicProvider
import random 
import uuid

fake = Faker()
 
def generate_orderID():
    return str(uuid.uuid4())

def generate_productID():
    num  = range(1,2000)
    productID = random.sample(num,1)[0]
    return productID

def generate_name():
    return fake.name()

# 17 categories
def grab_random_category_product(fake):
    selection = random.randint(1,17)
    product = None
    match selection:
        case 1:
            product = fake.beauty_product()
        case 2:
            product = fake.books_product()
        case 3:
            product = fake.electronics_product()
        case 4:
            product = fake.finearts_product()
        case 5:
            product = fake.health_product()
        case 6:
            product = fake.home_garden_product()
        case 7:
            product = fake.music_product()
        case 8:
            product = fake.instruments_product()
        case 9:
            product = fake.office_product()
        case 10:
            product = fake.outdoor_product()
        case 11:
            product = fake.pet_product()
        case 12:
            product = fake.software_product()
        case 13:
            product = fake.sports_product()
        case 14:
            product = fake.toy_games_product()
        case 15:
            product = fake.video_games_product()
        case 16:
            product = fake.video_product()
        case 17:
            product = fake.watch_product()
        case _:
            product = None

def getBeautyProvider():
    product_provider = DynamicProvider (
        provider_name = 'beauty_product',
        elements= ["Moisturizer","Cleanser","Sunscreen","Foundation","Concealer","Blush","Mascara","Lipstick","Eyeliner","Eyeshadow","Serum",
            "Toner","Face Mask","Exfoliator","Hair Conditioner","Shampoo","Body Lotion","Nail Polish","Perfume","Makeup Remover"],
    )
    return product_provider

def getBooksProvider():
    product_provider = DynamicProvider (
        provider_name = 'books_product',
        elements= ["To Kill a Mockingbird","1984","The Great Gatsby","The Catcher in the Rye","Moby-Dick","Pride and Prejudice", "War and Peace", 
                    "The Hobbit", "Crime and Punishment", "The Lord of the Rings"],
    )
    return product_provider

def getElectronicsProvider():
    product_provider = DynamicProvider (
        provider_name = 'electronics_product',
        elements= ["microwave", "oven", "toaster", "refrigerator", "dishwasher"],
    )
    return product_provider

def getFineArtsProvider():
    product_provider = DynamicProvider (
        provider_name = 'finearts_product',
        elements= ["floral painting", "scenic painting", "animal painting", " mermaid sculpture", "modern sculpture", "romantic poetry", "sad poetry", "intense poetry"],
    )
    return product_provider

def getHealthProvider():
    product_provider = DynamicProvider (
        provider_name = 'health_product',
        elements= ["fish oil", "magnesium", "feminine products", "motrin", "advil", "toe fungus cream"],
    )
    return product_provider

def getHomeGardenProvider():
    product_provider = DynamicProvider (
        provider_name = 'home_garden_product',
        elements= ["red plush throw pillow", "white plush throw pillow", "blue plush throw pillow", "red fuzzy blanket", "white fuzzy blanket", "blue fuzzy blanket",
                    "vanilla candle", "citrus candle", "shovel", "planter pots", "soil", "strawberry seeds", "tomato seeds", "blackberry seeds"],
    )
    return product_provider

def getMusicProvider():
    product_provider = DynamicProvider (
        provider_name = 'music_product',
        elements= ["big ben", "into the ocean", "clean slate", "demons", "Shrek", "The other woman", "Save Willy"],
    )
    return product_provider

def getInstrumentsProvider():
    product_provider = DynamicProvider (
        provider_name = 'instruments_product',
        elements= ["guitar", "flute", "drums", "cello", "conga", "piano"],
    )
    return product_provider

def getOfficeProvider():
    product_provider = DynamicProvider (
        provider_name = 'office_product',
        elements= ['Paper','Pens','Pencils','Notebooks','Binders','Folders','Stapler','Staples','Paper Clips','Rubber Bands','Highlighters','Markers','Whiteboard','Whiteboard Markers','Eraser'],
    )
    return product_provider

def getOutdoorProvider():
    product_provider = DynamicProvider (
        provider_name = 'outdoor_product',
        elements= ['Camping Tent','Sleeping Bag','Camping Stove','Cooler','Backpack','Hiking Boots','Outdoor Clothing','Sleeping Pad','Lantern','First Aid Kit','Fishing Rod','Fishing Tackle',
            'Binoculars','Campfire Grill','Multi-tool','Camping Chairs','Portable Water Filter','Map and Compass','Flashlight','Fire Starter','Sunscreen','Bug Spray','Water Bottle',
            'Portable Charger'],
    )
    return product_provider

def getPetProvider():
    product_provider = DynamicProvider (
        provider_name = 'pet_product',
        elements= ['Pet Food','Water Bowl','Food Bowl','Pet Bed','Leash','Collar','Harness','Grooming Brush','Cat Litter','Litter Box','Pet Carrier','Toys','Scratching Post','Pet Shampoo',
            'Dental Chews','Pet Brush','Pet Nail Clippers','Pet Crate','Feeding Station','Pet Gates','Pet Cleaning Wipes','Training Pads','Pet Backpack','Pet Clothes','Pet Carrier Bag'],
    )
    return product_provider

def getSoftwareProvider():
    product_provider = DynamicProvider (
        provider_name = 'software_product',
        elements= ['Windows 11','macOS Ventura','Ubuntu','Fedora','Android','iOS', 'Adobe Photoshop'],
    )
    return product_provider

def getSportsProvider():
    product_provider = DynamicProvider (
        provider_name = 'sports_product',
        elements= ['Soccer Ball','Basketball','Baseball Glove','Baseball Bat','Volleyball','Tennis Racket','Golf Clubs','Golf Balls','Golf Tees','Golf Glove',
            'Golf Bag','Rangefinder'],
    )
    return product_provider

def getToyGamesProvider():
    product_provider = DynamicProvider (
        provider_name = 'toy_games_product',
        elements= ['Soccer Ball','Basketball','Baseball Glove','Baseball Bat','Volleyball','Tennis Racket','Golf Clubs','Golf Balls','Golf Tees','Golf Glove',
            'Golf Bag','Rangefinder'],
    )
    return product_provider

def getVideoGamesProvider():
    product_provider = DynamicProvider (
        provider_name = 'video_games_product',
        elements= ['The Legend of Zelda: Breath of the Wild','Grand Theft Auto V','Red Dead Redemption 2','Assassin\'s Creed Valhalla','Spider-Man (PS4)','Horizon Forbidden West',
                        'Call of Duty: Modern Warfare II','Battlefield 2042','DOOM Eternal','Overwatch 2','Counter-Strike: Global Offensive','Apex Legends'],
    )
    return product_provider

def getVideoProvider():
    product_provider = DynamicProvider (
        provider_name = 'video_product',
        elements= ['Mad Max: Fury Road','Inception','The Dark Knight','Avengers: Endgame','Jurassic Park','Mission: Impossible – Fallout','Star Wars: Episode IV - A New Hope',
                        'Blade Runner 2049','The Matrix','Avatar','The Lord of the Rings: The Fellowship of the Ring','Guardians of the Galaxy'],
    )
    return product_provider

def getWatchProvider():
    product_provider = DynamicProvider (
        provider_name = 'watch_product',
        elements= ['Rolex Submariner','Omega Seamaster','Patek Philippe Nautilus','Audemars Piguet Royal Oak','Tag Heuer Carrera','Breitling Navitimer','Longines Master Collection',
                    'Omega Speedmaster Professional','IWC Pilot’s Watch','Jaeger-LeCoultre Reverso','Cartier Tank','Tissot Le Locle'],
    )
    return product_provider