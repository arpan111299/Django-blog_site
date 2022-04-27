from django.urls import path


from customadmin.views import *

urlpatterns= [
    path('customadmin/', LoginAdminView.as_view(), name="customadmin"),
]