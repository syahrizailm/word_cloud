from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("word_cloud/wordcloud/query_integral_image.pyx"))
