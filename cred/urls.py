from django.conf.urls import re_path
from django.conf import settings
import cred.views as v

LOCAL_PREFIX = ""
app_name = 'cred'

urlpatterns = [
    # New list views
    re_path(r'^list/$', v.list, name="list"),
    re_path(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/$', v.list, name="list"),
    re_path(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/$', v.list, name="list"),
    re_path(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/page-(?P<page>\d+)/$', v.list, name="list"),

    # Search dialog for mobile
    re_path(r'^search/$', v.search, name='search'),

    # Single cred views
    re_path(r'^detail/(?P<cred_id>\d+)/$', v.detail, name="detail"),
    re_path(r'^detail/(?P<cred_id>\d+)/fingerprint/$', v.ssh_key_fingerprint, name="ssh_key_fingerprint"),
    re_path(r'^detail/(?P<cred_id>\d+)/download/$', v.downloadattachment, name="downloadattachment"),
    re_path(r'^detail/(?P<cred_id>\d+)/ssh_key/$', v.downloadsshkey, name="downloadsshkey"),
    re_path(r'^edit/(?P<cred_id>\d+)/$', v.edit, name='edit'),
    re_path(r'^delete/(?P<cred_id>\d+)/$', v.delete, name='delete'),
    re_path(r'^add/$', v.add, name="add"),

    # Adding to the change queue
    re_path(r'^addtoqueue/(?P<cred_id>\d+)/$', v.addtoqueue, name='addtoqueue'),

    # Bulk views (for buttons on list page)
    re_path(r'^addtoqueue/bulk/$', v.bulkaddtoqueue, name="bulkaddtoqueue"),
    re_path(r'^delete/bulk/$', v.bulkdelete, name="bulkdelete"),
    re_path(r'^undelete/bulk/$', v.bulkundelete, name="bulkundelete"),
    re_path(r'^addtag/bulk/$', v.bulktagcred, name="bulktagcred"),

    # Tags
    re_path(r'^tag/$', v.tags, name="tags"),
    re_path(r'^tag/add/$', v.tagadd, name="tagadd"),
    re_path(r'^tag/edit/(?P<tag_id>\d+)/$', v.tagedit, name="tagedit"),
    re_path(r'^tag/delete/(?P<tag_id>\d+)/$', v.tagdelete, name="tagdelete"),
]

if not settings.RATTIC_DISABLE_EXPORT:
    urlpatterns += [
        # Export views
        re_path(r'^export.kdb$', v.download),
        re_path(r'^export-by-(?P<cfilter>\w+)/(?P<value>[^/]*).kdb$', v.download, name='download'),
    ]
