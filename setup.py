from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="abhishekjadhav3470",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhishekjadhav3470/Simple_dvc_project.git",
    author_email="abhishek@ineuron.ai",
    # package_dir={"": "src"},
    # packages=find_packages(where="src"),
    packages=['src'],
    license="GNU",
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',        # Make sure there are no syntax issues here
        'scikit-learn'
    ]
)
