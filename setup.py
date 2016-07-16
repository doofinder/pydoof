from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()


setup(name='PyDoof', version='2.4.2', author='JoeZ99',
      author_email='jzarate@gmail.com',
      description="Doofinder's search & management API client",
      url='https://github.com/doofinder/pydoof',
      packages=['pydoof'],
      requires=['requests(>=1.2.3)'],
      install_requires=['requests>=1.2.3'],
      provides=['PyDoof'],
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
          ]
      )
