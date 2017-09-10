from setuptools import setup, find_packages

setup(
    name='biscuit',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'pytest',
        'PyMySQL',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'mock',
    ],
)
