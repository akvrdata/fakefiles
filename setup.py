from setuptools import setup, find_packages

# setup(
#     name="fakefiles",
#     version="0.1",
#     packages=find_packages(),
#     include_package_data=True,
#     install_requires=["Click", "pyyaml", "mimesis"],
# entry_points='''
#     [console_scripts]
#     fakefiles=src.main:cli
# ''',
# )

# old config
setup(
    name="fakefiles",
    version="0.5.5",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click", "pyyaml", "mimesis"],
    entry_points="""
        [console_scripts]
        fakefiles=src.main:cli
        uploadfiles=src.awsmods:cli
    """,
)