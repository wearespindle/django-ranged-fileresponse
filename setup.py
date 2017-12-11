from setuptools import setup

tests_require = [
    'pytest>=3.0.5',
    'pytest-cov>=2.4.0',
    'pytest-flake8>=0.8.1',
    'django>=1.8.0',
]

setup(
    name='django-ranged-fileresponse',
    version='0.1.2',
    description='Modified Django FileResponse that adds Content-Range headers.',
    url='https://github.com/wearespindle/django-ranged-fileresponse',
    author='Spindle',
    author_email='opensource@wearespindle.com',
    license='MIT',
    packages=['ranged_fileresponse'],
    zip_safe=False,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
)
