import numpy as np
from setuptools import dist, setup, Extension

# To install and compile to your anaconda/python site-packages, simply run:
# $ pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
# Note that the original compile flags below are GCC flags unsupported by the Visual C++ 2015 build tools.
# They can safely be removed.

INSTALL_REQUIRES = ['setuptools',
                    'cython',
                    'numpy',
                    'matplotlib']

dist.Distribution().fetch_build_eggs(INSTALL_REQUIRES)


ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs=[np.get_include(), '../common'],
        extra_compile_args=[]  # originally was ['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(name='pycocotools',
      packages=['pycocotools'],
      package_dir={'pycocotools': 'pycocotools'},
      version='2.0',
      ext_modules=ext_modules,
      install_requires=INSTALL_REQUIRES,
      setup_requires=['cython', 'numpy']
      )
