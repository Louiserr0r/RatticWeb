from django.conf.urls import include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tastypie.api import Api
from cred.api import CredResource, TagResource
from staff.api import GroupResource
from django.conf import settings
from ratticweb import views as main_views

# Configure the error handlers
handler500 = 'ratticweb.views.handle500'
handler404 = 'ratticweb.views.handle404'

# Setup the API
v1_api = Api(api_name='v1')
v1_api.register(CredResource())
v1_api.register(TagResource())
v1_api.register(GroupResource())

# Setup the base paths for applications, and the API
base_urlpatterns = [
    # Apps:
    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^account/', include('account.urls')),
    re_path(r'^cred/', include('cred.urls')),
    re_path(r'^staff/', include('staff.urls')),
    re_path(r'^help/', include('help.urls')),

    # API
    re_path(r'^api/', include(v1_api.urls)),

    # Language
    re_path(r'^i18n/', include('django.conf.urls.i18n')),

    # two Factor
    # re_path(r'^', include('two_factor.urls', namespace='two_factor')),
]

# If in debug mode enable the Django admin interface
if settings.DEBUG:
    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    base_urlpatterns += [
        # Uncomment the admin/doc line below to enable admin documentation:
        re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        re_path(r'^admin/', include(admin.site.urls)),
    ]
else:
    from django.views.static import serve
    from .settings import STATIC_ROOT
    base_urlpatterns.append(re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}))
    

# Strip any leading slash from the RATTIC_ROOT_URL
if settings.RATTIC_ROOT_URL[0] == '/':
    root = settings.RATTIC_ROOT_URL[1:]
else:
    root = settings.RATTIC_ROOT_URL

# Serve RatticDB from an alternate root if requested
urlpatterns = [
    re_path(r'^' + root, include(base_urlpatterns)),
]

# Serve the static files from the right location in dev mode
urlpatterns += staticfiles_urlpatterns()
