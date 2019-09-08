#from urllib.request import urlopen

import pandas as pd
import io
import requests
import re
import json

#url="https://slalom-hackathon.s3.us-east-2.amazonaws.com/MO+BMF+6.10.2019.csv"
#s=requests.get(url).content
c=pd.read_csv('./altere_data.csv')
c.insert(2,'website','none')
ein = c['EIN']



url = "https://s3.amazonaws.com/irs-form-990/index_2018.json"



r = requests.get(url)


j = r.json()

rowdat = j['Filings2018']




for i in range(len(c)):
    print(i)


    irs_xml_loc = list(filter(lambda einval: einval['EIN'] == str(c['EIN'][i]), rowdat))

    if len(irs_xml_loc) == 0 :
        print(str(c['EIN'][i]) + " is invalid")
        continue
    xml_req = requests.get(irs_xml_loc[0]['URL']).content
    website = re.search('<WebsiteAddressTxt>(.*)</WebsiteAddressTxt>', xml_req)
    c['website'][i] = website





c = c[c['website'] != 'none']
c.head()

c.to_csv(r'./final.csv')

#data = json.loads(r.json())

#print (json.dumps(data.to))
