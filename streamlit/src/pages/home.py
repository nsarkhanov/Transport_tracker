import streamlit as st
from PIL import Image


def app():

    ####################################################
    header = st.beta_container()
    team = st.beta_container()
    project = st.beta_container()
    activities = st.beta_container()
    github = st.beta_container()

    ####################################################
    with header:
        st.title("Prediction of actions of  People ")
        image = Image.open('./assets/1.png')
        st.image(image, caption='Machine Learning', use_column_width=False)

        st.markdown("")

        st.markdown("")
        with team:
            st.title('Huawei Fit Team ')
            image = Image.open('./assets/jb.png')
            st.image(image, caption='Team members', use_column_width=False)
            col1, col2, col3, col4, col5 = st.beta_columns(5)
            with col1:
                image = Image.open('./assets/ola.jpeg')
                st.image(image, caption="")
                st.markdown(
                    '[  Olatunde Salami](https://www.linkedin.com/in/olatunde-salami/)')
            with col2:
                image = Image.open('./assets/agatiya.jpeg')
                st.image(image, caption="")
                st.markdown(
                    '[  Agathiya Raja](https://www.linkedin.com/in/agathiya-raja-62877213b/)')
            with col3:
                image = Image.open('./assets/than.jpeg')
                st.image(image, caption="")
                st.markdown(
                    '[  Thanh Nguyen](https://www.linkedin.com/in/nguyenphuocxuanthanh/)')
            with col4:
                image = Image.open('./assets/pathi.jpeg')
                st.image(image, caption="")
                st.markdown(
                    '[  Lakshmipathi rao Devalla](https://www.linkedin.com/in/devalla-lakshmipathirao/)')
            with col5:
                image = Image.open('./assets/nurlan.jpeg')
                st.image(image, caption="")
                st.markdown(
                    '[  Nurlan Sarkhanov](https://www.linkedin.com/in/nurlan-sarkhanov-8749a698/)')
            st.text(' ')
            st.text(' ')
    with project:
        st.header('About Project')
        st.subheader("Analysis sensors data")
        st.markdown(
            """### * Information  *
Our dataset is based on the thirteen users who collected the data during their 
daily activities. \nThe dataset includes all sensors available in phones and distinguishes
five transportation modes: \nbeing on a car, on a bus, on a train, standing still and walking.
The dataset was used to build different models, whit different classification algorithms \n
-    DecisionTreeClassifier\n
-    KNeighborsClassifier\n
-    LogisticRegression\n
-    RandomForestClassifier\n
-    GradientBoostingClassifier\n
-    XGBClassifier\n
-    LGBMClassifier\n
-    GaussianNB\n
-    SVC(kernel="linear", C=0.025)\n
-    SVC(gamma=2, C=1)\n
-    MLPClassifier \n  
-    QuadraticDiscriminantAnalysis\n
-    GaussianProcessClassifier\n
reaching a maximum level of accuracy of ** 96% **.


""")

    with activities:

        st.header('Activities from Kanban')
        image2 = Image.open('./assets/kanban.png')
        st.image(image2, caption='Team  Timetable', use_column_width=True)
        st.text(' ')

    with github:
        # github section:
        st.header('GitHub / Instructions')
        st.markdown(
            'Check the instruction [here](https://github.com/Huawei-Watch-Strive-School/Building-Week-2/)')
        st.text(' ')
