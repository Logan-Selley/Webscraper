from bs4 import BeautifulSoup
import requests
import json
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        #
        
app = Application()
app.master.title('test')
app.mainloop()



url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
tweetArr = []
for tweet in content.find_all('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class":"author"}).text.encode('utf-8'),
        "date": tweet.find('h5', attrs={"class":"dateTime"}).text.encode('utf-8'),
        "tweet": tweet.find('p', attrs={"class":"content"}).text.encode('utf-8'),
        "likes": tweet.find('p', attrs={"class":"likes"}).text.encode('utf-8'),
        "shares": tweet.find('p', attrs={"class":"shares"}).text.encode('utf-8')
    }
    tweetArr.append(tweetObject)
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)
    