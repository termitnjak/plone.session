# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '3.6.2.dev0'
longdescription = open('README.rst').read()
longdescription += '\n'
longdescription += open('CHANGES.rst').read()

setup(
    name='plone.session',
    version=version,
    description='Session based auth tkt authentication for Zope',
    long_description=longdescription,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Framework :: Plone',
        'Framework :: Zope2',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration :: Authentication/Directory',  # noqa
    ],
    keywords='PAS session authentication Zope auth_tkt',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/plone.session',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    extras_require=dict(
      test=[
          'zope.configuration',
          'zope.publisher',
      ]
    ),
    install_requires=[
      'plone.keyring',
      'plone.protect',
      'Products.PluggableAuthService',
      'setuptools',
      'zope.component',
      'zope.interface',
      'Zope2',
    ],
)
