from setuptools import setup, find_packages

setup(name='msgtools',
    python_requires='~=3.5',
    version='0.34.13',
    description='Tools for fixed binary protocols',
    url='https://github.com/MilesEngineering/MsgTools/',
    author='Miles Gazic',
    author_email='miles.gazic@gmail.com',
    license='LGPLv2',
    packages=find_packages(),
    zip_safe=False,
    keywords='development tools messaging messages message generator protocol networking',
    project_urls = {
        'Documentation': 'https://github.com/MilesEngineering/MsgTools/wiki',
        'Source': 'https://github.com/MilesEngineering/MsgTools/',
        'Tracker': 'https://github.com/MilesEngineering/MsgTools/issues',
    },
    classifiers = [
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Utilities'
    ],
    entry_points = {
        'console_scripts': ['msgparser=msgtools.parser.parser:main',
                            'msgcheck=msgtools.parser.check:main',
                            'msgconsole=msgtools.console.console:main',
                            'msginflux=msgtools.database.influxdb:main',
                            'msginitwebapp=msgtools.webapp.webapp:main',
                            'msgfindprints=msgtools.debug.findprints:main',
                            'msgcsvparse=msgtools.csvparse.csvparse:main'],
        'gui_scripts': ['msgscope=msgtools.scope.scope:main [gui]',
                        'msgserver=msgtools.server.server:main [gui]',
                        'msginspector=msgtools.inspector.inspector:main [gui]',
                        'msgguibuilder=msgtools.guibuilder.guibuilder:main [gui]',
                        'msgscript=msgtools.script.script:main [gui]',
                        'msgplot=msgtools.lib.msgplot:main [gui]',
                        'msgbandwidthtestecho=msgtools.noisemaker.bandwidthtestecho:main [gui]',
                        'msgbandwidthtester=msgtools.noisemaker.bandwidthtester:main [gui]',
                        'msgnoisemaker=msgtools.noisemaker.noisemaker:main [gui]',
                        'msglumberjack=msgtools.lumberjack.lumberjack:main [gui]',
                        'msgdebug=msgtools.debug.debug:main [gui]',
                        'msglauncher=msgtools.launcher.launcher:main [gui]'],
        'msgtools.parser.plugin': ['c=msgtools.parser.c.language',
                                   'cpp=msgtools.parser.cpp.language',
                                   'java=msgtools.parser.java.language',
                                   'javascript=msgtools.parser.javascript.language',
                                   'python=msgtools.parser.python.language',
                                   'html=msgtools.parser.html.language',
                                   'matlab=msgtools.parser.matlab.language',
                                   'swift=msgtools.parser.swift.language', 
                                   'kotlin=msgtools.parser.kotlin.language'],
        'msgtools.server.plugin': ['serial=msgtools.server.SerialPlugin:plugin_info',
                                   'bluetoothSPP=msgtools.server.SerialPlugin:bt_plugin_info',
                                   'bluetoothRFCOMM=msgtools.server.BluetoothRFCOMM:plugin_info',
                                   'bluetoothRFCOMMQt=msgtools.server.BluetoothRFCOMMQt:plugin_info',
                                   'influxdb=msgtools.database.influx_msgserver_plugin:plugin_info'],
        'msgtools.launcher.plugin': ['scope=msgtools.scope.launcher:info',
                                   'script=msgtools.script.launcher:info',
                                   'server=msgtools.server.launcher:info',
                                   'inspector=msgtools.inspector.launcher:info',
                                   'debug=msgtools.debug.launcher:info'],
    },
    install_requires=[
        'pyyaml',
        'websockets',
        'janus',
        'jinja2'
    ],
    extras_require={
        'gui':  ["pyqtgraph", "pyqt5", 'qscintilla'],
        'serverserial': ["pyqtserial"],
    },
    package_data={
        # Include all Template files for the code generator and web app tool
        '': ['*Template*', 'bootstrap.min.css', 'webapp/template.*', 'webapp/lib/**', '*.png']
    }
)
