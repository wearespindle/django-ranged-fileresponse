from setuptools import setup

setup(name='django-ranged-fileresponse',
      version='0.1.1',
      description='Modified Django FileResponse that adds Content-Range headers.',
      url='https://github.com/wearespindle/django-ranged-fileresponse',
      author='Spindle',
      author_email='jeroen@wearespindle.com',
      license='MIT',
      packages=['django'],
      zip_safe=False)
