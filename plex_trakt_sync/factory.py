from plex_trakt_sync.decorators import memoize


class Factory:
    @property
    @memoize
    def trakt_api(self):
        from plex_trakt_sync.trakt_api import TraktApi

        trakt = TraktApi()

        return trakt

    @property
    @memoize
    def plex_api(self):
        from plex_trakt_sync.config import CONFIG
        from plex_trakt_sync.plex_api import PlexApi
        from plexapi.server import PlexServer

        url = CONFIG["PLEX_BASEURL"]
        token = CONFIG["PLEX_TOKEN"]
        server = PlexServer(url, token)
        plex = PlexApi(server)

        return plex

    @property
    @memoize
    def media_factory(self):
        from plex_trakt_sync.media import MediaFactory

        trakt = self.trakt_api
        plex = self.plex_api
        mf = MediaFactory(plex, trakt)

        return mf


factory = Factory()
