from setuptools import setup

packages = [
    'discordio',
    'discordio.interactions',
    'discordio.core'
]

setup(
    name='discordio',
    description='API wrapper for Discord on Python 3',
    version='0.0.1dev',
    author='timka123',
    packages=packages
)