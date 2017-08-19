from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from server import views as server_views
from client import views as client_views
from core import views as core_views
from rest_framework.authtoken import views as token_views
#from client.routes import Routes as client_routes

core_router = routers.DefaultRouter()
core_router.register(r'users', core_views.UserViewSet)
core_router.register(r'groups', core_views.GroupViewSet)

server_router = routers.DefaultRouter()
server_router.register(r'clients', server_views.ClientViewSet)

client_router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^server/api/', include(server_router.urls)),
    url(r'^core/api/', include(core_router.urls)),
    url(r'^client/api/', include(client_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^account/login/', token_views.obtain_auth_token)
]

#url(r'^api/clientreservation/$', client_views.ClientReservationList.as_view()),
    #url(r'^client/api/', include(client_router.urls)),
    

# urlpatterns += client_routes.getRoutes()
