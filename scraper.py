from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys



def get_page_links(pageDriver, baseUrl):
    a_tags = driver.find_elements_by_tag_name('a')
    #  links = [link.get_attribute('href') for link in elements if (baseUrl in link.get_attribute('href'))]

    # Get all urls
    urls = [tag.get_attribute('href') for tag in a_tags]

    #Get urls that start with baseUrl
    useful_urls = [url for url in urls if url and baseUrl in url]

    return useful_urls

def get_page_text(pageDriver):
    pageBody = pageDriver.find_element_by_xpath("/html/body")
    if not pageBody:
        return ""
    return pageBody.text


visited_urls = set()
unvisited_urls = set()
error_urls = set()
my_map = {}

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--log-level=1')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

fileName = input('Please enter file name to write: ')
baseUrl = input("Please enter website's base url: ")
unvisited_urls.add(baseUrl)

while unvisited_urls:
    # Remove url from unvisited and add it to visited
    currPage = unvisited_urls.pop()
    print(currPage)
    visited_urls.add(currPage)

    # Get page content
    try:
        driver.get(currPage)
    except:
        error_urls.add(currPage)
        print('Error getting page: ', currPage)
        continue

    # Get links
    try:
        currLinks = get_page_links(driver, baseUrl)
    except:
        error_urls.add(currPage)
        print('Error getting links: ', currPage)
        continue

    # Get text
    try:
        currText = get_page_text(driver)
    except:
        error_urls.add(currPage)
        print('Error getting text: ', currPage)
        continue

    # Add links to unvisited if they haven't been visited already
    for link in currLinks:
        if link not in visited_urls:
            unvisited_urls.add(link)

    my_map[currPage] = currText

print("-----------------------------------------DATA RECOVER IS DONE")
textToWrite = ""
if len(error_urls) > 1:
    textToWrite += "List of urls that did not work: \n"
    for url in error_urls:
        textToWrite += f"This url failed: {url}\n"
    textToWrite += "\n\n"

for key in my_map:
    textToWrite += ('-'*30 + key + '-'*30 + '\n') 
    textToWrite += f'{my_map[key]}\n\n\n\n'


textToWrite = textToWrite.encode("ascii", errors="ignore").decode()
with open(f'{fileName}.txt', 'w') as f:
    f.write(textToWrite)

sys.exit('Program finished')