from django.urls import path

from todoapp import views

urlpatterns = [
   path("index",views.index,name="index"),
   path("",views.form,name="form"),
   path("view",views.view,name="view"),
   path('update/<int:id>/',views.update,name="update"),
   path('delete/<int:id>/', views.delete, name="delete")


]