#!/usr/bin/env python
# Copyright 2021 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from setuptools import find_packages, setup


# Load the package metadata from __version__.py
with open(os.path.join("src", "accelerate", "__version__.py")) as f:
    exec(f.read())

# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setup(
    name="accelerate",
    version=VERSION,
    description="A simple way to launch, train, and use PyTorch models on almost any device and distributed configuration, automatic mixed precision (including fp8), and easy-to-configure FSDP and DeepSpeed support",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="deep learning, pytorch, distributed training, mixed precision, fsdp, deepspeed",
    author="The HuggingFace team",
    author_email="accelerate@huggingface.co",
    url="https://github.com/huggingface/accelerate",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={
        "console_scripts": [
            "accelerate=accelerate.commands.accelerate_cli:main",
        ]
    },
    python_requires=">=3.8.0",
    install_requires=[
        "numpy>=1.17",
        "packaging>=20.0",
        "psutil",
        "pyyaml",
        "torch>=1.10.0",
        "huggingface_hub>=0.10.0",
    ],
    extras_require={
        "deepspeed": ["deepspeed>=0.9.3"],
        "rich": ["rich>=10.0.0"],
        "test": [
            "datasets",
            "parameterized",
            "pytest",
            "pytest-xdist",
            "safetensors>=0.3.1",
            "transformers>=4.26.0",
        ],
        "quality": [
            "black~=23.1",
            "isort>=5.5.4",
            "ruff>=0.0.241",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)