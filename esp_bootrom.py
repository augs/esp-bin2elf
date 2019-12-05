# esp-bin2elf written by Joel Sandin <jsandin@gmail.com>
#
# MIT licence

def get_bootrom_contents():
    return open('bootrom.bin', 'rb').read()

# boomrom symbols are listed here:
# https://github.com/espressif/ESP8266_RTOS_SDK/blob/master/ld/eagle.rom.addr.v6.ld

symbols = {
    'SPI_sector_erase':   0x400040c0,
    'SPI_page_program':   0x40004174,
    'SPI_read_data':      0x400042ac,
    'SPI_read_status':    0x400043c8,
    'SPI_write_status':   0x40004400,
    'SPI_write_enable':   0x4000443c,
    'Wait_SPI_Idle':      0x4000448c,
    'Enable_QMode':       0x400044c0,
    'Disable_QMode':      0x40004508,

    'Cache_Read_Enable':  0x40004678,
    'Cache_Read_Disable': 0x400047f0,

    'lldesc_build_chain': 0x40004f40,
    'lldesc_num2link':    0x40005050,
    'lldesc_set_owner':   0x4000507c,

    '__adddf3':           0x4000c538,
    '__addsf3':           0x4000c180,
    '__divdf3':           0x4000cb94,
    '__divdi3':           0x4000ce60,
    '__divsi3':           0x4000dc88,
    '__extendsfdf2':      0x4000cdfc,
    '__fixdfsi':          0x4000ccb8,
    '__fixunsdfsi':       0x4000cd00,
    '__fixunssfsi':       0x4000c4c4,
    '__floatsidf':        0x4000e2f0,
    '__floatsisf':        0x4000e2ac,
    '__floatunsidf':      0x4000e2e8,
    '__floatunsisf':      0x4000e2a4,
    '__muldf3':           0x4000c8f0,
    '__muldi3':           0x40000650,
    '__mulsf3':           0x4000c3dc,
    '__subdf3':           0x4000c688,
    '__subsf3':           0x4000c268,
    '__truncdfsf2':       0x4000cd5c,
    '__udivdi3':          0x4000d310,
    '__udivsi3':          0x4000e21c,
    '__umoddi3':          0x4000d770,
    '__umodsi3':          0x4000e268,
    '__umulsidi3':        0x4000dcf0,

    'bzero':              0x40002ae8,
    'memcmp':             0x400018d4,
    'memcpy':             0x400018b4,
    'memmove':            0x400018c4,
    'memset':             0x400018a4,

    'strcmp':             0x40002aa8,
    'strcpy':             0x40002a88,
    'strlen':             0x40002ac8,
    'strncmp':            0x40002ab8,
    'strncpy':            0x40002a98,
    'strstr':             0x40002ad8,
}
