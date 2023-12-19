from setuptools import setup, find_packages

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setup(
        name='rolypoly',
        version='0.0.0',
        author='Siddhartha Banerjee',
        author_email='info@emotive.academy',
        description='A Python library for working with 2D mechanics of rigid bodies',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='www.emotive.academy',
        packages=find_packages(),
        package_data={'': ['LICENSE']},
        include_package_data=True,
        package_dir={'rolypoly': 'src'},
        classifiers=[
            'Development Status :: Alpha',
            'Intended Audience :: Developers',
            'License :: GNU GPLv3',
            'Programming Language :: Python :: 3.12',
        ],
        python_requires='>=3.12',
        install_requires=[
            'numpy',
        ],
    )