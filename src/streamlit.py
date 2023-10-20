
import streamlit as st  # 🎈 data web app development
import scopuscaller as sc


@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")


st.set_page_config(
    page_title="ScholarScout 🐦‍⬛",
    page_icon="✅",
    layout="wide",
)

st.title("ScholarScout🐦‍⬛ retrieves relevant research from SCOPUS")
st.caption("Please consider starring ⭐ the [repo](https://github.com/voidcuriousity/scholarscout), if you find it useful")

api_key = st.text_input("Enter API key. If you don't have one, you can get [here](https://dev.elsevier.com/api_key_settings.html)", "API_KEY")
user_input = st.text_input(
    "Enter two or more keywords separated by comma. e.g., transfer learning,transportation. __NO SPACE before or after comma__."
)
year = st.text_input(
    "The default year up to which articles will be searched. Default is __2023__.", 2023
)
user_input = user_input.split(",")

with st.form(key="my_form_to_submit"):
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    df = sc.get_titles(api_key, user_input, year)
    df = sc.get_abstracts(df)
    csv = convert_df(df)
    st.download_button(
        "Press to Download",
        csv,
        "_".join(user_input) + ".csv",
        "text/csv",
        key="download-csv",
    )

