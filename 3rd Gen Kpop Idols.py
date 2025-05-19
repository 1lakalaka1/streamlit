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

# 3세대 아이돌 그룹 및 데뷔 연도 (임의 선정)
groups = ["BTS", "EXO", "TWICE", "SEVENTEEN", "BLACKPINK", "Red Velvet", "NCT 127", "GOT7", "MAMAMOO", "Stray Kids"]
debut_years = [2013, 2012, 2015, 2015, 2016, 2014, 2016, 2014, 2014, 2018]

# 데이터프레임 생성
data = {
    "Group": groups,
    "Debut Year": debut_years
}
df = pd.DataFrame(data)

# ‘Generation’ 컬럼 추가
df["Generation"] = "3rd Generation"

# 정렬 적용
if option == "Newest Debut":
    df = df.sort_values("Debut Year", ascending=False)
elif option == "Oldest Debut":
    df = df.sort_values("Debut Year")

# 레이아웃 분할
col1, col2 = st.columns(2)
with col1:
    st.subheader("📅 Debut Years")
    st.dataframe(df)
with col2:
    st.subheader("📈 Debut Year Chart")
    st.bar_chart(df.set_index("Group")["Debut Year"])