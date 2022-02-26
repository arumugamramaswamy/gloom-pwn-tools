from pwn import gdb, process

def get_process(binary, debug=False) -> process:
    if debug:
        return gdb.debug(binary)
    else:
        return process(binary)

