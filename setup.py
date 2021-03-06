import codecs

from setuptools import setup, find_packages


def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()

setup(
    name='django-querysetsequence',
    packages=find_packages(),
    version='0.8',
    description='Chain together multiple (disparate) QuerySets to treat them as a single QuerySet.',
    long_description=long_description(),
    author='Percipient Networks, LLC',
    author_email='support@strongarm.io',
    url='https://github.com/percipient/django-querysetsequence',
    download_url='https://github.com/percipient/django-querysetsequence',
    keywords=['django', 'queryset', 'chain', 'multi', 'multiple', 'iterable'],
    license='ISC',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'License :: OSI Approved :: ISC License (ISCL)',
    ],
    install_requires=[
        'django>=1.8.0',
    ],
)
