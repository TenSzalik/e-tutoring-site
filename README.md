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

## Requirements

You need to install:

- Docker
- Docker Compose
- Postgres

Check that everything is working:

```sh
docker -v
```

```sh
docker-compose -v
```

```sh
psql --version
```

## Running the project

1. Clone the repository:

    ```sh
    git clone https://github.com/TenSzalik/e-tutoring-site
    ```

2. Navigate to the project directory:

    ```sh
    cd backend
    ```

3. Run the project using Docker Compose:

    ```sh
    docker-compose up --build
    ```

4. Run migrations:


    ```sh
    docker-compose run django python manage.py migrate
    ```


5. Create super-user:


    ```sh
    docker-compose run django python manage.py createsuperuser
    ```


6. Open a web browser and go to `http://0.0.0.0:8000/admin` to login

7. You can see the endpoints here:

    `http://0.0.0.0:8000/api/`

    `http://0.0.0.0:8000/api/schema/swagger/`

    `http://0.0.0.0:8000/api/schema/redoc/`


## Useful commands

- To stop the docker use the keyboard shortcut `Ctrl + C`


- Start again:

    ```sh
    docker-compose up
    ```

- Remove all containers:

    ```sh
    docker-compose down
    ```

- Check active containers:

    ```sh
    docker ps
    ```

- To completely remove the project, execute the following command:

    ```sh
    docker-compose down -v
    ```

    This command will remove the containers, network, and delete all data from Postgres.
