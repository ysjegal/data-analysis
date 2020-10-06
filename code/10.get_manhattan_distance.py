#%%
from haversine import haversine
import pandas as pd
import pickle

#%% 최근접 시설 3개와의 거리
def get_distance_nearest_3(building, facility_file_path, adjacent_gu):
    
    try:
        facility = pd.read_csv(facility_file_path, encoding='cp949')
    except:
        facility = pd.read_csv(facility_file_path, encoding='utf8')
    
    dist_1st = []
    dist_2nd = []
    dist_3rd = []
    
    for bi in building.index:
        b_lat = building.iloc[bi]['위도']
        b_lng = building.iloc[bi]['경도']
        
        distance_list = []
        for gu in adjacent_gu[building.iloc[bi]['gu']]:
            
            for fi in facility.loc[facility['gu']==gu].index:
                f_lat = facility.iloc[fi]['위도']
                f_lng = facility.iloc[fi]['경도']
                
                # m단위의 manhattan dist
                dist = (haversine((f_lat,f_lng), (b_lat,f_lng)) + haversine((b_lat, f_lng), (b_lat, b_lng))) * 1000 
                
                
                
                distance_list.append(dist)
        
        distance_list.sort()
        dist_1st.append(distance_list[0])
        dist_2nd.append(distance_list[1])
        dist_3rd.append(distance_list[2])
    
    return dist_1st, dist_2nd, dist_3rd

#%% 해당 자치구 소속 시설과의 거리
def get_nearest_facility(building, facility_file_path, adjacent_gu):
    
    try:
        facility = pd.read_csv(facility_file_path, encoding='cp949')
    except:
        facility = pd.read_csv(facility_file_path, encoding='utf8')
    
    dist_list = []
    
    for bi in building.index:
        b_lat = building.iloc[bi]['위도']
        b_lng = building.iloc[bi]['경도']
        
        lat = facility.loc[facility['gu'] == building.iloc[bi]['gu']]['위도']
        lng = facility.loc[facility['gu'] == building.iloc[bi]['gu']]['경도']
        
        f_lat = lat.values
        f_lng = lng.values
        
        print(f_lat[0])
        
        dist = (haversine((f_lat[0],f_lng[0]), (b_lat,f_lng[0])) + haversine((b_lat, f_lng[0]), (b_lat, b_lng))) * 1000 # m단위의 manhattan dist
        dist_list.append(dist)
    
    return dist_list
   
#%% 일정거리 내 시설의 개수
def get_num_of_facilities(building, facility_file_path, adjacent_gu):
    
    try:
        facility = pd.read_csv(facility_file_path, encoding='cp949')
    except:
        facility = pd.read_csv(facility_file_path, encoding='utf8')
    

    num_of_facility = []
    
    for bi in building.index:
        b_lat = building.iloc[bi]['위도']
        b_lng = building.iloc[bi]['경도']
        
        distance_list = []
        for gu in adjacent_gu[building.iloc[bi]['gu']]:
            
            for fi in facility.loc[facility['gu']==gu].index:
                f_lat = facility.iloc[fi]['위도']
                f_lng = facility.iloc[fi]['경도']
                
                dist = (haversine((f_lat,f_lng), (b_lat,f_lng)) + haversine((b_lat, f_lng), (b_lat, b_lng))) * 1000 # m단위의 manhattan dist
                distance_list.append(dist)
        
        distance_list.sort()
        
        # 걷는 속도 5km/h로 20분간 걸을 수 있는 거리는 1333m
        for i in range(len(distance_list)):
            if distance_list[i] > 1333:
                num_of_facility.append(i)
                break
    
    return num_of_facility

#%% 모든 지하철역과의 거리
def get_nearest_station(subway, building):
    
    nearest_station = {}
    distance = []
    
    for bi in building.index:
        b_lat = building.iloc[bi]['위도']
        b_lng = building.iloc[bi]['경도']
        
        subway_dict = {}
        
        for si in subway.index:
#            print(building.iloc[bi]['location'], 'to', subway.iloc[si]['지하철역'])
            s_lat = subway.iloc[si]['위도']
            s_lng = subway.iloc[si]['경도']
            
            dist = (haversine((s_lat,s_lng), (b_lat,s_lng)) + haversine((b_lat, s_lng), (b_lat, b_lng))) * 1000 # m단위의 manhattan dist
            subway_dict[subway.iloc[si]['지하철역']] = dist
        
        distance.append(subway_dict.values())
        
        sorted_subway_dict = sorted(subway_dict.items(), key=operator.itemgetter(1))
        nearest_station[bi] = [sorted_subway_dict[0][0], sorted_subway_dict[1][0], sorted_subway_dict[2][0]]
    
    subway_index_dict = {station: i for i, station in enumerate(subway['지하철역'])}
    
    df = pd.DataFrame(distance)
    df.index = building.index
    df.columns = subway_index_dict.keys()
    
    return df, nearest_station

#%%
def get_dataframe(dataframe, facility_name, dist_1st, dist_2nd, dist_3rd):
    
    dataframe['{}_1st'.format(facility_name)] = dist_1st
    dataframe['{}_2nd'.format(facility_name)] = dist_2nd
    dataframe['{}_3rd'.format(facility_name)] = dist_3rd
    
    return dataframe
   
#%%
building = pd.read_csv('../11.data/02.2.building_geometry/00.y_geometry.csv', encoding='cp949')
with open('../11.data/00.adjacent_gu.pickle', 'rb') as r:
    adjacent_gu = pickle.load(r)

#%% 최근접 시설 3개와의 거리
file_list = ['000.public_institution_dong','003.middleschool','004.highschool']

facility_name_list = ['주민센터','중학교','고등학교']

df = pd.DataFrame()
for i in range(len(file_list)):
    print(facility_name_list[i])
    dist_1st, dist_2nd, dist_3rd = get_distance_nearest_3(building, '../11.data/04.2.facilities_geometry/{}_geometry.csv'.format(file_list[i]), adjacent_gu)
    df = get_dataframe(df, facility_name_list[i], dist_1st, dist_2nd, dist_3rd)

df.index = building.index

df.to_csv('../11.data/10.features/22.주민센터,중학고,고등학교.csv', encoding='cp949')

#%% 해당 자치구 소속 시설과의 거리
file_list = ['100.public_institution_gu']

facility_name_list = ['구청']

df = pd.DataFrame()

print(facility_name_list[0])
dist_list = get_nearest_facility(building, '../11.data/04.2.facilities_geometry/{}_geometry.csv'.format(file_list[0]), adjacent_gu)
df = get_dataframe(df, facility_name_list[0], dist_list)

df.index = building.index

df.to_csv('../11.data/10.features/23.구청.csv', encoding='cp949')

#%% 일정거리 내 시설의 개수
file_list = ['200.lifeservice']

facility_name_list = ['생활서비스']

df = pd.DataFrame()
for i in range(len(file_list)):
    print(facility_name_list[i])
    num_of_facility = get_num_of_facilities(building, '../11.data/04.2.facilities_geometry/{}_geometry.csv'.format(file_list[i]), adjacent_gu)
    df = get_dataframe(df, facility_name_list[i], num_of_facility)

df.index = building.index

df.to_csv('../11.data/10.features/00.생활서비스.csv', encoding='cp949')

#%% 모든 지하철역과의 거리
subway = pd.read_csv('../11.data/03.2.subway_geometry/00.subway_geometry.csv', encoding='cp949')

df, nearest_station = get_nearest_station(subway, building)

df.to_csv('../11.data/10.features/24.지하철역까지의 거리.csv', encoding='cp949')


