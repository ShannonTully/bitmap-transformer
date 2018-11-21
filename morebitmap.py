# There is a bunch more stuff you can add if you like
# This is very bare bones

import cmd
import struct
from random import randint


class BitmapManipulator(cmd.Cmd):
    intro = 'Welcome to the bitmap manipulator.   Type help or ? to list commands.\n'
    prompt = '> '

    def invert(self, original, new):
        with open(f'{original}', 'rb') as fd:
            sig = fd.read(2).decode()
            size = struct.unpack('I', fd.read(4))
            reserved_1 = struct.unpack('H', fd.read(2))
            reserved_2 = struct.unpack('H', fd.read(2))
            offset = struct.unpack('H', fd.read(2))

        with open(f'{original}', 'rb') as fd:
            source = bytearray(fd.read())
            mv = memoryview(source)
            mv_list = mv.tolist()

            color_table = mv[54:offset[0]]
            pixel_array = mv[offset[0]:]

        for idx in range(0, len(color_table) - 1):
            color_table[idx] = 255 - color_table[idx]

        mv[54:offset[0]] = color_table

        with open(f'{new}', 'wb') as fw:
            fw.write(mv.tobytes())

    def random_colors(self, original, new):
        with open(f'{original}', 'rb') as fd:
            sig = fd.read(2).decode()
            size = struct.unpack('I', fd.read(4))
            reserved_1 = struct.unpack('H', fd.read(2))
            reserved_2 = struct.unpack('H', fd.read(2))
            offset = struct.unpack('H', fd.read(2))

        with open(f'{original}', 'rb') as fd:
            source = bytearray(fd.read())
            mv = memoryview(source)
            mv_list = mv.tolist()

            color_table = mv[54:offset[0]]
            pixel_array = mv[offset[0]:]

        for idx in range(0, len(color_table) - 1):
            color_table[idx] = randint(0, 255)

        mv[54:offset[0]] = color_table

        with open(f'{new}', 'wb') as fw:
            fw.write(mv.tobytes())

    def random_pixels(self, original, new):
        with open(f'{original}', 'rb') as fd:
            sig = fd.read(2).decode()
            size = struct.unpack('I', fd.read(4))
            reserved_1 = struct.unpack('H', fd.read(2))
            reserved_2 = struct.unpack('H', fd.read(2))
            offset = struct.unpack('H', fd.read(2))

        with open(f'{original}', 'rb') as fd:
            source = bytearray(fd.read())
            mv = memoryview(source)
            mv_list = mv.tolist()

            color_table = mv[54:offset[0]]
            pixel_array = mv[offset[0]:]

        for idx in range(0, len(pixel_array) - 1):
            pixel_array[idx] = randint(0, 255)

        mv[offset[0]:] = pixel_array

        with open(f'{new}', 'wb') as fw:
            fw.write(mv.tobytes())

    def red(self, original, new):
        with open(f'{original}', 'rb') as fd:
            sig = fd.read(2).decode()
            size = struct.unpack('I', fd.read(4))
            reserved_1 = struct.unpack('H', fd.read(2))
            reserved_2 = struct.unpack('H', fd.read(2))
            offset = struct.unpack('H', fd.read(2))

        with open(f'{original}', 'rb') as fd:
            source = bytearray(fd.read())
            mv = memoryview(source)
            mv_list = mv.tolist()

            color_table = mv[54:offset[0]]
            pixel_array = mv[offset[0]:]

        for idx in range(0, len(color_table) - 3, 4):
            color_table[idx+2] = 0

        mv[54:offset[0]] = color_table

        with open(f'{new}', 'wb') as fw:
            fw.write(mv.tobytes())

    def blue(self, original, new):
        with open(f'{original}', 'rb') as fd:
            sig = fd.read(2).decode()
            size = struct.unpack('I', fd.read(4))
            reserved_1 = struct.unpack('H', fd.read(2))
            reserved_2 = struct.unpack('H', fd.read(2))
            offset = struct.unpack('H', fd.read(2))

        with open(f'{original}', 'rb') as fd:
            source = bytearray(fd.read())
            mv = memoryview(source)
            mv_list = mv.tolist()

            color_table = mv[54:offset[0]]
            pixel_array = mv[offset[0]:]

        for idx in range(0, len(color_table) - 3, 4):
            color_table[idx] = 0

        mv[54:offset[0]] = color_table

        with open(f'{new}', 'wb') as fw:
            fw.write(mv.tobytes())

    def green(self, original, new):
        with open(f'{original}', 'rb') as fd:
            sig = fd.read(2).decode()
            size = struct.unpack('I', fd.read(4))
            reserved_1 = struct.unpack('H', fd.read(2))
            reserved_2 = struct.unpack('H', fd.read(2))
            offset = struct.unpack('H', fd.read(2))

        with open(f'{original}', 'rb') as fd:
            source = bytearray(fd.read())
            mv = memoryview(source)
            mv_list = mv.tolist()

            color_table = mv[54:offset[0]]
            pixel_array = mv[offset[0]:]

        for idx in range(0, len(color_table) - 3, 4):
            color_table[idx+1] = 0

        mv[54:offset[0]] = color_table

        with open(f'{new}', 'wb') as fw:
            fw.write(mv.tobytes())

    def do_transform(self, arg):
        """
        To use this type in 'transform' followed by
        the original file location and the new file location
        and the type of change you would like to do.

        transform <original> <new> <transform>
        """
        args = arg.split()
        if args[2] == 'invert':
            self.invert(args[0], args[1])
        elif args[2] == 'random_colors':
            self.random_colors(args[0], args[1])
        elif args[2] == 'random_pixels':
            self.random_pixels(args[0], args[1])
        elif args[2] == 'red':
            self.red(args[0], args[1])
        elif args[2] == 'blue':
            self.blue(args[0], args[1])
        elif args[2] == 'green':
            self.green(args[0], args[1])


if __name__ == '__main__':
    BitmapManipulator().cmdloop()

# Old Stuff

#     source = bytearray(fd.read())
#     mv = memoryview(source)
#     mv_list = mv.tolist()

#     sig = mv[0:2]
#     file_size = mv[2:6]
#     offset = mv[10:14]
#     width = mv[18:22]
#     height = mv[22:26]

#     offset_int = int(''.join([str(num) for num in offset.tolist()]))
#     pixel_array = mv[1078:]

# for idx in range(0, len(pixel_array) - 3, 4):
#     pixel_array[idx] = 255 - pixel_array[idx]
#     pixel_array[idx + 1] = 255 - pixel_array[idx+1]
#     pixel_array[idx + 2] = 255 - pixel_array[idx+2]
#     # pixel_array[idx + 3] = 255 - pixel_array[idx+3]

# mv[1078:] = pixel_array

# with open(f'{new}', 'xb') as fw:
#     fw.write(mv.tobytes())
