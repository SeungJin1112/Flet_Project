import requests
import pandas as pd
import numpy as np
import folium

g_map_instance = None;
g_map_rest_api_key = '2072e54e0364040f53dda8f558b64e0d';
g_map_search_keyword_url = 'https://dapi.kakao.com/v2/local/search/keyword.json'

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
    def fn_get_instance(self): pass;

    def _locationData(self, region, page_num):
        url = g_map_search_keyword_url
        params = {'query': region,'page': page_num}
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
            'place_url': []
        }

        for place in places:
            data['ID'].append(place['id'])
            data['stores'].append(place['place_name'])
            data['X'].append(float(place['x']))
            data['Y'].append(float(place['y']))
            data['road_address'].append(place['road_address_name'])
            data['place_url'].append(place['place_url'])
        
        return pd.DataFrame(data)
    
    def createMap(self, dfs):
        # 지도 시작 위치 수정 필 (현재 위치로)
        m = folium.Map(location=[33.4935,126.6266], zoom_start=12)

        for i in range(len(dfs)):
            folium.Marker([dfs['Y'][i],dfs['X'][i]],
                    tooltip=dfs['stores'][i],
                    popup=dfs['place_url'][i],
                    ).add_to(m)
            
        return m

    def searchKeywords(self):
        df = None
        for loca in ['약국', '병원']:
            for page in range(1,4):
                local_name = self._locationData(loca, page)
                local_elec_info = self._locationInfo(local_name)

                if df is None:
                    df = local_elec_info
                elif local_elec_info is None:
                    continue
                else:
                    df = pd.concat([df, local_elec_info],join='outer', ignore_index = True)
        return df