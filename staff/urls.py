from django.conf.urls import re_path
from django.conf import settings
from .views import NewUser, UpdateUser
import staff.views as v

app_name='staff'

urlpatterns = [
    # Views in views.py
    re_path(r'^$', v.home, name="home"),

    # User/Group Management
    re_path(r'^userdetail/(?P<uid>\d+)/$', v.userdetail, name="userdetail"),
    re_path(r'^removetoken/(?P<uid>\d+)/$', v.removetoken, name='removetoken'),
    re_path(r'^groupdetail/(?P<gid>\d+)/$', v.groupdetail, name='groupdetail'),

    # Auditing
    re_path(r'^audit-by-(?P<by>\w+)/(?P<byarg>\d+)/$', v.audit, name="audit"),

    # Importing
    re_path(r'^import/keepass/$', v.upload_keepass, name="upload_keepass"),
    re_path(r'^import/process/$', v.import_overview, name="import_overview"),
    re_path(r'^import/process/(?P<import_id>\d+)/$', v.import_process, name="import_process"),
    re_path(r'^import/process/(?P<import_id>\d+)/ignore/$', v.import_ignore, name="import_ignore"),

    # Undeletion
    re_path(r'^credundelete/(?P<cred_id>\d+)/$', v.credundelete, name="credundelete"),
]

# URLs we remove if using LDAP groups
if not settings.USE_LDAP_GROUPS:
    urlpatterns += [
        # Group Management
        re_path(r'^groupadd/$', v.groupadd, name="groupadd"),
        re_path(r'^groupedit/(?P<gid>\d+)/$', v.groupedit, name="groupedit"),
        re_path(r'^groupdelete/(?P<gid>\d+)/$', v.groupdelete, name="groupdelete"),
        re_path(r'^useredit/(?P<pk>\d+)/$', UpdateUser.as_view(), name="user_edit"),
        re_path(r'^userdelete/(?P<uid>\d+)/$', v.userdelete, name="userdelete"),
    ]

# User add is disabled only when LDAP config exists
if not settings.LDAP_ENABLED:
    urlpatterns += [
        # User Management
        re_path(r'^useradd/$', NewUser.as_view(), name="user_add"),
    ]
