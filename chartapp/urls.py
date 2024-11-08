from django.urls import path
from .views import login_view, chart_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('chart/', chart_view, name='chart'),
    path('api/chart-data/', chart_data_api, name='chart_data_api')

]
