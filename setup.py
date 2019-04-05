from setuptools import setup, find_packages

pkj_name = 'payparts'

with open('requirements.txt') as f:
    requires = f.read().splitlines()


setup(
    name='django-ok-payparts',
    version='0.1',
    description='Django seo app',
    long_description=open('README.md').read(),
    author='Oleg Kleschunov',
    author_email='igorkleschunov@gmail.com',
    url='https://github.com/LowerDeez/ok-payparts',
    packages=[pkj_name] + [pkj_name + '.' + x for x in find_packages(pkj_name)],
    include_package_data=True,
    license='MIT',
    install_requires=requires,
    classifiers=[
        'Environment :: Web Environment',
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]

)
