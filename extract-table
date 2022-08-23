from bs4 import BeautifulSoup
import pandas as pd
import requests


def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  

def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        line = rowgetDataText(tr, 'td')
        if len(line) > 0:
            rows.append(line) # data row
    return rows

def table_to_excel(html):
    bs= BeautifulSoup(html, 'html.parser')
    table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('cellspacing') and tag['cellspacing']=="1")
    dados = tableDataText(table)
    df = pd.DataFrame(dados)
    return df.rename(columns=df.iloc[0]).drop(df.index[0])

if __name__ == '__main__':

    url = "URLFILE"
    f = open(url, "r")
    table = table_to_excel(f)
    print(table)
    # soup = BeautifulSoup(fp, 'html.parser')
    # if response.status_code == 200:
    #     tabela_to_excel(fp)
