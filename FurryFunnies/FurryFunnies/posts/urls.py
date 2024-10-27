from django.urls import path,include

from FurryFunnies.posts import views
from FurryFunnies.posts.views import CreatePostView,DetailPostView,EditPostView,DeletePostView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create post'),
    path('<int:post_id>/', include([
        path('details/', DetailPostView.as_view(), name = 'post details'),
        path('edit/', EditPostView.as_view(), name= 'edit post'),
        path('delete/', DeletePostView.as_view(), name = 'delete post'),
    ]))
]