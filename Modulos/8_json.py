import json

import json

# Strings para Dicionário 
person =  '{"name": "Rodrigo", "languagens": ["Python", "Javascript"]}' 
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])

# Convertendo dicionário para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_dict))
print(type(person_json))

#Formatando json
print(json.dumps(person_dict, indent = 4, sort_keys=True))


#salvando json em txt
with open("person.txt","w") as json_file:
    json.dump(person_dict, json_file)