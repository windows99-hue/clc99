"""
Linux Kernel Boot Simulation using loading99 decorator
使用 loading99 装饰器模拟 Linux 内核启动过程
"""

import time
import random
from clc99 import loading99, err99, print_notrun

print_notrun("made by deepseek")

def print_kernel_header():
    """Print kernel boot header"""
    print("Linux version 6.1.0-generic (user@localhost) (gcc 11.3.0) #1 SMP Mon Nov 13 10:00:00 UTC 2023")
    print()

def simulate_kernel_boot():
    """Simulate the complete Linux kernel boot process"""
    
    print_kernel_header()
    
    # Phase 1: Early kernel initialization
    print("[    0.000000] Initializing kernel...")
    time.sleep(0.5)
    
    # BIOS/UEFI and hardware detection
    @loading99(text="[    0.001234] Detecting hardware...", success_text="OK", suppress_output=True)
    def detect_hardware():
        time.sleep(0.8)
        # Simulate hardware detection
        hardware = ["CPU: Intel(R) Core(TM) i7-12700K", "RAM: 16384MB", "Storage: NVMe SSD 1TB"]
        for item in hardware:
            print(f"[    0.002000] {item}")
            time.sleep(0.1)
    
    detect_hardware()
    
    # Memory initialization
    @loading99(text="[    0.500000] Setting up memory...", success_text="OK", suppress_output=True)
    def setup_memory():
        time.sleep(0.6)
        print("[    0.550000] Memory: 15872K/16384K available")
        print("[    0.551000] DMA zone: 64 pages used for DMA")
    
    setup_memory()
    
    # CPU initialization
    @loading99(text="[    0.800000] Initializing CPUs...", success_text="OK", suppress_output=True)
    def setup_cpus():
        time.sleep(0.4)
        print("[    0.850000] SMP: Total of 8 processors activated")
        print("[    0.851000] CPU: All CPU(s) started in x86_64 mode")
    
    setup_cpus()
    
    # Phase 2: Kernel subsystems
    print("\n[    1.200000] Starting kernel subsystems...")
    
    # Process scheduler
    @loading99(text="[    1.201000] Initializing process scheduler...", success_text="OK")
    def init_scheduler():
        time.sleep(0.5)
    
    init_scheduler()
    
    # Interrupts
    @loading99(text="[    1.500000] Setting up interrupt handling...", success_text="OK")
    def setup_interrupts():
        time.sleep(0.3)
    
    setup_interrupts()
    
    # Timer subsystem
    @loading99(text="[    1.700000] Initializing timer subsystem...", success_text="OK")
    def init_timers():
        time.sleep(0.4)
    
    init_timers()
    
    # Phase 3: Device drivers
    print("\n[    2.000000] Loading device drivers...")
    
    # PCI subsystem
    @loading99(text="[    2.001000] PCI: Probing PCI hardware...", success_text="OK", suppress_output=True)
    def probe_pci():
        time.sleep(0.6)
        devices = [
            "PCI: Found USB controller at 0000:00:14.0",
            "PCI: Found SATA controller at 0000:00:17.0", 
            "PCI: Found Network controller at 0000:02:00.0"
        ]
        for device in devices:
            print(f"[    2.100000] {device}")
            time.sleep(0.1)
    
    probe_pci()
    
    # Storage drivers
    @loading99(text="[    2.500000] Initializing storage controllers...", success_text="OK")
    def init_storage():
        time.sleep(0.5)
    
    init_storage()
    
    # Filesystem drivers
    @loading99(text="[    2.800000] Registering filesystems...", success_text="OK", suppress_output=True)
    def register_filesystems():
        time.sleep(0.4)
        fs_list = ["ext4", "btrfs", "vfat", "ntfs", "proc", "sysfs", "tmpfs"]
        for fs in fs_list:
            print(f"[    2.850000] {fs} filesystem registered")
            time.sleep(0.05)
    
    register_filesystems()
    
    # Network subsystem
    @loading99(text="[    3.100000] Initializing network stack...", success_text="OK")
    def init_network():
        time.sleep(0.5)
    
    init_network()
    
    # Phase 4: Mounting filesystems
    print("\n[    3.500000] Mounting filesystems...")
    
    @loading99(text="[    3.501000] Mounting root filesystem...", success_text="OK", suppress_output=True)
    def mount_root():
        time.sleep(0.7)
        print("[    3.600000] EXT4-fs: mounted filesystem with ordered data mode")
        print("[    3.601000] VFS: Mounted root (ext4 filesystem) on device 8:2")
    
    mount_root()
    
    # Phase 5: Starting userspace
    print("\n[    4.000000] Starting userspace initialization...")
    
    # Init system
    @loading99(text="[    4.001000] Starting init system...", success_text="OK", suppress_output=True)
    def start_init():
        time.sleep(0.8)
        print("[    4.200000] systemd 252.4-1 running in system mode")
        print("[    4.201000] Detected architecture x86-64")
    
    start_init()
    
    # Services starting
    @loading99(text="[    4.500000] Starting system services...", success_text="OK", suppress_output=True)
    def start_services():
        time.sleep(1.0)
        services = [
            "Started Journal Service",
            "Started Device-Mapper Event Activation",
            "Started Network Manager", 
            "Started SSH Server",
            "Started User Login Management",
            "Started Display Manager"
        ]
        for service in services:
            print(f"[    4.600000] {service}")
            time.sleep(0.1)
    
    start_services()
    
    # Final boot message
    print("\n[    5.500000] Linux kernel boot completed successfully!")
    print("[    5.501000] Welcome to Linux 6.1.0-generic")
    print()

