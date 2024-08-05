from faker.providers import DynamicProvider

beauty_list = ["Moisturizer","Cleanser","Sunscreen","Foundation","Concealer","Blush","Mascara","Lipstick","Eyeliner","Eyeshadow","Serum",
            "Toner","Face Mask","Exfoliator","Hair Conditioner","Shampoo","Body Lotion","Nail Polish","Perfume","Makeup Remover"]

book_list = ["To Kill a Mockingbird","1984","The Great Gatsby","The Catcher in the Rye","Moby-Dick","Pride and Prejudice", "War and Peace", 
                    "The Hobbit", "Crime and Punishment", "The Lord of the Rings"]

electronic_list = ["microwave", "oven", "toaster", "refrigerator", "dishwasher"]

fine_arts_list = ["floral painting", "scenic painting", "animal painting", " mermaid sculpture", "modern sculpture", "romantic poetry", "sad poetry", "intense poetry"]

health_list = ["fish oil", "magnesium", "feminine products", "motrin", "advil", "toe fungus cream"]

home_garden = ["red plush throw pillow", "white plush throw pillow", "blue plush throw pillow", "red fuzzy blanket", "white fuzzy blanket", "blue fuzzy blanket",
                    "vanilla candle", "citrus candle", "shovel", "planter pots", "soil", "strawberry seeds", "tomato seeds", "blackberry seeds"]

music_list = ["big ben", "into the ocean", "clean slate", "demons", "Shrek", "The other woman", "Save Willy"]

instrument_list =["guitar", "flute", "drums", "cello", "conga", "piano"]

office_list = ['Paper','Pens','Pencils','Notebooks','Binders','Folders','Stapler','Staples','Paper Clips','Rubber Bands','Highlighters','Markers','Whiteboard','Whiteboard Markers','Eraser']

outdoor_list = ['Camping Tent','Sleeping Bag','Camping Stove','Cooler','Backpack','Hiking Boots','Outdoor Clothing','Sleeping Pad','Lantern','First Aid Kit','Fishing Rod','Fishing Tackle',
            'Binoculars','Campfire Grill','Multi-tool','Camping Chairs','Portable Water Filter','Map and Compass','Flashlight','Fire Starter','Sunscreen','Bug Spray','Water Bottle',
            'Portable Charger']

pet_list = ['Pet Food','Water Bowl','Food Bowl','Pet Bed','Leash','Collar','Harness','Grooming Brush','Cat Litter','Litter Box','Pet Carrier','Toys','Scratching Post','Pet Shampoo',
            'Dental Chews','Pet Brush','Pet Nail Clippers','Pet Crate','Feeding Station','Pet Gates','Pet Cleaning Wipes','Training Pads','Pet Backpack','Pet Clothes','Pet Carrier Bag']

software_list = ['Windows 11','macOS Ventura','Ubuntu','Fedora','Android','iOS', 'Adobe Photoshop']

sports_list = ['Soccer Ball','Basketball','Baseball Glove','Baseball Bat','Volleyball','Tennis Racket','Golf Clubs','Golf Balls','Golf Tees','Golf Glove',
            'Golf Bag','Rangefinder']

toys_list = ['Soccer Ball','Basketball','Baseball Glove','Baseball Bat','Volleyball','Tennis Racket','Golf Clubs','Golf Balls','Golf Tees','Golf Glove',
            'Golf Bag','Rangefinder']

video_game_list = ['The Legend of Zelda: Breath of the Wild','Grand Theft Auto V','Red Dead Redemption 2','Assassin\'s Creed Valhalla','Spider-Man (PS4)','Horizon Forbidden West',
                        'Call of Duty: Modern Warfare II','Battlefield 2042','DOOM Eternal','Overwatch 2','Counter-Strike: Global Offensive','Apex Legends']

video_list = ['Mad Max: Fury Road','Inception','The Dark Knight','Avengers: Endgame','Jurassic Park','Mission: Impossible – Fallout','Star Wars: Episode IV - A New Hope',
                        'Blade Runner 2049','The Matrix','Avatar','The Lord of the Rings: The Fellowship of the Ring','Guardians of the Galaxy']

