from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('promts/<int:promt_id>', promt_detail, name='promt_detail')
]