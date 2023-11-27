from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticlesDetailView.as_view(), name='article-details'),
    path('add_post/', views.AddPostView.as_view(), name='add-post'),
    path('article/<int:pk>/comment/', views.AddCommentView.as_view(), name='add-comment'),
    path('add_category/', views.AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', views.DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='category-list'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
]
