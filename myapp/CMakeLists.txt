add_executable(../Gui.py)
target_link_libraries(qt-appimage-template Qt5::Core Qt5::Widgets Qt5::Qml ${ZLIB_LIBRARIES})

install(TARGETS qt-appimage-template DESTINATION bin COMPONENT binaries)
