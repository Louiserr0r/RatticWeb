from django.conf.urls import url
from django.conf import settings
from .views import NewUser, UpdateUser
import staff.views as v
urlpatterns = [
    # Views in views.py
    url(r'^$', v.home),

    # User/Group Management
    url(r'^userdetail/(?P<uid>\d+)/$', v.userdetail),
    url(r'^removetoken/(?P<uid>\d+)/$', v.removetoken),
    url(r'^groupdetail/(?P<gid>\d+)/$', v.groupdetail),

    # Auditing
    url(r'^audit-by-(?P<by>\w+)/(?P<byarg>\d+)/$', v.audit),

    # Importing
    url(r'^import/keepass/$', v.upload_keepass),
    url(r'^import/process/$', v.import_overview),
    url(r'^import/process/(?P<import_id>\d+)/$', v.import_process),
    url(r'^import/process/(?P<import_id>\d+)/ignore/$', v.import_ignore),

    # Undeletion
    url(r'^credundelete/(?P<cred_id>\d+)/$', v.credundelete),
]

# URLs we remove if using LDAP groups
if not settings.USE_LDAP_GROUPS:
    urlpatterns += [
        # Group Management
        url(r'^groupadd/$', v.groupadd),
        url(r'^groupedit/(?P<gid>\d+)/$', v.groupedit),
        url(r'^groupdelete/(?P<gid>\d+)/$', v.groupdelete),
        url(r'^useredit/(?P<pk>\d+)/$', UpdateUser.as_view(), name="user_edit"),
        url(r'^userdelete/(?P<uid>\d+)/$', v.userdelete),
    ]

# User add is disabled only when LDAP config exists
if not settings.LDAP_ENABLED:
    urlpatterns += [
        # User Management
        url(r'^useradd/$', NewUser.as_view(), name="user_add"),

    ]
