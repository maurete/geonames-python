import sys
import urllib
import urllib2
import simplejson as json

class GeoNames:
    DOMAIN = 'http://api.geonames.org/'
    USERNAME = ''

    def __init__(self, username):
        self.USERNAME = username

    def fetchJson(self, method, params):
        uri = self.DOMAIN + '%s?%s&username=%s' % (method, urllib.urlencode(params), self.USERNAME)
        resource = urllib2.urlopen(uri).readlines()
        js = json.loads(resource[0])
        return js

    def get(self, geonameId, **kwargs):
        method = 'getJSON'
        valid_kwargs = ('lang',)
        params = {'geonameId': geonameId}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        return self.fetchJson(method, params)

    def children(self, geonameId, **kwargs):
        method = 'childrenJSON'
        valid_kwargs = ('maxRows', 'lang',)
        params = {'geonameId': geonameId}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        results = self.fetchJson(method, params)

        if('geonames' in results):
            return results['geonames']
        else:
            return None

    def search(self, **kwargs):
        method = 'searchJSON'
        valid_kwargs = ('q', 'name', 'name_equals', 'name_startsWith', 'maxRows', 'startRow', 'country', 'countryBias', 'continentCode', 'adminCode1', 'adminCode2', 'adminCode3', 'featureClass', 'featureCode', 'lang', 'type', 'style', 'isNameRequired', 'tag', 'operator', 'charset',)
        params = {}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        results = self.fetchJson(method, params)

        if('geonames' in results):
            return results['geonames']
        else:
            return None

    def postalCodeSearch(self, **kwargs):
        method = 'postalCodeSearchJSON'
        valid_kwargs = ('postalcode', 'postalcode_startsWith', 'placename', 'placename_startsWith', 'maxRows', 'country', 'countryBias', 'style', 'operator', 'isReduced', 'charset',)
        params = {}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        results = self.fetchJson(method, params)

        if('postalCodes' in results):
            return results['postalCodes']
        else:
            return None

    def findNearbyPostalCodes(self, **kwargs):
        method = 'findNearbyPostalCodesJSON'
        valid_kwargs = ('postalcode', 'placename', 'maxRows', 'country', 'localCountry', 'lat', 'lng', 'radius', 'style',)
        params = {}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        results = self.fetchJson(method, params)

        if('postalCodes' in results):
            return results['postalCodes']
        else:
            return None

    def hierarchy(self, geonameId, **kwargs):
        method = 'hierarchyJSON'
        valid_kwargs = ('lang')
        params = {'geonameId': geonameId}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        results = self.fetchJson(method, params)

        if('geonames' in results):
            return results['geonames']
        else:
            return None

    def countrySubdivision(self, lat, lng, **kwargs):
        method = 'countrySubdivisionJSON'
        valid_kwargs = ('lang')
        params = {'lat': lat, 'lng': lng}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        results = self.fetchJson(method, params)

        if results:
            return results
        else:
            return None

    def cities(self, north, south, east, west, **kwargs):
        method = 'citiesJSON'
        valid_kwargs = ('lang')
        params = {'north': north, 'south': south, 'east': east, 'west': west}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        results = self.fetchJson(method, params)

        if('geonames' in results):
            return results['geonames']
        else:
            return None

    def weather(self,north, south, east, west, **kwargs):
        method = 'weatherJSON'
        valid_kwargs = ('lang')
        params = {'north': north, 'south': south, 'east': east, 'west': west}
        for key in kwargs:
            if key in valid_kwargs:
                params[key] = kwargs[key]
        results = self.fetchJson(method, params)

        if('weatherObservations' in results):
            return results['weatherObservations']
        else:
            return None
