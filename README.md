<h1>Installation  Django</h1>
<h3> 1. install python </h3>
<h5>Python https://www.python.org/downloads/windows/  </h5>
//check python version  $ python --version
<h3>install virtualenvwrapper</h3>
<h5>$ pip install virtualenvwrapper-win </h5>
<h3>Create Project</h3>
<h5>1. mkdir django  // create folder </h5>
<h5>2. cd django </h5>
<h5>3. virtualenv .</h5>
<h5>4 .\Scripts\activate</h5>
<h5>pip install django</h5>
<h5>pip freeze  //check packgage </h5>
<h3>Create Django Project</h3>
<h5>1. python .\Scripts\django-admin.py startproject mysite  <strong>If not used</strong>     django-admin startproject mysite</h5>
<h5>2. cd mysite </h5>
<h5>3. python manage.py makemigrations</h5>
<h5>4. python manage.py migrate</h5>
<h5>5. python manage.py runserver  //runserver http://127.0.0.1:8000/</h5>


<h1>if you have django on laptop you can pull project and startproject for dev</h1>
<h3>Database usage postgresql  https://www.enterprisedb.com/downloads/postgres-postgresql-downloads </h3>
<h3> 1. go to setting.py use setting follow</h3>
<h5>$ pip install psycopg2 </h5>  
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

