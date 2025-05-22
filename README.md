# Remind-Me-Later 🕒
A simple and responsive Django + Tailwind CSS web app that lets users schedule reminders by date, time, and message, with options to receive them via email or SMS. Built with a clean UI, fetch-based API, and mobile-friendly layout.

---

## 📌 Features

- 📅 Set reminders with date and time
- 💬 Add a custom message
- ✉️ Choose delivery method: Email or SMS
- 💻 Responsive design using Tailwind CSS
- 🧠 Backend powered by Django
- 🌐 Frontend uses vanilla JS for form submission via Fetch API
- ✅ Displays success or error messages dynamically

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, Tailwind CSS, JavaScript (Fetch API)
- **Styling**: Tailwind CDN
- **Database**: SQLite (default with Django)
- **API**: Simple Django view accepting JSON POST requests

---

## 📁 Project Structure

REMIND_ME_LATER/
├── node_modules/
├── remind_me_later/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── reminders/
│   ├── __pycache__/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
├── templates/
│   └── index.html
├── venv/
├── db.sqlite3
├── manage.py
├── package-lock.json
├── package.json
└── README.md


---

## 🚀 Getting Started

### 1. Clone the repository

git clone https://github.com/Monicakhinchi/Remind-Me-Later.git
cd remind-me-later


2. Set up virtual environment (optional but recommended)

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3. Install dependencies

pip install django

4. Run migrations

python manage.py makemigrations
python manage.py migrate

5. Start the development server

python manage.py runserver


Then open your browser and go to:
http://127.0.0.1:8000/

🔄 API Endpoint
POST /api/reminders/
Accepts JSON data with:

{
  "date": "YYYY-MM-DD",
  "time": "HH:MM",
  "message": "Reminder text",
  "reminder_type": "email" | "sms"
}


📱 Responsive Design
This project uses Tailwind CSS with max-w-md, w-full, and sm: breakpoints to ensure full mobile responsiveness. Works across phones, tablets, and desktops.



✅ To Do / Future Improvements

✅ Add backend logic to actually send email or SMS

⏰ Add periodic background tasks with Celery or Django Q

🔐 Add user login and reminder history

📦 Docker support

📲 PWA or mobile notification support


🙋‍♂️ Author
Monica Khinchi
Made with ❤️ using Django and Tailwind.
