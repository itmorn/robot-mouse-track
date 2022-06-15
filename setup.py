from distutils.core import setup
from setuptools import find_packages

# with open("README.rst", "r", encoding="utf-8") as f:
#     long_description = f.read()
# python setup.py sdist build
# twine upload dist/*
setup(name='robot_mouse_track',  # 包名
      version='0.0.6',  # 版本号
      description='A small example package',
      long_description='随着互联网技术的发展，鼠标轨迹识别算法在很多人机交互产品中的需求日益增加，比如，一些网站为了防止被爬，增加了一些滑块验证码，但是一些软件已经可以模拟人的行为破解滑块验证码。本项目就是通过对鼠标轨迹的特征分析，判定是否是人的行为还是机器行为。常见应用场景：网站反爬虫、在线考试系统脚本刷题。',
      author='itmorn',
      author_email='12567148@qq.com',
      url='https://github.com/itmorn/robot-mouse-track',
      install_requires=[],
      license='Apache License',
      # packages=find_packages(),
      packages=['robot_mouse_track','robot_mouse_track.risk_motion'],
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )
