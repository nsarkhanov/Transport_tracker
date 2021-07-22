"""Main module for the streamlit app"""
import streamlit as st
import src.pages.home
#import src.pages.projects
import src.pages.application
#import src.pages.skills
#import src.pages.edu
# import src.pages.recommendations
#import src.pages.notes

st.set_page_config(layout='wide')

# st.write(
#     """
#     <style>
#     .big-font {
#     font-size:200px !important;
#      }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# @st.cache(suppress_st_warning=True)
def main():
    PAGES = {
        "Home": src.pages.home,
        "Application": src.pages.application,
        # "My Notes": src.pages.notes,
        # "Education": src.pages.edu,
        # "Skills": src.pages.skills,
        # "Projects": src.pages.projects,
        # "Recommendations": src.pages.recommendations

    }

    st.sidebar.title('Navigation')
    selection = st.sidebar.selectbox("Menu", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

    st.sidebar.title("Hire US")
    st.sidebar.info(
        """
        If you are looking to hire a Data Scientist, reach out 
        to us on [LinkedIn](https://www.linkedin.com/in/nurlan-sarkhanov-8749a698/)
""")


if __name__ == "__main__":
    main()
