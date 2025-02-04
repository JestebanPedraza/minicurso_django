from django.urls import path
from .views import CreateClientView, UpdateClientView, DeleteClientView, ListClientView, logout_view

app_name = "crud"

urlpatterns = [
    path('clients/create/', CreateClientView.as_view(), name='create_client'),
    path('clients/update/<int:pk>',
         UpdateClientView.as_view(), name='update_client'),
    path('clients/delete/<int:pk>',
         DeleteClientView.as_view(), name='delete_client'),
    path('clients/', ListClientView.as_view(), name='list_client'),
    path('logout/', logout_view, name='logout'),

]
