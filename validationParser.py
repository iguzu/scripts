data = {}
body = input_data.get('body')
if body:
    body = body.split('\n')
    for item in body:
        kv = item.split(':')
        if len(kv) == 2:
            data[kv[0].strip()] = kv[1].strip()
    urgency = data.get('urgency_flag', 'false')
    data['priority'] = 'HIGH' if urgency == 'true' else 'MEDIUM'
    output = [data]
else:
    output = [{}]
