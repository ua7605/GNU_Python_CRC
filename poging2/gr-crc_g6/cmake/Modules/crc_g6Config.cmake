INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_CRC_G6 crc_g6)

FIND_PATH(
    CRC_G6_INCLUDE_DIRS
    NAMES crc_g6/api.h
    HINTS $ENV{CRC_G6_DIR}/include
        ${PC_CRC_G6_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    CRC_G6_LIBRARIES
    NAMES gnuradio-crc_g6
    HINTS $ENV{CRC_G6_DIR}/lib
        ${PC_CRC_G6_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(CRC_G6 DEFAULT_MSG CRC_G6_LIBRARIES CRC_G6_INCLUDE_DIRS)
MARK_AS_ADVANCED(CRC_G6_LIBRARIES CRC_G6_INCLUDE_DIRS)

