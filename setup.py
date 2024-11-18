from setuptools import setup, find_packages

setup(
    name="Sagittal_Average",
    version="0.1.2",
    packages=find_packages(where="src"), 
    package_dir={"": "src"},  
    entry_points={
        'console_scripts': ['sagittal_average_run = sagittal_average.command:process']
    },
    install_requires=[
        'numpy',
        'pandas',
    ],
)
