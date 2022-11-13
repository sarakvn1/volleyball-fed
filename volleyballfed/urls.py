from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Volleyball Reservation Backend Endpoints",
        default_version='v1',
        description="Volleyball Reservation API",
        terms_of_service="https://www.myapp.com/policies/terms/",
        contact=openapi.Contact(email="sarakvn@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    # JWT
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh ', TokenRefreshView.as_view(), name='token_refresh'),

    # swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
]
