import requests
from bs4 import BeautifulSoup


text = "A-W-S"
from PIL import Image, ImageDraw, ImageFont
import numpy as np
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1",size,"black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ','#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print( "\n".join(strings))

menu_text = """
        
Thanks for using A-W-S. Please use the README
to make changes to the software that best suite 
your needs.
            
       
****** SOME DISCLAIMERS ABOUT WEB SCRAPING:******
Not all websites on the internet allow web scraping.
Please check to see if the website you are going to scrape
allows it before attempting to do so. Check the sites
robot.txt by going to "url".com/robots.txt!
*************************************************
                    
                - Brendan McKenney
                
                
Please choose one of the options below.       
                    
    1. Scrape raw HTML data using a URL
    2. Enter a URL and scrape for relevant information based on HTML tags
                
"""



while True:
    print(menu_text)
    choice = input()

    if choice == '1':
        print("Please enter the url of the website you would like to scrap for data.")
        url = input()
        response = requests.get(url)
        content = BeautifulSoup(response.content, "html.parser")

        print(content)

    if choice =='2':
        print("Please enter the URL:")
        url = input()
        response = requests.get(url)
        target = BeautifulSoup(response.content, "html.parser")

        description = target.find_all('p', attrs={"class": "description"})
        price = target.find_all('h4', attrs={"class": "pull-right price"})

        print(description)
        print(price)
