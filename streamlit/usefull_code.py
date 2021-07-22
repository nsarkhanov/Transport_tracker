# from sys import Path
# import base64


# def img_to_bytes(img_path):
#     img_bytes = Path(img_path).read_bytes()
#     encoded = base64.b64encode(img_bytes).decode()
#     return encoded


# header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
#     img_to_bytes("header.png")
# )
# st.markdown(
#     header_html, unsafe_allow_html=True,
# )


# st.write('## Add interactions using widgets!')
# a = st.slider('Number 1')
# b = st.slider('Number 2')
# st.write('Answer is', a + b)


# sex = st.multiselect('Sex', ['male', 'female'])
# if(len(sex) == 1):
#     data = data[data.Sex == sex[0]]
# st.write(data)
