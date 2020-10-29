"""foodgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.contrib.flatpages import views

from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", include("django.contrib.flatpages.urls")),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("api/", include('api.urls')),
    path('about-author/', views.flatpage,
         {'url': '/about-author/'}, name='about-author'),
    path('about-spec/', views.flatpage,
         {'url': '/about-spec/'}, name='about-spec'),
    path("", include("recipe.urls")),

]

handler404 = "recipe.views.page_not_found"  # noqa
handler500 = "recipe.views.server_error"  # noqa
