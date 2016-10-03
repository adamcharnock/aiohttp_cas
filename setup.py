from setuptools import setup

setup(name='aiohttp_cas',
      version='0.0.1',
      description="CAS 1/2/3 authentication middleware for aiohttp.web",
      classifiers=['License :: OSI Approved :: MIT License',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Internet :: WWW/HTTP'
                  ],
       author='G. Ryan Sablosky',
       author_email='gsablosky@bard.edu',
       url='TBD',
       license='Apache 2',
       packages=['aiohttp_cas'],
       install_requires=[
           'aiohttp>=1.0.2',
           'lxml',
           'aiohttp_session',],
       include_package_data=True)