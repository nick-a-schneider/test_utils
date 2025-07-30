cmake_minimum_required(VERSION 3.15)
project(test_utils LANGUAGES C)

add_library(test_utils INTERFACE)

target_include_directories(test_utils INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

add_library(test_utils::test_utils ALIAS test_utils)

install(TARGETS test_utils
    EXPORT test_utilsTargets
    INCLUDES DESTINATION include
)

install(DIRECTORY include/ DESTINATION include)

install(EXPORT test_utilsTargets
    FILE test_utilsTargets.cmake
    NAMESPACE test_utils::
    DESTINATION lib/cmake/test_utils
)
