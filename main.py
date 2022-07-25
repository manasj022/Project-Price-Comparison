import requests,webbrowser
from bs4 import BeautifulSoup
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

 
# to search
query = input("Enter the name of the product : ") 
#
######

#For amazon
query_a=query+" amazon"
for j in search(query_a, tld="co.in", num=1, stop=1, pause=2):
    print(j)
##

#For Flipkart
query_f=query+" flipkart"
for k in search(query_f, tld="co.in", num=1, stop=1, pause=2):
    print(k)


#For retrieving the prices
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.65'}
amazon_response=requests.get(j,headers=headers)
amazon_soup=BeautifulSoup(amazon_response.content,"html.parser")
amazon_price=float(amazon_soup.find('span',attrs='a-price-whole').text.replace(",",""))




flipkart_response=requests.get(k,headers=headers)
flipkart_soup=BeautifulSoup(flipkart_response.content,"html.parser")
flipkart_price=float(flipkart_soup.find('div',attrs="_30jeq3 _16Jk6d").text.replace(",","")[1:])






print("Price on Amazon is : ₹",str(amazon_price))
print("Price on Flipkart is : ₹",str(flipkart_price))
