
import streamlit as st  # 🎈 data web app development
import scopuscaller as sc

@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")


st.set_page_config(
    page_title="ScholarScout 🐦‍⬛",
    page_icon="✅",
    # layout="wide",
)

st.title("ScholarScout🐦‍⬛ retrieves relevant research from SCOPUS")
st.caption("Please consider starring ⭐ the [repo](https://github.com/voidcuriousity/scholarscout), if you find it useful")

api_key = st.text_input("Enter API key. If you don't have one, you can get [here](https://dev.elsevier.com/api_key_settings.html)", "API_KEY")
user_input = st.text_input(
    "Enter two or more keywords separated by comma. __NO SPACE before or after comma__ . Unless your keywords are already quite niche, using 3-4 keywords is often a good practice. e.g., vulnerable users,transportation,road safety"
)
year = st.text_input(
    "The default year up to which articles will be searched. Default is __2023__.", 2023
)
user_input = user_input.split(",")

with st.form(key="my_form_to_submit"):
    submit_button = st.form_submit_button(label="Submit")
    
if submit_button:
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    
    try:
        df = sc.get_titles(api_key, user_input, year)
        my_bar.progress(25, text=progress_text)
        df = sc.get_abstracts(df)
        my_bar.progress(100, text=progress_text)
        
        my_bar.empty()
        csv = convert_df(df)
        st.download_button(
            "Press to Download",
            csv,
            "_".join(user_input) + ".csv",
            "text/csv",
            key="download-csv",
        )

    except Exception as KeyError:
        st.error('There seems to be something wrong. Check your API and keywords', icon="🚨")

st.subheader("FAQs")
st.markdown("__1. What is SCOPUS API?__")
st.markdown("- The SCOPUS API enables users to query its extensive database for articles based on specific keywords. To access this API, users need to create an account on SCOPUS, either through their university or personally, and generate an API key. The API specifications can be found at this [link](https://dev.elsevier.com/api_key_settings.html). By utilizing this API, users can retrieve information such as the title, authors, affiliations, DOIs, and more from scientific articles. Additionally, depending on the article's access level and authorized API, it is also possible to obtain the article's abstract text.")

st.markdown("__2. How do i get SCOPUS API?__")
st.markdown("- If you haven't already created a SCOPUS account, please visit the SCOPUS platform and create a private account, or use your university credentials. Once logged in, you can create a new API key by following these steps. Provide a label of your choice, and you can leave the website input field empty as it is not essential. Before using the API and accessing data, it's crucial to carefully review and understand the \"API SERVICE AGREEMENT\" and \"Text and Data Mining (TDM) Provisions,\" which will be presented to you during the API key generation process. Make sure to copy your API key for later use.")

st.markdown("__3. Why does it Utilize the Semantic Scholar Database?__")
st.markdown("- The ability to retrieve abstracts from SCOPUS depends on the API level. In our experience, abstracts are generally not accessible via SCOPUS. As a result, we leverage the Semantic Scholar database to obtain article abstracts.")

st.markdown("__4. How to Properly Acknowledge ScholarScout🐦‍⬛?__")
st.markdown("- If you found ScholarScout🐦‍⬛ useful, we would greatly appreciate it if you could cite or attribute it in your work. For details on attributing parent repositories, please check the [pypi package](https://pypi.org/project/scopus-caller/) for details.")

st.markdown("__5. The application runs for an extended period without producing any results?__")
st.markdown("- This typically happens when your search keywords are too broad, resulting in a large number of articles to be retrieved. To address this, consider adding more specific keywords to fine-tune your search. Unless your keywords are already quite niche, using 3-4 keywords is often a good practice.")

st.markdown("__6. Encountering Issues?__")
st.markdown("- We sincerely apologize for any inconvenience you may have experienced. As ScholarScout🐦‍⬛ is still in its early stages of development, we are actively monitoring and addressing issues on an ongoing basis. Your feedback is highly valuable in helping us improve the service. If you encounter any issues or have suggestions, please feel free to open an issue on [GitHub](https://github.com/voidcuriousity/scholarscout). ")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)