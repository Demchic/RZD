from django.urls import path
from . import views

urlpatterns = [
    path('', views.applications_home, name='applications_home'),
    path('create', views.ArticlesCreateView.as_view(), name='create'),
    path('<int:pk>/delete', views.AplliDeleteView.as_view(), name='appli-delete'),
    path('<int:pk>', views.AplliDetailView.as_view(), name='appli-detail'),
    path('<int:pk>/export', views.export_to_docx, name='appli-export'),
    path('<int:pk>/export_excel', views.export_excel, name='appli-export-excel'),
]
