from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()


setup(name='PyDoof', version='2.6.0', author='JoeZ99',
      author_email='jzarate@gmail.com',
      description="Doofinder's search & management API client",
      url='https://github.com/doofinder/pydoof',
      packages=['pydoof'],
      requires=['requests(>=1.2.3)', 'future(>=0.17.1)'],
      install_requires=['requests>=1.2.3', 'future>=0.17.1'],
      test_suite='nose.collector',
      tests_require=['nose', 'HTTPretty>=0.0.14'],
      provides=['PyDoof'],
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
          ]
      )
