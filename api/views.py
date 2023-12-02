from django.http import HttpResponse, JsonResponse
from .tasks import test_func

# Create your views here.

def test(request):
    segundos = request.GET.get('segundos', None)
    segundos = int(segundos)
    test_func.apply_async(args=[segundos], countdown=segundos)
    return HttpResponse("Done")

