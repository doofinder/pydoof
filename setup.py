from setuptools import setup, find_packages

with open('README.txt') as file:
    long_description = file.read()


setup(name='PyDoofBeta', version='3.2.1', author='Doofinder',
      author_email='support@doofinder.com',
      description="Doofinder's search & management API client",
      url='https://github.com/doofinder/pydoof',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['requests >= 1.2.3'],
      test_suite='nose.collector',
      tests_require=['nose', 'HTTPretty>=0.0.14'],
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
      ])
