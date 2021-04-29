INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_CRC crc)

FIND_PATH(
    CRC_INCLUDE_DIRS
    NAMES crc/api.h
    HINTS $ENV{CRC_DIR}/include
        ${PC_CRC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    CRC_LIBRARIES
    NAMES gnuradio-crc
    HINTS $ENV{CRC_DIR}/lib
        ${PC_CRC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(CRC DEFAULT_MSG CRC_LIBRARIES CRC_INCLUDE_DIRS)
MARK_AS_ADVANCED(CRC_LIBRARIES CRC_INCLUDE_DIRS)

