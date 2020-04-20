from django.urls import path
from .api_views import CooperativeApiView, CategoriesApiView
from .views import CooperativeListView, CooperativeDetailView

urlpatterns = [
    path('list/', CooperativeListView.as_view(), name='cooperatives_list'),
    path('details/<int:pk>/', CooperativeDetailView.as_view(), name='details'),
    path('api/v2/cooperatives/', CooperativeApiView.as_view(),
         name="cooperatives"),
    path('api/v2/categories/', CategoriesApiView.as_view(), name="categories")
]
