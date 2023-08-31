# NoFluffTutoring

A website for tutors and students. Allows you to place adverts, make appointments etc.

## Tech stack

### Backend

- Python

- Django / Django REST Framework

- Pytest

- PostgreSQL

- Docker

More in `backend/requirements.txt`

### Frontend

- JavaScript

- TypeScript

- React

- Vite

- TailwindCSS

## Requirements

You need to install:

- docker
- docker compose

Check that everything is working:

`docker -v`

`docker compose -v`

## Running the project

### Backend

1. Clone the repository:

    `git clone https://github.com/TenSzalik/e-tutoring-site`

2. Navigate to the `backend` directory

3. Run the project using Docker Compose:

    `docker compose up --build`

4. Run migrations:

    `docker compose run django python manage.py migrate`


5. Create super-user:

    `docker compose run django python manage.py createsuperuser`

6. Open a web browser and go to `http://0.0.0.0:8000/admin` to login

7. You can see the endpoints here:

    `http://0.0.0.0:8000/api/`

    `http://0.0.0.0:8000/api/schema/swagger/`

    `http://0.0.0.0:8000/api/schema/redoc/`


### Useful commands

- Run pytest

    `docker exec -it <container_name> pytest`

### Frontend

1. Move to `frontend/` directory

2. Install node

    `npm install`

3. Run server

    `npm run dev`
