from setuptools import setup, find_packages


version = '0.0.1'


install_requires = (
    'fabric>=1.8',
)


setup(
    name='fab-deploy',
    packages=find_packages(),
    version=version,
    description='',
    long_description='',
    author='incuna',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/fab-deploy/',
    install_requires=install_requires,
    zip_safe=False,
)
