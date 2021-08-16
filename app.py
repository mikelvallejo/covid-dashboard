import streamlit as st
import src.pages.home
import src.pages.data
import src.pages.dashboard
import src.pages.contribute
import src.pages.about


PAGES = {
    "Home": src.pages.home,
    "Data": src.pages.data,
    "Dashboard": src.pages.dashboard,
}

def main():
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Navigate", list(PAGES.keys()))
    PAGES[choice].main()
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is built using [Streamlit](https://streamlit.io) by [Mikel Vallejo](hhttps://github.com/mikelvallejo).
        """
    )
    st.sidebar.title("Contribute")
    st.sidebar.info("Feel free to contribute to this open source project. The github link can be found "
                    "[here](https://github.com/mikelvallejo/covid-dashboard)")

if __name__ == "__main__":
    main()