def update(dict1,dict2,keys):
    for i in keys:
        dict1[i]=dict2[i]
    return dict1 
    
dict1={"a":"apple","b":"bat","c":"cat"}
dict2={"d":"dictionary","e":"event","f":"function"}
keys={"e","f"}
print(update(dict1,dict2,keys))