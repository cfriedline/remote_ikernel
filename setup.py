# default to setuptools so that 'setup.py develop' is available,
# but fall back to standard modules that do the same
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='remote_ikernel',
      version='0.5.0',
      description='Running IPython kernels through batch queues',
      long_description=open('README.rst').read(),
      author='Tom Daff',
      author_email='tdd20@cam.ac.uk',
      license='BSD',
      url='https://github.com:macdems/remote_ikernel',
      packages=['remote_ikernel'],
      scripts=['bin/remote_ikernel'],
      install_requires=['notebook', 'pexpect', 'tornado'],
      classifiers=[
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License'])
