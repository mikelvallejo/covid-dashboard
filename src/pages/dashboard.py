import streamlit as st
from datetime import datetime, timedelta
from src.pages.utils.fetch_url import fetch_url
from src.pages.utils.load_data import load_data
from src.pages.utils.load_css import local_css
from src.pages.utils.load_time_series import load_time_series


def main():
    date = datetime.today()
    df=None
    while True:
        try:
            df = load_data(fetch_url(date))
        except Exception as e:
            date = date - timedelta(days=1)
            continue
        break
    df = df[['Country_Region', 'Last_Update', 'Confirmed', 'Deaths', 'Incident_Rate', 'Case_Fatality_Ratio']]

    st.title('Total stats by country')
    country_selected = st.selectbox('Select Country', df['Country_Region'].unique())
    by_country = df[df.Country_Region == country_selected].groupby(['Country_Region']).agg({'Last_Update': 'max', 'Confirmed': 'sum', 'Deaths': 'sum', 'Incident_Rate': 'mean', 'Case_Fatality_Ratio': 'mean'}).reset_index()
    st.dataframe(by_country)