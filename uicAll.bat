pyside6-uic src/ui_main.ui > ui_main.py

rem pyside6-rcc --compress 9 --compress-algo zlib --threshold 20 src/resources.qrc -o resources_rc.py