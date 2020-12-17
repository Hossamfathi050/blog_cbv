from django.urls import path

from . import views

app_name='post'


urlpatterns = [

    path('cbv', views.PostList.as_view(),name='post_list_cbv'),

    path('cbv/<int:pk>',views.PostDetail.as_view(),name='post_details_cbv'),

    path('cbv/<int:pk>/edit',views.PostUpdate.as_view(),name='post_update_cbv'),



]
