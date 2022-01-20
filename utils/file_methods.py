import json


def Open():
    with open('db/data.json', 'r', encoding='utf8') as file:
        return json.load(file)


def Save(obj):
    with open('db/data.json', 'w', encoding='utf8') as file:
        json.dump(obj, file, ensure_ascii=False, indent='\t')


def Db(id):
    id = str(id)
    obj = Open()
    if obj.get(id):
        return obj
    obj[id] = {}
    obj[id]['Шаббат'] = 0
    obj[id]['Опыт'] = 0
    Save(obj)
    return obj