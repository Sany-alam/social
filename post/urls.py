from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.post,name="post"),
    path('<int:post_id>',views.single_post,name="single_post"),
    path('create',views.cpost,name="cpost"),
    path('comment/add',views.addcomment,name="addcomment"),
    path('comment/<int:id>',views.comments,name="comments"),
]
