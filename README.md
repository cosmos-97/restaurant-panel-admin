# fastfoo-python-admin

### Terminal commands
Note: Be sure to make a copy of the `.env.example` file called `.env` (`cp .env.example .env`), and then set the variables inside the `.env` file to the desired values.

    Export all env:
        ```
            export $(cat .env | xargs)

        ```

    Install dependencies:
        ```
            curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
            cd /usr/local/bin && \
            ln -s /opt/poetry/bin/poetry && \
            poetry config virtualenvs.create false

        ```
    
    Install library:
        ```
            cd web/
            poetry install

        ```

    To run migration and upgrade database and create SuperUser:
        ```
            cd web/
            PYTHONPATH=. poetry run alembic upgrade head
            PYTHONPATH=. poetry run python app/initial_data.py

        ```

    To run application with gunicorn and sock:
        ```

            cd web/
            poetry run gunicorn app.main:app --workers 4  --worker-class uvicorn.workers.UvicornWorker --bind unix:gunicorn.sock

        ```

    To run application with gunicorn and port:
        ```

            cd web/
            poetry run gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000

        ```

    To run application with uvicorn and port:
        ```

            cd web/
            poetry run uvicorn --host 0.0.0.0 --port 5000 --reload app.main:app 

        ```