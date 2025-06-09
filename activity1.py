student_info={"id1":{"name":"Lila","class":"5", "subj_integer":["english", "math", "science"]}
"id2":{"name":"Kate","class":"5", "subj_integer":["english", "math", "science"]}}
"id3":{"name":"Lisa","class":"6", "subj_integer":["english", "math", "science"]}}
"id4":{"name":"Janet","class":"6", "subj_integer":["english", "math", "science"]}}
result={}
for key, value in student_info.items():
    if value not in result.values():
        result[key]=value
        print(value)