watch_list = ['Rolex Submariner','Omega Seamaster','Patek Philippe Nautilus','Audemars Piguet Royal Oak','Tag Heuer Carrera','Breitling Navitimer','Longines Master Collection',
                    'Omega Speedmaster Professional','IWC Pilot’s Watch','Jaeger-LeCoultre Reverso','Cartier Tank','Tissot Le Locle']

def generate_productID(fake):
     productID = fake.random_number(digits=5, fix_len=True)
     return productID

def generate_customerID(fake):
     customerID = fake.random_number(digits=5, fix_len=True)
     return customerID

def generate_name(fake):
    name_provider = DynamicProvider(
        provider_name = "customer_name",
        elements = [fake.name()],
    )
    return name_provider

def getProductCategoryProvider():
    product_category_provider = DynamicProvider(
        provider_name = 'category',
        elements = ['Beauty', 'Books', 'Electronics', 'Fine Art', 'Health & Personal Care', 
                        'Home & Garden', 'Music & DVD', 'Musical Instruments', 'Office Products', 
                        'Outdoors', 'Pet Supplies', 'Software', 'Sports', 'Toys & Games', 'Video Games', 
                        'Video & Blu-ray', 'Watches'],
    )
    return product_category_provider

# 17 categories
def grab_random_category_product(fake):
    selection = fake.pyint(min_value=1, max_value=17)
    product = None
    category = None
    match selection:
        case 1:
            product = fake.beauty_product()
            category = 'Beauty'
            index = beauty_list.index(product) + 1
            product_id = selection * index
        case 2:
            product = fake.books_product()
            category = 'Books'
            index = book_list.index(product) + 1
            product_id = selection * index
        case 3:
            product = fake.electronics_product()
            category = 'Electronics'
            index = electronic_list.index(product) + 1
            product_id = selection * index
        case 4:
            product = fake.finearts_product()
            category = 'Fine Art'
            index = fine_arts_list.index(product) + 1
            product_id = selection * index
        case 5:
            product = fake.health_product()
            category = 'Health & Personal Care'
            index = health_list.index(product) + 1
            product_id = selection * index
        case 6:
            product = fake.home_garden_product()
            category = 'Home & Garden'
            index = home_garden.index(product) + 1
            product_id = selection * index
        case 7:
            product = fake.music_product()
            category = 'Music & DVD'
            index = music_list.index(product) + 1
            product_id = selection * index
        case 8:
            product = fake.instruments_product()
            category = 'Musical Instruments'
            index = instrument_list.index(product) + 1
            product_id = selection * index
        case 9:
            product = fake.office_product()
            category = 'Office Products'
            index = office_list.index(product) + 1
            product_id = selection * index
        case 10:
            product = fake.outdoor_product()
            category = 'Outdoors'
            index = outdoor_list.index(product) + 1
            product_id = selection * index
        case 11:
            product = fake.pet_product()
            category = 'Pet Supplies'
            index = pet_list.index(product) + 1
            product_id = selection * index
        case 12:
            product = fake.software_product()
            category = 'Software'
            index = software_list.index(product) + 1
            product_id = selection * index
        case 13:
            product = fake.sports_product()
            category = 'Sports'
            index = sports_list.index(product) + 1
            product_id = selection * index
        case 14:
            product = fake.toy_games_product()
            category = 'Toys & Games'
            index = toys_list.index(product) + 1
            product_id = selection * index
        case 15:
            product = fake.video_games_product()
            category = 'Video Games'
            index = video_game_list.index(product) + 1
            product_id = selection * index
        case 16:
            product = fake.video_product()
            category = 'Video & Blu-ray'
            index = video_list.index(product) + 1
            product_id = selection * index
        case 17:
            product = fake.watch_product()
            category = 'Watches'
            index = watch_list.index(product) + 1
            product_id = selection * index
    return product + ',' + category

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