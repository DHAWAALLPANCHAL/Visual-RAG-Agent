
# setup.py is the fallback installation script when pyproject.toml does not work
from setuptools import setup, find_packages
import os

version_folder = os.path.dirname(os.path.join(os.path.abspath(__file__)))

with open(os.path.join(version_folder, 'verl/version/version')) as f:
    __version__ = f.read().strip()

install_requires = [
  'accelerate',
  'codetiming',
  'datasets',
  'dill',
  'hydra-core',
  'math-verify',
  'numpy',
  'pandas',
  'peft',
  'pyarrow>=15.0.0',
  'pybind11',
  'pylatexenc',
  'ray>=2.10',
  'tensordict<0.6',
  'torchdata',
  'transformers',
  'vllm<=0.6.3',
  'wandb',
]

TEST_REQUIRES = ['pytest', 'yapf', 'py-spy']
PRIME_REQUIRES = ['pyext']
GEO_REQUIRES = ['mathruler']
GPU_REQUIRES = ['liger-kernel', 'flash-attn']

extras_require = {
  'test': TEST_REQUIRES,
  'prime': PRIME_REQUIRES,
  'geo': GEO_REQUIRES,
  'gpu': GPU_REQUIRES,
}

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='verl',
    version=__version__,
    package_dir={'': '.'},
    packages=find_packages(where='.'),
    url='https://github.com/volcengine/verl',
    license='Apache 2.0',
    author='Bytedance - Seed - MLSys',
    author_email='zhangchi.usc1992@bytedance.com, gmsheng@connect.hku.hk',
    description='verl: Volcano Engine Reinforcement Learning for LLM',
    install_requires=install_requires,
    extras_require=extras_require,
    package_data={'': ['version/*'],
                  'verl': ['trainer/config/*.yaml'],},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)