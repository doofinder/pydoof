from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()


setup(name='PyDoof', version='4.1.0', author='Doofinder',
      python_requires='>=3.6.7',
      author_email='support@doofinder.com',
      description="Doofinder's search & management API client",
      url='https://github.com/doofinder/pydoof',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['requests >= 1.2.3'],
      tests_require=['parameterized >= 0.7.4'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6.7', # On Python >= 3.7 this displays a warning
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
      ])
