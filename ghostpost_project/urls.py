"""ghostpost_project URL Configuration

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
from django.urls import path
from ghostpost_app import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('upvote/<int:upvote_id>', views.upvotes_view, name="upvote_page"),
    path('downvote/<int:downvote_id>', views.downvotes_view, name="downvote_page"),
    path('boasts/', views.boasts_view, name="boasts_page"),
    path('roasts/', views.roasts_view, name="roasts_page"),
    path('sortvotes/', views.sort_view, name="sortvotes_page"),
    path('createpost/', views.createpost_view, name="createpost_page"),
    # path('deletepost/<int:post_id>', views.deletepost_view, name="deletepost_page"),
    path('admin/', admin.site.urls),
]
