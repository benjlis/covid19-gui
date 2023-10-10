import dotenv
import os
import requests
import streamlit as st

_ = dotenv.load_dotenv()
DC_USER = os.getenv('DC_USER')
DC_PSWD = os.getenv('DC_PSWD')
access_endpoint = "https://accounts.muckrock.com/api/token/"
params = {'username': DC_USER, 'password': DC_PSWD}
response = requests.post(access_endpoint, data = params )
refresh_token = response.json()["refresh"]
access_token = response.json()["access"]

# download metadata
DC_API = "https://api.www.documentcloud.org/api"
DC_DOC = "https://www.documentcloud.org/documents/20793561-leopold-nih-foia-anthony-fauci-emails"
# download list of documents belonging to the project
search_endpoint = f"{DC_API}/oembed?url={DC_DOC}" 
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(search_endpoint, headers=headers)
pdf_viewer=response.json()['html']

st.write("# DocmentCloud PDF Viewer")
st.markdown(pdf_viewer, unsafe_allow_html=True)
