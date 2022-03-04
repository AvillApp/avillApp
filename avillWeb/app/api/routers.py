from rest_framework.routers import DefaultRouter
from ..account.views import AccountViewset, PhotoViewset
from ..servicios.views import ServiciosViewset, Type_serviciosViewset
from ..pedidos.views import *
from ..vehiculo.views import VehiculoViewset
from ..chat.views import ChatViewset
from ..facturas.views import ComisionViewset, FacturaViewset

router = DefaultRouter()

router.register(r'accounts', AccountViewset, basename='accounts')
router.register(r'photos', PhotoViewset, basename='photos')

router.register(r'services', ServiciosViewset, basename='services')
router.register(r'typeservices', Type_serviciosViewset,
                basename='typeservices')
router.register(r'orders', PedidosViewset, basename='orders')
router.register(r'ordersup', PedidosUpdateViewset, basename='ordersup')

# router.register(r'ordersconduc/<pk>/',  PedidoVehiculoViewset,
#                 basename='ordersconduc')
router.register(r'activiorders', PedidosActividViewset, basename='actpedidos')
router.register(r'cars', VehiculoViewset, basename='cars')
router.register(r'ratting/account', RatingAccountViewset,
                basename='rattingAccount')
router.register(r'ratting/order', RatingPedidoViewset,
                basename='rattingPedido')

router.register(r'chat/order', ChatViewset,
                basename='chatPedido')  

router.register(r'facturas', FacturaViewset,
                basename='Factura')  

router.register(r'facturas/comision', ComisionViewset,
                basename='comisionFactura')  


urlpatterns = router.urls
