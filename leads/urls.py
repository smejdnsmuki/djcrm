from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    # path('', views.lead_list, name='lead-list'),
    path('', views.LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', views.LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', views.AssignAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/category/', views.LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('create/', views.LeadCreateView.as_view(), name='lead-create'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
]