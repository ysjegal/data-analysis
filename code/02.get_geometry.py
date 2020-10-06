#%%
import googlemaps
import pandas as pd

#%%

import googlemaps
gmaps_key = "AIzaSyB_E3nbdEdLmPJhxR1xU0MKAj3BJrI-0t0"
gmaps = googlemaps.Client(key = gmaps_key)


#%%
def get_geometry_data(data):
    lat = [] #위도
    lng = [] #경도
    for location in data['location']:
        try:
            geometry = gmaps.geocode(location, language='ko')[0]['geometry']['location']
            lat.append(geometry['lat'])
            lng.append(geometry['lng'])
        except:
            print(location)
            lat.append(0)
            lng.append(0)

    data['위도'] = lat
    data['경도'] = lng
    
    return data

#%%

# file_list에 위도 경도를 구하고 싶은 데이터 이름 .csv 빼고 넣으시면 됩니다
file_list = ['00.public_institution_dong','01.public_institution_gu','02.public_institution_fire','03.public_institution_healty','05.preschool','06.elementaryschool','07.middleschool','08.highschool']


for file_name in file_list:
    print(file_name)
    
    # Encoding error 처리
    # 읽어오고싶은 file path 커스터마이징 하시면 됩니다
    # 그대로 쓰실거면 "11.data/04.facilities" 파일 안에 csv파일 넣어두시면 됩니다
    # {} 안에는 .csv를 제외한 파일 이름이 들어가도록
    try:
        data = pd.read_csv('../11.data/04.facilities/{}.csv'.format(file_name), encoding='cp949')
    except:
        data = pd.read_csv('../11.data/04.facilities/{}.csv'.format(file_name), encoding='utf8')
    
    data = get_geometry_data(data)
    
    # 위도 경도를 구할 필요가 없는 데이터는 "11.data/04.facilities_geometry"에 바로 넣어두세요
    # 저장하고 싶은 file path 써주시면 됩니다
    data.to_csv('../11.data/04.facilities_geometry/{}_geometry.csv'.format(file_name), encoding='cp949')