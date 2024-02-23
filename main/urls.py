from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from .views import logout_route

urlpatterns = [
    path('', include_docs_urls(title='VibeVista API')),
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),

    path('user-profile/', include('user_profile.urls')),
    path('partner-profile/', include('partner_profile.urls')),
    path('partner-characteristics/', include('characteristics.urls')),
    path('partner-likes/', include('likes.urls')),
]