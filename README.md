##### I developed this script to help a NWMSU faculty with an investigation project. She needed to scrape all text from a website, including all pages in the website.

##### There are websites with hundreds and hundres of pages so this was not something easily achieved by hand but fairly easy with this automation tool.

##### The scraper receives name of the file to write all text to as well as base url of the website.

### FOR EXAMPLE with filename to write=TEST and website's base url=https://www.juangrosso.com/ the scraper will do the following:

1 - Get https://www.juangrosso.com/ source code and add it to a set of visited_urls
2 - Get all links inside https://www.juangrosso.com/ source code and add them to a set of unvisited_urls
3 - Get all text from https://www.juangrosso.com/ and add a record to a map with https://www.juangrosso.com/ as key and the text as value
4 - Pop a url from unvisited_urls and repeat process until no urls are left

## Important Note: only urls that begin with the base url entered will be used.