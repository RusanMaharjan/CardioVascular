import streamlit as st


def Home():
    st.Page("app.py", title='Home')
    st.header("Home")


pages = {
    "Home": [
         st.Page(Home)
    ],
    "Models": [
        st.Page("logistic.py", title='Logisitc'),
        st.Page("svm.py", title='SVM')
    ]
}

pg = st.navigation(pages, position='top')

pg.run()

