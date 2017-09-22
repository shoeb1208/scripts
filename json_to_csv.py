#!/usr/bin/python

import json
import csv
from pprint import pprint
with open('test.json') as data_file:
    data = json.load(data_file)
print "ID,impactScore,baseScore,exploitabilityScore"
for item in data['CVE_Items']:
        print item["cve"]["CVE_data_meta"]["ID"],",",item["impact"]["baseMetricV2"]["impactScore"],",",item["impact"]["baseMetricV2"]["cvssV2"]["baseScore"],",",item["impact"]["baseMetricV2"]["exploitabilityScore"]

data_file.close()
