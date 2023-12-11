import requests
import pandas as pd
import numpy as np
import folium
import json
import geocoder
from geopy.geocoders import Nominatim

g_map_instance = None;
g_map_rest_api_key = '';
g_map_search_category_url = 'https://dapi.kakao.com/v2/local/search/category.json'

class MapKaKaoAPI():
    _map = None;

    def __init__(self): 
        global g_map_instance;

        if g_map_instance == None:
            g_map_instance = self;
            
    def fn_start(self): pass;
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

    def fn_get_instance(self):
        global g_map_instance

        if g_map_instance is None:
            g_map_instance = MapKaKaoAPI()
        return g_map_instance

    def _locationData(self, region, page_num, lat, lng):
        url = g_map_search_category_url
        params = {'category_group_code': region, 'page': page_num, 'x': lng, 'y': lat, 'radius': 500}
        headers = {"Authorization": "KakaoAK " + g_map_rest_api_key}

        places = requests.get(url, params=params, headers=headers).json()['documents']
        return places

    def _locationInfo(self, places):
        data = {
            'ID': [],
            'stores': [],
            'X': [],
            'Y': [],
            'road_address': [],
            'place_url': [],
            'category_name': []
        }

        for place in places:
            data['ID'].append(place['id'])
            data['stores'].append(place['place_name'])
            data['X'].append(float(place['x']))
            data['Y'].append(float(place['y']))
            data['road_address'].append(place['road_address_name'])
            data['place_url'].append(place['place_url'])
            data['category_name'].append(place['category_group_name'])
        
        return pd.DataFrame(data)
    
    '''
    def createMap(self, dfs):
        location = self.currentLocation()
        lat = float(location['lat'])
        lng = float(location['lng'])

        m = folium.Map(location=[lat, lng], zoom_start=12)

        for i in range(len(dfs)):
            folium.Marker([dfs['Y'][i],dfs['X'][i]],
                    tooltip=dfs['stores'][i],
                    popup=dfs['place_url'][i],
                    ).add_to(m)
            
        return m
    '''
    
    def _currentLocation(self):
        g = geocoder.ip('me')

        # 현재 위치 위도, 경도 
        # return {'lat': g.latlng[0], 'lng': g.latlng[1]}

        # 숭실대학교 정보과학관 위도, 경도 
        return {'lat': 37.494628751291614, 'lng': 126.95963837868054}

    def searchKeywords(self):
        location = self._currentLocation()
        lat = location['lat']
        lng = location['lng']

        df = None
        for loca in ['HP8', 'PM9']:
            local_name = self._locationData(loca, 1, lat, lng)
            local_elec_info = self._locationInfo(local_name)

            if df is None:
                df = local_elec_info.head(3)
            else:
                df = pd.concat([df, local_elec_info.head(3)], join='outer', ignore_index=True)

        return df