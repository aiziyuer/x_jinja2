from setuptools import setup, find_packages

setup(
    name="x-jinja2",  # 包名
    version="0.1.0",  # 版本号
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    description="让jinja2自带各类好用的filter",  # 简短描述
    long_description=open("README.md").read(),  # 详细描述
    long_description_content_type="text/markdown",  # 描述内容类型
    author="aiziyuer",  # 作者名
    author_email="910217951@qq.com",  # 作者邮箱
    url="https://github.com/aiziyuer/x_jinja2",  # 项目主页
    license="MIT",  # 许可证
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # 支持的 Python 版本
    install_requires=[
        "jinja2",
        "jinja2_ansible_filters",
        "jsonpath-ng",
        "json5",
    ],  # 依赖项
)
