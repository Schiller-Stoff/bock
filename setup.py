from setuptools import setup, find_packages

# might be a silly thing todo?
def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


setup(
    author="Sebastian Stoff",
    author_email="SebastianStoff@gmx.at",
    description="Small clit - tool to support GAMS4+ local development",
    name='bock',
    version='0.1.0',
    packages=find_packages(exclude=("tests")),
    include_package_date=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        bock=bock.cli:cli
    """,
)