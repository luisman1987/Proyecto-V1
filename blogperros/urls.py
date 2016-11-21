from django.conf.urls import include, url
from blogperros import views
from django.conf import settings
from django.conf.urls. static import static
#Imports para la autenticacion
from django.conf.urls import patterns,url
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$', login, {'template_name': 'blogperros/login.html', }),
    url(r'^perro_detalle/(?P<pk>[0-9]+)/$', 'blogperros.views.detalle_perro'),
    url(r'^perro/nuevo/$', 'blogperros.views.perro_nuevo', name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', 'blogperros.views.perro_editar', name='editar'),

    url(r'^listado/personas/$', 'blogperros.views.listado_personas', name='listado'),
    url(r'^persona/detalle/(?P<pk>[0-9]+)/$', 'blogperros.views.detalle_persona'),
    url(r'^persona/nueva/$', 'blogperros.views.persona_nueva', name='persona_nueva'),
    url(r'^editar/(?P<pk>[0-9]+)/edit/$', 'blogperros.views.editar_persona', name='post_edit'),

    url(r'^Menu/$', 'blogperros.views.main', name='main'),
    url(r'^signup$', 'blogperros.views.signup', name='signup'),
    url(r'^login$', login, {'template_name': 'blogperros/login.html', }, name="login"),
    url(r'^home$', 'blogperros.views.listado_perros', name='home'),
    url(r'^logout$', logout, {'template_name': 'blogperros/main.html', }, name="logout"),

    url(r'^asignacion/nueva/$', 'blogperros.views.asignacion_nueva', name='asignacion_nueva'),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
