from django.urls import path
from .views import (
    home,
    post_list,
    post_detail,
    post_api,
    post_api_detail,
)

urlpatterns = [
    path('', home),
    path('posts/', post_list),
    path('posts/<int:id>/', post_detail),

    # API endpoints
    path('api/posts/', post_api),
    path('api/posts/<int:id>/', post_api_detail),
]