import web


print "Conectar"


db = web.database(
    dbn='mysql',
    host='localhost',
    db=  'craftsystem',
    user= 'root',
    pw= '1234',
    port=3308
    )
print "Conectado"