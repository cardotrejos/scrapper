from bs4 import BeautifulSoup
import requests

def get_data():
    page = requests.get("https://www.superfinanciera.gov.co/jsp/index.jsf")
    # Tags = []
    src = page.content

    soup = BeautifulSoup(src, 'html.parser')

    tables = []
    for table_tag in soup.find_all("div", class_="cont_Indicador"):
      table = table_tag.find('table')
      tables.append(table)

    consu_ordin = tables[1]

    data = consu_ordin.tbody.findAll('tr')
    values = []
    keys = []
    data_dict = {}

    for i in range(len(data)):
        key = data[i].find_all("td")[0].string.strip()
        keys.append(key)
        value = data[i].find_all("td")[1].string
        if value != None :
            values.append(value.strip())
            
    data_dict[keys[0]] = values[0]
    data_dict[keys[2]] = values[1]

    return data_dict

print(get_data())