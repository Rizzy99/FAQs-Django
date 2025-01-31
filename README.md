<<<<<<< HEAD
# FAQs-Django
=======
# Django Multilingual FAQ API
This project provides a multilingual FAQ system using Django, CKEditor, and Redis.

## Installation
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## API Usage
- `GET /api/faqs/` → Fetch FAQs in English
- `GET /api/faqs/?lang=hi` → Fetch FAQs in Hindi
- `GET /api/faqs/?lang=bn` → Fetch FAQs in Bengali

>>>>>>> b35a728 (feat: Add multilingual FAQ model)
