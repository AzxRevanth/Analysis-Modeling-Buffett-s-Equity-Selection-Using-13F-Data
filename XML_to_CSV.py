import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np


def parse_xml_to_dataframe(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    namespace = {'sec': 'http://www.sec.gov/edgar/document/thirteenf/informationtable'}

    holdings_data = []
    for info in root.findall('sec:infoTable', namespace):
        issuer = info.find('sec:nameOfIssuer', namespace).text
        title = info.find('sec:titleOfClass', namespace).text
        cusip = info.find('sec:cusip', namespace).text
        value = info.find('sec:value', namespace).text
        shares = info.find('sec:shrsOrPrnAmt/sec:sshPrnamt', namespace).text


        holdings_data.append({
            'issuer': issuer,
            'title': title,
            'cusip': cusip,
            'value': value,
            'shares': shares,
        })

    df = pd.DataFrame(holdings_data)
    return df


xml_files = [
    "2024-08-14.xml",
    "2024-11-14.xml",
    "2025-02-14.xml",
    "2025-05-15.xml"
]

dates = [f.replace(".xml", "") for f in xml_files]

# dataframes = [parse_xml_to_dataframe(f) for f in xml_files]

dfs = []

for file , date_str in zip(xml_files, dates):
    df = parse_xml_to_dataframe(file)
    df['date'] = date_str
    dfs.append(df)

Forms_final_df = pd.concat(dfs, ignore_index=True)
print(Forms_final_df)  

Forms_final_df.to_csv("Warren_Buffett_final_df.csv", index=False)
