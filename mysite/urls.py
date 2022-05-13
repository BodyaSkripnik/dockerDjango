from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from blog import views

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api/',include('blog.urls')),
    path('firstlist/', views.firstlist),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
