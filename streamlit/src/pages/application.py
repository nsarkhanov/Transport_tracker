# # st.markdown('You dont burn any calorie ')
# from src.pages.time_series import time_series
import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import joblib
import time
from sklearn.pipeline import Pipeline, make_pipeline
from PIL import Image
from sys import stdout


@st.cache()
def load_data():
    df = pd.read_csv('./data/test_data.csv')
    return df


def times(df, clf):
    X = df.drop('target', axis=1)
    y = df.target
    s = clf.score(X, y)*100

    st.success("model score: %.1f" % s)

    predictions = []
    for i in range(df.shape[0]):
        x_test = df.drop('target', axis=1).values[i].reshape(1, -1)
        x_test = pd.DataFrame(
            x_test, columns=df.drop('target', axis=1).columns)
        time.sleep(0.11)
        pred = clf.predict(x_test)
        if pred == 'Car':
            predictions.append('Car')
        elif pred == 'Still':
            predictions.append('Still')
        elif pred == 'Walking':
            predictions.append('Walking')

        if len(predictions) == 5:
            still_cont = 0
            walk_cont = 0
            car_cont = 0
            time.sleep(0.41)
            for p in predictions:
                if p == 'Still':
                    still_cont += 1
                elif p == 'Car':
                    car_cont += 1
                elif p == 'Walking':
                    walk_cont += 1
            if still_cont >= 3:
                st.write('You are currently in still position')
            elif walk_cont >= 3:
                st.write('You are currently walking')
            elif car_cont >= 3:
                st.write('You are currently in a car')
            predictions.remove(predictions[0])


@st.cache()
def load_pip():
    preprocessor = joblib.load('./model/preprocessor.x')
    model = joblib.load('./model/model.x')
    return model, preprocessor


# @st.cache(suppress_st_warning=True)
def app():
    st.title("Machine Learning Application - :male-construction-worker: ")
    st.subheader("Upload  Dataset")
    train_data = st.file_uploader("", type=['csv'])
    df = load_data()
    X = df.drop('target', axis=1)
    y = df.target
    sample = pd.read_csv('./data/sample.csv')
    model, preprocessor = load_pip()
    clf = Pipeline([('pre', preprocessor), ('classification', model)])
    clf.predict(X)
    score = clf.score(X, y)*100
    data_agree = st.checkbox('If you dont have data try ')

    if train_data is not None:
        file_info = {'file name': train_data.name,
                     'file type': train_data.type}
        st.write(file_info)
        st.subheader('Train data loaded ')

    if data_agree:
        info_data = st.checkbox('info about our data')

        if info_data:
            st.warning('Uploading data')
            upload_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.021)
                upload_bar.progress(percent_complete + 1)
            st.success(
                """ Data is collected from differet users. \nIt contains 70 columns and has  so many missing values.""")
            st.markdown("")
            st.markdown("")
            st.markdown("Raw data from users ")
            st.dataframe(df)
            st.markdown("")
            st.markdown("")
            st.warning('Check missing  values')
            st.dataframe(df.isna().sum())
            st.markdown("")
            st.markdown("")
            st.subheader("Look the data describtion ")
            st.markdown("")
            st.dataframe(df.describe())
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.subheader("Lets talk about our model")
            st.markdown("")

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        prep = st.checkbox("Preprocessing section")
        if prep:
            st.markdown(preprocessor)

    with col2:

        model_info = st.checkbox("The Best Model")
        if model_info:
            st.markdown(model)
    with col3:
        optuna_info = st.checkbox("Optuna best parameters")
        if optuna_info:
            st.markdown(
                """ max_depth': 31, 'n_estimators': 424, 'learning_rate': 0.03442141971119425, 'min_data_in_leaf': 33""")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.title("Run the model with best parameters ")
    start = st.checkbox('Start the Machine')
    if start:
        st.warning('Predicting')
        pred_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.041)
            pred_bar.progress(percent_complete + 1)

        st.success("Result ")
        st.write(round(score, 2))

    tracker = st.subheader('Position Tracker ')
    if tracker:
        start_b = st.checkbox("Start  position tracker ")
        if start_b:
            pred_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.0041)
                pred_bar.progress(percent_complete + 1)
            times(sample, clf)
            # stdout.write(times(sample, clf))

    pred = st.checkbox('Calorie calculator')
    if pred:
        p = ['No', 'Yes']
        next_ = st.radio("What is your choice?", p)
        if next_:
            st.subheader("What is your position")

            coll1, coll2, coll3 = st.beta_columns(3)
            if next_ == 'Yes':
                with coll1:
                    car_cal = st.checkbox('You use Car')
                    if car_cal:
                        st.markdown('You dont burn any calorie ')
                with coll2:
                    walking_cat = st.checkbox("You are walking ")
                    if walking_cat:
                        st.markdown(
                            'You have burned some calories')
                with coll3:
                    still_cal = st.checkbox("You are not moving")
                    if still_cal:
                        st.markdown('You dont burn any calorie ')
