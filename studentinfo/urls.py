from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add'),
    path('edit-student/', views.edit_student, name='edit'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)