from django.urls import path
from post_blog import views

urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('createpost', views.createpost,name='createpost'),
    path('editpost/<int:post_pk>',views.editpost,name='editpost'),
    path('deletepost/<int:post_pk>',views.deletepost,name='deletepost'),
    path('post_detail/<int:post_pk>', views.post_detail, name="post_detail"),
    path('post_list/categories/<int:categories_pk>', views.categories, name="post_list"),
    path('post_detail/feedback/<int:post_pk>', views.feedback, name='feedback'),    

]
