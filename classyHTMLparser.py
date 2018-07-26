from bs4 import BeautifulSoup
##take soup from property search website and parse
class ParseHTMLtables:

    def __init__(self, soup):
        
        self.soup = BeautifulSoup(soup, 'lxml')
        ##find all tables
        self.tables = self.soup.find_all("table")
        ##cycle through each table  
        for table in self.tables:
            print table.title
            ##find table rows per table 
            self.table_rows = table.find_all('tr')
            for tr in self.table_rows:
                ##find table data per row
                self.th = tr.find_all('th')
                self.td = tr.find_all('td')
                print [i.text.strip('\n') for i in self.th],[i.text.strip('\n') for i in self.td]
            




        
        
