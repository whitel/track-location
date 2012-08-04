import sys, os
import ConfigParser
import psycopg2
from bottle import get, post, route, run, HTTPError, debug, template, static_file, default_app


@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name
 
@route('/')
def index():
    return '<strong>Hello World!</strong>'

@route('/track-location/')
#@post('/track-location/')
def track_location():
    #collect the location and time from the user
    #geoX = request.forms.get('geoX')
    #geoY = request.forms.get('geoY')
    #time = request.forms.get('time')

    config = ConfigParser.ConfigParser()
    config.read('config.conf')
    
    #Define our connection string
    conn_string = "host='" + config.get("Postgres Creds", "host") + "' "
    conn_string += "port='" + config.get("Postgres Creds", "port") + "' "
    conn_string += "user='" + config.get("Postgres Creds", "user") + "' "
    conn_string += "password='" + config.get("Postgres Creds", "pass") + "' "
    conn_string += "dbname='" + config.get("Postgres Creds", "db_name") + "' "
 
    con = None
    try:
    	# print the connection string we will use to connect
    	print "Connecting to database\n	->%s" % (conn_string)
     
    	# get a connection, if a connect cannot be made an exception will be raised here
    	con = psycopg2.connect(conn_string)
     
        cur = con.cursor()
        print "Connected!\n"

        cur.execute('SELECT version()')          
        ver = cur.fetchone()
        print ver    


    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)
                
    finally:        
        if con:
            con.close()
        

    out = str(config.sections())
    out += str(config.get("Postgres Creds", "user"))
    return out
    #save it in the db

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_GEAR_DIR'], 
    'runtime/repo/wsgi/views/')) 

application=default_app()