#%%
import pandas as pd
import numpy as np
import pickle
from scipy.sparse import coo_matrix
import googlemaps

#%%
gmaps_key = "AIzaSyB_E3nbdEdLmPJhxR1xU0MKAj3BJrI-0t0"
gmaps = googlemaps.Client(key = gmaps_key)

#%%
def process_station_and_line_name(data):
    
    data.loc[data['지하철역']=='회현(남대문시장)','지하철역'] = '회현'
    data.loc[data['지하철역']=='화랑대(서울여대입구)','지하철역'] = '화랑대'
    data.loc[data['지하철역']=='한성대입구(삼선교)','지하철역'] = '한성대입구'
    data.loc[data['지하철역']=='충정로(경기대입구)','지하철역'] = '충정로'
    data.loc[data['지하철역']=='총신대입구(이수)','지하철역'] = '총신대입구'
    data.loc[data['지하철역']=='청량리(지상)','지하철역'] = '청량리'
    data.loc[data['지하철역']=='청량리(지하)','지하철역'] = '청량리'
    data.loc[data['지하철역']=='청량리(서울시립대입구)','지하철역'] = '청량리'
    data.loc[data['지하철역']=='천호(풍납토성)','지하철역'] = '천호'
    data.loc[data['지하철역']=='증산(명지대앞)','지하철역'] = '증산'
    data.loc[data['지하철역']=='잠실(송파구청)','지하철역'] = '잠실'
    data.loc[data['지하철역']=='이촌(국립중앙박물관)','지하철역'] = '이촌'
    data.loc[data['지하철역']=='월드컵경기장(성산)','지하철역'] = '월드컵경기장'
    data.loc[data['지하철역']=='월곡(동덕여대)','지하철역'] = '월곡'
    data.loc[data['지하철역']=='용두(동대문구청)','지하철역'] = '용두'
    data.loc[data['지하철역']=='왕십리(성동구청)','지하철역'] = '왕십리'
    data.loc[data['지하철역']=='올림픽공원(한국체대)','지하철역'] = '올림픽공원'
    data.loc[data['지하철역']=='온수(성공회대입구)','지하철역'] = '온수'
    data.loc[data['지하철역']=='오목교(목동운동장앞)','지하철역'] = '오목교'
    data.loc[data['지하철역']=='어린이대공원(세종대)','지하철역'] = '어린이대공원'
    data.loc[data['지하철역']=='양재(서초구청)','지하철역'] = '양재'
    data.loc[data['지하철역']=='안암(고대병원앞)','지하철역'] = '안암'
    data.loc[data['지하철역']=='아차산(어린이대공원후문)','지하철역'] = '아차산'
    data.loc[data['지하철역']=='쌍용(나사렛대)','지하철역'] = '쌍용'
    data.loc[data['지하철역']=='신천','지하철역'] = '잠실새내'
    data.loc[data['지하철역']=='신창(순천향대)','지하철역'] = '신창'
    data.loc[data['지하철역']=='신정(은행정)','지하철역'] = '신정'
    data.loc[data['지하철역']=='숭실대입구(살피재)','지하철역'] = '숭실대입구'
    data.loc[data['지하철역']=='숙대입구(갈월)','지하철역'] = '숙대입구'
    data.loc[data['지하철역']=='성신여대입구(돈암)','지하철역'] = '성신여대입구'
    data.loc[data['지하철역']=='성내','지하철역'] = '잠실나루'
    data.loc[data['지하철역']=='서울대입구(관악구청)','지하철역'] = '서울대입구'
    data.loc[data['지하철역']=='새절(신사)','지하철역'] = '새절'
    data.loc[data['지하철역']=='상월곡(한국과학기술연구원)','지하철역'] = '상월곡'
    data.loc[data['지하철역']=='상봉(시외버스터미널)','지하철역'] = '상봉'
    data.loc[data['지하철역']=='삼성(무역센터)','지하철역'] = '삼성'
    data.loc[data['지하철역']=='미아(서울사이버대학)','지하철역'] = '미아'
    data.loc[data['지하철역']=='몽촌토성(평화의문)','지하철역'] = '몽촌토성'
    data.loc[data['지하철역']=='동작(현충원)','지하철역'] = '동작'
    data.loc[data['지하철역']=='동두천 중앙','지하철역'] = '동두천중앙'
    data.loc[data['지하철역']=='대흥(서강대앞)','지하철역'] = '대흥'
    data.loc[data['지하철역']=='대림(구로구청)','지하철역'] = '대림'
    data.loc[data['지하철역']=='남한산성입구(성남법원.검찰청)','지하철역'] = '남한산성입구'
    data.loc[data['지하철역']=='남부터미널(예술의전당)','지하철역'] = '남부터미널'
    data.loc[data['지하철역']=='굽은다리(강동구민회관앞)','지하철역'] = '굽은다리'
    data.loc[data['지하철역']=='군자(능동)','지하철역'] = '군자'
    data.loc[data['지하철역']=='구의(광진구청)','지하철역'] = '구의'
    data.loc[data['지하철역']=='교대(법원.검찰청)','지하철역'] = '교대'
    data.loc[data['지하철역']=='광흥창(서강)','지하철역'] = '광흥창'
    data.loc[data['지하철역']=='광화문(세종문화회관)','지하철역'] = '광화문'
    data.loc[data['지하철역']=='광나루(장신대)','지하철역'] = '광나루'
    data.loc[data['지하철역']=='공릉(서울과학기술대)','지하철역'] = '공릉'
    data.loc[data['지하철역']=='고려대(종암)','지하철역'] = '고려대'
    data.loc[data['지하철역']=='경복궁(정부서울청사)','지하철역'] = '경복궁'
    data.loc[data['지하철역']=='강변(동서울터미널)','지하철역'] = '강변'
    
    data.loc[data['호선명']=='9호선2~3단계','호선명'] = '9호선'
    data.loc[data['호선명']=='9호선2단계','호선명'] = '9호선'
    
    return data

