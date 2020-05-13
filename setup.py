from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()


setup(name='PyDoof', version='3.0', author='Doofinder',
      author_email='support@doofinder.com',
      description="Doofinder's search & management API client",
      url='https://github.com/doofinder/pydoof',
      packages=['pydoof'],
      install_requires=['requests >= 1.2.3', 'pydoof-core == 1.0.1'],
      test_suite='nose.collector',
      tests_require=['nose', 'HTTPretty>=0.0.14'],
      provides=['PyDoof'],
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
          ]
      )
