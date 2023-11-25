from setuptools import setup, find_packages

with open("README.MD", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = 'src',
    version= '0.0.1',
    author= 'abhishekjadhav',
    description='A small packages for dvc ml pipeline demo',
    long_description= long_description,
    long_description_content_type = "text/markdown",
    author_email= 'abhishekjadhav3470@gmail.com',
    url="https://github.com/abhishekjadhav3470/Simple_dvc_project.git",
    package_dir={"" : "src"}, 
    packages=find_packages(where="src"),
    license="GNU", 
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'dvc[gdrive]', 
        'dvc[s3]'
        'pandas',
        'scikit-learn' 
    ]

)