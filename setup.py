from setuptools import setup

setup(
    name='biscuit',
    packages=['biscuit'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pytest',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'mock',
    ],
)
