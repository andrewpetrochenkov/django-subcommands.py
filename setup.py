import setuptools

setuptools.setup(
    name='django-subcommands',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
