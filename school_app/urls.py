from django.urls import path, re_path
from school_app import views

# Template URL's: Template notation can only be done if this is set
app_name = 'school_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name="list"),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name="detail"),
    # re_path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name="detail"),
]
