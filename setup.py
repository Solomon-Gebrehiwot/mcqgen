from setuptools import setup, find_packages

setup (
    name='mcqgenerator',
    version='0.0.1',
    author='SG',
    author_email='solocelestial@gmail.com',
    install_requires =["openai", "langchain", "streamlit", "python_dotenv","PyPDF2"],
    packages=find_packages()
   )

