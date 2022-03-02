import json
with open('sample-data.json', 'r') as j:
    a = json.load(j)
    
with open('jso.txt', 'w') as q:
    print("Interface Status", file = q)
    print('=' * 80, file = q)
    print("DN                                                 Description           Speed    MTU  ", file = q)
    print("-------------------------------------------------- --------------------  ------  ------", file = q) 
    for i in a['imdata']:
        dn = i['l1PhysIf']['attributes']['dn']
        descr = i['l1PhysIf']['attributes']['descr']
        speed = i['l1PhysIf']['attributes']['speed']
        mtu = i['l1PhysIf']['attributes']['mtu']
        print(f'{dn}\t\t\t\t\t\t{descr}\t\t{speed}    {mtu}', file = q)
        