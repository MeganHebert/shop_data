from faker import Faker
import random 
import uuid
from faker.providers import DynamicProvider

fake = Faker()
 
def generate_orderID():
    return str(uuid.uuid4())

def generate_productID():
    num  = range(1,2000)
    productID = random.sample(num,1)[0]
    return productID

def getNameProvider():
    name_provider = DynamicProvider(
        provider_name = "customer_name",
        elements = [fake.name()],
    )
    return name_provider

def generate_products():
        beauty = ["Moisturizer","Cleanser","Sunscreen","Foundation","Concealer","Blush","Mascara","Lipstick","Eyeliner","Eyeshadow","Serum",
            "Toner","Face Mask","Exfoliator","Hair Conditioner","Shampoo","Body Lotion","Nail Polish","Perfume","Makeup Remover"]
        
        books = ["To Kill a Mockingbird","1984","The Great Gatsby","The Catcher in the Rye","Moby-Dick","Pride and Prejudice", "War and Peace", 
                    "The Hobbit", "Crime and Punishment", "The Lord of the Rings"]
        
        electronics= ["microwave", "oven", "toaster", "refrigerator", "dishwasher"]

        fine_art = ["floral painting", "scenic painting", "animal painting", " mermaid sculpture", "modern sculpture", "romantic poetry", "sad poetry", "intense poetry"]

        health_pc = ["fish oil", "magnesium", "feminine products", "motrin", "advil", "toe fungus cream"]

        home_garden = ["red plush throw pillow", "white plush throw pillow", "blue plush throw pillow", "red fuzzy blanket", "white fuzzy blanket", "blue fuzzy blanket",
                    "vanilla candle", "citrus candle", "shovel", "planter pots", "soil", "strawberry seeds", "tomato seeds", "blackberry seeds"]
        
        music_dvd = ["big ben", "into the ocean", "clean slate", "demons", "Shrek", "The other woman", "Save Willy"]

        instruments = ["guitar", "flute", "drums", "cello", "conga", "piano"]

        office = ['Paper','Pens','Pencils','Notebooks','Binders','Folders','Stapler','Staples','Paper Clips','Rubber Bands','Highlighters','Markers','Whiteboard','Whiteboard Markers','Eraser']

        outdoor = ['Camping Tent','Sleeping Bag','Camping Stove','Cooler','Backpack','Hiking Boots','Outdoor Clothing','Sleeping Pad','Lantern','First Aid Kit','Fishing Rod','Fishing Tackle',
            'Binoculars','Campfire Grill','Multi-tool','Camping Chairs','Portable Water Filter','Map and Compass','Flashlight','Fire Starter','Sunscreen','Bug Spray','Water Bottle',
            'Portable Charger']
        
        pet =  ['Pet Food','Water Bowl','Food Bowl','Pet Bed','Leash','Collar','Harness','Grooming Brush','Cat Litter','Litter Box','Pet Carrier','Toys','Scratching Post','Pet Shampoo',
            'Dental Chews','Pet Brush','Pet Nail Clippers','Pet Crate','Feeding Station','Pet Gates','Pet Cleaning Wipes','Training Pads','Pet Backpack','Pet Clothes','Pet Carrier Bag']

        software = ['Windows 11','macOS Ventura','Ubuntu','Fedora','Android','iOS', 'Adobe Photoshop']

        sports = ['Soccer Ball','Basketball','Baseball Glove','Baseball Bat','Volleyball','Tennis Racket','Golf Clubs','Golf Balls','Golf Tees','Golf Glove',
            'Golf Bag','Rangefinder']
        
        toys_games = ['Building Blocks','Dolls','Action Figures','Stuffed Animals','Toy Cars','Train Sets','Monopoly','Scrabble','Chess','Checkers','Clue','The Game of Life',
                         'Video Game Consoles','Handheld Game Devices','Interactive Robots','Remote-Controlled Cars','Drones','Virtual Reality Headsets']
        
        video_games = ['The Legend of Zelda: Breath of the Wild','Grand Theft Auto V','Red Dead Redemption 2','Assassin\'s Creed Valhalla','Spider-Man (PS4)','Horizon Forbidden West',
                        'Call of Duty: Modern Warfare II','Battlefield 2042','DOOM Eternal','Overwatch 2','Counter-Strike: Global Offensive','Apex Legends']
        
        video_blueR = ['Mad Max: Fury Road','Inception','The Dark Knight','Avengers: Endgame','Jurassic Park','Mission: Impossible – Fallout','Star Wars: Episode IV - A New Hope',
                        'Blade Runner 2049','The Matrix','Avatar','The Lord of the Rings: The Fellowship of the Ring','Guardians of the Galaxy']
        
        watches = ['Rolex Submariner','Omega Seamaster','Patek Philippe Nautilus','Audemars Piguet Royal Oak','Tag Heuer Carrera','Breitling Navitimer','Longines Master Collection',
                    'Omega Speedmaster Professional','IWC Pilot’s Watch','Jaeger-LeCoultre Reverso','Cartier Tank','Tissot Le Locle']
        
        
        return beauty, books, electronics, fine_art, health_pc, home_garden, music_dvd, instruments, office, outdoor, pet, software, sports, toys_games, video_games, video_blueR, watches
