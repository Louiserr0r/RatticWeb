from django.conf.urls import re_path
from django.conf import settings
import cred.views as v

LOCAL_PREFIX = "cred.views"

urlpatterns = [
    # New list views
    re_path(r'^list/$', v.list, name=LOCAL_PREFIX + '.list'),
    re_path(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/$', v.list),
    re_path(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/$', v.list),
    re_path(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/page-(?P<page>\d+)/$', v.list),

    # Search dialog for mobile
    re_path(r'^search/$', v.search),

    # Single cred views
    re_path(r'^detail/(?P<cred_id>\d+)/$', v.detail),
    re_path(r'^detail/(?P<cred_id>\d+)/fingerprint/$', v.ssh_key_fingerprint),
    re_path(r'^detail/(?P<cred_id>\d+)/download/$', v.downloadattachment),
    re_path(r'^detail/(?P<cred_id>\d+)/ssh_key/$', v.downloadsshkey),
    re_path(r'^edit/(?P<cred_id>\d+)/$', v.edit),
    re_path(r'^delete/(?P<cred_id>\d+)/$', v.delete),
    re_path(r'^add/$', v.add),

    # Adding to the change queue
    re_path(r'^addtoqueue/(?P<cred_id>\d+)/$', v.addtoqueue),

    # Bulk views (for buttons on list page)
    re_path(r'^addtoqueue/bulk/$', v.bulkaddtoqueue),
    re_path(r'^delete/bulk/$', v.bulkdelete),
    re_path(r'^undelete/bulk/$', v.bulkundelete),
    re_path(r'^addtag/bulk/$', v.bulktagcred),

    # Tags
    re_path(r'^tag/$', v.tags, name=LOCAL_PREFIX+".tags"),
    re_path(r'^tag/add/$', v.tagadd),
    re_path(r'^tag/edit/(?P<tag_id>\d+)/$', v.tagedit),
    re_path(r'^tag/delete/(?P<tag_id>\d+)/$', v.tagdelete),
]

if not settings.RATTIC_DISABLE_EXPORT:
    urlpatterns += [
        # Export views
        re_path(r'^export.kdb$', v.download),
        re_path(r'^export-by-(?P<cfilter>\w+)/(?P<value>[^/]*).kdb$', v.download),
    ]
