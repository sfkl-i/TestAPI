# TestAPI
To run project local use:
__pip install -r requirements.txt__
<br>Then configure database settigns in __settings.py__ and do __python manage.py migrate__
<br>And __python manage.py runserver__
<br>To start task with Celery to reset the upvotes every day: __celery -A tasks worker --loglevel=INFO__
<br>If you want to run Redis on Docker execute this:
__docker run -d -p 6379:6379 redis__
