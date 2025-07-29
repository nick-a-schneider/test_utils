cmake_minimum_required(VERSION 3.15)
project(test_utils CXX)




add_library(test_utils src/test_utils.cpp)
target_include_directories(test_utils PUBLIC include)



set_target_properties(test_utils PROPERTIES PUBLIC_HEADER "include/test_utils.h")
install(TARGETS test_utils)
