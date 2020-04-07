import os

readme = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.rst')
long_description = open(readme).read()

SETUP_ARGS = dict(
    name='realpython-django-receipts',
    version='1.0.2',
    description='Sample installable django app',
    long_description=long_description,
    url='https://github.com/realpython/django-receipts',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires=">=3.7",
    install_requires=[
        'Django>=3.0',
    ],
    test_suite='load_tests.get_suite',
)

if __name__ == '__main__':
    from setuptools import setup, find_packages

    SETUP_ARGS['packages'] = find_packages()
    setup(**SETUP_ARGS)
