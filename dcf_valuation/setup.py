from setuptools import setup, find_packages

setup(
    name="dcf_valuation",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0"
    ],
    author="ht",
    description="DCF valuation model",
    python_requires=">=3.7"
) [[1]] [[7]]