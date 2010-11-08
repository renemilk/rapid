from distutils.core import setup

version='0.5.0'

with open('rapid/version.py','wb') as version_file:
	version_file.write('dist_version="%s"'%version)

setup(
    name='rapid-spring',
    version=version,
    author='Tobi Vollebregt',
    author_email='tobivollebregt@gmail.com',
    packages=['rapid', 'rapid.ui', 'rapid.ui.qt', 'rapid.ui.text', 'rapid.util', 'rapid.unitsync'],
    scripts=['bin/rapid','bin/rapid-gui'],
    url='http://pypi.python.org/pypi/rapid-spring/',
    license='LICENSE.txt',
    description='spring content downloading',
    long_description=open('README.txt').read(),
    # running `setup.py sdist' gives a warning about this, but still
    # install_requires is the only thing that works with pip/easy_install...
    install_requires=['bitarray'],
)
