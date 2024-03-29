from setuptools import setup

setup(
    name='statsd-wrap',
    version='1.0.0',
    description='Wrapper for Datadog StatsD client.',
    author='giosg',
    author_email='developers@giosg.com',
    url='https://github.com/giosg/statsd-wrap',
    package_data={"statsd_wrap": ["py.typed"]},
    packages=["statsd_wrap"],
    # TODO: Maybe load these from requirements.txt
    install_requires=[
        'datadog==0.44.0',
    ],
    extras_require={
        'dev': [
            'flake8',
            'mypy',
        ]
    },
    classifiers=[],
)
