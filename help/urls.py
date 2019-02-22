from django.conf.urls import re_path
import help.views as v

app_name = "help"

urlpatterns = [
    re_path(r'^$', v.home),
    re_path(r'^(?P<page>[\w\-]+)/$', v.markdown),
]
