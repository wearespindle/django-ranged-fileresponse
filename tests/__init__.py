from django.conf import settings


# Make sure django can initialize for testing.
settings.configure(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
})