#%%
def get_drop_index(data):

    drop_index = []
    for i, station in enumerate(data['지하철역']):
        try:
            if gmaps.geocode(station+"역", language='ko')[0]['address_components'][2]['long_name'] == '서울특별시' or gmaps.geocode(station+"역", language='ko')[0]['address_components'][1]['long_name'] == '서울특별시':
                continue
            else:
                drop_index.append(i)
        except:
            
            print(i, station)
    
    return drop_index


#%%
def get_station_line_matrix(processed_seoul_data):
    line_data = processed_seoul_data[['지하철역','호선명']].groupby(['지하철역','호선명']).count().reset_index()
    
    line_name = processed_seoul_data.호선명.unique()
    line_name.sort()
    
    index2station = {index: station for index, station in enumerate(line_data.지하철역.unique())}
    station2index = {v: k for k, v in index2station.items()}
    index2line = {index: line for index, line in enumerate(line_name)}
    line2index = {v: k for k, v in index2line.items()}
    
    row_index = [station2index[station] for station in line_data.지하철역.values]
    col_index = [line2index[line] for line in line_data.호선명.values]
    value = np.ones((len(line_data),1)).flatten()
    station_line_matrix = coo_matrix((value, (row_index, col_index))).toarray()
    
    return station_line_matrix, index2line, index2station

#%%
subway_sum_data = pd.read_csv('../11.data/03.1.subway/01.subway_sum_data.csv', encoding='utf8')

gb_subway = subway_sum_data[['지하철역','호선명']].groupby(['지하철역','호선명']).count().reset_index()

#%%
drop_index = get_drop_index(gb_subway)

#%%
for i in [414, 281, 310]:
    drop_index.append(i)

#%%
drop_index.append(325)

#%%
seoul_station = gb_subway.drop(gb_subway.index[drop_index])

#%%
filtered_seoul_station = process_station_and_line_name(seoul_station)

#%%
gb_filtered_seoulstation = filtered_seoul_station[['지하철역','호선명']].groupby(['지하철역','호선명']).count().reset_index()

#%%
noooooo = gb_filtered_seoulstation.groupby(['지하철역']).count()

#%%
wow = pd.read_csv('../11.data/03.2.subway_geometry/00.subway_geometry.csv', encoding='cp949')

for station in wow['지하철역']:
    if station not in noooooo.index:
        print(station)

#%%
gb_filtered_seoulstation.loc[337] = ['구룡', '분당선']
gb_filtered_seoulstation.loc[338] = ['송정', '공항철도 1호선']


#%%
station_line_matrix, index2line, index2station = get_station_line_matrix(gb_filtered_seoulstation)

#%%
df = pd.DataFrame(station_line_matrix, columns = index2line.values())
df.index = index2station.values()

#%%
df.to_csv('../11.data/10.features/25.최근접3개역의 호선.csv', encoding='cp949')
