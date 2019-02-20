from django.conf.urls import url
import help.views as v

urlpatterns = [
    url(r'^$', v.home),
    url(r'^(?P<page>[\w\-]+)/$', v.markdown),
]
