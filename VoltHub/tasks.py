from celery import shared_task

@shared_task
def add(x, y):
    """A simple task that adds two numbers."""
    return x + y