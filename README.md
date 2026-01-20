# Amazon Product Availability Checker 🛒

This Python project tracks the availability of an Amazon product using its ASIN ID and sends an email notification when the product becomes available.

## 🔧 Technologies Used
- Python
- Web Scraping
- Email Automation
- Task Scheduling

## 📦 Modules Used

| Module | Purpose |
|------|--------|
| requests | Send HTTP requests to Amazon |
| lxml | Parse HTML content |
| time | Delay execution |
| schedule | Run script at intervals |
| smtplib | Send email notifications |

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository.

### 2️⃣ Install Dependencies:
pip install -r requirements.txt

### 3️⃣ Configure Email Credentials
Edit main.py and update:
GMAIL_USERNAME = "your_email@gmail.com"
GMAIL_PASSWORD = "your_app_password"
receiver_email_id = "receiver_email@gmail.com"
## 🔐 Use Gmail App Password instead of your real password

### 4️⃣ Set Amazon ASIN
ASIN = "YOUR_PRODUCT_ASIN"

### 5️⃣ Run the Script
python main.py

---

## ⏰ How It Works
- Script runs every 1 minute.
- Checks Amazon product availability.
- Sends email only if product is in stock.

---

## 🖼 Screenshot
![Application Screenshot]()
