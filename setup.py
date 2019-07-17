from setuptools import find_packages, setup


setup(setup_requires=["pbr"],
      pbr=True,
      package_dir={'': 'src'},
      packages=find_packages(where='src'))
