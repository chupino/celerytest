from celery import shared_task

@shared_task(bind=True)
def test_func(self,segundos):
    return f"Tarea realizada despues de: {segundos} segundos"