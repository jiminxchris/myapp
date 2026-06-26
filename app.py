import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 앱 제목 및 설명 설정
st.title('California Housing Data Dashboard')
st.write('캘리포니아 주택 데이터를 시각화하는 웹 대시보드입니다.')

# 2. 데이터 로드 함수 (캐싱을 통해 매번 파일을 다시 읽지 않도록 최적화)
@st.cache_data
def load_data():
    # 데이터 파일이 app.py와 같은 폴더에 있다고 가정합니다.
    return pd.read_csv('california_housing_train.csv')

# 데이터 불러오기
df = load_data()

# 3. 데이터프레임 미리보기
st.subheader('데이터프레임 미리보기')
st.dataframe(df.head()) # display() 대신 st.dataframe() 사용

# 4. 첫 번째 시각화: 수입과 집값의 관계
st.subheader('Median Income vs Median House Value')
fig1, ax1 = plt.subplots(figsize=(10, 6)) # Streamlit에서는 객체 지향 방식을 권장합니다.
ax1.scatter(df['median_income'], df['median_house_value'], alpha=0.5)
ax1.set_title('Median Income vs Median House Value')
ax1.set_xlabel('Median Income')
ax1.set_ylabel('Median House Value')
ax1.grid(True)
st.pyplot(fig1) # plt.show() 대신 st.pyplot() 사용

# 5. 두 번째 시각화: 주택 연식 분포
st.subheader('Distribution of Housing Median Age')
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.hist(df['housing_median_age'], bins=30, edgecolor='black')
ax2.set_title('Distribution of Housing Median Age')
ax2.set_xlabel('Housing Median Age')
ax2.set_ylabel('Frequency')
ax2.grid(True)
st.pyplot(fig2)
