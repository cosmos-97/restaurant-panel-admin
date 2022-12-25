#! /usr/bin/env bash

# Let the DB start
PYTHONPATH=. python /project/app/backend_pre_start.py

# Run migrations
PYTHONPATH=. alembic upgrade head

# Create initial data in DB
PYTHONPATH=. python /project/app/initial_data.py

uvicorn app.main:app --host 0.0.0.0 --port 5500