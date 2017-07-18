from setuptools import setup

description = 'Modified Django FileResponse that adds Content-Range headers.'

setup(
    name='django-ranged-fileresponse',
    version='0.1.1',
    description=description,
    url='https://github.com/wearespindle/django-ranged-fileresponse',
    author='Spindle',
    author_email='jeroen@wearespindle.com',
    license='MIT',
    packages=['ranged_fileresponse'],
    install_requires=[
        'django',
    ],
    zip_safe=False,
)
