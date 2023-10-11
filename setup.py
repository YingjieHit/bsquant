from setuptools import setup, find_packages

setup(
    name='bsquant',  # 库名
    version='0.0.1',  # 版本号
    packages=find_packages(),  # 包含的包
    install_requires=[  # 依赖项
        'numpy',
        'pandas',
        # 添加其他依赖
    ],
    author='Zhang Yingjie',  # 作者名
    author_email='yingjiehit@gmail.com',  # 作者邮箱
    description='A great Quantitative Trading project',  # 简要描述
    url='https://github.com/YingjieHit/bsquant',  # 项目的URL
    keywords=['quantitative', 'trading', 'finance', 'cta'],  # 关键词
)