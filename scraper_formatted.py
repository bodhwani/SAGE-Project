import dateutil.parser as parser
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from datetime import timedelta, date
from collections import defaultdict, OrderedDict

dates = []
d={}
all_dates = []

def crawl(link):
    data = urlopen(link).read()
    soup = BeautifulSoup(data,'lxml')

    tables = soup.find( "table", {"class":"wikitable collapsible"} )

    all_tr = tables.find_all("tr")

    for i in all_tr[4:]:
        temp = i.find(["td","span"], {"class": "nowrap"})

        if(temp is not None):
            td_value = (i.find("td"))
            try:
                check = int(td_value.get_text()[:2])
                inv_date = td_value.get_text()
                if "[" in inv_date:
                    arrow_index = inv_date.index("[")
                    inv_date = inv_date[0:arrow_index]
                    year_date =  year + " " + inv_date
                    date = parser.parse(year_date)
                    # print("date = ", date)
                    dates.append(date.isoformat())

            except:
                continue
    return dates

def generate(start, end):
    date_array = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))

    for date_object in date_array:
        all_dates.append(date_object.isoformat())

    return all_dates

def export(dates, year):
    start = datetime.datetime.strptime(year + "-01-01", "%Y-%m-%d")
    end = datetime.datetime.strptime(str(int(year)+1) + "-01-01", "%Y-%m-%d")
    all_dates = generate(start, end)

    for i in all_dates:
        d[i]=0

    all_dates_c = list(all_dates)
    
    for i in dates:
        initial = i[:-9] + "T00:00:00"
        index = all_dates.index(initial)
        prev = all_dates_c[index]
        all_dates_c[index] = i
        d[all_dates_c[index]] = d.pop(prev) + 1

    ordered_dict = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    dfObj = pd.DataFrame(list(ordered_dict.items()))
    dfObj.columns = ['date', 'value']
    dfObj.to_csv('output.csv', index = False)


year = "2019"
link = "https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches"

dates = crawl(link)

export(dates,year)

