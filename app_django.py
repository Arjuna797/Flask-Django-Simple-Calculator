import os
from django.conf import settings
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.urls import path

BASE_DIR = os.path.dirname(__file__)

# Django minimal inline configuration
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    STATIC_URL='/static/',
    STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')],
)

def index(request):
    with open(os.path.join(BASE_DIR, 'templates', 'index.html')) as f:
        return HttpResponse(f.read())

urlpatterns = [
    path('', index),
]

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    print("🚀 Running Django Calculator on http://localhost:8081")
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8081"])
