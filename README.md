

# Restaurant API

A simple API to manage a restaurant's menu and bookings.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python and Pip installed on your local development machine.

### Installing

Clone the repository:

```
git clone https://github.com/TheodoreRed/LittleLemon.git
```

Change into the project directory:

```bash
cd [Your Project Folder]
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the development server:

```bash
python manage.py runserver
```

You should now be able to access the API via your browser or Postman/Insomnia at `http://127.0.0.1:8000/`.

## API Endpoints

### 1. Menu Items
#### i. List and Create Menu Items
- **Endpoint:** `/restaurant/menu/`
- **Method:** 
    - `GET`: Retrieve a list of all menu items.
    - `POST`: Create a new menu item.

#### ii. Retrieve, Update, and Delete a Single Menu Item
- **Endpoint:** `/restaurant/menu/<int:pk>`
- **Method:** 
    - `GET`: Retrieve details of a menu item.
    - `PUT` & `PATCH`: Update details of a menu item.
    - `DELETE`: Delete a menu item.

### 2. Tables/Bookings
#### i. List and Create Bookings
- **Endpoint:** `/restaurant/tables/`
- **Method:** 
    - `GET`: Retrieve a list of all bookings.
    - `POST`: Create a new booking.

#### ii. Retrieve, Update, and Delete a Single Booking
- **Endpoint:** `/restaurant/tables/<int:pk>`
- **Method:** 
    - `GET`: Retrieve details of a booking.
    - `PUT` & `PATCH`: Update details of a booking.
    - `DELETE`: Delete a booking.

### 3. Authentication
#### i. Obtain Auth Token
- **Endpoint:** `/auth/token/login/`
- **Method:** `POST`
- **Note:** Use this endpoint to obtain the authentication token by providing the `username` and `password`.

### 4. Authentication and User Management (Using Djoser)
- **Endpoints:** Various, under `/auth/`
- **Method:** Vary per endpoint

#### i. User Registration
- **Endpoint:** `/auth/users/`
- **Method:** `POST`
- **Description:** Register a new user.
```
  {
    "username": "newuser",
    "password": "securepassword123",
    "email": "user@example.com"
}
```


#### ii. User Login (Obtain Auth Token)
- **Endpoint:** `/auth/token/login/`
- **Method:** `POST`
- **Description:** Obtain an authentication token by providing `username` and `password`.

#### iii. User Logout (Delete Auth Token)
- **Endpoint:** `/auth/token/logout/`
- **Method:** `POST`
- **Description:** Logout the user and delete the authentication token.

#### iv. User Password Change
- **Endpoint:** `/auth/users/set_password/`
- **Method:** `POST`
- **Description:** Allow authenticated users to change their password.

#### v. User Password Reset
- **Endpoint:** `/auth/users/reset_password/`
- **Method:** `POST`
- **Description:** Reset the user password by sending them an email with a reset link.

#### vi. User Details
- **Endpoint:** `/auth/users/me/`
- **Method:** `GET`, `PUT`, `PATCH`
- **Description:** Retrieve, update, and manage the authenticated user's data.




## Built With

- Django
- Django Rest Framework

