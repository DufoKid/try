from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("catalogue_ms/", views.catalogue_ms, name="catalogue_ms"), #routing,function name dlm views.py
    path('newmentor',views.newmentor,name='newmentor'),
    path('newstudent', views.newstudent, name='newstudent'), 
    path('updatementor/<str:mentor_id>/',views.updatementor,name='updatementor'),
    path('updatementor/updatedatamentor/<str:mentor_id>/', views.updatedatamentor, name='updatedatamentor'),
    path('updatestudent/<str:student_id>/', views.updatestudent, name='updatestudent'),
    path('updatestudent/updatedatastudent/<str:student_id>/', views.updatedatastudent, name='updatedatastudent'),
    path('deletementor/<str:mentor_id>/', views.deletementor, name='deletementor'),
    path('deletementor/deletedatamentor/<str:mentor_id>/', views.deletedatamentor, name='deletedatamentor'),
]
