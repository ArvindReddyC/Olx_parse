from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
final = ''    #results are appended to this string.

#======================For loop to get results based on price==============

for i,y in zip([40000,50000,60000,70000],[50000,60000,70000,80000]):
    html =   requests.get(f'https://www.olx.in/hosur_g4059174/q-iphone-12?filter=price_between_{i}_to_{y}&isSearchCall=true&sorting=asc-price',headers=headers)
    soup = BeautifulSoup(html.content,'html.parser')
    li_items = soup.find_all('li',{'data-aut-id':'itemBox'}) 
    for each_item in li_items:
        final = final +  'https://www.olx.in'+each_item.a['href'] + '\n'
        for each_span in each_item.find_all('span'):
            final = final + each_span.get_text() +'\n'

#======================Writing results to a txt file ==============
text_file = open("listings.txt", "w")
text_file.write(final)
text_file.close()
