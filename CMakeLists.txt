cmake_minimum_required(VERSION 3.16.0)
include($ENV{IDF_PATH}/tools/cmake/project.cmake)

list(APPEND EXTRA_COMPONENT_DIRS $ENV{IDF_PATH}/examples/peripherals/rmt/led_strip/components/led_strip)
project(esp_test)