def simulate_kernel_boot_with_errors():
    """Simulate kernel boot with potential errors (more realistic)"""
    
    print("\n" + "="*60)
    print("SIMULATION 2: Kernel Boot with Potential Errors")
    print("="*60)
    print()
    
    print_kernel_header()
    print("[    0.000000] Initializing kernel...")
    time.sleep(0.3)
    
    # Hardware detection with potential failure
    @loading99(text="[    0.001000] Detecting hardware...", success_text="OK", suppress_output=True)
    def detect_hardware_with_errors():
        time.sleep(0.5)
        print("[    0.100000] CPU: Intel(R) Core(TM) i7-12700K")
        print("[    0.101000] RAM: 16384MB")
        
        # Simulate occasional hardware issues
        if random.random() < 0.3:
            print("[    0.102000] WARNING: SMBus controller not responding")
        
        print("[    0.103000] Storage: NVMe SSD 1TB")
    
    detect_hardware_with_errors()
    
    # Driver loading with potential failures
    @loading99(text="[    1.500000] Loading device drivers...", success_text="OK", suppress_output=True)
    def load_drivers_with_errors():
        time.sleep(0.6)
        drivers = [
            "ahci: SS PCH AHCI controller found",
            "e1000e: Intel(R) PRO/1000 Network Driver", 
            "nvidia: loading NVIDIA graphics driver"
        ]
        
        for driver in drivers:
            print(f"[    1.600000] {driver}")
            time.sleep(0.1)
            
        # Simulate driver loading failure
        if random.random() < 0.4:
            print("[    1.700000] ERROR: nvidia: Failed to initialize graphics driver")
            print("[    1.701000] WARNING: Falling back to nouveau driver")
    
    load_drivers_with_errors()
    
    # Critical system check
    @loading99(text="[    3.000000] Performing system integrity check...", success_text="PASSED")
    def system_integrity_check():
        time.sleep(0.8)
        # Simulate occasional integrity issues
        if random.random() < 0.2:
            err99("INTEGRITY_FAIL", "Kernel integrity verification failed")
    
    try:
        system_integrity_check()
    except:
        print("[    3.500000] CRITICAL: System boot halted due to integrity failure")
        return
    
    # Final successful boot
    print("\n[    4.500000] Linux kernel boot completed!")
    print("[    4.501000] System ready for login")
    print()

if __name__ == "__main__":
    print("Linux Kernel Boot Simulation")
    print("=" * 50)
    print()
    
    # Run normal boot simulation
    simulate_kernel_boot()
    
    # Wait a moment before next simulation
    time.sleep(2)
    
    print("Boot simulation completed!")