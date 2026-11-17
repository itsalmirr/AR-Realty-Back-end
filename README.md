# AR Realty API

Django REST API behind the AR Realty website: property listings, realtors, inquiries and user accounts, plus an admin panel where staff manage them.

**Stack:** Python 3.11 · Django 4.2 · Django REST Framework · Simple JWT · PostgreSQL · Cloudinary · Gunicorn

## Features

- Published listings with up to six photos each, stored on Cloudinary and served six per page.
- Quick search by address, city, state (name or abbreviation), ZIP code or title, and three random picks for a "more listings" section that exclude the listing being viewed.
- JWT authentication with Simple JWT: registration with a profanity filter, and read, update and delete for the signed-in user's profile.
- Listing inquiries for signed-in users, each visible only to the user who sent it, and public business inquiries.
- Django admin with the JET theme for listings, realtors, inquiries and users; generated API docs at `/docs/` and an OpenAPI schema at `/openapi`.

## API

| Method | Path | Auth | Description |
|---|---|---|---|
| POST | `/api/token/`, `/api/token/refresh/` | | Obtain or refresh a JWT pair |
| POST | `/api/user/register/` | | Register |
| GET, PUT, DELETE | `/api/user/me/` | JWT | The signed-in user's profile |
| GET | `/api/listings/` | | Published listings, six per page |
| GET | `/api/listings/quicksearch/?q=` | | Search listings |
| GET | `/api/listings/random/?slug=` | | Three random listings other than `slug` |
| GET | `/api/listings/<slug>/` | | One listing |
| GET | `/api/realtors/` | | Realtors |
| GET | `/api/realtor/info/<slug>/`, `/api/realtor/listings/<slug>/` | | A realtor and their listings |
| GET | `/api/inquiries/` | JWT | Your inquiries |
| POST | `/api/inquiries/create` | JWT | Ask about a listing |
| DELETE | `/api/inquiries/<listing-id>/` | JWT | Withdraw an inquiry |
| POST | `/api/contact/business-inquiries/` | | Business inquiry |

## Run locally

You need PostgreSQL and a Cloudinary account.

```sh
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # SECRET_KEY, DB_*, CLOUDINARY_* and the rest
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The admin panel is at `/admin/`.

## Screenshots

Admin panel:

<img src="https://res.cloudinary.com/iamalmiir/image/upload/v1669624330/django_admin_panel1_et7wom.png" alt="AR Realty admin panel" />
<img src="https://res.cloudinary.com/iamalmiir/image/upload/v1669624442/django_admin_panel2_duuzsq.png" alt="AR Realty admin panel" />

## Layout

```
backend/    settings, URLs, WSGI and ASGI entry points
listings/   listing model, search, pagination
realtors/   realtor model and endpoints
contacts/   listing and business inquiries
users/      custom user model, registration, profanity filter
```
