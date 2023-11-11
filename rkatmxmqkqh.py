mport streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("데이터 시각화 및 파일 업로드")

    # 파일 업로드
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type="csv")

    if uploaded_file is not None:
        # 업로드된 파일을 DataFrame으로 읽기
        df = pd.read_csv(uploaded_file)

        # 데이터 프레임 출력
        st.write("업로드된 데이터 프레임:", df)

        # 데이터 프레임의 기본 통계 정보 출력
        st.write("데이터 프레임의 기본 통계 정보:", df.describe())

        # 선택한 컬럼의 히스토그램 그리기
        selected_column = st.selectbox("히스토그램을 그릴 컬럼 선택:", df.columns)
        plt.figure(figsize=(8, 6))
        sns.histplot(df[selected_column], bins=20, kde=True)
        st.pyplot()

if __name__ == "__main__":
    main()
