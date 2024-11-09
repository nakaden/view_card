import streamlit as st
import pandas as pd

st.title("csv checker")

uploader = st.file_uploader("Choose a file")

if uploader is not None:
    df = pd.read_csv(uploader)
    columns = st.multiselect("列の絞り込み", df.columns, [df.columns[0]])

    # 列選択
    filterd_df = df[columns]

    # 詳細検索
    col1 , col2,  col3, col4 = st.columns((2, 1, 2, 1))
    with col1:
        more_filter = st.selectbox(label="列", options=columns, label_visibility="collapsed")
    with col2:
        st.text("が")
    with col3:
        word = st.text_input(label="文字列", label_visibility="collapsed")
    with col4:
        st.text("を含む")

    # テーブルデータ表示
    if word:
        # 特定の文字を含む行に絞り込んで表示する
        # https://note.nkmk.me/python-pandas-str-contains-match/#strcontains
        st.dataframe(filterd_df[filterd_df[more_filter].str.contains(word, na=False)])
    else:
        st.dataframe(filterd_df)
