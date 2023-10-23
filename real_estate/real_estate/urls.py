
from django.contrib import admin
from django.urls import path
from listing.views import real_estate_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',real_estate_list)
]
