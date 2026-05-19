import subprocess

def nuke_drive(device_node):
    print(f"WARNING: Wiping everything on {device_node}...")
    
    # Unmount first
    subprocess.run(["sudo", "umount", device_node], check=False)
    
    # Wipe the partition table and format as FAT32
    try:
        subprocess.run(["sudo", "mkfs.vfat", "-I", device_node], check=True)
        print("Drive formatted successfully. It is now clean.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to format drive: {e}")
