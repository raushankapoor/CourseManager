from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('getcourses', views.get_courses),
  path('addcourse', views.add_course),
  path('deletecourse/<int:course_id>', views.delete_course),
  path('getwishlist',views.get_wishlist),
  path('addwishlist',views.add_wishlist),
  path('deletewishlist/<int:wishlist_id>',views.delete_wishlist)
]