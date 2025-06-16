from setuptools import setup, find_packages

setup(
    name="bgpdata-api-message",
    version="4.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    author="BGPDATA",
    description="Protocol implementation for Python",
    zip_safe=False,
)