from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in akshay_app/__init__.py
from akshay_app import __version__ as version

setup(
	name="akshay_app",
	version=version,
	description="test app",
	author="akshay",
	author_email="akshay.shaharwale@syscort.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
