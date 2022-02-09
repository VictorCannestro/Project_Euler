from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'numpy',
    'datetime',
    'pandas'
]
TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',
    # to be able to run `python setup.py checkdocs`
    'collective.checkdocs', 'pygments',
]

setup(
    name='Project Euler',
    author='Victor Cannestro',
    description='Solutions to problems from the Project Euler webpage',
    long_description='README.md',
    url='https://github.com/VictorCannestro/Project_Euler',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
    }
)
