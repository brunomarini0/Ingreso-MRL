import json
import requests

users = [179571326]
site_id = "MLA"

p_file = open('productos.csv','w')
for u in users:
  url_prod = "https://api.mercadolibre.com/sites/"+site_id+"/search?seller_id="+str(u)
  resp = requests.get(url_prod)
  j = resp.json()
  prods = j.get('results')
  for p in prods:
    p_id = p.get('id')
    p_title = p.get('title')
    p_cat_id = p.get('category_id')
    
    url_cat = "https://api.mercadolibre.com/categories/" + p_cat_id
    resp_cat = requests.get(url_cat)
    j_cat = resp_cat.json()
    p_cat_name = j_cat.get('name')

    line = p_id + ";" + p_title + ";" + p_cat_id + ";" + p_cat_name + "\n"
    p_file.write(line)
p_file.close()