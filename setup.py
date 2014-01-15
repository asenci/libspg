from distutils.core import setup

setup(
    name='libspg',
    version='0.1',
    packages=['libspg'],
    url='https://bitbucket.org/asenci/libspg',
    license='ISC License',
    author='Andre Sencioles Vitorio Oliveira',
    author_email='andre@bcp.net.br',
    description='Python library for interacting with Brazil NPAC SPG',
    requires=['lxml']
)
