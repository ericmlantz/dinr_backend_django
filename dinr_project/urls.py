from dinr import views
from django.contrib import admin
from django.urls import include, path
from dinr import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',views.UserView, 'users')
router.register(r'restaurants',views.RestaurantView, 'restaurants')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
