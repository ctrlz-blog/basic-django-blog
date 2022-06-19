from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('posts/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
