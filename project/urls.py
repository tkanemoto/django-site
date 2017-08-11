"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('portfolios.urls')),

    # Basic Apps
    url(r'^blog/', include('basic.blog.urls')),
    #url(r'^bookmarks/', include('basic.bookmarks.urls')),
    #url(r'^books/', include('basic.books.urls')),
    url(r'^comments/', include('basic.comments.urls')),
    #url(r'^events/', include('basic.events.urls')),
    #url(r'^flagging/', include('basic.flagging.urls')),
    #url(r'^groups/', include('basic.groups.urls')),
    #url(r'^invitations/', include('basic.invitations.urls')),
    #url(r'^photos', include('basic.media.urls.photos')),
    #url(r'^videos', include('basic.media.urls.videos')),
    #url(r'^messages/', include('basic.messages.urls')),
    #url(r'^movies/', include('basic.movies.urls')),
    #url(r'^music/', include('basic.music.urls')),
    #url(r'^people/', include('basic.people.urls')),
    #url(r'^places/', include('basic.places.urls')),
    url(r'^users/', include('basic.profiles.urls')),
    #url(r'^relationships/', include('basic.relationships.urls')),
    # url(r'^tools/', include('basic.tools.urls')),
    # Apps
    url(r'^player/', include('player.urls')),
    url(r'^torrent/', include('torrent.urls')),
    url(r'^', include('base.urls')),
    # Login
    url('^social/', include('social_django.urls', namespace='social')),
    url(r'^auth/', include('django.contrib.auth.urls')),
]
