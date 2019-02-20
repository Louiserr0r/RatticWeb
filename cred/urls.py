from django.conf.urls import url
from django.conf import settings
import cred.views as v

urlpatterns = [
    # New list views
    url(r'^list/$', v.list),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/$', v.list),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/$', v.list),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/page-(?P<page>\d+)/$', v.list),

    # Search dialog for mobile
    url(r'^search/$', v.search),

    # Single cred views
    url(r'^detail/(?P<cred_id>\d+)/$', v.detail),
    url(r'^detail/(?P<cred_id>\d+)/fingerprint/$', v.ssh_key_fingerprint),
    url(r'^detail/(?P<cred_id>\d+)/download/$', v.downloadattachment),
    url(r'^detail/(?P<cred_id>\d+)/ssh_key/$', v.downloadsshkey),
    url(r'^edit/(?P<cred_id>\d+)/$', v.edit),
    url(r'^delete/(?P<cred_id>\d+)/$', v.delete),
    url(r'^add/$', v.add),

    # Adding to the change queue
    url(r'^addtoqueue/(?P<cred_id>\d+)/$', v.addtoqueue),

    # Bulk views (for buttons on list page)
    url(r'^addtoqueue/bulk/$', v.bulkaddtoqueue),
    url(r'^delete/bulk/$', v.bulkdelete),
    url(r'^undelete/bulk/$', v.bulkundelete),
    url(r'^addtag/bulk/$', v.bulktagcred),

    # Tags
    url(r'^tag/$', v.tags),
    url(r'^tag/add/$', v.tagadd),
    url(r'^tag/edit/(?P<tag_id>\d+)/$', v.tagedit),
    url(r'^tag/delete/(?P<tag_id>\d+)/$', v.tagdelete),
]

if not settings.RATTIC_DISABLE_EXPORT:
    urlpatterns += [
        # Export views
        url(r'^export.kdb$', v.download),
        url(r'^export-by-(?P<cfilter>\w+)/(?P<value>[^/]*).kdb$', v.download),
    ]
