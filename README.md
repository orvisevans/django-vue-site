# django-vue-site

An exercise in combining a Django backend with a Vue frontend, focusing in functionality.

The backend and frontend are served from separate servers. The Vue site communicates with the Django backend via a RESTful API.

## Dependencies

- Node 14+
- Yarn
- Python 3
- Pyenv
- Poetry

## Start the Backend (Django) Server:

```bash
cd backend
poetry install
poetry shell
python manage.py runserver
```

## Start the Frontend (Vue) Server:

```bash
cd frontend
yarn install
yarn serve
```
