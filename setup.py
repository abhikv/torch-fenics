from distutils.core import setup

setup(name='torch-fenics',
      version='0',
      description='PyTorch-FEniCS interface',
      author='Patrik Barkman',
      author_email='barkm@kth.se',
      packages=['torch_fenics'],
      install_requires=['pyadjoint', 'torch==0.4.1'],
      dependency_links=['git+https://bitbucket.org/barkm/pyadjoint.git@torch-fenics#egg=pyadjoint-2017.2.0']
      )


