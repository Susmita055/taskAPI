from django.urls import  path, include
from .views import *
from rest_framework import routers, urlpatterns, views
router = routers.DefaultRouter()
#router.register(r'tasks', TaskViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    #path('tasks/', include(router.urls) ),
    path('api-jwt-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',register,name='register'),
    path('login/',Login.as_view(), name='login'),
    path('task/', TaskList.as_view(), name="task"),
    path('task/<int:pk>/', taskDetail.as_view(), name='taskone'),

]