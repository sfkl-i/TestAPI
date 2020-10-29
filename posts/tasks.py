from celery.task.schedules import crontab
from celery.task import periodic_task
import os
from .models import Post


@periodic_task(run_every=crontab(minute=0, hour=0))
def reset_upvotes():
    for q in Post.objects.all():
        q.amount_of_upvotes = 0
        q.save()
