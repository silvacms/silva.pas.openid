from setuptools import setup, find_packages

version = '0.1'

setup(name='silva.pas.openid',
      version=version,
      description="OpenID PAS plugin",
      long_description= open('README.txt').read(),
      classifiers=[
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='pas openid silva',
      author='Sylvain Viollon',
      author_email='info@infrae.com',
      url='http://svn.infrae.com/silva.pas.openid/trunk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['silva.pas'],
      include_package_data=True,
      zip_safe=False,
      install_requires=["python-openid <= 2.0.999",
                        "plone.session",
                        "setuptools"],
      )

