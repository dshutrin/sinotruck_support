from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('login', login_view),
    path('logout', logout_view),
    path('users/update_task', update_user_task),
    path('edit_me', edit_me),

    path('my_trash', trash),
    path('add_to_trash/<int:pid>', add_product_to_trash),
    path('remove_from_trash/<int:pid>', remove_from_trash_by_pid),
    path('remove_from_trash', remove_from_trash),
    path('add_order', add_order),

    path('orders', main_orders),
    path('orders/<int:order_id>', order_detail),
    path('orders/my', my_orders),
    path('orders/my/<int:order_id>', my_order_detail),

    path('contacts', contacts),

    path('managers', managers),
    path('managers/add', add_manager),

    path('dealers', dealer),
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
    path('folders/<int:fid>/delete', delete_folder),

    path('folders/<int:folder_id>/add_folder', add_folder_to_folder),
    path('folders/<int:folder_id>/add_file', add_file_to_folder),

    path('users/<int:user_id>', get_user_details),
    path('users/<int:user_id>/delete', delete_user),
    path('edituser/<int:user_id>', edit_user),
    path('user_history/<int:user_id>', user_history),

    path('chat/<int:user_id>', get_chat),
    path('chat/messages/add', add_message),
    path('chat/<int:uid>/send_file', send_file_message),

    path('activity', activity),
    path('activity/stats', activity_stats),
    path('activity/load', load_activity),
    path('load_activity', load_activity_file)
]
