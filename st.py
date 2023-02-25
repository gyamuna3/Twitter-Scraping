import streamlit as st
import snscrape.modules
import snscrape.modules.twitter as sntwitter
import pandas as pd
from io import BytesIO
import pyxlsb
from pyxlsb import open_workbook as open_xlsb

st.image("twitter1.jpg")
st.header("TWITTER SCRAPING")
st.subheader("Lets scrape some tweets")
user = st.text_input("Enter the key to scrape")
limit = st.slider("How many tweets do you want to get?", 0, 1000, step=10)
fromdate = st.date_input("Start date") 
enddate = st.date_input("Last date")
   

# list to append tweet data to
tweets_list2 = []

#TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'query:{user} since:{fromdate} until:{enddate}').get_items()):
    if i>limit:
        break
    tweets_list2.append([tweet.id,tweet.url, tweet.username, tweet.count, tweet.content,tweet.outlinksss])
    
#dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['ID','URL', 'Username', 'Count', 'Content','Outlinks'])
st.dataframe(tweets_df2)


st.download_button("Click to Download Csv file",
                   tweets_df2.to_csv(),
                   mime ='text/csv')


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer,index = True,sheet_name ='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

df = to_excel(tweets_df2)
st.download_button("Click to Download Excel File",
                   data= df)


