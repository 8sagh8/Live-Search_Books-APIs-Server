from YaMehdiData.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
import json, io, sys
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serverAPI.serializers import *

################################################
# ~~~~~ General Functions ~~~~~~~~~ #
################################################
# Authorized Person ## auth_person = auth_Person_Function(str(request.user))
def auth_Person_Function(current_user_name):
    if (current_user_name.lower() == 'admin' or current_user_name.lower() == 'sam'):
        return "Authorized Person"
    return False

### Log out View

def LogOutView(request):
    auth.logout(request)
    return redirect("/")

### Delete data from JSON File
def deleteData_JSON(file_name, item_id, dictName):
    fileName = file_name
    itemID = item_id 

    jsonFile = open(f'staticfiles/{fileName}')
    data = json.load(jsonFile)
    jsonFile.close()

    for index in range(len(data['need'])):
        if data['need'][index]['id'] == str(itemID):
            data['need'].pop(index)
            break

    my_json = json.dumps(data, indent=1)

    with open(f'staticfiles/{fileName}', mode='w+') as myFile:
        myFile.write(my_json)
    myFile.close()


################################################
# ~~~~~ JSON FILES Functions & VIEWS ~~~~~~~~~ #
################################################
# create 'authorizedPersonJSON.json' file
def _createAuthPersonJSON(request):
    auth_person = Authorized_Person.objects.all()
    authPerson_list = [] # will store all auth.per in here 

    for person in auth_person:
        authPerson_list.append({
            "name": person.auth_name,
            "data_status" : person.data_status,
            "data_user" : '',
        })
        
    json_person = {"authPerson": authPerson_list}
    my_json = json.dumps(json_person, indent=1)

    with open('staticfiles/authorizedPersonJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "AuthPerson"

# create 'topicsJSON.json' file
def _createTopicsJSON():
    topics = Topic.objects.all()
    topics_list = [] # will store all topics and then go inside json_topic

    for t in topics:
        topics_list.append({
            "id": t.id, "_topic": t._topic,
            "data_status" : t.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "topics" : topics_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/topicsJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Topics"

# create 'categoriesJSON.json' file
def _createCategoriesJSON():
    categories = Category.objects.all()
    categories_list = [] # will store all categories and then go inside json file

    for c in categories:
        categories_list.append({
            "id": c.id,
            "_category": c._category,
            "data_status" : c.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "categories" : categories_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/categoriesJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Categories"


    # create 'statusJSON.json' file
def _createStatusJSON():
    status = Status.objects.all()
    status_list = [] # will store all status and then go inside json file

    for s in status:
        status_list.append({
            "id": s.id, 
            "_status": s._status,
            "data_status" : s.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "status" : status_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/statusJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Status"

    # create 'religionJSON.json' file
def _createReligionJSON():
    religion = Religion.objects.all()
    religion_list = [] # will store all religion and then go inside json file

    for r in religion:
        religion_list.append({
            "id": r.id, 
            "_sect": r._sect,
            "data_status" : r.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "religion" : religion_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/religionJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Religion"


    # create 'personJSON.json' file
def _createPersonJSON():
    person = Person.objects.all()
    person_list = [] # will store all person and then go inside json file

    for p in person:
        person_list.append({
            "id": p.id, 
            "_p_name": p._p_name,
            "_birth_year": p._birth_year, 
            "_death_year": p._death_year,
            "data_status" : p.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "person" : person_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/personJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Persons"

    # create 'needJSON.json' file
def _createNeedJSON():
    need = Need.objects.all()
    need_list = [] # will store all need and then go inside json file

    for n in need:
        need_list.append({
            "id": n.id, 
            "_need": n._need,
            "data_status" : n.data_status,
            "data_user" : n.data_user,
        })

    # will store need json in here
    json_data = { "need" : need_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/needJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Need"

    # create 'languageJSON.json' file
def _createLanguageJSON():
    language = Language.objects.all()
    language_list = [] # will store all language and then go inside json file

    for l in language:
        language_list.append({
            "id": l.id, 
            "_language": l._language,
            "data_status" : l.data_status,
            "data_user" : '',
        })

    # will store language json in here
    json_data = { "language" : language_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/languageJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Language"

    # create 'bookJSON.json' file
def _createBookJSON():
    book = Book.objects.all()
    book_list = [] # will store all book and then go inside json file

    for b in book:
        book_list.append({
            "id": b.id,
            "name": b.name, 
            "author": str(b.author),
            "sect": str(b.sect),
            "cat": str(b.cat), 
            "status": str(b.status), 
            "need": str(b.need), 
            "lang": str(b.lang),
            "data_status" : b.data_status,
            "data_user" : '',
        })
    
    # will store language json in here
    json_data = { "book" : book_list }
    
    # convert into json data
    my_json = json.dumps(json_data, indent=1)
    
    with open('staticfiles/bookJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Book"


    # create 'referenceJSON.json' file
def _createReferenceJSON():
    reference = Reference.objects.all()
    reference_list = [] # will store all reference and then go inside json file
    
    for r in reference:
        reference_list.append({
            "id": r.id,
            "subject": str(r.subject),
            "speaker" : str(r.speaker),
            "personFor" : str(r.personFor),
            "book" : str(r.book),
            "vol_para" : r.vol_para,
            "page_chapter" : r.page_chapter,
            "hadees_verse" : r.hadees_verse,
            "description" : r.description,
            "data_status" : r.data_status,
            "data_user" : '',
        })

    # will store reference json in here
    json_data = { "reference" : reference_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=2)

    with io.open('staticfiles/referenceJSON.json', mode='w+', encoding="utf-16") as myFile:
        myFile.write(my_json)
    
    return "Reference"

########################################################
def CreateJSONView(request):
    auth_person = auth_Person_Function(str(request.user))
    msg = []
    if request.method == "POST":
        create_authPerson = _createAuthPersonJSON(request)
        msg.append(create_authPerson)
        # create Topics File
        created_file = _createTopicsJSON()
        msg.append(created_file)
        # create Categories File
        created_file = _createCategoriesJSON()
        msg.append(created_file)
        # create Status File
        created_file = _createStatusJSON()
        msg.append(created_file)
        # create Religion File
        created_file = _createReligionJSON()
        msg.append(created_file)
        # create Person File
        created_file = _createPersonJSON()
        msg.append(created_file)
        # create Need File
        created_file = _createNeedJSON()
        msg.append(created_file)
        # create Language File
        created_file = _createLanguageJSON()
        msg.append(created_file)
        # create Books File
        created_file = _createBookJSON()
        msg.append(created_file)
        # create References File
        created_file = _createReferenceJSON()
        msg.append(created_file)


    return render(request, 'haq/jsonFiles/createJSON.html', {
        'auth_person' : auth_person,
        "msg" : msg,
    })


############################################
def PostJSONView(request):
    auth_person = auth_Person_Function(str(request.user))
    msg = []
    need_list = None
    if request.method == "POST":
        # create_authPerson = _createAuthPersonJSON(request)
        # msg.append(create_authPerson)
        # # create Topics File
        # created_file = _createTopicsJSON()
        # msg.append(created_file)
        # # create Categories File
        # created_file = _createCategoriesJSON()
        # msg.append(created_file)
        # # create Status File
        # created_file = _createStatusJSON()
        # msg.append(created_file)
        # # create Religion File
        # created_file = _createReligionJSON()
        # msg.append(created_file)
        # # create Person File
        # created_file = _createPersonJSON()
        # msg.append(created_file)
        # create Need File
        need_list = _postNeedJSON()
        # # create Language File
        # created_file = _createLanguageJSON()
        # msg.append(created_file)
        # # create Books File
        # created_file = _createBookJSON()
        # msg.append(created_file)
        # # create References File
        # created_file = _createReferenceJSON()
        # msg.append(created_file)


    return render(request, 'haq/jsonFiles/postJSON.html', {
        'auth_person' : auth_person,
        'need_list' : need_list,
    })

    ##############################################
    ################################################
    # ~~~~~ POST FUNCTIONS INTO DATABASE ~~~~~~~~~ #
    ################################################

    # POST 'needJSON.json' file into DATABASE
def _postNeedJSON():
    data_list = []

    jsonFile = open('staticfiles/needJSON.json')
    data = json.load(jsonFile)
    jsonFile.close()

    for need in data['need']:
        if '-N-' == need['data_status']:
            temp = []
            for v in need.values():
                temp.append(v)
            data_list.append(temp)
    return (len(data_list), data_list)
    
def AddNeedView(request):
    auth_person = auth_Person_Function(str(request.user))
    need_list = []

    if request.method == "POST":
        needID = request.POST["needID"]
        needName = request.POST["needName"]
        needUser = request.POST["needUser"]

        # persisting data into database
        new_value = Need(_need = needName, data_status = '-P-', data_user = needUser)
        new_value.save()

        # deleting data from JSON file
        print("before", flush=True)
        deleteData_JSON("needJSON.json", eval(needID), 'need') 
        print("after", flush=True)
        need_list = _postNeedJSON() # get fresh data

    return render(request, 'haq/jsonFiles/postJSON.html', {
        'auth_person' : auth_person,
        "need_list" : need_list
    })

def DeleteNeedView(request):
    auth_person = auth_Person_Function(str(request.user))
    need_list = []

    if request.method == "POST":
        needID = request.POST["needID"]

        # deleting data from JSON file
        deleteData_JSON("needJSON.json", eval(needID), 'need') 
        need_list = _postNeedJSON() # get fresh data

    return render(request, 'haq/jsonFiles/postJSON.html', {
        'auth_person' : auth_person,
        "need_list" : need_list
    })