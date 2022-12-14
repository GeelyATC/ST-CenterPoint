import os
from setuptools import find_packages, setup
from setuptools import Extension, dist, find_packages, setup

dist.Distribution().fetch_build_eggs(["Cython", "numpy>=1.11.1"])

def readme():
    try:
        with open("README.md", encoding="utf-8") as f:
            content = f.read()
        return content
    except:
        return "No description"


if __name__ == "__main__":
    setup(
        name="det3d",
        version="1.0",
        description="centerpoint det3d",
        long_description=readme(),
        author="daxiongpro",
        author_email="910660298@qq.com",
        keywords="computer vision, 3d object detection",
        url="https://github.com/daxiongpro/centerpoint",
        packages=find_packages(exclude=("configs", "tools", "demo")),
        package_data={"det3d.ops": ["*/*.so"]},
        license="Apache License 2.0",
        setup_requires=["pytest-runner", "cython", "numpy"],
        zip_safe=False,
    )
