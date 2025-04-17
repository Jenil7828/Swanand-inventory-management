# 📦 Swanand Inventory Management System

The **Swanand Inventory Management System** is a Django-based web application designed to manage inventory, stock transfers, transaction logs, and more. This system helps businesses maintain real-time stock data and streamline inventory operations.

---

## ✨ Features

- 🗃️ **Inventory Management** — Track company products, quantities, costs, and storage locations.
- 🔁 **Stock Transfers** — Manage stock movement between different branches or locations.
- 🧾 **Transaction Logs** — Filter and review detailed logs of all inventory transactions.
- 📤 **Export Options** — Download records in **CSV**, **Excel**, or **PDF** formats.
- 🌙 **Dark Mode** — Toggle a night-friendly dark theme that remembers your preference.
- 📱 **Responsive UI** — Seamlessly usable on both desktop and mobile devices.

---

## ⚙️ Requirements

- 🐍 Python 3.x
- 🌐 Django 3.x or later
- 🛢️ SQLite (default) or custom DB via Django settings
- 📦 Optional dependencies for export:
  - `pandas` (Excel/CSV)
  - `reportlab` (PDF)

---

## 🚀 Getting Started

### 1. 🔁 Clone the Repository

<pre>
  git clone https://github.com/Jenil7828/Swanand-inventory-management.git
  cd Swanand-inventory-management
</pre>
### 2. 🐍 Create a Virtual Environment
<pre>
  python -m venv venv
</pre>


Activate it:
<pre>
  - **Windows**:
  .\venv\Scripts\activate
  
  - **Mac/Linux**:
  source venv/bin/activate
</pre>

  

### 3. 📦 Install Dependencies
<pre>
  pip install -r requirements.txt
</pre>

### 4. 🛠️ Apply Migrations

<pre>
  python manage.py migrate
</pre> 

### 5. 🔐 Create a Superuser (Optional)

<pre>
  python manage.py createsuperuser
</pre>

### 6. ▶️ Run the Server

<pre>
  python manage.py runserver
</pre>

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Folder Structure
<pre lang="markdown"> 
inventory_management/               # 🌐 Main Django project directory
├── invent/                         # 📦 Django app: 'invent'
│   ├── migrations/                 # 🔄 Database migration files
│   ├── static/                     # 🎨 Static files for frontend
│   │   ├── css/                    # 🎨 CSS styling
│   │   ├── font/                   # 🔤 Fonts used
│   │   └── js/                     # 💡 JavaScript files
│   ├── templates/                 # 🧾 HTML templates
│   │   └── invent/                # 📁 App-specific templates
│   ├── __init__.py                # 📍 Package indicator
│   ├── admin.py                   # 🛠️ Admin interface
│   ├── apps.py                    # ⚙️ App config
│   ├── forms.py                   # 📝 Django forms
│   ├── models.py                  # 🗃️ Data models
│   ├── tests.py                   # ✅ App tests
│   ├── urls.py                    # 🌐 App URL routing
│   └── views.py                   # 👁️ View logic
├── inventory_management/          # ⚙️ Project config/settings
│   ├── __init__.py
│   ├── asgi.py                    # ⚡ ASGI entry point
│   ├── settings.py                # 🔧 Project settings
│   ├── urls.py                    # 🌍 Main URL routing
│   └── wsgi.py                    # 🔌 WSGI entry point
├── staticfiles/                   # 📁 Collected static files (via collectstatic)
├── db.sqlite3                     # 🗄️ Default SQLite DB
├── db_backup.sqlite3             # 🗂️ Backup DB file
├── manage.py                      # 🧰 Django management script
├── README.md                      # 📖 Project documentation
└── requirements.txt               # 📦 Python dependencies
 </pre>
---

## 🧾 Exporting Data

Easily export data using the following:

- 📄 **CSV** — Download logs as `.csv` files
- 📊 **Excel** — Export records to `.xlsx` format
- 📕 **PDF** — Generate professional `.pdf` reports

---

## 🌗 Dark Mode

Toggle between light and dark themes using the 🌙 / ☀️ icon on the interface. Your preference is saved automatically!

---

## 🤝 Contributing

Want to improve this project? Here’s how:

1. Fork this repo 🍴
2. Create a branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to your branch: `git push origin feature-branch`
5. Create a pull request 📬

---

## 🧠 Tips

- Use the **Django Admin Panel** to view and manage data at `/admin`
- Make sure to **collect static files** if deploying
- Use the dark mode toggle for better nighttime viewing

---



> Made with 💡 by [Jenil Rathod](https://github.com/Jenil7828)
