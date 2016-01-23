import os
from setuptools import setup
from setuptools import find_packages


version = '0.1-dev'
shortdesc = "PayMill Payment for bda.plone.shop"

setup(
    name='bda.plone.paymillpayment',
    version=version,
    description=shortdesc,
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: Zope Public License 2.1 (ZPL 2.1)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    author='Norbert Marrale',
    author_email='norbert@infocatch.com',
    license='Zope Public Licence 2.1',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['bda', 'bda.plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
        'bda.plone.payment',
        'paymill-wrapper',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
