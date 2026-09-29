# Little Lemon - Back-End Capstone Project

A robust back-end application for the **Little Lemon** restaurant built using **Django**, **Django REST Framework (DRF)**, and **MySQL**. This project features user authentication via Djoser, token-based security, a menu management API, and a table booking system.

---

## Prerequisites & Setup

1. **Clone the Repository & Navigate to Project Directory:**
```bash
git clone https://github.com/shehab-hub-0/LittleLemon.git
cd LittleLemon-main

```


2. **Create and Activate a Virtual Environment:**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```


3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure Database:**
* Create a MySQL database named `LittleLemon` (MySQL 8.0+).
* Update `littleLemon/settings.py` with your local MySQL `USER` and `PASSWORD`.


5. **Run Migrations & Create Superuser:**
```bash
python manage.py migrate
python manage.py createsuperuser

```


6. **Run the Development Server:**
```bash
python manage.py runserver

```


7. **Run Unit Tests:**
```bash
python manage.py test

```



---

## Endpoints Reference

### 🌐 Static Pages & Admin

* **Home Page:** `GET [http://127.0.0.1:8000/restaurant/](http://127.0.0.1:8000/restaurant/)`
* **Django Admin:** `[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)`

### 🔒 Authentication (Djoser + Token)

All protected endpoints require the following header:

```http
Authorization: Token <your_token>

```

* **Register User:** `POST [http://127.0.0.1:8000/auth/users/](http://127.0.0.1:8000/auth/users/)` *(Body: username, password)*
* **Login (Get Token):** `POST [http://127.0.0.1:8000/auth/token/login/](http://127.0.0.1:8000/auth/token/login/)` *(Body: username, password)*
* **Logout:** `POST [http://127.0.0.1:8000/auth/token/logout/](http://127.0.0.1:8000/auth/token/logout/)` *(Header: Authorization)*
* **Alternative Token Auth:** `POST [http://127.0.0.1:8000/restaurant/api-token-auth/](http://127.0.0.1:8000/restaurant/api-token-auth/)` *(Body: username, password)*
* **Protected Message View:** `GET [http://127.0.0.1:8000/restaurant/message/](http://127.0.0.1:8000/restaurant/message/)` *(Requires Token)*

### 🍽️ Menu API

* **List / Create Menu Items:**
* `GET [http://127.0.0.1:8000/restaurant/menu/items/](http://127.0.0.1:8000/restaurant/menu/items/)`
* `POST [http://127.0.0.1:8000/restaurant/menu/items/](http://127.0.0.1:8000/restaurant/menu/items/)` *(JSON Body: title, price, inventory)*


* **Retrieve / Update / Delete Item:**
* `GET / PUT / DELETE [http://127.0.0.1:8000/restaurant/menu/items/](http://127.0.0.1:8000/restaurant/menu/items/)<id>` *(Note: No trailing slash)*



### 📅 Table Booking API

* **List / Create Bookings:**
* `GET / POST [http://127.0.0.1:8000/restaurant/booking/tables/](http://127.0.0.1:8000/restaurant/booking/tables/)` *(JSON Body: name, no_of_guests, booking_date e.g., 2026-10-05T20:00:00)*


* **Retrieve / Update / Delete Booking:**
* `GET / PUT / DELETE [http://127.0.0.1:8000/restaurant/booking/tables/](http://127.0.0.1:8000/restaurant/booking/tables/)<id>/`