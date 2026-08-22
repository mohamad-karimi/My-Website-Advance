from .tasks import send_email_task
from django.http import HttpResponse, JsonResponse
import requests
from django.views.decorators.cache import cache_page

# Create your views here.
def send_email(request):
    send_email_task.delay()
    return HttpResponse("<h1>sending done</h1>")

@cache_page(60)
def test_delay(request):
    response = requests.get("https://443f204a-2244-4831-87c3-42dd7251889e.mock.pstmn.io/blog/api/v1/post/")
    return JsonResponse(response.json())
