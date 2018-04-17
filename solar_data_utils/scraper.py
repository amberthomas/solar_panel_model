#import urllib2
import sys
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



md = {'04':16, '03':30}
pattern = '<table id=\"history_table\"(.*<tbody>.*)</tbody>'


def main(month):
    print('Program starting')
    days = md[month]
    with open('test_scrape.csv', 'w+') as tsf:
        for d in range(1, days + 1):
            date = month + str(d)
            url = 'https://www.wunderground.com/personal-weather-station/dashboard?ID=KCASTANF2#history/tdata/s2018' + date +'/e2018' + date +'/mdaily'
            browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
            print ('Driver opened')
            browser.get(url)
            print ('Webpage for date %s found' % date)
            tsf.write(date + '\n')
            for row in browser.find_elements_by_css_selector("#history_table tr"):
                cells = row.find_elements_by_tag_name("td")
                #cells = WebDriverWait(browser, 120).until(find_cells(row))
                if len(cells) > 0:
                    if cells[0].text == 'Time':
                        print (cells[0].text)
                        continue
                    row_csv = ''
                    for cell in cells: 
                        row_csv += cell.text + ','
                    row_csv = row_csv[:-1]
                    row_csv += '\n'
                    tsf.write(row_csv)
                    #print (row_csv)
            browser.quit() 
            print('Page closed')


if __name__ == '__main__':
    if (len(sys.argv) != 2): 
        print ('argument error in main')
        sys.exit(0)
    main(sys.argv[1])

