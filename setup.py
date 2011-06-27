from setuptools import setup
import doccito

setup(
    name='doccito',
    version = doccito.get_version(),

    author='rootbuzz',
    author_email='info@rootbuzz.com',

    description=('Send alerts, notifications, and messages based '
                'on events in your django application'),
    long_description=open('README.markdown').read(),

    license='MIT',
    keywords='documentation',

    url='http://doccito.com',

    install_requires=[
        "markdown"
    ],

    packages=[
        'alert',
        'alert.management',
        'alert.management.commands',
        'alert.migrations',
    ],

    include_package_data=True,


    classifiers=[
    	'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)