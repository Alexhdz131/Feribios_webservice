import web


print "Conectar"


db = web.database(
    dbn='mysql',
    host='localhost',
    db=  'ferreteria_ahp1',
    user= 'root',
    pw= '1234',
    port=3308
    )
print "Conectado"