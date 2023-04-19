# How to Setup a Django Application and Deploy Using Docker

### How to run using docker-compose:


### How to run without Docker:
#### Windows:
Requirements: 
  - python > 3.7
  - pip

1.
```python
python3 -m venv ~/venv/django-docker
source ~/venv/django-docker/Scripts/activate
pip install -r requirements.txt
```
(*Note: depends on the python version, you may want to use `source ~/venv/django-docker/bin/activate` instead)

     
2. `cd mysite` and Run `python manage.py runserver`
(*Note: this is a very simple application. Add '/1' to the server path to view the functionality.)
