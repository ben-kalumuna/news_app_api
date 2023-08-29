from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = "https://newsapi.org/v2/everything?q=Criket&from=2023-08-16&sortBy=popularity&apiKey=e9188823509c48d4b9cfedc3a6e9273d"
    
    
    cricket_news = requests.get(url).json()
    
    
    a= cricket_news['articles']
    desc =[]
    title =[]
    img =[]
    
    for i in range(len(a)):
        f =a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToimage'])
        
    mylist =zip(title, desc, img)
    context ={'mylist': mylist}
    
    return render (request, 'index.html', context)    
        
    
    
    