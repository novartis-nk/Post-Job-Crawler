from django.shortcuts import render
import random 
from .link_generator import link_gen
from .card_crawl import get_cards





# Create your views here.
def get_the_form_value(request):
  data= {}
  if request.method == "POST":
    data  = request.POST
    Kword = data.get("Kword")
    #print(f'this is the returned Kword Value :{Kword}')
    city  = data.get("city")
    #print(f'this is the returned city Value :{city}')
    if city == None or city =='None':
      city=''
    urls  =link_gen(city=city, Kword=Kword)
    cards = get_cards(urls)
    
    random.shuffle(cards)
    for i in urls : print( f'this is the url :{i} /n')
    data = {
      "Kword": Kword,
      "city" : city,
      "cards": cards
    }
    return render(request, "cardView.html", data )

  urls = ['https://www.simplyhired.com/search?q=&l=remote']
  for i in urls : print( f'this is the url :{i} /n')
  cards = get_cards(urls)
  random.shuffle(cards)
  return render(request, 'index.html', {'cards' : cards})