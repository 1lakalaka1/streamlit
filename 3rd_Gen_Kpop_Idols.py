import streamlit as st
import pandas as pd
import random

# 페이지 설정
st.set_page_config(page_title="3rd Generation K-Pop Idols", layout="wide")
st.title("🎤 3rd Generation K-Pop Idols")

# 사이드바 필터
st.sidebar.header("View Options")
option = st.sidebar.selectbox(
    "Sort by",
    ["All", "Newest Debut", "Oldest Debut"]
)

# 3세대 아이돌 그룹 및 데뷔 연도 (임의 선정 및 조정)
groups = ["BTS", "EXO", "TWICE", "SEVENTEEN", "BLACKPINK", "Red Velvet", "NCT 127", "GOT7", "MAMAMOO", "Stray Kids"]
debut_years = [2013, 2012, 2015, 2015, 2016, 2014, 2016, 2014, 2014, 2018]

# 데뷔 연도를 2010~2019 범위로 조정 (단순히 예시를 위한 조정)
adjusted_debut_years = [year if 2010 <= year <= 2018 else random.randint(2010, 2018) for year in debut_years]

# 데이터프레임 생성
data = {
    "Group": groups,
    "Debut Year": adjusted_debut_years
}
df = pd.DataFrame(data)

# ‘Generation’ 컬럼 추가
df["Generation"] = "3rd Generation"

# 정렬 적용
if option == "Newest Debut":
    df = df.sort_values("Debut Year", ascending=False)
elif option == "Oldest Debut":
    df = df.sort_values("Debut Year")

# 데뷔 연도별 그룹 수 집계 (꺾은선 그래프를 위해)
debut_year_counts = df.groupby("Debut Year").size().reset_index(name="Number of Groups")

# 레이아웃 분할
col1, col2 = st.columns(2)
with col1:
    st.subheader("📅 Debut Years")
    st.dataframe(df)
with col2:
    st.subheader("📈 Debut Year Trend (2010-2018)")
    # 꺾은선 그래프 표시
    debut_years_range = range(2010, 2019)
    debut_counts_dict = {year: 0 for year in debut_years_range}
    for year, count in zip(debut_year_counts["Debut Year"], debut_year_counts["Number of Groups"]):
        if year in debut_counts_dict:
            debut_counts_dict[year] = count
    
    debut_counts_df = pd.DataFrame(list(debut_counts_dict.items()), columns=['Year', 'Count'])
    st.line_chart(debut_counts_df.set_index("Year"))
