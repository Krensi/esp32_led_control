# The following lines of boilerplate have to be in your project's CMakeLists
# in this exact order for cmake to work correctly

# BUILD OPTIONS
## ESP 32
# cmake -G Ninja -DPYTHON_DEPS_CHECKED=1 -DESP_PLATFORM=1 -DIDF_TARGET=esp32 -DCCACHE_ENABLE=1
## ESP 32S2
# -G Ninja -DPYTHON_DEPS_CHECKED=1 -DESP_PLATFORM=1 -DIDF_TARGET=esp32s2 -DCCACHE_ENABLE=1

cmake_minimum_required(VERSION 3.5)

if(NOT DEFINED ENV{IDF_PATH})
    # Set idf path to the folder of your idf git repo
    message(CRITICAL_ERROR Environment variable \"IDF_PATH\" is not set!)
else()
    message(STATUS Environment variable set idf path to: $ENV{IDF_PATH})
    message(STATUS Running export script to export PATH variable)

    # Load environment variables
    execute_process(COMMAND cmd /c $ENV{IDF_PATH}/export.bat
            WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
            RESULT_VARIABLE GIT_SUBMOD_RESULT)
endif()

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(startup_time)
