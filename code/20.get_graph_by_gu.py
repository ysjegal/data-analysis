#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#%%
font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#%%
# 그리고 싶은 그래프에 해당하는 데이터 입력
data = pd.read_csv('../11.data/04.1.facilities/06.elementaryschool.csv', encoding='cp949')

#%%
# 구를 기반으로 group by
gb_data = data.groupby(['gu']).count()

#%%
y_pos = np.arange(len(gb_data.index))

#%%
plt.figure(figsize=(20,10))

# count하고 싶은 column 설정하세요
plt.bar(y_pos, gb_data['location'], align='center', alpha=0.5)
plt.xticks(y_pos, gb_data.index)

# 축 이름 바꾸세요
plt.ylabel('# of facility')
          
# 그래프 이름 바꾸세요
plt.title('구 별 초등학교 수')

# 디렉토리 알아서 설정
# 맨 마지막에 파일명 바꾸세요
plt.savefig('../11.data/20.gu_graph/초등학교수')