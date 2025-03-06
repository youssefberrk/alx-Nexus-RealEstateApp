# Django Real Estate Application

This is a Django-based Real Estate Application. The project is structured with multiple apps to handle different functionalities of the application.

## Project Structure

- `api/`: Contains the main Django project settings and configurations.
- `application/`: Handles the application-related functionalities.
- `property/`: Manages property-related data and operations.
- `users/`: Manages user-related data and operations.

## Getting Started

### Prerequisites

- Python 3.x
- Django 5.1.6
- PostgreSQL (for production)
- SQLite (for development)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/real-estate-app.git
    cd real-estate-app/server
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:

    Create a `.env` file in the  directory and add the following variables:

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=your_db_port
    ```

### Database Setup

1. Apply the migrations:

    ```sh
    python manage.py migrate
    ```

2. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

### Running the Server

Start the development server:

```sh
python manage.py runserver
```

### API Endpoints

The API endpoints are defined in the respective apps. You can access the admin panel at /admin.

## Applications
- Users
=> Manages user authentication and profiles.

- Property
=> Handles property listings and related data.

- Application
=> Manages applications for properties.

## API routes

The API routes are documented using Swagger. You can access the Swagger documentation at `/swagger/`.

### Creating a User

To create a superuser, run the following command:

```sh
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password for the superuser.

### Example API Routes

Here are some example(not really accurate) API routes with `curl` but dont' forget to add authentication (bearer Token) on the header as well
commands:

#### Create a User

```sh
curl -X POST "http://localhost:8000/users/" -H "Content-Type: application/json" -d '{
  "username": "newuser",
  "password": "password123",
  "email": "newuser@example.com"
}'
```


#### List Properties

```sh
curl -X GET "http://localhost:8000/properties/" -H "Accept: application/json"
```

#### Apply for a Property

```sh
curl -X POST "http://localhost:8000/applications/" -H "Content-Type: application/json" -d '{
  "property_id": 1,
  "user_id": 1,
  "application_date": "2025-03-06"
}'
```

You can find more detailed information about the API endpoints and their usage in the Swagger documentation.
