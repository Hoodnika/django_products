from django.urls import path

from version_app.apps import VersionAppConfig
from version_app.views import VersionListView, VersionCreateView, VersionDetailView, VersionUpdateView, VersionDeleteView
from version_app.views import control

app_name = VersionAppConfig.name

urlpatterns = [
    path('control/', VersionListView.as_view(), name='version_list'),
    path('control/create/', VersionCreateView.as_view(), name='version_create'),
    path('control/version_detail/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
    path('control/version_update/<int:pk>/', VersionUpdateView.as_view(), name='version_update'),
    path('control/version_delete/<int:pk>/', VersionDeleteView.as_view(), name='version_delete'),
    path('future_control/', control, name='version_app_list'),
]
