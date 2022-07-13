from django.urls import path, include


from dolphin import views

urlpatterns = [path("log/", views.add_log, name="add_log")]
