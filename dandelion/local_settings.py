# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a9cky6msp%i37(*w%_bkfki!cm5vgn)v$f*b%%a7kdx=pcfzg+'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'USER':'postgres',
		'NAME':'4ddb',
		'PASSWORD':'1234',
    }
}




