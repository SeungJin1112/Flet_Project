import requests
import pandas as pd
import numpy as np
import requests
import io
import geocoder
from PIL import Image
from geopy.geocoders import Nominatim

g_map_instance = None;
g_map_rest_api_key = '2072e54e0364040f53dda8f558b64e0d';
g_map_search_category_url = 'https://dapi.kakao.com/v2/local/search/category.json'

g_map_client_id = "l9zt6fqlhb"
g_map_client_secret = "h84fNL2XTVJ69atcf8zf3jibJpkrC2PVsPKBs35k"

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
    
    def getStaticMap(self):
        marker_lonlat = {
            'X': [],
            'Y': [],
        }

        result_data = self.searchKeywords()

        for index, row in result_data.iterrows():
            marker_lonlat['X'].append(row['X'])
            marker_lonlat['Y'].append(row['Y'])

        endpoint = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
        headers = {
            "X-NCP-APIGW-API-KEY-ID": g_map_client_id,
            "X-NCP-APIGW-API-KEY": g_map_client_secret,
        }
        lon, lat = "126.95963837868054", "37.494628751291614"
        _center = f"{lon},{lat}"
        _level = 15
        _w, _h = 1024, 1024
        _maptype = "basic"
        _format = "jpg"
        _scale = 1
        #_markers = f"""type:d|size:mid|pos:{lon} {lat}|color:red"""
        markers_list = []
        for x, y in zip(marker_lonlat['X'], marker_lonlat['Y']):
            markers_list.append(f"type:d|size:mid|pos:{x} {y}|color:red")
        _markers = '|'.join(markers_list)
        _lang = "ko"
        _dataversion = "201.3"

        url = f"{endpoint}?center={_center}&level={_level}&w={_w}&h={_h}&maptype={_maptype}&format={_format}&scale={_scale}&lang={_lang}&dataversion={_dataversion}&markers={_markers}"
        res = requests.get(url, headers=headers)

        image_data = io.BytesIO(res.content)
        image = Image.open(image_data)

        # 새로운 크기 설정
        new_size = (3000, 1780)

        # 이미지 크기 변경
        resized_image = image.resize(new_size)

        # 변경된 이미지 저장 (필요한 경우)
        resized_image.save("src/image/test.jpg")
        
        #image.save('test.jpg')