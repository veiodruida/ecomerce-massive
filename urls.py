from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Index page
    (r'', include('gmapi.urls.media')),
    url(r'^$', 'massive.engine.views.index', name='index'),
    url(r'^contato/$', 'massive.engine.views.contato', name='contactus'),

    # Login/logout
    url(r'^usuario/registrar/$', 'massive.engine.views.registra_usuario', name='user_signup'),
    url(r'^usuario/login/$', 'massive.engine.views.login_usuario', name='login_usuario'),
    url(r'^usario/logout/$', 'massive.engine.views.logout_usuario', name='logout_usuario'),

    # Admin
    url(r'^man/', include(admin.site.urls)),
   # url('^setup/$', 'massivecoupon.socialregistration.views.setup', name='socialregistration_setup'),
   # url('^logout/$', 'massivecoupon.socialregistration.views.logout', name='social_logout'),

    # Static stuff (apache should serve this in production)
    (r'^(robots.txt)$', 'django.views.static.serve', {'document_root': '/var/www/massivecoupon/'}),
)
#((r'^media/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.MEDIA_ROOT})),
if settings.LOCAL:
    urlpatterns = urlpatterns + patterns('',
        ((r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT})),
        )

from django.conf import settings
from django.conf.urls.defaults import *


# Setup Facebook URLs if there's an API key specified
#if getattr(settings, 'FACEBOOK_API_KEY', None) is not None:
#    urlpatterns = urlpatterns + patterns('',
#        url('^facebook/login/$', 'massivecoupon.socialregistration.views.facebook_login',
#            name='facebook_login'),
#
#        url('^facebook/connect/$', 'massivecoupon.socialregistration.views.facebook_connect',
#            name='facebook_connect'),
#
#        url('^xd_receiver.htm', 'django.views.generic.simple.direct_to_template',
#            {'template':'socialregistration/xd_receiver.html'},
#            name='facebook_xd_receiver'),
#    )
#
##Setup Twitter URLs if there's an API key specified
#if getattr(settings, 'TWITTER_CONSUMER_KEY', None) is not None:
#    urlpatterns = urlpatterns + patterns('',
#        url('^twitter/redirect/$', 'massivecoupon.socialregistration.views.oauth_redirect',
#            dict(
#                consumer_key=settings.TWITTER_CONSUMER_KEY,
#                secret_key=settings.TWITTER_CONSUMER_SECRET_KEY,
#                request_token_url=settings.TWITTER_REQUEST_TOKEN_URL,
#                access_token_url=settings.TWITTER_ACCESS_TOKEN_URL,
#                authorization_url=settings.TWITTER_AUTHORIZATION_URL,
#                callback_url='twitter_callback'
#            ),
#            name='twitter_redirect'),
#
#        url('^twitter/callback/$', 'socialregistration.views.oauth_callback',
#            dict(
#                consumer_key=settings.TWITTER_CONSUMER_KEY,
#                secret_key=settings.TWITTER_CONSUMER_SECRET_KEY,
#                request_token_url=settings.TWITTER_REQUEST_TOKEN_URL,
#                access_token_url=settings.TWITTER_ACCESS_TOKEN_URL,
#                authorization_url=settings.TWITTER_AUTHORIZATION_URL,
#                callback_url='twitter'
#            ),
#            name='twitter_callback'
#        ),
#        url('^twitter/$', 'socialregistration.views.twitter', name='twitter'),
#    )
#
## Setup FriendFeed URLs if there's an API key specified
#if getattr(settings, 'FRIENDFEED_CONSUMER_KEY', None) is not None:
#    urlpatterns = urlpatterns + patterns('',
#        url('^friendfeed/redirect/$', 'socialregistration.views.oauth_redirect',
#            dict(
#                consumer_key=settings.FRIENDFEED_CONSUMER_KEY,
#                secret_key=settings.FRIENDFEED_CONSUMER_SECRET_KEY,
#                request_token_url=settings.FRIENDFEED_REQUEST_TOKEN_URL,
#                access_token_url=settings.FRIENDFEED_ACCESS_TOKEN_URL,
#                authorization_url=settings.FRIENDFEED_AUTHORIZATION_URL,
#                callback_url='friendfeed_callback'
#            ),
#            name='friendfeed_redirect'),
#
#        url('^friendfeed/callback/$', 'socialregistration.views.oauth_callback',
#            dict(
#                consumer_key=settings.FRIENDFEED_CONSUMER_KEY,
#                secret_key=settings.FRIENDFEED_CONSUMER_SECRET_KEY,
#                request_token_url=settings.FRIENDFEED_REQUEST_TOKEN_URL,
#                access_token_url=settings.FRIENDFEED_ACCESS_TOKEN_URL,
#                authorization_url=settings.FRIENDFEED_AUTHORIZATION_URL,
#                callback_url='friendfeed'
#            ),
#            name='friendfeed_callback'
#        ),
#        url('^friendfeed/$', 'massivecoupon.socialregistration.views.friendfeed', name='friendfeed'),
#    )
#
#urlpatterns = urlpatterns + patterns('',
#    url('^openid/redirect/$', 'massivecoupon.socialregistration.views.openid_redirect',
#        name='openid_redirect'),
#    url('^openid/callback/$', 'massivecoupon.socialregistration.views.openid_callback',
#        name='openid_callback')
#)

urlpatterns = urlpatterns + patterns('',
    url(r'^(?P<cidade_slug>\w+)/$', 'massive.engine.views.cidade_index', name='cidade_index'),
    
    url(r'^(?P<cidade_slug>\w+)/assinar/$', 'massive.engine.views.inscricao_cidade',
        name='city_subscribe'),
                                     
    url(r'^(?P<cidade_slug>\w+)/(?P<oferta_slug>[-\w]+)/$',
        'massive.engine.views.oferta_detalhe', name='oferta_detalhe'),
                                     
    url(r'^(?P<cidade_slug>\w+)/(?P<oferta_slug>[-\w]+)/(?P<quantidade>\d+)/checkout/completo/$',
        'massive.engine.views.oferta_checkout_complete', name='oferta_checkout_complete'),
                                     
    url(r'^(?P<cidade_slug>\w+)/(?P<oferta_slug>[-\w]+)/comprar/$',
        'massive.engine.views.oferta_checkout', name='oferta_checkout'),
      
                                     
#    (r'^ofertas/(?P<cidade>[-\w]+)/$',
#     'show_oferta_cidade', {
#     'nome_template':'catalogo/cidade.html'},'catalogo_cidade'),
#    (r'^ofertas/(?P<cidade>[-\w]+)/(?P<oferta_slug>[-\w]+)/$',
#     'show_oferta', {
#     'nome_template':'catalogo/oferta.html'},'catalogo_oferta'),
#     (r'^email/$', 'amigoForm',{ 'nome_template':'catalogo.html' }, 'emailAmigo'),
)

