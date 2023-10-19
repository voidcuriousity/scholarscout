
import streamlit as st  # 🎈 data web app development
import scopuscaller as sc


@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")


st.set_page_config(
    page_title="ScholarSchout",
    page_icon="✅",
    layout="wide",
)

st.title("ScholarScout quickly finds relevant and authoritative research from SCOPUS")

api_key = st.text_input("Enter API key", "")
user_input = st.text_input(
    "Enter keywords separated by comma. e.g., transfer learning,transportation"
)
year = st.text_input(
    "The publication year to filter the articles. Default is 2023.", 2023
)
user_input = user_input.split(",")

with st.form(key="my_form_to_submit"):
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    df = sc.get_titles(api_key, user_input, year)
    df = sc.get_abstracts(df)
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button(
        "Press to Download",
        csv,
        "_".join(user_input) + ".csv",
        "text/csv",
        key="download-csv",
    )
