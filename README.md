# How to Setup a Django Application and Deploy Using Docker

### How to run using docker-compose:

1. From parent directory run `docker-compose build` 

2. `docker-compose up` to run in current terminal or `docker-compose up -d` to run in the background

3. If there are changes, rebuild with step 1

### Inspecting containers:

Run `docker exec -it django-app /bin/bash` (when the container is running) or `docker run -it django-app /bin/bash` (when the container is stopped). Python code is stored at `/app`

--------------------------------------------

### How to run without Docker:
#### Windows:
Requirements: 
  - python > 3.7
  - pip

1. Create a virtual environment & install requirements.txt
```python
python3 -m venv ~/venv/django-docker
source ~/venv/django-docker/Scripts/activate
pip install -r requirements.txt
```
(*Note: depends on the python version, you may want to use `source ~/venv/django-docker/bin/activate` instead)

     
2. `cd mysite` and run `python manage.py runserver`
(*Note: this is a very simple application. Add '/1' to the server path to view the functionality.)
