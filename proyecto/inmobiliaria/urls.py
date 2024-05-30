from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('terrenos',views.terrenos, name='terrenos'),
    path('terrenos/agregar',views.agregar, name='agregar'),
    path('terrenos/editar',views.editar, name='editar'),
    path('borrar/<int:id>',views.borrar, name='borrar'),
    path('terrenos/editar/<int:id>',views.editar, name='editar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)