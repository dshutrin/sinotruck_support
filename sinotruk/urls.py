from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('login', login_view),
    path('logout', logout_view),

    path('managers', managers),
    path('managers/add', add_manager),

    path('dealers', dealers),
    path('dealers/add', add_dealer),

    path('clients', clients),
    path('pricelist', pricelist),

    path('files', files),
    path('files/<int:doc_id>', get_document),
    path('files/add', add_file),

    path('users/<int:user_id>', get_user_details),
    path('users/<int:user_id>/delete', delete_user),

    path('activity', activity),
]
