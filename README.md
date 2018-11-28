<h1>Installation for windows</h1>
<h5>Python https://www.python.org/downloads/windows/  
<h5>$ pip install virtualenvwrapper-win </h5>
<h5>$ pip install django </h5>
<h5>$ pip install psycopg2 </h5>
<h3>Database usage postgresql  https://www.enterprisedb.com/downloads/postgres-postgresql-downloads </h3>
<h3> 1. go to setting.py use setting follow</h3>
    
 <h5>   DATABASES = {</h5>
<h5>    'default': {</h5>
 <h5>       'ENGINE': 'django.db.backends.postgresql',</h5>
 <h5>       'NAME': 'postgres',</h5>
 <h5>       'USER': 'postgres',</h5>
  <h5>      'PASSWORD': 'ubcdins5',</h5>
  <h5>      'HOST': 'localhost',</h5>
<h5> }</h5>
<h5>}
<h3>2. migrate database after connect </h3>
<h5>$ python manage.py migrate</h5>

<h3>run project</h3>
<h5>$ python manage.py runserver</h5>

