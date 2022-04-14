from django.shortcuts import render
# Create your views here.
import pandas as pd
import pymongo  # for mongodb access
import pandas as pd
import requests
from newspaper import Article
import nltk
nltk.download('punkt')
import os 

conn = os.getenv( "MONGODB_URI")
client = pymongo.MongoClient(conn)
general=[]
Entertainment=[]
business=[]
health=[]
science=[]
sports=[]
technology=[]
urlS=''
# Create a database
def putData():
    
# Establish connection
    conn = os.getenv( "MONGODB_URI")
    client = pymongo.MongoClient(conn)

# Import the csv files
    db = client.Headlines
    business = pd.read_csv('business.csv')
    entertainment = pd.read_csv('entertainment.csv')
    general=pd.read_csv('general.csv')
    health=pd.read_csv('health.csv')
    science=pd.read_csv('science.csv')
    sports=pd.read_csv('sports.csv')
    technology=pd.read_csv('technology.csv')

    data = business.to_dict(orient='records')
    db.business.insert_many(data)

    data = entertainment.to_dict(orient='records')
    db.entertainment.insert_many(data)

    data = general.to_dict(orient='records')
    db.general.insert_many(data)

    data = health.to_dict(orient='records')
    db.health.insert_many(data)

    data = science.to_dict(orient='records')
    db.science.insert_many(data)

    data = sports.to_dict(orient='records')
    db.sports.insert_many(data)

    data = technology.to_dict(orient='records')
    db.technology.insert_many(data)

def getData():
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    for list in categories:

        url = ('http://newsapi.org/v2/top-headlines?'
            'country=us&'
            'category=' + list + '&'
                                'language=en&'
                                'apiKey=0e97cac02d994073b9a7d649b05e16f7')
        urlResponse = requests.get(url)
        urlResponse = urlResponse.json()
        articles = []
        for item in urlResponse['articles']:
            dict = {

                "title": item['title'],
                "urlToImage": item['urlToImage'],
                "description": item['description'],
                "url": item['url']
            }
            articles = articles + [dict]

        conn = os.getenv( "MONGODB_URI")
        client = pymongo.MongoClient(conn)

        if len(articles) > 0:
            df = pd.DataFrame(urlResponse['articles'])
            df = df.loc[:, ["title", "urlToImage","url"]]
            df.to_csv(list + '.csv')
def delData():
    conn = os.getenv( "MONGODB_URI")
    client = pymongo.MongoClient(conn)

# Create a database
    db = client.Headlines

    db.business.delete_many({})
    db.entertainment.delete_many({})
    db.general.delete_many({})
    db.health.delete_many({})
    db.science.delete_many({})
    db.sports.delete_many({})
    db.technology.delete_many({})
def extractData():
    conn = os.getenv( "MONGODB_URI")
    client = pymongo.MongoClient(conn)
    db = client.Headlines

    hG = pd.DataFrame(db.general.find())

    count=1
    global general
    for (i,j,k) in zip(hG.title,hG.urlToImage,hG.url):

        general=general+[
        {"id":count,"name":i,"image":j,"url":k},
        ]
        count=count+1

    hG = pd.DataFrame(db.entertainment.find())

    count=1
    global Entertainment

    for (i,j,k) in zip(hG.title,hG.urlToImage,hG.url):
        Entertainment=Entertainment+[
        {"id":count,"name":i,"image":j,"url":k},
        ]
    
        count=count+1


    hG = pd.DataFrame(db.business.find())

    count=1
    global business
    for (i,j,k) in zip(hG.title,hG.urlToImage,hG.url):
        business=business+[
        {"id":count,"name":i,"image":j,"url":k},
        ]
    
        count=count+1



    hG = pd.DataFrame(db.health.find())
    count=1
    global health
    for (i,j,k) in zip(hG.title,hG.urlToImage,hG.url):
        health=health+[
        {"id":count,"name":i,"image":j,"url":k},
        ]
    
        count=count+1

    hG = pd.DataFrame(db.science.find())
    count=1
    global science
    for (i,j,k) in zip(hG.title,hG.urlToImage,hG.url):
        science=science+[
        {"id":count,"name":i,"image":j,"url":k},
        ]
    
        count=count+1


    hG = pd.DataFrame(db.sports.find())
    count=1
    global sports
    for (i,j,k) in zip(hG.title,hG.urlToImage,hG.url):
        sports=sports+[
        {"id":count,"name":i,"image":j,"url":k},
        ]
    
        count=count+1


    hG = pd.DataFrame(db.technology.find())
    count=1
    global technology
    for (i,j,k) in zip(hG.title,hG.urlToImage,hG.url):
        technology=technology+[
        {"id":count,"name":i,"image":j,"url":k},
        ]
    
        count=count+1


def home(request):
    delData()
    getData()
    putData()
    extractData()
    
    return render(request,'home.html',{'title': 'Home','general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})

def scienceNews(request):  
    delData()
    getData()
    putData()
    extractData()  
    return render(request,'science.html',{'title': 'Science','general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})

def sportsNews(request):  
    delData()
    getData()
    putData()
    extractData()  
    return render(request,'sports.html',{'title': 'Sports','general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})

def technologyNews(request):  
    delData()
    getData()
    putData()
    extractData()  
    return render(request,'technology.html',{'title': 'Technology','general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})

def businessNews(request):  
    delData()
    getData()
    putData()
    extractData()  
    return render(request,'business.html',{'title': 'Business','general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})

def healthNews(request):  
    delData()
    getData()
    putData()
    extractData()  
    return render(request,'health.html',{'title': 'Health','general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})

def entertainmentNews(request):  
    delData()
    getData()
    putData()
    extractData()  
    return render(request,'entertainment.html',{'title': 'EntertainmentNews','general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})

def summarize(request,pk1,pk2):
    putData()
    extractData()

    
    pk2=(int(pk2))
    pk2=pk2-1
    print(pk2)
    url=''
    if(pk1=='general'):
        list=general[pk2]
        url=list['url']
    if(pk1=='entertainment'):

        list=Entertainment[pk2]
        url=list['url']
    if(pk1=='business'):
        list=business[pk2]
        url=list['url']  
    if(pk1=='sports'):
        list=sports[pk2]
        url=list['url'] 
    if(pk1=='science'):
        list=science[pk2]
        url=list['url']
    if(pk1=='technology'):
        list=technology[pk2]
        url=list['url']
    if(pk1=='health'):
        list=health[pk2]
        url=list['url']
    
    my_article = Article(url, language="en")
    my_article.download()
    my_article.parse()

    my_article.nlp()
    summary={}
    summary=my_article.summary
    
    
    return render(request,'summarize.html',{"sum":summary})


