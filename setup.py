from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
                'scikit-learn==0.18.2',
                'oletools==0.50',
                'pandas==0.17.1',
                ]

setup(
    name='mmbot',
    version='1.1.1',
    description='Malicious Macro Bot: Python module to classify and cluster Microsoft office documents.  '
                'Uses machine learning techniques to determine if VBA code is malicious or benign and '
                'groups similar documents together.',
    url='https://github.com/egaus/mmbot',
    author='Evan Gaustad',
    author_email='evan.gaustad@gmail.com',
    license='MIT',
    packages=find_packages(exclude='tests'),
    scripts=['cli/mmbot'],
    install_requires=requirements,
    keywords='mmbot malicious macro bot office document security cyber malware',
    # include_package_data=True,
    package_data={'mmbot': ['model/modeldata.pickle.gz', 'model/vocab.txt']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
)

