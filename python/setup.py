from setuptools import setup, find_packages

setup(
    name="bgpdata-api-message",
    version="4.0.0",
    packages=find_packages(include=["bgpdata", "bgpdata.*"]),
    install_requires=[],
    author="BGPDATA",
    description="Protocol implementation for Python",
    zip_safe=False,
)