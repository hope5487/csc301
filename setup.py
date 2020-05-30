from setuptools import setup, find_packages

setup(
    name='Flask-CI-Example',
    packages=find_packages(),
    version='0.1',
    long_description=__doc__,
    zip_safe=False,
    test_suite='nose.collector',
    include_package_data=True,
    install_requires=[
        'click==7.1.2',
        'Flask==1.1.2',
        'Flask-SQLAlchemy==2.4.1',
        'itsdangerous==1.1.0',
        'Jinja2==2.11.2',
        'MarkupSafe==1.1.1',
        'SQLAlchemy==1.3.17',
        'Werkzeug==1.0.1',
    ],
    tests_require=['nose'],
)