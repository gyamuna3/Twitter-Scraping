Twitter-Scraping
 
Twitter is a social media platform having Trillions of data, when we need to analyse the data we cannot copy and paste all those data so We use SNSCRAPE python package.
 
In this project,I retrived data like Tweets, date, id, url, tweet content, user,reply count, retweet count, language from Twitter using a Keyword or Hashtag that is present in the Twitter systems.

I have used Streamlit to create the webpage, and Snscrape to Extract the data from Twitter. After Scraping data from Twitter, I have used Python MongoDB to store the data in a Database for future use.

I have imported the required libraries like pandas, snscarpe, and streamlit ,created my front end by using streamlit text inputs and buttons.

The user is required to provide the Username, Date range and number of tweets to be scraped. After this, the dataframe is displayed which consists of all the scraped data.

After displaying the data, It is stored in the Database by using MongoDB. Then The user may Download the file in CSV or JSON file.
