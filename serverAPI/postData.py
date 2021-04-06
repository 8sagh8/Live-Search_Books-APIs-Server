
##########################################################
# ~~~~~ Post Dictionary Typed Data to Files ~~~~~~~~~ #
##########################################################

import json
# #  Fetch data from 'authorizedPersonJSON.json' File 
# def get_authPerson_json():
#     file_obj = open('staticfiles/authorizedPersonJSON.json')
#     data_dict = json.load(file_obj)
#     file_obj.close()
    
#     return data_dict

# #  Fetch data from 'topicsJSON.json' File 
# def get_topics_json():
#     file_obj = open('staticfiles/topicsJSON.json')
#     data_dict = json.load(file_obj)
#     file_obj.close()
    
#     return data_dict

# #  Fetch data from 'categoriesJSON.json' File 
# def get_categories_json():
#     file_obj = open('staticfiles/categoriesJSON.json')
#     data_dict = json.load(file_obj)
#     file_obj.close()
#     return data_dict

# #  Fetch data from 'statusJSON.json' File 
# def get_status_json():
#     file_obj = open('staticfiles/statusJSON.json')
#     data_dict = json.load(file_obj)
#     file_obj.close()
#     return data_dict

# #  Fetch data from 'religionJSON.json' File 
# def get_religion_json():
#     file_obj = open('staticfiles/religionJSON.json')
#     data_dict = json.load(file_obj)
#     file_obj.close()
#     return data_dict

# #  Fetch data from 'personJSON.json' File 
# def get_person_json():
#     file_obj = open('staticfiles/personJSON.json')
#     data_dict = json.load(file_obj)
#     file_obj.close()
#     return data_dict

#  Fetch data from 'needJSON.json' File 
def post_need_json(postValue):
    # Opening JSON file
    jsonFile = open('staticfiles/needJSON.json',)
    # returns JSON object as 
    data = json.load(jsonFile)
    jsonFile.close() # Closing file

    if type(data['need'][-1]['id']) == str:
        unique_id = eval(data['need'][-1]['id'])
    else:
        unique_id = data['need'][-1]['id']

    unique_id = str(unique_id + 1)
    
    data['need'].append({
        'id': unique_id, 
        '_need': postValue['newItem'], 
        'data_status':'-N-', 
        'data_user': postValue['curr_user']
        })

    # storing data into json file
    my_json = json.dumps(data, indent=1)
    with open('staticfiles/needJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    jsonFile.close() # Closing file
    
    return "Job is Done"

# #  Fetch data from 'languageJSON.json' File 
# def get_language_json():
#     file_obj = open('staticfiles/languageJSON.json')
#     data_dict = json.load(file_obj)
#     file_obj.close()
#     return data_dict

# #  Fetch data from 'bookJSON.json' File 
# def get_book_json():
#     file_obj = open('staticfiles/bookJSON.json')
#     data_dict = json.load(file_obj)
#     file_obj.close()
#     return data_dict

# #  Fetch data from 'referenceJSON.json' File 
# def get_reference_json():
#     file_obj = open('staticfiles/referenceJSON.json', encoding='utf-16')
#     data_dict = json.load(file_obj)
#     file_obj.close()

#     return data_dict