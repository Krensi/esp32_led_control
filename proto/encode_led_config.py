import led_config_pb2

def c_array(binary_string):
    print("{ ", end="")

    for i, element in enumerate(binary_string):
        print(f"0x{element:x}", end="")

        if i < len(binary_string) - 1:
            print(", ", end="")

    print(" }")

myConfig = led_config_pb2.LedConfig()
segment = myConfig.segments.add()

segment.index_led_start = 0
segment.index_led_end = 24

standard_mode = led_config_pb2.LedConfig.Segment.Standard()
color_list = standard_mode.color_list.add()
color_list.value_red = 255
color_list.value_green = 0
color_list.value_blue = 0

segment.standard.CopyFrom(standard_mode)

result = myConfig.SerializeToString()

print("Config")
c_array(result)