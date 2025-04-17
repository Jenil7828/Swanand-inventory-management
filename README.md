# Swanand Inventory Management System

The **Swanand Inventory Management System** is a web application built with Django for managing inventory, stock transfers, transaction logs, and other related tasks. This system aims to help businesses maintain real-time stock data, perform stock transfers, and track transactions with ease.

## Features

- **Inventory Management**: Manage and track company products, their quantities, costs, and locations.
- **Stock Transfers**: Record and manage stock transfers between different locations.
- **Transaction Logs**: View and filter detailed transaction records for stock entries and transfers.
- **Export Options**: Export transaction logs and stock entries in various formats like CSV, Excel, and PDF.
- **Dark Mode**: A dark mode theme for a better user experience during night-time usage.
- **Responsive Design**: The interface is responsive, making it usable on both desktop and mobile devices.

## Requirements

- Python 3.x
- Django 3.x+
- Database: SQLite (default) or any other database configured in Django settings.
- (Optional) Additional dependencies based on the export functionality (e.g., `pandas` for Excel/CSV export, `reportlab` for PDF export).

## Setup

### 1. Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/Jenil7828/Swanand-inventory-management.git
cd Swanand-inventory-management


### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies:


python -m venv venv

Activate the virtual environment:
- For **Windows**:
    .\venv\Scripts\activate
    
- For **Mac/Linux**:
    source venv/bin/activate

### 3. Install Dependencies
Install all required dependencies using `pip`:

pip install -r requirements.txt


### 4. Apply Migrations
Run migrations to set up the database schema:

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
If you want to access the Django admin interface, create a superuser:

python manage.py createsuperuser

Follow the prompts to create the user.

### 6. Run the Development Server
Start the Django development server:

python manage.py runserver

You can access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Exporting Data
The system provides the ability to export transaction logs and stock entries in multiple formats (CSV, Excel, PDF). You can access the export options from the **Transaction Log** and **Stock Entries** sections.

- **CSV Export**: Click the **📄 CSV** button to download data as CSV.
- **Excel Export**: Click the **📊 Excel** button to download data as Excel.
- **PDF Export**: Click the **📄 PDF** button to download data as a PDF.

## Dark Mode
The application supports **Dark Mode**, which can be toggled by clicking the **🌓** button at the top-right corner. Your theme preference will be saved in local storage and applied on subsequent visits.

## Folder Structure

Here’s the project folder structure:


inventory_management/  # Main Django project directory
├── invent/             # Django application named 'invent'
│   ├── migrations/    # Contains database migration files for the 'invent' app
│   │   └── ...
│   ├── static/        # Static files for the 'invent' app
│   │   ├── css/       # CSS files for the 'invent' app
│   │   │   ├── company_product.css
│   │   │   ├── create_user.css
│   │   │   ├── inventory_status.css
│   │   │   ├── login.css
│   │   │   ├── stock_transfer.css
│   │   │   ├── style.css
│   │   │   └── transaction_log.css
│   │   ├── font/      # Font files for the 'invent' app
│   │   │   └── NotoSansDevanagari-Regular.ttf
│   │   └── js/        # JavaScript files for the 'invent' app
│   │       ├── company_product.js
│   │       ├── create_user.js
│   │       ├── inventory_status.js
│   │       ├── login.js
│   │       ├── script.js
│   │       ├── stock_transfer.js
│   │       └── transaction_log.js
│   ├── templates/     # HTML templates for the 'invent' app
│   │   └── invent/    # Conventionally, templates for an app are in a subdirectory named after the app
│   │       ├── company_product.html
│   │       ├── create_user.html
│   │       ├── index.html
│   │       ├── inventory_pdf.html
│   │       ├── inventory_status.html
│   │       ├── login.html
│   │       ├── stock_entries_pdf.html
│   │       ├── stock_transfer.html
│   │       └── transaction_log.html
│   ├── __init__.py    # Makes the 'invent' directory a Python package
│   ├── admin.py       # Defines admin interface for the 'invent' app models
│   ├── apps.py        # Configuration for the 'invent' app
│   ├── forms.py       # Defines forms used in the 'invent' app
│   ├── models.py      # Defines data models for the 'invent' app
│   ├── tests.py       # Contains tests for the 'invent' app
│   ├── urls.py        # Defines URL patterns for the 'invent' app
│   └── views.py       # Contains view functions for the 'invent' app
├── inventory_management/ # Inner directory with project-level settings
│   ├── __init__.py    # Makes the 'inventory_management' directory a Python package
│   ├── asgi.py        # Asynchronous Server Gateway Interface entry-point
│   ├── settings.py    # Main project settings
│   ├── urls.py        # Project-level URL patterns
│   └── wsgi.py        # Web Server Gateway Interface entry-point
├── staticfiles/       # Directory where collected static files are stored (may be empty in development)
│   └── ... (assuming there are contents within staticfiles)
├── db.sqlite3         # Default SQLite database file
├── db_backup.sqlite3  # A backup of the SQLite database
├── manage.py          # Django management script for various tasks
├── README.md          # Project description and other important information
└── requirements.txt   # Lists the project's Python dependencies

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request to merge changes into the `main` branch.


### Instructions for Use:
- **Run the App**: Follow the setup instructions to install dependencies and run the Django development server locally.
- **Access Features**: You can manage inventory, transfer stock, view transaction logs, and export data as per the instructions above.
- **Theme**: The system also includes a dark mode feature which persists across sessions.

