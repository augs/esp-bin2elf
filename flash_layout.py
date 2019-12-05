# esp-bin2elf written by Joel Sandin <jsandin@gmail.com>
#
# MIT licence

# data from here: https://github.com/esp8266/esp8266-wiki/wiki/Memory-Map
#
# I'm not sure if these values are true for all flash chip sizes and (2nd+ stage)
# bootloader versions so take these as "guidelines" - study the bootloader for
# the target, poke through the actual flash dump, adjust values accordingly.


class FlashDataSection(object):
    def __init__(self, offset, size, name, description):
        self.offset = offset    # byte offset in flash dump
        self.size = size        # size in k (1024 bytes)
        self.name = name
        self.description = description

    def __str__(self):
        rep = "FlashDataSection("
        rep += "offset: 0x%x, " % self.offset
        rep += "size (in k, or 1024 bytes): %d, " % self.size
        rep += "name: %s, " % self.name
        rep += "description: %s)" % self.description

        return rep


# commented sections below aren't included by existing linker scripts,
# and may not appear in the memory map - read from flash directly?
layout_without_ota_updates = {
    '.text': FlashDataSection(0x00000, 248, '.text', 'User Application'),
    '.irom0.text': FlashDataSection(0x40000, 240, '.irom0.text', 'SDK libraries')
    # FlashDataSection(0x3e000, 8, '.master_device_key', 'OTA device key')
    # FlashDataSection(0x7c000, 8, '.esp_init_data_default', 'Default config'),
    # FlashDataSection(0x7e000, 8, '.blank', 'Wifi configuration?')
}

ota_slot_one = {
    '.text': FlashDataSection(0x01000, 64, '.text', 'User Application, slot 1'),
    '.irom0.text': FlashDataSection(0x11000, 180, '.irom0.text', 'SDK libraries, slot 1')
    # FlashDataSection(0x3e000, 8, '.master_device_key', 'OTA device key')
    # FlashDataSection(0x40000, 4, '.unused', 'Unused')
    # FlashDataSection(0x7e000, 8, '.blank', 'Wifi configuration?')
}


def make_slot_two_layout(flash_size):
    halfway_point = flash_size / 2
    text_off = halfway_point + 0x1000
    irom_off = text_off + (64 * 1024)

    return {
        '.text': FlashDataSection(text_off, 64, '.text', 'User Application, slot 2'),
        '.irom0.text': FlashDataSection(irom_off, 180, '.irom0.text', 'SDK libraries, slot 2')
        # FlashDataSection(0x3e000, 8, '.master_device_key', 'OTA device key')
        # FlashDataSection(0x40000, 4, '.unused', 'Unused')
        # FlashDataSection(0x7e000, 8, '.blank', 'Wifi configuration?')
    }


ota_slot_two_4_megabit = make_slot_two_layout(0x080000)
ota_slot_two_8_megabit = make_slot_two_layout(0x100000)
