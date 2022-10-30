from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newEntry", views.newEntry, name="newEntry" ),
    path("save", views.save, name="save"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("editPage",views.editPage, name='editPage'),
    path("saveEdit",views.saveEdit, name='saveEdit')
]


