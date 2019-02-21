from django.conf.urls import include, re_path
from django.conf import settings

from .views import profile, newapikey, deleteapikey, RatticSessionDeleteView
from .views import RatticTFADisableView, RatticTFABackupTokensView
from .views import RatticTFASetupView, RatticTFALoginView
from .views import RatticTFAGenerateApiKey
from account.views import rattic_change_password, ldap_password_change
from django.contrib import auth as dj_auth

from two_factor.views import QRGeneratorView

urlpatterns = [
    re_path(r'^$', profile, {}),
    re_path(r'^newapikey/$', newapikey, {}),
    re_path(r'^deleteapikey/(?P<key_id>\d+)/$', deleteapikey, {}),

    re_path(r'^logout/$', dj_auth.views.LogoutView, {
        'next_page': settings.RATTIC_ROOT_URL}),

    # View to kill other sessions with
    re_path(r'^killsession/(?P<pk>\w+)/', RatticSessionDeleteView.as_view(), name='kill_session'),

    # Two Factor Views
    re_path(r'^login/$', RatticTFALoginView.as_view(), name='login'),
    re_path(r'^generate_api_key$', RatticTFAGenerateApiKey.as_view(), name="generate_api_key"),

    re_path(r'^two_factor/disable/$', RatticTFADisableView.as_view(), name='tfa_disable'),
    re_path(r'^two_factor/backup/$', RatticTFABackupTokensView.as_view(), name='tfa_backup'),
    re_path(r'^two_factor/setup/$', RatticTFASetupView.as_view(), name='tfa_setup'),
    re_path(r'^two_factor/qr/$', QRGeneratorView.as_view(), name='tfa_qr'),
]

if settings.GOAUTH2_ENABLED:
    urlpatterns += [
        re_path(r'', include('social_auth.urls')),
    ]

# URLs we don't want enabled with LDAP
if not settings.LDAP_ENABLED:
    urlpatterns += [
        re_path(r'^reset/$', dj_auth.views.PasswordResetView,
            {
                'post_reset_redirect': '/account/reset/done/',
                'template_name': 'password_reset.html'
            },
            name="password_reset"
        ),

        re_path(r'^reset/done/$', dj_auth.views.PasswordResetDoneView, {
            'template_name': 'password_reset_done.html'},
            name="password_reset_done"
        ),

        re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', dj_auth.views.PasswordResetConfirmView, {
            'post_reset_redirect': '/',
            'template_name': 'password_reset_confirm.html'},
            name="password_reset_confirm"
        ),

        re_path(r'^changepass/$', rattic_change_password, {
            'post_change_redirect': '/account/',
            'template_name': 'account_changepass.html'}, name='password_change')
    ]

# URLs we do want enabled with LDAP
if settings.LDAP_ENABLED and settings.AUTH_LDAP_ALLOW_PASSWORD_CHANGE:
    urlpatterns += [
        re_path(r'^changepass/$', ldap_password_change, {}, name='password_change')
    ]
