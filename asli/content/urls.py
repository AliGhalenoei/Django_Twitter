from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.HomePageView.as_view(),name='home'),
    path('detail_twit/<int:pk>/',views.DetailTwitPageView.as_view(),name='detail_twit'),
    # Update Comment..
    path('update_comment/<int:pk>/',views.UpdateCommentTwitView.as_view(),name='update_comment'),
    path('delete_comment/<int:pk>/',views.DeleteCommentTwitView.as_view(),name='delete_comment'),
    # Relation Like Twit urls...
    path('like/<int:pk>/',views.LikeTwitView.as_view(),name='like'),
    path('dislike/<int:pk>/',views.DisLikeTwitView.as_view(),name='dislike'),
    # Relation Save Twit urls...
    path('save_twit/<int:pk>/',views.SaveTwitView.as_view(),name='save_twit'),
    path('unsave_twit/<int:pk>/',views.UnSaveTwitView.as_view(),name='unsave_twit'),
    path('list_saves/<int:pk>/',views.ListSaveTwitView.as_view(),name='list_save'),
    # CRUD Twit urls...
    path('new/',views.CreateNewTwitView.as_view(),name='new'),
    path('edit/<int:pk>/',views.UpdateTwitView.as_view(),name='edit_twit'),
    path('delete/<int:pk>/',views.DeleteTwitView.as_view(),name='delete_twit'),
]
