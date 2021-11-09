from rest_framework.routers import DefaultRouter
from ..account.views import AccountViewset
from ..servicios.views import ServiciosViewset, Type_serviciosViewset
from ..pedidos.views import PedidosViewset, PedidosActividViewset, PedidosUpdateViewset
from ..vehiculo.views import VehiculoViewset

router = DefaultRouter()

router.register(r'accounts', AccountViewset, basename='accounts')
router.register(r'services', ServiciosViewset, basename='services')
router.register(r'typeservices', Type_serviciosViewset,
                basename='typeservices')
router.register(r'orders', PedidosViewset, basename='orders')
router.register(r'ordersup', PedidosUpdateViewset, basename='ordersup')
router.register(r'activiorders', PedidosActividViewset, basename='actpedidos')
router.register(r'cars', VehiculoViewset, basename='cars')

urlpatterns = router.urls
