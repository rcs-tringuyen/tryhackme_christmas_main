# Import the libraries we downloaded earlier
# if you try importing without installing them, this step will fail


# this parses the webpage into something that beautifulsoup can read over
soup = BeautifulSoup(html.content, 'lxml')
# lxml is just the parser for reading the html 
# this is the line that grabs all the links # stores all the links in the links variable
links = soup.find_all('a') 
for link in links:      
    # prints each link    
    print(link)