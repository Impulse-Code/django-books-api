from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Books_View.as_view(),name='books'),
    path('<str:pk>',views.Get_Book.as_view(),name='book'),
    # path('',views.book_list,name='book_list'),
    # path('<str:pk>',views.book,name='book'),
    # path('create_book/',views.create_book,name='create_book'),
]
