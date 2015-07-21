# A HackerNews clone in Django

##Instructions to run this
- `git clone git@github.com:dbajpeyi/hackernews-clone.git`
- `cd hackernews-clone && pip install -r requirements.txt`
- `bower install`
- `cd project && python manage.py collectstatic`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`
-  Run scraper `python manage.py crawl_site` )

- Go to `localhost:8000/register/`
- Register yourself, login and try it out!!
-

##Todos :
- Move management command to celery tasks (?)
- Write unittests

