"""
URL configuration for lost_and_found project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from items import views
from items.views import claim_lost_item, claim_found_item, my_claims, approve_claim

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("admin-items/", views.admin_items_list, name="admin_items_list"),
    path("admin-items/delete-lost/<int:item_id>/", views.delete_lost_item, name="delete_lost_item"),
    path("admin-items/delete-found/<int:item_id>/", views.delete_found_item, name="delete_found_item"),
    path("lost/", views.lost_items_list, name="lost_items_list"),
    path("found/", views.found_items_list, name="found_items_list"),
    path("lost/add/", views.add_lost_item, name="add_lost_item"),
    path("found/add/", views.add_found_item, name="add_found_item"),
    path("claim/lost/<int:item_id>/", views.claim_lost_item, name="claim_lost_item"),
    path("claim/found/<int:item_id>/", views.claim_found_item, name="claim_found_item"),


]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
