import streamlit as st
import pandas as pd
import plotly.express as px

st.title("WiFi Data Analysis")

# File uploader widget
uploaded_file = st.file_uploader("Choose the measurement .csv file:", type=['csv'])

if uploaded_file is not None:
    # read the csv file
    df = pd.read_csv(uploaded_file)

    # computing the statistics - create a class to do this
    ping_stats = {
    "Start Time": pd.to_datetime(df["timestamp"].iloc[0]).strftime("%Y:%m:%d %H:%M:%S"),
    "End Time": pd.to_datetime(df["timestamp"].iloc[-1]).strftime("%Y:%m:%d %H:%M:%S"),
    "Average": f"{df["ping"].mean():.2f} ms",
    "Std": f"{df["ping"].std():.2f} ms",
    "Min": f"{df["ping"].min():.2f} ms",
    "Max": f"{df["ping"].max():.2f} ms"
    }

    # ping - display statistics
    st.write(f"**Ping - Statistics**")

    # st.write(f"**Average**: ", f"{df["ping"].mean():.2}")
    st.write(ping_stats)
    
    # timeseries data
    st.write(f"**Ping - TimeSeries Trend**")
    st.line_chart(df["ping"])

    # plotly histogram
    st.write(f"**Ping - Histogram**")
    fig = px.histogram(
        df["ping"], 
        x = "ping", 
        nbins = 60, 
    )

    fig.update_layout(bargap=0.1)
    st.plotly_chart(fig, width='stretch')