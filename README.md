# A HackerNews clone in Django

##Instructions to run this

- Install postgres, create db `newsdb`:   
      `sudo su - postgres`   
      `createdb -d newsdb -U admin`   
      `ctrl + D`   
- `git clone git@github.com:dbajpeyi/hackernews-clone.git`
- `cd hackernews-clone && pip install -r requirements.txt`
- `bower install`
- `cd project && python manage.py collectstatic`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`- This might fail, need to define a `user.py` file for postgres uname and password can't be on github
- - Go to `localhost:8000/register/`
- Register yourself, login and try it out!!

##CELERY
    
- `celery multi start w1 -A settings -l info` to start celery daemon
- `celery -A settings beat` 
-  Go to settings.py to change the schedule under CELERY_BEAT_SCHEDULER






[Issues/Todo](https://github.com/dbajpeyi/hackernews-clone/issues)

