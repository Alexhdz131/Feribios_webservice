import web


print "Conectar"


db = web.database(
    dbn='mysql',
    host='c9cujduvu830eexs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    db=  'ufieql1f90kzz50h',
    user= 'dox3t6g7obt4dj40',
    pw= 'wqnj186edmmgwcvw',
    port=3306
    )
print "Conectado"