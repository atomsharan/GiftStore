# 🎁 GiftStore - Your Ultimate Gift Shopping Platform

> A modern, user-friendly Django-based e-commerce platform for discovering and purchasing the perfect gifts.

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-darkgreen?logo=django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue?logo=sqlite)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)](https://github.com)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [📦 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Configuration](#️-configuration)
- [📚 Usage Guide](#-usage-guide)
- [🛠️ Development](#️-development)
- [🔧 Admin Panel](#-admin-panel)
- [❓ FAQ](#-faq)
- [📝 License](#-license)

---

## ✨ Features

- ✅ **Product Catalog**: Browse gifts by categories with detailed descriptions and images
- ✅ **User Authentication**: Secure registration and login system
- ✅ **Shopping Cart**: Add/remove items and manage your purchases
- ✅ **Order Management**: Track order status from pending to delivery
- ✅ **Admin Panel**: Manage products, categories, and orders efficiently
- ✅ **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- ✅ **Inventory Management**: Real-time stock tracking
- ✅ **User Accounts**: View purchase history and manage profile

---

## 📦 Project Structure

```
gift-store/
├── base/                    # Main Django app
│   ├── models.py           # Database models (Product, Order, Cart, etc.)
│   ├── views.py            # View logic and business logic
│   ├── urls.py             # URL routing
│   ├── admin.py            # Django admin configuration
│   ├── context_processors.py # Global template context
│   └── migrations/         # Database migration files
├── store/                   # Django project configuration
│   ├── settings.py         # Project settings and configuration
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Homepage
│   ├── product_list.html  # Products listing page
│   ├── product_detail.html # Individual product page
│   ├── cart.html          # Shopping cart page
│   ├── checkout.html      # Checkout page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   └── my-account.html    # User account page
├── static/                 # Static files (CSS, JS, images)
│   └── assets/
├── media/                  # User-uploaded files (product images)
│   └── products/
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── add_sample_data.py     # Script to populate sample data
└── README.md              # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (3.13 recommended)
- **pip** (Python package manager)
- **Git** (for version control)

### Installation Steps

#### 1️⃣ **Clone the Repository**

```powershell
git clone https://github.com/atomsharan/GiftStore.git
cd GiftStore
```

#### 2️⃣ **Create Virtual Environment**

```powershell
# Create virtual environment
python -m venv gnv

# Activate virtual environment
gnv\Scripts\Activate.ps1
# If you get execution policy error, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 3️⃣ **Install Dependencies**

```powershell
pip install django pillow
```

#### 4️⃣ **Apply Migrations**

```powershell
python manage.py migrate
```

#### 5️⃣ **Create Superuser (Admin Account)**

```powershell
python manage.py createsuperuser
# Follow the prompts to create admin account
```

#### 6️⃣ **Load Sample Data (Optional)**

```powershell
python manage.py runscript add_sample_data
```

#### 7️⃣ **Start Development Server**

```powershell
python manage.py runserver
```

🎉 **Your store is now running!** Visit: http://localhost:8000

---

## ⚙️ Configuration

### Important Settings in `store/settings.py`

| Setting | Default | Description |
|---------|---------|-------------|
| `DEBUG` | `True` | Set to `False` for production |
| `ALLOWED_HOSTS` | `[]` | Add your domain names here |
| `SECRET_KEY` | *Generated* | Keep this secret! Change for production |
| `DATABASES` | SQLite | Database configuration |

### Environment Variables (Recommended for Production)

Create a `.env` file:

```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=sqlite:///db.sqlite3
```

> ⚠️ **Security Warning**: Never commit `.env` file or sensitive data to version control!

---

## 📚 Usage Guide

### 👥 As a Customer

#### Browse Products
1. Visit the homepage at http://localhost:8000
2. Click on "Products" or browse by category
3. View product details, images, and prices
4. Check real-time stock availability

#### Create an Account
1. Click "Register" on the navigation bar
2. Fill in your details (username, email, password)
3. Click "Sign Up"
4. You can now access your cart and order history

#### Shopping
1. Select a product you want to purchase
2. Click "Add to Cart"
3. Adjust quantity in the cart if needed
4. Proceed to checkout
5. Enter delivery address and phone number
6. Place your order

#### Track Orders
1. Log in to your account
2. Click "My Account"
3. View your order history and status
4. Track real-time order updates

### 🔐 Admin Features

#### Access Admin Panel
1. Visit: http://localhost:8000/admin
2. Log in with superuser credentials
3. You now have access to:
   - Product management
   - Category management
   - Order tracking
   - User management

---

## 🔧 Admin Panel

### Managing Products

```
Admin Panel → Products → Add Product
```

**Required Fields:**
- Product Name
- Description
- Price
- Category
- Stock Quantity
- Product Image

### Managing Categories

```
Admin Panel → Categories → Add Category
```

**Fields:**
- Category Name
- Category Description

### Managing Orders

```
Admin Panel → Orders
```

**Status Options:**
- 🟡 Pending - Order received, awaiting processing
- 🔵 Processing - Order being prepared
- 🟣 Shipped - Order on the way
- 🟢 Delivered - Order delivered to customer
- ❌ Cancelled - Order has been cancelled

### Managing Users

```
Admin Panel → Users
```

- View all registered users
- Manage user accounts
- Reset passwords if needed

---

## 🛠️ Development

### Project Dependencies

```
Django==5.2          # Web framework
Pillow              # Image processing
```

### Running Tests

```powershell
python manage.py test base
```

### Database Migrations

```powershell
# Create new migrations (if models changed)
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View migration status
python manage.py showmigrations
```

### Collecting Static Files (Production)

```powershell
python manage.py collectstatic
```

### Database Models Overview

#### Product Model
- ID, Name, Description, Price
- Image, Category, Stock
- Availability Status
- Created/Updated Timestamps

#### Order Model
- Order ID, User Reference
- Customer Details (Name, Email, Address, Phone)
- Order Status (Pending, Processing, Shipped, etc.)
- Total Price
- Order Items (related to products)

#### Cart Model
- One cart per user
- Multiple cart items
- Auto-calculated total

---

## ❓ FAQ

<details>
<summary><b>Q: How do I reset my admin password?</b></summary>

```powershell
python manage.py changepassword admin_username
```

</details>

<details>
<summary><b>Q: How do I backup my database?</b></summary>

```powershell
# Simply copy the db.sqlite3 file to a safe location
Copy-Item db.sqlite3 db.sqlite3.backup
```

</details>

<details>
<summary><b>Q: Can I use a different database (PostgreSQL, MySQL)?</b></summary>

Yes! Update `DATABASES` in `store/settings.py`. Install the appropriate driver and configure the connection string.

</details>

<details>
<summary><b>Q: How do I deploy to production?</b></summary>

1. Set `DEBUG = False`
2. Update `ALLOWED_HOSTS`
3. Generate a strong `SECRET_KEY`
4. Use a production-grade database
5. Configure static file serving
6. Use Gunicorn or Waitress as WSGI server
7. Use Nginx or Apache as reverse proxy

</details>

<details>
<summary><b>Q: How do I add more features (payments, emails, etc.)?</b></summary>

1. Install the required package: `pip install package-name`
2. Add to `INSTALLED_APPS` in settings.py
3. Update models if needed: `python manage.py makemigrations`
4. Apply changes: `python manage.py migrate`
5. Update views and templates

</details>

<details>
<summary><b>Q: How do I debug issues?</b></summary>

1. Check Django logs in console
2. Use Django debug toolbar: `pip install django-debug-toolbar`
3. Check database with: `python manage.py dbshell`
4. Use print statements in views for debugging

</details>

---

## 🔗 Useful Links

- [Django Documentation](https://docs.djangoproject.com/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [HTML/CSS Reference](https://developer.mozilla.org/)
- [Python Documentation](https://docs.python.org/)

---

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Commit: `git commit -am 'Add feature'`
5. Push: `git push origin feature/your-feature`
6. Create a Pull Request

---

## 📞 Support

Having issues? Here's how to get help:

1. **Check the FAQ** section above
2. **Review Django Documentation**: https://docs.djangoproject.com/
3. **Check existing issues**: https://github.com/atomsharan/GiftStore/issues
4. **Create a new issue** with details about your problem

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Atom Sharan** - [GitHub](https://github.com/atomsharan)

---

## 🎯 Roadmap

- [ ] Payment Gateway Integration (Stripe/PayPal)
- [ ] Email Notifications
- [ ] Product Reviews and Ratings
- [ ] Wishlist Feature
- [ ] Advanced Search and Filters
- [ ] Order Tracking with Email Updates
- [ ] Mobile App
- [ ] Automated Tests
- [ ] API Documentation (REST/GraphQL)
- [ ] Admin Analytics Dashboard

---

<div align="center">

**Made with ❤️ for gift lovers everywhere**

[⬆ Back to Top](#-giftstore---your-ultimate-gift-shopping-platform)

</div>
