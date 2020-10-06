#%%
import googlemaps
import pandas as pd

#%%
gmaps_key = "AIzaSyB_E3nbdEdLmPJhxR1xU0MKAj3BJrI-0t0"
gmaps = googlemaps.Client(key = gmaps_key)

#%%
# 역 이름, 호선 이름 전처리
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
# 서울특별시에 위치하지 않은 역 index 수집
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
# 역 및 호선 명 필터링

station_data = pd.read_csv('../11.data/03.1.subway/01.subway_sum_data.csv', encoding='utf8')
processed_station = process_station_and_line_name(station_data)
gb_station = processed_station.groupby(['지하철역']).sum()['합계']

#%%
# 역 이름 기준으로 group by
gb_st = pd.DataFrame()
gb_st['지하철역'] = gb_station.index
gb_st['총이용량'] = gb_station.values

#%%
# 서울에 존재하지 않는 역에 대한 index 수
drop_index = get_drop_index(gb_st)

#%%
# except 처리된 역들이 서울 내에 없으면 drop_index에 추가
drop_index.append(221) # 삼산체육관
drop_index.append(252) # 석수
drop_index.append(321) # 쌍용동

#%%
# 서울이 아닌 역 제거
seoul_station = gb_st.drop(gb_st.index[drop_index])

#%%
# 역 별 구 설정
gu = []
index = []
sttn = []
for i, station in enumerate(seoul_station['지하철역']):
    try:
        if gmaps.geocode(gmaps.geocode(station+'역', language='ko')[0]['address_components'][1]['long_name'], language='ko')[0]['address_components'][1]['long_name'][-1] != '구':
            if gmaps.geocode(gmaps.geocode(station+'역', language='ko')[0]['address_components'][1]['long_name'], language='ko')[0]['address_components'][0]['long_name'][-1] != '구':
                print(i, "except", station)
                index.append(i)
                sttn.append(station)
                gu.append('x')
            else:
                gu.append(gmaps.geocode(gmaps.geocode(station+'역', language='ko')[0]['address_components'][1]['long_name'], language='ko')[0]['address_components'][0]['long_name'])
        else:
            gu.append(gmaps.geocode(gmaps.geocode(station+'역', language='ko')[0]['address_components'][1]['long_name'], language='ko')[0]['address_components'][1]['long_name']) 
    except:
        gu.append('x')
        print(i, station)
        
#%%
# 수동 ㅠㅠ
gu_self = ['금천구','강서구','강남구','강동구','강동구','강동구','마포구','강서구','종로구','마포구',
           '구로구','광진구','강동구','성동구','구로구','용산구','서초구','은평구','강남구','영등포구',
           '구로구','강남구','서대문구','금천구','성북구','중구','강동구','은평구','양천구','송파구',
           '강서구','송파구','동작구','은평구','동작구','강남구','성동구','노원구','송파구','용산구',
           '성동구','영등포구','강남구','성동구','동작구','구로구','동대문구','마포구','종로구','강서구',
           '영등포구','송파구','구로구','강서구','중구','은평구','마포구','종로구','강남구','서대문구',
           '성북구','강남구','마포구','용산구']

for i, indx in enumerate(index):
    gu[indx] = gu_self[i]

#%%
# 수동 2
gu[72] = '종로구' # 동대문
gu[123] = '강북구' # 삼양
gu[188] = '중구' # 약수

#%%
# 저장
seoul_station['gu'] = gu
seoul_station.to_csv('../11.data/03.1.subway/01.seoul_station_.csv', encoding='cp949', index=False)
