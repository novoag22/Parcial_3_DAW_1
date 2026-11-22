
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # INCLUIR LAS RUTAS HIJAS
    path('profiles/', include("myapp.urls")),
    path('', include("myapp.urls")),
]
