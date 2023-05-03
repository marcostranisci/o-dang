import gzip,json,csv
from tqdm import tqdm

PATH = '/media/nbdotti62/Elements/wikidata/'

props = ['P21','P106','P569','P27','P19','P1412','P20','P108','P39', 'P22','P40','P166',\
 'P26','P102','P25','P103','P937','P463','P119','P551','P3373','P184','P6886',\
 'P53','P2632','P172','P945','P1066','P1317','P1038','P802','P611']

fo = open('/home/nbdotti62/Documenti/PHD/o-dang/prova.csv',mode='a')

l = ['entity','links','labels']
l.extend(props)

writer = csv.DictWriter(fo,l,extrasaction='ignore')
#writer.writeheader()
with gzip.open('{}wikidata-20220103-all.json.gz'.format(PATH)) as f:
    for line in tqdm(f):
        au = None

        try:
            c = eval(line)
            d = dict(c[0])

            for x in d['claims']['P31']:

                if x['mainsnak']['datavalue']['value']['id'] == 'Q5':

                    try:
                        au = {'entity':d['id']}
                        au['links'] = d['sitelinks']
                        au['labels'] = d['labels']


                        break
                    except: break

            if au:
                for prop in props:


                    try:


                        if prop in list(d['claims']):
                            properties = [el['mainsnak'] for el in d['claims'][prop]]

                            au[prop] = properties
                    except Exception as e:continue

                writer.writerow(au)



        except Exception as e: continue
