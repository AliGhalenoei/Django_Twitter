from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('singin/',views.UserSinginView.as_view(),name='singin'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('password_reset/',views.UserPasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',views.UserPasswordResetDone.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',views.UserPasswordResetConfirm.as_view(),name='password_reset_confirm'),
    path('password_Reset_complete/',views.UserPasswordResetComplete.as_view(),name='password_reset_complete'),
    # Profile Page...
    path('profile/<int:pk>/',views.UserProfilePageView.as_view(),name='profile'),
    # Relation Follw Or...
    path('follw/<int:pk>/',views.UserFollwView.as_view(),name = 'follw'),
    path('unfollw/<int:pk>/',views.UserUnFollwView.as_view(),name = 'unfollw'),
    #Delete Accounts...
    path('delete_account/<int:pk>/',views.DeleteAccountView.as_view(),name='delete_account'),
]
