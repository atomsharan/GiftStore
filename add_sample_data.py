import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()

from base.models import Category, Product
from django.contrib.auth.models import User

def create_sample_data():
    # Create categories
    categories = [
        {"name": "Birthday Gifts", "description": "Perfect gifts for birthdays"},
        {"name": "Anniversary Gifts", "description": "Celebrate special moments"},
        {"name": "Wedding Gifts", "description": "Gifts for the happy couple"},
        {"name": "Holidays", "description": "Seasonal gifts for all occasions"},
        {"name": "For Him", "description": "Gifts specially curated for men"},
        {"name": "For Her", "description": "Gifts specially curated for women"},
        {"name": "For Kids", "description": "Fun and educational gifts for children"},
    ]
    
    for category_data in categories:
        Category.objects.get_or_create(
            name=category_data["name"],
            defaults={"description": category_data["description"]}
        )
    
    # Get all categories
    birthday = Category.objects.get(name="Birthday Gifts")
    anniversary = Category.objects.get(name="Anniversary Gifts")
    wedding = Category.objects.get(name="Wedding Gifts")
    holidays = Category.objects.get(name="Holidays")
    for_him = Category.objects.get(name="For Him")
    for_her = Category.objects.get(name="For Her")
    for_kids = Category.objects.get(name="For Kids")
    
    # Create products
    products = [
        {
            "name": "Personalized Photo Frame",
            "description": "A beautiful frame to cherish your memories",
            "price": 29.99,
            "stock": 50,
            "category": birthday
        },
        {
            "name": "Birthday Gift Basket",
            "description": "A curated basket filled with treats and goodies",
            "price": 49.99,
            "stock": 30,
            "category": birthday
        },
        {
            "name": "Anniversary Watch Set",
            "description": "Elegant matching watches for couples",
            "price": 199.99,
            "stock": 15,
            "category": anniversary
        },
        {
            "name": "Crystal Wine Glasses",
            "description": "Set of 2 premium crystal wine glasses",
            "price": 59.99,
            "stock": 25,
            "category": anniversary
        },
        {
            "name": "Wedding Memory Book",
            "description": "Beautiful album to record wedding memories",
            "price": 39.99,
            "stock": 40,
            "category": wedding
        },
        {
            "name": "Kitchen Appliance Set",
            "description": "Essential kitchen tools for the new home",
            "price": 129.99,
            "stock": 20,
            "category": wedding
        },
        {
            "name": "Christmas Gift Box",
            "description": "Festive box with holiday treats and decorations",
            "price": 44.99,
            "stock": 100,
            "category": holidays
        },
        {
            "name": "Luxury Scarf",
            "description": "Soft and stylish scarf for the winter season",
            "price": 34.99,
            "stock": 60,
            "category": holidays
        },
        {
            "name": "Premium Leather Wallet",
            "description": "Handcrafted leather wallet with multiple compartments",
            "price": 79.99,
            "stock": 45,
            "category": for_him
        },
        {
            "name": "Gourmet Shaving Kit",
            "description": "Luxury shaving accessories for the modern man",
            "price": 69.99,
            "stock": 35,
            "category": for_him
        },
        {
            "name": "Jewelry Box",
            "description": "Elegant box to store precious jewelry",
            "price": 89.99,
            "stock": 30,
            "category": for_her
        },
        {
            "name": "Spa Gift Set",
            "description": "Complete set of relaxation and pampering products",
            "price": 59.99,
            "stock": 40,
            "category": for_her
        },
        {
            "name": "Educational Building Blocks",
            "description": "Creative building set for young minds",
            "price": 29.99,
            "stock": 50,
            "category": for_kids
        },
        {
            "name": "Interactive Story Book",
            "description": "Engaging stories with interactive elements",
            "price": 19.99,
            "stock": 70,
            "category": for_kids
        },
        {
            "name": "Art and Craft Kit",
            "description": "Complete set for creative expression",
            "price": 24.99,
            "stock": 55,
            "category": for_kids
        }
    ]
    
    for product_data in products:
        Product.objects.get_or_create(
            name=product_data["name"],
            defaults={
                "description": product_data["description"],
                "price": product_data["price"],
                "stock": product_data["stock"],
                "category": product_data["category"],
                "is_available": True
            }
        )
    
    print("Sample data created successfully!")

if __name__ == "__main__":
    create_sample_data() 