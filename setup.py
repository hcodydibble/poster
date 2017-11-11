from setuptools import setup, find_packages

requires = [
    'requests'
]

tests_require = [
    'pytest',
    'pytest-cov',
    'tox'
]


setup(
    name='poster',
    version='0.1',
    description='Lets you post to your 401 learning journal from the terminal',
    author='H. Cody Dibble',
    author_email='hcodydibble@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'test': tests_require,
    },
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'post = src.poster:main',
        ],
    },
)
