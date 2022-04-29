data = {}
enbr_map = {'0 à 5': 1, '6 à 19': 6, '20 à 99': 20, '100 à 499': 100, '500 et plus': 500}
body = input_data.get('body')
if body:
    body = body.split('\n')
    for item in body:
        kv = item.split('=')
        if len(kv) == 2:
            data[kv[0].strip()] = kv[1].strip()
    lang = data.get('langue_correspondance')
    if lang and lang == 'Anglais':
        data['langue_correspondance'] = 'en'
    else:
        data['langue_correspondance'] = 'fr'
    data['nombre_employes'] = enbr_map.get(data.get('nbr_emp', ''), 500)
    output = [data]
else:
    output = [{}]
