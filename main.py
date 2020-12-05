# Brendan McKenney
# CSI-160
# Professor Blumberg


import requests
from bs4 import BeautifulSoup
import pyfiglet
from termcolor import colored

banner = pyfiglet.figlet_format("C-W-S")
url_hist = []
readme = """
Hello! I created this program for my CSI-160 Python programming course.
This is my final project for the course.
This web scraper is designed to work with any website that allows for web scraping.
As long as the user can find the Class name and class type they want to retrieve,
they can do so by entering it.

This program gives you the option to save

"""

intro_text = """


****** SOME DISCLAIMERS ABOUT WEB SCRAPING:******
Not all websites on the internet allow web scraping.
Please check to see if the website you are going to scrape
allows it before attempting to do so. Check the sites
robot.txt by going to "url".com/robots.txt!
*************************************************

                - Brendan McKenney

"""

menu_text = """
Please choose one of the options below.

    1. Scrape raw HTML data using a URL
    2. Enter a URL and scrape for relevant information based on HTML tags
    3. View your URL history
    4. Delete a URL from your URL history
    5. Clear URL history
    6. readme!

"""
print("\n\n\n")
print(colored("COOL WEB SCRAPER", 'red'))
print(intro_text)


def bulk_retriever(url):
    global content

    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")

    return content


def targeted_search(url_targeted, class_type, class_name):
    global type1

    response = requests.get(url_targeted)
    targeted_content = BeautifulSoup(response.content, "html.parser")

    type1 = targeted_content.find_all(class_type, attrs={"class": class_name})

    return type1


def add_url(url):
    entry = [url]
    url_hist.append(url)


def delete_url(url):
    for url in url_hist:
        if url_hist[0] == url:
            url_hist.remove(url)
        else:
            print("Couldn't find this URL for deletion. Make sure it was typed correctly.")


while True:
    print(banner)
    print(menu_text)
    choice = input()

    if choice == '1':
        try:
            print('Please enter the url of the website you would like to scrape for data:')
            url = input()
            print("WAIT! Would you like to save this URL to your URL history? ('y' or 'n')")
            save = input()
            if 'y' in save:
                add_url(url)
                print("*! URL saved to URL history.")

            else:
                print("URL NOT saved to history.")
            print(colored('*! Getting website content...', 'red'))
            print(colored('*! Just one second...', 'red'))
            print("\n\n\n")
            bulk_retriever(url)

            print(content)
        except:
            print(
                "*! Something went wrong. Check the url you entered and that the site you're trying to scrape allows it.")

    if choice == '2':
        try:
            print("Please enter the URL:")
            url_targeted = input()
            print("WAIT! Would you like to save this URL to your URL history? ('y' or 'n')")
            save = input()
            if 'y' in save:
                add_url(url_targeted)
                print(colored("*! URL saved to URL history.", 'red'))

            else:
                print(colored("URL NOT saved to history.", 'red'))
        except ValueError:
            print("*! Looks like you didn't type a value in the correct form.")
        try:
            print("If you know it, type the content type: (Ex. 'p' for a paragraph or 'h4' for heading 4)")
            class_type = input()
            print("Finally, type in the full name of the class: (Ex. 'description' or 'ratings')")
            print(colored("*! Remember: this won't work if the class name or class type doesn't exist on the site.",
                          'red'))
            class_name = input()

            targeted_search(url_targeted, class_type, class_name)
            print(type1)
        except:
            print(
                "*! Oops. Something went wrong. Check that your HTML parameters you entered exist on the site, "
                "and that you're requested site allows scraping.")

    if choice == '3':
        print(url_hist)

    if choice == '4':
        print(url_hist)
        print("Please enter the URL you'd like to delete from your history: ")
        url = input()
        delete_url(url)

        print(url_hist)


    if choice == '5':
        print("Clear your URL history? ('y' or 'n')")
        del_hist = input()
        if 'y' in del_hist:
            try:
                url_hist.clear()
                print("URL history: ", url_hist)
                print(colored("*! URL history cleared.", 'red'))
            except:
                print("Might be nothing to delete.")
        else:
            print("Won't delete history.")


    if choice == '6':
        print(readme)
