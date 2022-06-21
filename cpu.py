inter = 0

def do_insturctions(insts):
    # inst = instuction
    # insts = instuctions
    inst_ptr = 0
    not_done = True

    while not_done:
        operands = []
        
        match insts[inst_ptr]:
            new_inst_ptr = inst_ptr+1
            
            # goto next instuction
            case 0:
                inst_ptr = new_inst_ptr
            # long jmp with 64 bit uint
            case 1:
                if len(insts) >= new_inst_ptr:
                    inst_ptr = insts[new_inst_ptr]
                else:
                    # inst id, memory address
                    return [1, new_inst_ptr]
            # interupt with id X
            case 2:
                # todo: make this use a table of interupts that are
                # made by the os/bios
                inter = insts[new_inst_ptr]
                return
                

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
    print("bios starting")
    boot()
