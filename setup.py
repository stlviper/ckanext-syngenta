from setuptools import find_packages, setup

version = '0.1'

setup(
    name='ckanext-syngenta',
    version=version,
    description="CKAN extension for syngenta.",
    long_description="""\
    """,
    classifiers=[],
    keywords='ckan ckanext syngenta extension data theme',
    author='Corey Merkel',
    author_email='corey.merkel@ogsystems.com',
    url='',
    license='GPL v2.',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.syngenta'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    # Add plugins here, eg
    # myplugin=ckanext.syngenta:PluginClass
    syngenta=ckanext.syngenta.plugin:SyngentaPlugin
    """,
)
