r'''
Here we create a function for generating costumized ulr for sites that we want to crawl 
this is how it should work:
  for each website that we wanna crawl, first we should see how the url works and changes when we search 
  for a specific keyword, or applying a filter on search, then we find where to put the variables in url 
  to get the result that we want .
'''
def link_gen(city='', Kword='' ):
  # for e estekhdam
  urls =[]
  # generating url for example.com 
  if Kword != '' or city !='':
      url = f'https://www.simplyhired.com/search?q={Kword}&l={city}'
      url = url.strip()
      url = url.replace(" ", "+")
      urls.append(url)
  else:
    urls.append('none')

  return urls
