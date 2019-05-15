from django.urls import include, path

from . import views
from .views import CompanyListView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'company', CompanyListView)

urlpatterns = [
    path('', views.UserListView.as_view()),
]

urlpatterns += router.urls