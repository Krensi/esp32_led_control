# Install IDF
* Clone repository to folder (git clone https://github.com/espressif/esp-idf --recursive)
* Go to cloned dir and run install script (e.g. install.bat)
* Add environment variable ESP_IDF and set value to cloned dir path

# Setup project
* Copy any project from the examples folder of the cloned idf dir
* Open dir in CLion
* Edit CMakeLists file to automatically run export script -> This script prepends the needed directories (toolchain, ..) to your system path (see snipped below)
* Setup cmake config according to your target (see options below)
* Configure step should work now. Targets for building and flashing should appear
* COM port can be configured via environment variable ESPPORT -> e.g. ESPPORT=COM5 > Add to cmake configuration

# Open OCD jtag debugging
* Add Open OCD configuration
* Choose open ocd and gdb of esp idf (see installation folder /users/myuser/.espressif). Attention gdb is target specific (different gdb for esp32 and esp32s2)

# CMAKE snippet for running export
```
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
```

# CMAKE options
## ESP32
``
-G Ninja -DPYTHON_DEPS_CHECKED=1 -DESP_PLATFORM=1 -DIDF_TARGET=esp32 -DCCACHE_ENABLE=1
``

## ESP32S2
``
-G Ninja -DPYTHON_DEPS_CHECKED=1 -DESP_PLATFORM=1 -DIDF_TARGET=esp32s2 -DCCACHE_ENABLE=1
``