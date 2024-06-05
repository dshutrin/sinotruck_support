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
    path('clients/add', add_client),

    path('pricelist', pricelist),
    path('add_pricelist', add_pricelist),

    path('files', files),
    path('files/<int:doc_id>', get_document),
    path('files/add', add_file),

    path('folders/add', add_folder),
    path('folders/<int:fid>', folder_detail),

    path('users/<int:user_id>', get_user_details),
    path('users/<int:user_id>/delete', delete_user),
    path('edituser/<int:user_id>', edit_user),
    path('user_history/<int:user_id>', user_history),

    path('chat/<int:user_id>', get_chat),
    path('chat/messages/add', add_message),
    path('chat/<int:uid>/send_file', send_file_message),

    path('activity', activity),
    path('activity/load', load_activity),
    path('load_activity', load_activity_file)
]
