inter = 0
int_table = []

def jmp_x_bytes(X, new_ptr):
    return int.from_bytes(new_ptr+X, 'little')

def do_insturctions(insts):
    # inst = instuction
    # insts = instuctions
    inst_ptr = 0
    not_done = True

    while not_done:
        operands = []
        new_inst_ptr = inst_ptr+1
        
        match insts[inst_ptr]:
            
            # goto next instuction
            case 0:
                inst_ptr = new_inst_ptr
                

#                           == jumps ==

            # long jmp with 64 bit uint
            case 1:
                #inst_ptr = int.from_bytes(new_inst_ptr:new_inst_ptr+8, 'little')
                inst_ptr = jmp_x_bytes(8, new_inst_ptr)
            # 32 bit jmp
            case 2:
                inst_ptr = jmp_x_bytes(4, new_inst_ptr)
            # 16 bit jmp
            case 3:
                inst_ptr = jmp_x_bytes(2, new_inst_ptr)
            # 8 bit jmp
            case 4:
                inst_ptr = jmp_x_bytes(1, new_inst_ptr)
#                       == other things ==
            # interupt with id X
            case 10:
                inter = insts[new_inst_ptr]
                inst_ptr = int_table[insts[new_inst_ptr]]
                

def boot():
    # TODO: move this to the bios.
    # the cpu doesn't look for bootable devices;
    # the bios does that. that's the main point of the bios.
    with open("hard_drive.bin", "rb") as hdd:
        hdd.seek(512)
        if hdd.read(2) == b"\x55\xaa":
            hdd.seek(0)
        else:
            print("no bootable storage.")
            while 1:
                input("")


if __name__ == "__main__":
    print("starting emulator")
    boot()
