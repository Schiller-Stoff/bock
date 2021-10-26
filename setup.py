from setuptools import setup, find_packages

# might be a silly thing todo?
def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


setup(
    name='bock',
    version='0.1.0',
    packages=find_packages(),
    include_package_date=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        bock=bock.cli:cli
    """,
)