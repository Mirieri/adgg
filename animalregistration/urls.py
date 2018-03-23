from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('farmerregistration', views.Reg02MaininfoViewSet)
router.register('district', views.Reg01LkpmaindistrictViewSet, base_name='district')
router.register('animalregistration', views.Reg04MaininfoViewSet, base_name='animalregistration')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.Reg02MaininfoView.as_view(), name='animalmaininfo')
]

