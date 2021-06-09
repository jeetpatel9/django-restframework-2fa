import os
from setuptools import setup, find_packages


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def get_doc():

    with open("README.md", "r") as fh:

        return fh.read()


setup(
    name="django_restframework_2fa",
    version="0.0.1",
    description="Some description",
    long_description=get_doc(),
    long_description_content_type="text/markdown",
    url="https://github.com/jeetpatel9/django-restframework-2fa.git",
    py_modules=['helloworld'],
    package_dir={'': 'django_restframework_2fa'},
    author='Jeet Patel',
    author_email='jpatel99967@gmail.com',
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(
        exclude=['tests', 'tests.*', 'licenses', 'requirements']),
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "djangorestframework",
        "django",
        "djangorestframework-simplejwt",
        "pyjwt",
        "twilio==6.55.0",
        "djangorestframework-simplejwt==4.6.0",
        "django-phonenumber-field==5.2.0",
        "phonenumbers==8.12.24",

    ],
    extra_requires={
        "dev": [
            "mysqlclient==1.4.6",
            "pytest>=3.7",
            "twine 3.4.1",
        ]
    }
)
