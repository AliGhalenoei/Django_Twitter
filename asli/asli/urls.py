"""asli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('content/',include('content.urls')),
    path('api/',include('api.urls')),
    # JWT...
    path('api_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api_token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api_schema_swagger_ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#"refresh": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTY1MTg5MiwiaWF0IjoxNjk1NTY1NDkyLCJqdGkiOiI1YThmZmRkNDk2ODI0MDdiYmM4MDAyYmY3ZTZhZjc5ZCIsInVzZXJfaWQiOjF9.1v9APtsDxHmKZpBnlQtmKo5g7fj4OB0lWLuE_Ki1XTQ
#"access": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1NTY1NzkyLCJpYXQiOjE2OTU1NjU0OTIsImp0aSI6ImUxMzM2N2ZiNjlhYjQ4YWViMjJjMzc1Zjk0OTE1OTE1IiwidXNlcl9pZCI6MX0.EEO1EwLXCbiwt3s1VJyH9xMsLr7SdKtcknbNaThHYo0
