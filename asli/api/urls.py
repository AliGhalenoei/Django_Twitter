from django.urls import path
from rest_framework import routers
from .import views

urlpatterns = [
    # Comments Api
    path('list_create_comment/',views.ListCreateCommentTwitAPIView.as_view(),name='list_create_comment'),
    path('rud_comment/<int:pk>/',views.ListCreateCommentTwitAPIView.as_view(),name='rud_comment'),
    # Relation Api
    path('list_create_relation/',views.ListCreateRelationTwitAPIView.as_view(),name='list_create_relation'),
    path('rud_relation/<int:pk>/',views.RetrieveUpdateDestroyRelationTwitAPIView.as_view(),name='rud_relation'),
    # Save Twit Api
    path('list_create_save/',views.ListCreateSaveTwitAPIView.as_view(),name='list_create_save'),
    path('rud_save/<int:pk>/',views.RetrieveUpdateDestroySaveTwitAPIView.as_view(),name='rud_save'),
    # Accounts App urls...
    path('login_api/',views.LoginAPIView.as_view(),name='login_api'),
    path('singin_api/',views.SinginAPIView.as_view(),name='singin_api'),
    path('logout_api/',views.LogoutAPIView.as_view(),name='logout_api'),
    # Follw User
    path('list_create_follw_user/',views.ListCreateFollwUserAPIView.as_view(),name='list_create_follw_user'),
    path('rud_follw_user/<int:pk>/',views.RetrieveUpdateDestroyFollwUserAPIView.as_view(),name='rud_follw_user'),

]
router = routers.SimpleRouter()
router.register('twit_viewset',views.CRUD_TwotViewSet)
urlpatterns += router.urls
