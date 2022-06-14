import pandas as pd
import streamlit as st
import plotly.express as px

from dateutil import parser

from app import DCU, df_kpi_dc

st.header("Drop Identification")
st.sidebar.markdown("# Drop Dashboard - Short Term")

##### TOP WORST DC SHORT TERM #########
#######################################
st.subheader("Short Term Drop")
drop_threshold = st.slider('Drop Detection Threshold', min_value=5, max_value=30, value=10)

df_worst_dc = df_kpi_dc[df_kpi_dc["ecart_type"] <= -drop_threshold][df_kpi_dc["Info"].astype(str).str.isdigit()][df_kpi_dc["diff"] < 20]

col_list = [col for col in df_worst_dc.columns[-60:-2]]
col_list = ["DCU"] + col_list + ["diff"] + ["ecart_type"]
df_100 = df_worst_dc[col_list].reset_index()

st.dataframe(df_100[col_list])

df_chart_100 = df_100[col_list].iloc[:, :-2].T.reset_index().rename(columns={"index": "Date"})
df_chart_100.columns = ["Date"] + [x for x in df_chart_100.iloc[0, 1:].tolist()]
df_chart_100 = df_chart_100[1:]

# st.dataframe(df_chart_100.astype(str))

col1, col2 = st.columns([3,2])

for col in df_chart_100.columns[1:]:
    if int(col[-2:]) % 2 == 0:
        with col1:
            fig_kpi_dc = px.line(df_chart_100, x="Date", y=f"{col}", title=f"{col}", markers=True, text=f"{col}")
            fig_kpi_dc.update_xaxes(visible=True, fixedrange=False)
            fig_kpi_dc.update_layout(
                showlegend=True,
                plot_bgcolor="silver",
                font_family="Courier New",
                font_color="black",
                title_font_family="Times New Roman",
                title_font_color="blue",
                legend_title_font_color="green")
            fig_kpi_dc.update_traces(textposition="bottom center")
            st.plotly_chart(fig_kpi_dc)
    else:
        with col2:
            fig_kpi_dc = px.line(df_chart_100, x="Date", y=f"{col}", title=f"{col}", markers=True, text=f"{col}")
            fig_kpi_dc.update_xaxes(visible=True, fixedrange=False)
            fig_kpi_dc.update_layout(
                showlegend=True,
                plot_bgcolor="silver",
                font_family="Courier New",
                font_color="black",
                title_font_family="Times New Roman",
                title_font_color="blue",
                legend_title_font_color="green")
            fig_kpi_dc.update_traces(textposition="bottom center")
            st.plotly_chart(fig_kpi_dc)

