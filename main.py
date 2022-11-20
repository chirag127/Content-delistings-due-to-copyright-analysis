
import io
import zipfile
import requests
import pandas as pd

def get_all_data():
    # get data from database
    url = "https://storage.googleapis.com/transparencyreport/google-websearch-copyright-removals.zip"

    # download data
    r = requests.get(url)

    # unzip data
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

    # read data

    # read data
    df = pd.read_csv("google-websearch-copyright-removals.csv")

    # clean data
    print(df.head())