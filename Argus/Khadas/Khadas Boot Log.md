```
[   10.060644] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
[   10.060669] Linux version 6.1.99 (khadas@0e524bdb85c1) (aarch64-none-linux-gnu-gcc (Arm GNU Toolchain 12.2.Rel1 (Build arm-12.24)) 12.2.1 20221205, GNU ld (Arm GNU Toolchain 12.2.Rel1 (Build arm-12.24)) 2.39.0.20221210) #1.7.4 SMP Wed Apr 23 18:41:45 CST 2025
[   10.061625] random: crng init done
[   10.067238] Machine model: Khadas Edge2
[   10.073201] earlycon: uart8250 at MMIO32 0x00000000feb50000 (options '')
[   10.077136] printk: bootconsole [uart8250] enabled
[   10.077648] efi: UEFI not found.
[   10.080361] OF: fdt: Reserved memory: failed to reserve memory for node 'drm-cubic-lut@0': base 0x0000000000000000, size 0 MiB
[   10.081462] Reserved memory: created CMA memory pool at 0x00000003ff400000, size 8 MiB
[   10.082188] OF: reserved mem: initialized node cma, compatible id shared-dma-pool
[   10.355618] Zone ranges:
[   10.355866]   DMA      [mem 0x0000000000200000-0x00000000ffffffff]
[   10.356438]   DMA32    empty
[   10.356705]   Normal   [mem 0x0000000100000000-0x00000003ffefffff]
[   10.357272] Movable zone start for each node
[   10.357662] Early memory node ranges
[   10.357990]   node   0: [mem 0x0000000000200000-0x00000000083fffff]
[   10.358567]   node   0: [mem 0x0000000009400000-0x00000000efffffff]
[   10.359143]   node   0: [mem 0x0000000100000000-0x00000003fbffffff]
[   10.359718]   node   0: [mem 0x00000003fc500000-0x00000003ffefffff]
[   10.360293] Initmem setup node 0 [mem 0x0000000000200000-0x00000003ffefffff]
[   10.361733] On node 0, zone DMA: 512 pages in unavailable ranges
[   10.383628] On node 0, zone DMA: 4096 pages in unavailable ranges
[   10.456413] On node 0, zone Normal: 1280 pages in unavailable ranges
[   10.456985] On node 0, zone Normal: 256 pages in unavailable ranges
[   10.457748] psci: probing for conduit method from DT.
[   10.458789] psci: PSCIv1.1 detected in firmware.
[   10.459213] psci: Using standard PSCI v0.2 function IDs
[   10.459694] psci: Trusted OS migration not required
[   10.460149] psci: SMC Calling Convention v1.2
[   10.460872] percpu: Embedded 30 pages/cpu s82728 r8192 d31960 u122880
[   10.461500] pcpu-alloc: s82728 r8192 d31960 u122880 alloc=30*4096
[   10.461512] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 [0] 4 [0] 5 [0] 6 [0] 7 
[   10.461631] Detected VIPT I-cache on CPU0
[   10.462041] CPU features: detected: GIC system register CPU interface
[   10.462630] CPU features: detected: Virtualization Host Extensions
[   10.463203] CPU features: detected: ARM errata 1165522, 1319367, or 1530923
[   10.463844] alternatives: applying boot alternatives
[   10.464732] Built 1 zonelists, mobility grouping on.  Total pages: 4058188
[   10.465369] Kernel command line: root=UUID=9994ebbc-72ff-4fd4-a8f8-057055632ec0 rootflags=data=writeback rw rootfstype=ext4 storagemedia=emmc androidboot.storagemedia=emmc androidboot.mode=normal  khadas_board=Edge2 earlycon=uart8250,mmio32,0xfeb50000 console=ttyFIQ0 console=tty0 irqchip.gicv3_pseudo_nmi=0 partition_type=generic fan=auto lcd_panel=null hwver=EDGE2.V12  androidboot.fwver=bl31-v1.48,bl32-v1.19,uboot-04/23/2025
[   10.469300] Unknown kernel command line parameters "storagemedia=emmc khadas_board=Edge2 partition_type=generic fan=auto lcd_panel=null hwver=EDGE2.V12", will be passed to user space.
[   10.472186] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes, linear)
[   10.473618] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
[   10.474348] mem auto-init: stack:off, heap alloc:off, heap free:off
[   10.474925] software IO TLB: area num 8.
[   10.486434] software IO TLB: mapped [mem 0x00000000e9f00000-0x00000000edf00000] (64MB)
[   10.613066] Memory: 16043156K/16490496K available (15936K kernel code, 6196K rwdata, 6992K rodata, 7168K init, 1716K bss, 439148K reserved, 8192K cma-reserved)
[   10.614498] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=8, Nodes=1
[   10.615129] ftrace: allocating 62818 entries in 246 pages
[   10.709750] ftrace: allocated 246 pages with 6 groups
[   10.710317] trace event string verifier disabled
[   10.710936] rcu: Hierarchical RCU implementation.
[   10.711369] rcu: 	RCU event tracing is enabled.
[   10.711785] 	Rude variant of Tasks RCU enabled.
[   10.712200] 	Tracing variant of Tasks RCU enabled.
[   10.712638] rcu: RCU calculated value of scheduler-enlistment delay is 30 jiffies.
[   10.720426] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[   10.723508] GICv3: GIC: Using split EOI/Deactivate mode
[   10.723990] GICv3: 480 SPIs implemented
[   10.724341] GICv3: 0 Extended SPIs implemented
[   10.724771] Root IRQ handler: gic_handle_irq
[   10.725174] GICv3: GICv3 features: 16 PPIs
[   10.725948] GICv3: CPU0: found redistributor 0 region 0:0x00000000fe680000
[   10.726867] ITS [mem 0xfe640000-0xfe65ffff]
[   10.727296] ITS@0x00000000fe640000: allocated 8192 Devices @1001d0000 (indirect, esz 8, psz 64K, shr 0)
[   10.728177] ITS@0x00000000fe640000: allocated 32768 Interrupt Collections @1001e0000 (flat, esz 2, psz 64K, shr 0)
[   10.729133] ITS: using cache flushing for cmd queue
[   10.729605] ITS [mem 0xfe660000-0xfe67ffff]
[   10.730025] ITS@0x00000000fe660000: allocated 8192 Devices @100200000 (indirect, esz 8, psz 64K, shr 0)
[   10.730900] ITS@0x00000000fe660000: allocated 32768 Interrupt Collections @100210000 (flat, esz 2, psz 64K, shr 0)
[   10.731854] ITS: using cache flushing for cmd queue
[   10.732490] GICv3: using LPI property table @0x0000000100220000
[   10.733135] GIC: using cache flushing for LPI property table
[   10.733656] GICv3: CPU0: using allocated LPI pending table @0x0000000100230000
[   10.734365] rcu: srcu_init: Setting srcu_struct sizes based on contention.
[   10.864425] arch_timer: cp15 timer(s) running at 24.00MHz (phys).
[   10.864986] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
[   10.865965] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
[   10.867917] Console: colour dummy device 80x25
[   10.868329] printk: console [tty0] enabled
[   10.868710] printk: bootconsole [uart8250] disabled
[   10.869189] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=80000)
[   10.869209] pid_max: default: 32768 minimum: 301
[   10.869272] LSM: Security Framework initializing
[   10.869394] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[   10.869435] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[   10.870904] cblist_init_generic: Setting adjustable number of callback queues.
[   10.870922] cblist_init_generic: Setting shift to 3 and lim to 1.
[   10.871000] cblist_init_generic: Setting adjustable number of callback queues.
[   10.871015] cblist_init_generic: Setting shift to 3 and lim to 1.
[   10.871178] rcu: Hierarchical SRCU implementation.
[   10.871190] rcu: 	Max phase no-delay instances is 1000.
[   10.872003] Platform MSI: msi-controller@fe640000 domain created
[   10.872029] Platform MSI: msi-controller@fe660000 domain created
[   10.872386] PCI/MSI: /interrupt-controller@fe600000/msi-controller@fe640000 domain created
[   10.872416] PCI/MSI: /interrupt-controller@fe600000/msi-controller@fe660000 domain created
[   10.872603] EFI services will not be available.
[   10.872893] smp: Bringing up secondary CPUs ...
[   10.874033] Detected VIPT I-cache on CPU1
[   10.874114] GICv3: CPU1: found redistributor 100 region 0:0x00000000fe6a0000
[   10.874131] GICv3: CPU1: using allocated LPI pending table @0x0000000100240000
[   10.874169] CPU1: Booted secondary processor 0x0000000100 [0x412fd050]
[   10.875392] Detected VIPT I-cache on CPU2
[   10.875464] GICv3: CPU2: found redistributor 200 region 0:0x00000000fe6c0000
[   10.875480] GICv3: CPU2: using allocated LPI pending table @0x0000000100250000
[   10.875512] CPU2: Booted secondary processor 0x0000000200 [0x412fd050]
[   10.876662] Detected VIPT I-cache on CPU3
[   10.876733] GICv3: CPU3: found redistributor 300 region 0:0x00000000fe6e0000
[   10.876749] GICv3: CPU3: using allocated LPI pending table @0x0000000100260000
[   10.876779] CPU3: Booted secondary processor 0x0000000300 [0x412fd050]
[   10.877908] CPU features: detected: Spectre-v4
[   10.877912] CPU features: detected: Spectre-BHB
[   10.877915] Detected PIPT I-cache on CPU4
[   10.877960] GICv3: CPU4: found redistributor 400 region 0:0x00000000fe700000
[   10.877970] GICv3: CPU4: using allocated LPI pending table @0x0000000100270000
[   10.877992] CPU4: Booted secondary processor 0x0000000400 [0x414fd0b0]
[   10.879098] Detected PIPT I-cache on CPU5
[   10.879148] GICv3: CPU5: found redistributor 500 region 0:0x00000000fe720000
[   10.879159] GICv3: CPU5: using allocated LPI pending table @0x0000000100280000
[   10.879181] CPU5: Booted secondary processor 0x0000000500 [0x414fd0b0]
[   10.880296] Detected PIPT I-cache on CPU6
[   10.880345] GICv3: CPU6: found redistributor 600 region 0:0x00000000fe740000
[   10.880356] GICv3: CPU6: using allocated LPI pending table @0x0000000100290000
[   10.880377] CPU6: Booted secondary processor 0x0000000600 [0x414fd0b0]
[   10.881474] Detected PIPT I-cache on CPU7
[   10.881525] GICv3: CPU7: found redistributor 700 region 0:0x00000000fe760000
[   10.881535] GICv3: CPU7: using allocated LPI pending table @0x00000001002a0000
[   10.881556] CPU7: Booted secondary processor 0x0000000700 [0x414fd0b0]
[   10.881608] smp: Brought up 1 node, 8 CPUs
[   10.881847] SMP: Total of 8 processors activated.
[   10.881858] CPU features: detected: 32-bit EL0 Support
[   10.881868] CPU features: detected: Data cache clean to the PoU not required for I/D coherence
[   10.881882] CPU features: detected: Common not Private translations
[   10.881893] CPU features: detected: CRC32 instructions
[   10.881903] CPU features: detected: RCpc load-acquire (LDAPR)
[   10.881913] CPU features: detected: LSE atomic instructions
[   10.881923] CPU features: detected: Privileged Access Never
[   10.881933] CPU features: detected: RAS Extension Support
[   10.881944] CPU features: detected: Speculative Store Bypassing Safe (SSBS)
[   10.882011] CPU: All CPU(s) started at EL2
[   10.882023] alternatives: applying system-wide alternatives
[   10.886060] devtmpfs: initialized
[   10.900916] Registered cp15_barrier emulation handler
[   10.900928] Registered setend emulation handler
[   10.901002] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 6370867519511994 ns
[   10.901015] futex hash table entries: 2048 (order: 5, 131072 bytes, linear)
[   10.901185] pinctrl core: initialized pinctrl subsystem
[   10.901407] DMI not present or invalid.
[   10.901524] NET: Registered PF_NETLINK/PF_ROUTE protocol family
[   10.902289] DMA: preallocated 2048 KiB GFP_KERNEL pool for atomic allocations
[   10.902394] DMA: preallocated 2048 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[   10.902495] DMA: preallocated 2048 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[   10.902541] audit: initializing netlink subsys (disabled)
[   10.902633] audit: type=2000 audit(0.036:1): state=initialized audit_enabled=0 res=1
[   10.903189] Registered FIQ tty driver
[   10.903325] thermal_sys: Registered thermal governor 'fair_share'
[   10.903328] thermal_sys: Registered thermal governor 'step_wise'
[   10.903333] thermal_sys: Registered thermal governor 'user_space'
[   10.903338] thermal_sys: Registered thermal governor 'power_allocator'
[   10.903421] cpuidle: using governor menu
[   10.903660] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[   10.903757] ASID allocator initialised with 65536 entries
[   10.905616] ramoops: dmesg-0	0x18000@0x0000000000110000
[   10.905625] ramoops: dmesg-1	0x18000@0x0000000000128000
[   10.905855] ramoops: console	0x80000@0x0000000000140000
[   10.905867] ramoops: pmsg	0x30000@0x00000000001c0000
[   10.906121] printk: console [ramoops-1] enabled
[   10.906127] pstore: Registered ramoops as persistent store backend
[   10.906133] ramoops: using 0xe0000@0x110000, ecc: 0
[   10.931754] platform csi2-dcphy0: Fixed dependency cycle(s) with /mipi0-csi2
[   10.931788] platform mipi0-csi2: Fixed dependency cycle(s) with /csi2-dcphy0
[   10.931877] platform csi2-dcphy1: Fixed dependency cycle(s) with /mipi1-csi2
[   10.931905] platform mipi1-csi2: Fixed dependency cycle(s) with /csi2-dcphy1
[   10.931990] platform csi2-dphy0: Fixed dependency cycle(s) with /mipi2-csi2
[   10.932016] platform mipi2-csi2: Fixed dependency cycle(s) with /csi2-dphy0
[   10.932151] platform mipi0-csi2: Fixed dependency cycle(s) with /rkcif-mipi-lvds
[   10.932178] platform rkcif-mipi-lvds: Fixed dependency cycle(s) with /mipi0-csi2
[   10.932291] platform mipi1-csi2: Fixed dependency cycle(s) with /rkcif-mipi-lvds1
[   10.932318] platform rkcif-mipi-lvds1: Fixed dependency cycle(s) with /mipi1-csi2
[   10.932432] platform mipi2-csi2: Fixed dependency cycle(s) with /rkcif-mipi-lvds2
[   10.932459] platform rkcif-mipi-lvds2: Fixed dependency cycle(s) with /mipi2-csi2
[   10.932575] platform rkcif-mipi-lvds-sditf: Fixed dependency cycle(s) with /rkisp0-vir0
[   10.932602] platform rkisp0-vir0: Fixed dependency cycle(s) with /rkcif-mipi-lvds-sditf
[   10.932669] platform rkcif-mipi-lvds1-sditf: Fixed dependency cycle(s) with /rkisp0-vir1
[   10.932697] platform rkisp0-vir1: Fixed dependency cycle(s) with /rkcif-mipi-lvds1-sditf
[   10.932770] platform rkcif-mipi-lvds2-sditf: Fixed dependency cycle(s) with /rkisp1-vir0
[   10.932797] platform rkisp1-vir0: Fixed dependency cycle(s) with /rkcif-mipi-lvds2-sditf
[   10.942099] platform fdd90000.vop: Fixed dependency cycle(s) with /dp@fde50000
[   10.942130] platform fde50000.dp: Fixed dependency cycle(s) with /vop@fdd90000
[   10.942429] platform fdd90000.vop: Fixed dependency cycle(s) with /hdmi@fde80000
[   10.942458] platform fde80000.hdmi: Fixed dependency cycle(s) with /vop@fdd90000
[   10.948596] platform fed80000.phy: Fixed dependency cycle(s) with /i2c@feaa0000/fusb302@22/connector
[   10.953627] rockchip-gpio fd8a0000.gpio: probed /pinctrl/gpio@fd8a0000
[   10.953921] rockchip-gpio fec20000.gpio: probed /pinctrl/gpio@fec20000
[   10.954112] rockchip-gpio fec30000.gpio: probed /pinctrl/gpio@fec30000
[   10.954345] rockchip-gpio fec40000.gpio: probed /pinctrl/gpio@fec40000
[   10.954564] rockchip-gpio fec50000.gpio: probed /pinctrl/gpio@fec50000
[   10.954603] rockchip-pinctrl pinctrl: probed pinctrl
[   10.956476] hw_wdt enter probe
[   10.956490] hlm hw-gpios: 8.
[   10.956500] create_khadas_attrs
[   10.963481] fiq_debugger fiq_debugger.0: error -ENXIO: IRQ fiq not found
[   10.963496] fiq_debugger fiq_debugger.0: error -ENXIO: IRQ wakeup not found
[   10.963505] fiq_debugger_probe: could not install nmi irq handler
[   10.963764] printk: console [ttyFIQ0] enabled
[   10.963888] Registered fiq debugger ttyFIQ0
[   10.965561] iommu: Default domain type: Translated 
[   10.965572] iommu: DMA domain TLB invalidation policy: strict mode 
[   10.965722] SCSI subsystem initialized
[   10.965787] usbcore: registered new interface driver usbfs
[   10.965807] usbcore: registered new interface driver hub
[   10.965823] usbcore: registered new device driver usb
[   10.965884] mc: Linux media interface: v0.10
[   10.965903] videodev: Linux video capture interface: v2.00
[   10.965933] pps_core: LinuxPPS API ver. 1 registered
[   10.965940] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[   10.965953] PTP clock support registered
[   10.965975] EDAC MC: Ver: 3.0.0
[   10.966261] arm-scmi firmware:scmi: Enabled polling mode TX channel - prot_id:16
[   10.966314] arm-scmi firmware:scmi: SCMI Notifications - Core Enabled.
[   10.966345] arm-scmi firmware:scmi: SCMI Protocol v2.0 'rockchip:' Firmware version 0x0
[   10.967725] Advanced Linux Sound Architecture Driver Initialized.
[   10.969222] rockchip-cpuinfo cpuinfo: SoC		: 35880000
[   10.969233] rockchip-cpuinfo cpuinfo: Serial		: 625cb8526458aaf9
[   10.969966] clocksource: Switched to clocksource arch_sys_counter
[   10.970090] VFS: Disk quotas dquot_6.6.0
[   10.970114] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[   10.970150] FS-Cache: Loaded
[   10.970220] CacheFiles: Loaded
[   10.974328] NET: Registered PF_INET protocol family
[   10.974486] IP idents hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[   10.981199] tcp_listen_portaddr_hash hash table entries: 8192 (order: 5, 131072 bytes, linear)
[   10.981292] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
[   10.981321] TCP established hash table entries: 131072 (order: 8, 1048576 bytes, linear)
[   10.981968] TCP bind hash table entries: 65536 (order: 9, 2097152 bytes, linear)
[   10.983210] TCP: Hash tables configured (established 131072 bind 65536)
[   10.983257] UDP hash table entries: 8192 (order: 6, 262144 bytes, linear)
[   10.983504] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes, linear)
[   10.983792] NET: Registered PF_UNIX/PF_LOCAL protocol family
[   10.983980] RPC: Registered named UNIX socket transport module.
[   10.983990] RPC: Registered udp transport module.
[   10.983996] RPC: Registered tcp transport module.
[   10.984002] RPC: Registered tcp NFSv4.1 backchannel transport module.
[   10.984377] PCI: CLS 0 bytes, default 64
[   10.984715] Trying to unpack rootfs image as initramfs...
[   10.985213] rockchip-thermal fec00000.tsadc: Missing rockchip,grf property
[   10.985424] thermal thermal_zone1: power_allocator: sustainable_power will be estimated
[   10.985499] thermal thermal_zone2: power_allocator: sustainable_power will be estimated
[   10.985573] thermal thermal_zone3: power_allocator: sustainable_power will be estimated
[   10.985646] thermal thermal_zone4: power_allocator: sustainable_power will be estimated
[   10.985720] thermal thermal_zone5: power_allocator: sustainable_power will be estimated
[   10.985794] thermal thermal_zone6: power_allocator: sustainable_power will be estimated
[   10.986030] rockchip-thermal fec00000.tsadc: tsadc is probed successfully!
[   10.990947] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
[   10.991448] kvm [1]: IPA Size Limit: 40 bits
[   10.991466] kvm [1]: GICv3: no GICV resource entry
[   10.991473] kvm [1]: disabling GICv2 emulation
[   10.991486] kvm [1]: GIC system register CPU interface enabled
[   10.992440] kvm [1]: vgic interrupt IRQ9
[   10.992924] kvm [1]: VHE mode initialized successfully
[   11.388289] Freeing initrd memory: 15904K
[   11.446277] Initialise system trusted keyrings
[   11.446399] workingset: timestamp_bits=46 max_order=22 bucket_order=0
[   11.448998] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[   11.449287] NFS: Registering the id_resolver key type
[   11.449303] Key type id_resolver registered
[   11.449310] Key type id_legacy registered
[   11.449345] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
[   11.449353] nfs4flexfilelayout_init: NFSv4 Flexfile Layout Driver Registering...
[   11.468996] Key type asymmetric registered
[   11.469007] Asymmetric key parser 'x509' registered
[   11.469032] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 242)
[   11.469120] io scheduler mq-deadline registered
[   11.469128] io scheduler kyber registered
[   11.470434] rockchip-csi2-dphy-hw fedc0000.csi2-dphy0-hw: csi2 dphy hw probe successfully!
[   11.470526] rockchip-csi2-dphy-hw fedc8000.csi2-dphy1-hw: csi2 dphy hw probe successfully!
[   11.477262] rockchip-hdptx-phy-hdmi fed60000.hdmiphy: hdptx phy init success
[   11.479441] rk-pcie fe190000.pcie: invalid prsnt-gpios property in node
[   11.479801] iep: Module initialized.
[   11.479841] mpp_service mpp-srv: 53c0acb01bce author: Tao Huang 2024-12-09 video: rockchip: mpp: Fix typos in Rockchip copyright notices
[   11.479853] mpp_service mpp-srv: probe start
[   11.481418] mpp_vepu2 jpege-ccu: probing start
[   11.481429] mpp_vepu2 jpege-ccu: probing finish
[   11.482303] mpp_rkvdec2 fdc30000.rkvdec-ccu: rkvdec-ccu, probing start
[   11.482367] mpp_rkvdec2 fdc30000.rkvdec-ccu: ccu-mode: 1
[   11.482376] mpp_rkvdec2 fdc30000.rkvdec-ccu: probing finish
[   11.482722] mpp_rkvenc2 rkvenc-ccu: probing start
[   11.482732] mpp_rkvenc2 rkvenc-ccu: probing finish
[   11.483153] mpp_service mpp-srv: probe success
[   11.486452] rk-pcie fe190000.pcie: can't get current limit.
[   11.486721] rk-pcie fe190000.pcie: host bridge /pcie@fe190000 ranges:
[   11.486761] rk-pcie fe190000.pcie:       IO 0x00f4100000..0x00f41fffff -> 0x00f4100000
[   11.486793] rk-pcie fe190000.pcie:      MEM 0x00f4200000..0x00f4ffffff -> 0x00f4200000
[   11.486821] rk-pcie fe190000.pcie:      MEM 0x0a00000000..0x0a3fffffff -> 0x0a00000000
[   11.486883] rk-pcie fe190000.pcie: iATU unroll: enabled
[   11.486901] rk-pcie fe190000.pcie: iATU regions: 8 ob, 8 ib, align 64K, limit 8G
[   11.493226] dma-pl330 fea10000.dma-controller: Loaded driver for PL330 DMAC-241330
[   11.493249] dma-pl330 fea10000.dma-controller: 	DBUFF-128x8bytes Num_Chans-8 Num_Peri-32 Num_Events-16
[   11.494121] dma-pl330 fea30000.dma-controller: Loaded driver for PL330 DMAC-241330
[   11.494135] dma-pl330 fea30000.dma-controller: 	DBUFF-128x8bytes Num_Chans-8 Num_Peri-32 Num_Events-16
[   11.495006] dma-pl330 fed10000.dma-controller: Loaded driver for PL330 DMAC-241330
[   11.495020] dma-pl330 fed10000.dma-controller: 	DBUFF-128x8bytes Num_Chans-8 Num_Peri-32 Num_Events-16
[   11.495717] rockchip-pvtm fda40000.pvtm: pvtm@0 probed
[   11.495776] rockchip-pvtm fda50000.pvtm: pvtm@1 probed
[   11.495832] rockchip-pvtm fda60000.pvtm: pvtm@2 probed
[   11.495887] rockchip-pvtm fdaf0000.pvtm: pvtm@3 probed
[   11.495938] rockchip-pvtm fdb30000.pvtm: pvtm@4 probed
[   11.496484] rockchip-system-monitor rockchip-system-monitor: system monitor probe
[   11.497228] Serial: 8250/16550 driver, 10 ports, IRQ sharing disabled
[   11.497693] febc0000.serial: ttyS9 at MMIO 0xfebc0000 (irq = 35, base_baud = 1500000) is a 16550A
[   11.503920] rk_iommu fdca0000.iommu: av1d iommu enabled
[   11.506349] rockchip-vop2 fdd90000.vop: Adding to iommu group 18
[   11.515004] rockchip-vop2 fdd90000.vop: [drm:vop2_bind] vp0 assign plane mask: Cluster0 | Esmart0[0x5], primary plane phy id: Esmart0[2]
[   11.515038] rockchip-vop2 fdd90000.vop: [drm:vop2_bind] vp1 assign plane mask: Cluster1 | Esmart1[0xa], primary plane phy id: Esmart1[3]
[   11.515059] rockchip-vop2 fdd90000.vop: [drm:vop2_bind] vp2 assign plane mask: Cluster2 | Esmart2[0x140], primary plane phy id: Esmart2[8]
[   11.515079] rockchip-vop2 fdd90000.vop: [drm:vop2_bind] vp3 assign plane mask: Cluster3 | Esmart3[0x280], primary plane phy id: Esmart3[9]
[   11.515314] [drm] failed to init overlay plane Cluster0-win1
[   11.515353] [drm] failed to init overlay plane Cluster1-win1
[   11.515388] [drm] failed to init overlay plane Cluster2-win1
[   11.515422] [drm] failed to init overlay plane Cluster3-win1
[   11.526758] rockchip-vop2 fdd90000.vop: bin=0
[   11.526977] rockchip-vop2 fdd90000.vop: leakage=46
[   11.526991] rockchip-vop2 fdd90000.vop: leakage-volt-sel=2
[   11.527031] rockchip-vop2 fdd90000.vop: error -ENODEV: _opp_set_regulators: no regulator (vop) found
[   11.527061] rockchip-vop2 fdd90000.vop: failed to set opp config
[   11.527071] rockchip-vop2 fdd90000.vop: failed to init opp info
[   11.527080] rockchip-vop2 fdd90000.vop: Unsupported VOP aclk dvfs
[   11.527094] rockchip-drm display-subsystem: bound fdd90000.vop (ops 0xffffffc0090b3688)
[   11.527620] dwhdmi-rockchip fde80000.hdmi: registered ddc I2C bus driver
[   11.528089] rockchip-drm display-subsystem: bound fde80000.hdmi (ops 0xffffffc0090cc6d0)
[   11.528274] rockchip-drm display-subsystem: bound fde50000.dp (ops 0xffffffc0090cf6c0)
[   11.529392] [drm] Initialized rockchip 4.0.0 20140818 for display-subsystem on minor 0
[   11.529460] rockchip-drm display-subsystem: route-dsi0: failed to get logo,offset
[   11.529475] rockchip-drm display-subsystem: route-hdmi0: failed to get logo,offset
[   11.529486] rockchip-drm display-subsystem: can't not find any logo display
[   11.529498] rockchip-drm display-subsystem: failed to show kernel logo
[   11.529557] rockchip-drm display-subsystem: [drm] Cannot find any crtc or sizes
[   11.529621] rockchip-drm display-subsystem: [drm] Cannot find any crtc or sizes
[   11.529648] rockchip-drm display-subsystem: [drm] Cannot find any crtc or sizes
[   11.529798] rockchip-drm display-subsystem: [drm] run display error_event monitor
[   11.533429] dw-hdmi-qp-hdcp dw-hdmi-qp-hdcp.1.auto: dw_hdcp_qp_hdcp_probe success
[   11.535414] brd: module loaded
[   11.538178] loop: module loaded
[   11.538343] lkdtm: No crash points registered, enable through debugfs
[   11.540355] rockchip-spi feb20000.spi: no high_speed pinctrl state
[   11.540697] spi spi2.0: Fixed dependency cycle(s) with /spi@feb20000/rk806single@0/regulators/DCDC_REG7
[   11.540738] spi spi2.0: Fixed dependency cycle(s) with /spi@feb20000/rk806single@0/pinctrl_rk806/rk806_dvs1_pwrdn
[   11.540756] spi spi2.0: Fixed dependency cycle(s) with /spi@feb20000/rk806single@0/pinctrl_rk806/rk806_dvs3_null
[   11.540772] spi spi2.0: Fixed dependency cycle(s) with /spi@feb20000/rk806single@0/pinctrl_rk806/rk806_dvs2_null
[   11.540788] spi spi2.0: Fixed dependency cycle(s) with /spi@feb20000/rk806single@0/pinctrl_rk806/rk806_dvs1_null
[   11.541249] rk806 spi2.0: chip id: RK806,ver:0x2, 0x1
[   11.541371] rk806 spi2.0: ON: 0x40 OFF:0x0
[   11.541442] rk806 spi2.0: shutdown-sequence missing!
[   11.541453] rk806 spi2.0: vb-shutdown-sequence missing!
[   11.541463] rk806 spi2.0: dvs-suspend-control-by missing!
[   11.552959] rk806 spi2.0: no sleep-setting state
[   11.552976] rk806 spi2.0: no reset-setting pinctrl state
[   11.552986] rk806 spi2.0: no dvs-setting pinctrl state
[   11.553573] rockchip-spi feb20000.spi: probed, poll=0, rsd=0, cs-inactive=0, ready=0
[   11.554997] CAN device driver interface
[   11.556386] platform fc000000.usb: Fixed dependency cycle(s) with /i2c@feaa0000/fusb302@22
[   11.565348] xhci-hcd xhci-hcd.7.auto: xHCI Host Controller
[   11.565375] xhci-hcd xhci-hcd.7.auto: new USB bus registered, assigned bus number 1
[   11.565448] xhci-hcd xhci-hcd.7.auto: hcc params 0x0220fe64 hci version 0x110 quirks 0x0000808002010010
[   11.565480] xhci-hcd xhci-hcd.7.auto: irq 70, io mem 0xfcd00000
[   11.565553] xhci-hcd xhci-hcd.7.auto: xHCI Host Controller
[   11.565566] xhci-hcd xhci-hcd.7.auto: new USB bus registered, assigned bus number 2
[   11.565579] xhci-hcd xhci-hcd.7.auto: Host supports USB 3.0 SuperSpeed
[   11.565657] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
[   11.565672] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   11.565684] usb usb1: Product: xHCI Host Controller
[   11.565693] usb usb1: Manufacturer: Linux 6.1.99 xhci-hcd
[   11.565703] usb usb1: SerialNumber: xhci-hcd.7.auto
[   11.565971] hub 1-0:1.0: USB hub found
[   11.565993] hub 1-0:1.0: 1 port detected
[   11.566158] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[   11.566212] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 6.01
[   11.566225] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   11.566237] usb usb2: Product: xHCI Host Controller
[   11.566246] usb usb2: Manufacturer: Linux 6.1.99 xhci-hcd
[   11.566256] usb usb2: SerialNumber: xhci-hcd.7.auto
[   11.566467] hub 2-0:1.0: USB hub found
[   11.566486] hub 2-0:1.0: 1 port detected
[   11.566675] usbcore: registered new interface driver cdc_acm
[   11.566687] cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
[   11.566752] ehci-platform fc880000.usb: EHCI Host Controller
[   11.566763] ohci-platform fc8c0000.usb: Generic Platform OHCI controller
[   11.566774] ehci-platform fc880000.usb: new USB bus registered, assigned bus number 3
[   11.566782] ohci-platform fc8c0000.usb: new USB bus registered, assigned bus number 4
[   11.566827] usbcore: registered new interface driver uas
[   11.566827] ohci-platform fc8c0000.usb: irq 74, io mem 0xfc8c0000
[   11.566856] ehci-platform fc880000.usb: irq 71, io mem 0xfc880000
[   11.566877] usbcore: registered new interface driver usb-storage
[   11.567024] mousedev: PS/2 mouse device common for all mice
[   11.567128] ehci-platform fc800000.usb: EHCI Host Controller
[   11.567135] ohci-platform fc840000.usb: Generic Platform OHCI controller
[   11.567144] ohci-platform fc840000.usb: new USB bus registered, assigned bus number 5
[   11.567164] ehci-platform fc800000.usb: new USB bus registered, assigned bus number 6
[   11.567203] ohci-platform fc840000.usb: irq 73, io mem 0xfc840000
[   11.567306] ehci-platform fc800000.usb: irq 72, io mem 0xfc800000
[   11.567524] .. rk pwm remotectl v2.0 init
[   11.567653] input: fd8b0030.pwm as /devices/platform/fd8b0030.pwm/input/input0
[   11.567848] remotectl-pwm fd8b0030.pwm: Controller support pwrkey capture
[   11.568745] input: rk805 pwrkey as /devices/platform/feb20000.spi/spi_master/spi2/spi2.0/rk805-pwrkey.5.auto/input/input1
[   11.568994] i2c_dev: i2c /dev entries driver
[   11.579984] ehci-platform fc880000.usb: USB 2.0 started, EHCI 1.00
[   11.580138] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
[   11.580158] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   11.580171] usb usb3: Product: EHCI Host Controller
[   11.580181] usb usb3: Manufacturer: Linux 6.1.99 ehci_hcd
[   11.580190] usb usb3: SerialNumber: fc880000.usb
[   11.580440] hub 3-0:1.0: USB hub found
[   11.580470] hub 3-0:1.0: 1 port detected
[   11.593323] ehci-platform fc800000.usb: USB 2.0 started, EHCI 1.00
[   11.593677] usb usb6: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
[   11.593714] usb usb6: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   11.593742] usb usb6: Product: EHCI Host Controller
[   11.593764] usb usb6: Manufacturer: Linux 6.1.99 ehci_hcd
[   11.593786] usb usb6: SerialNumber: fc800000.usb
[   11.594252] hub 6-0:1.0: USB hub found
[   11.594321] hub 6-0:1.0: 1 port detected
[   11.619050] rtc-hym8563 2-0051: rtc information is valid
[   11.626202] rtc-hym8563 2-0051: registered as rtc0
[   11.627207] rtc-hym8563 2-0051: setting system clock to 2025-05-03T15:34:19 UTC (1746286459)
[   11.627304] mcu_probe
[   11.627407] usb usb5: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 6.01
[   11.627427] usb usb5: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   11.627438] usb usb5: Product: Generic Platform OHCI controller
[   11.627449] usb usb5: Manufacturer: Linux 6.1.99 ohci_hcd
[   11.627458] usb usb5: SerialNumber: fc840000.usb
[   11.627890] hub 5-0:1.0: USB hub found
[   11.627912] hub 5-0:1.0: 1 port detected
[   11.628198] usb usb4: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 6.01
[   11.628238] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   11.628266] usb usb4: Product: Generic Platform OHCI controller
[   11.628289] usb usb4: Manufacturer: Linux 6.1.99 ohci_hcd
[   11.628311] usb usb4: SerialNumber: fc8c0000.usb
[   11.628356] platform csi2-dcphy1: Fixed dependency cycle(s) with /i2c@feab0000/imx415f@1a
[   11.628443] i2c 3-001a: Fixed dependency cycle(s) with /csi2-dcphy1
[   11.628617] platform csi2-dcphy1: Fixed dependency cycle(s) with /i2c@feab0000/os08a10f@36
[   11.628677] i2c 3-0036: Fixed dependency cycle(s) with /csi2-dcphy1
[   11.628887] gsensor_kxtj3 3-000e: sensor_register_device: kxtj9, id = 11
[   11.628900] i2c i2c-3: sensor_probe: gs_kxtj3,00000000a1298283
[   11.628933] hub 4-0:1.0: USB hub found
[   11.628989] hub 4-0:1.0: 1 port detected
[   11.629378] gsensor_kxtj3 3-000e: sensor_chip_init:gs_kxtj3:devid=0x35,ops=0x0000000092c0c50d
[   11.630854] input: gsensor as /devices/platform/feab0000.i2c/i2c-3/3-000e/input/input2
[   11.630936] gsensor_kxtj3 3-000e: sensor_irq_init:use polling,delay=30 ms
[   11.631008] gsensor_kxtj3 3-000e: sensor_misc_device_register:miscdevice: accel
[   11.631020] gsensor_kxtj3 3-000e: sensor_probe:initialized ok,sensor name:kxtj9,type:2,id=11

[   11.631790] platform csi2-dcphy0: Fixed dependency cycle(s) with /i2c@feac0000/imx415b@1a
[   11.631857] i2c 4-001a: Fixed dependency cycle(s) with /csi2-dcphy0
[   11.631983] platform csi2-dcphy0: Fixed dependency cycle(s) with /i2c@feac0000/os08a10b@36
[   11.632043] i2c 4-0036: Fixed dependency cycle(s) with /csi2-dcphy0
[   11.632810] edt_ft5x06 6-0038: probing for EDT FT5x06 I2C
[   11.689092] rk-pcie fe190000.pcie: PCIe Linking... LTSSM is 0x3
[   11.766659] rk-pcie fe190000.pcie: PCIe Link up, LTSSM is 0x30011
[   11.766696] rk-pcie fe190000.pcie: PCIe Gen.1 x1 link up
[   11.766853] rk-pcie fe190000.pcie: PCI host bridge to bus 0004:40
[   11.766883] pci_bus 0004:40: root bus resource [bus 40-4f]
[   11.766915] pci_bus 0004:40: root bus resource [io  0x0000-0xfffff] (bus address [0xf4100000-0xf41fffff])
[   11.766946] pci_bus 0004:40: root bus resource [mem 0xf4200000-0xf4ffffff]
[   11.766971] pci_bus 0004:40: root bus resource [mem 0xa00000000-0xa3fffffff pref]
[   11.767026] pci 0004:40:00.0: [1d87:3588] type 01 class 0x060400
[   11.767070] pci 0004:40:00.0: reg 0x38: [mem 0x00000000-0x0000ffff pref]
[   11.767151] pci 0004:40:00.0: supports D1 D2
[   11.767174] pci 0004:40:00.0: PME# supported from D0 D1 D3hot
[   11.778311] pci 0004:40:00.0: Primary bus is hard wired to 0
[   11.778346] pci 0004:40:00.0: bridge configuration invalid ([bus 01-ff]), reconfiguring
[   11.778569] pci 0004:41:00.0: [14e4:449d] type 00 class 0x028000
[   11.778684] pci 0004:41:00.0: reg 0x10: [mem 0x00000000-0x0000ffff 64bit]
[   11.778762] pci 0004:41:00.0: reg 0x18: [mem 0x00000000-0x003fffff 64bit]
[   11.779322] pci 0004:41:00.0: supports D1 D2
[   11.779345] pci 0004:41:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[   11.790041] pci_bus 0004:41: busn_res: [bus 41-4f] end is updated to 41
[   11.790096] pci 0004:40:00.0: BAR 8: assigned [mem 0xf4200000-0xf47fffff]
[   11.790126] pci 0004:40:00.0: BAR 6: assigned [mem 0xf4800000-0xf480ffff pref]
[   11.790160] pci 0004:41:00.0: BAR 2: assigned [mem 0xf4400000-0xf47fffff 64bit]
[   11.790229] pci 0004:41:00.0: BAR 0: assigned [mem 0xf4200000-0xf420ffff 64bit]
[   11.790298] pci 0004:40:00.0: PCI bridge to [bus 41]
[   11.790322] pci 0004:40:00.0:   bridge window [mem 0xf4200000-0xf47fffff]
[   11.792984] pcieport 0004:40:00.0: PME: Signaling with IRQ 93
[   11.843322] usb 6-1: new high-speed USB device number 2 using ehci-platform
[   11.956836] edt_ft5x06 6-0038: touchscreen probe failed
[   11.956969] goodix_ts_probe() start
[   11.957000] Goodix-TS 6-0014: supply tp not found, using dummy regulator
[   11.990619] usb 6-1: New USB device found, idVendor=1a40, idProduct=0101, bcdDevice= 1.11
[   11.990663] usb 6-1: New USB device strings: Mfr=0, Product=1, SerialNumber=0
[   11.990690] usb 6-1: Product: USB 2.0 Hub
[   11.991241] hub 6-1:1.0: USB hub found
[   11.991368] hub 6-1:1.0: 4 ports detected
[   12.107335] <<-GTP-ERROR->> I2C Read: 0x8000, 10 bytes failed, errcode: -6! Process reset.
[   12.204006] <<-GTP-ERROR->> I2C Read: 0x8000, 10 bytes failed, errcode: -6! Process reset.
[   12.300670] <<-GTP-ERROR->> I2C Read: 0x8000, 10 bytes failed, errcode: -6! Process reset.
[   12.386663] usb 6-1.1: new full-speed USB device number 3 using ehci-platform
[   12.397338] <<-GTP-ERROR->> I2C Read: 0x8000, 10 bytes failed, errcode: -6! Process reset.
[   12.470133] xhci-hcd xhci-hcd.8.auto: xHCI Host Controller
[   12.470158] xhci-hcd xhci-hcd.8.auto: new USB bus registered, assigned bus number 7
[   12.470249] xhci-hcd xhci-hcd.8.auto: hcc params 0x0220fe64 hci version 0x110 quirks 0x0000808002010010
[   12.470280] xhci-hcd xhci-hcd.8.auto: irq 69, io mem 0xfc000000
[   12.470359] xhci-hcd xhci-hcd.8.auto: xHCI Host Controller
[   12.470372] xhci-hcd xhci-hcd.8.auto: new USB bus registered, assigned bus number 8
[   12.470385] xhci-hcd xhci-hcd.8.auto: Host supports USB 3.0 SuperSpeed
[   12.470472] usb usb7: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.01
[   12.470487] usb usb7: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   12.470499] usb usb7: Product: xHCI Host Controller
[   12.470508] usb usb7: Manufacturer: Linux 6.1.99 xhci-hcd
[   12.470518] usb usb7: SerialNumber: xhci-hcd.8.auto
[   12.470761] hub 7-0:1.0: USB hub found
[   12.470786] hub 7-0:1.0: 1 port detected
[   12.470956] usb usb8: We don't know the algorithms for LPM for this host, disabling LPM.
[   12.471022] usb usb8: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 6.01
[   12.471035] usb usb8: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   12.471047] usb usb8: Product: xHCI Host Controller
[   12.471056] usb usb8: Manufacturer: Linux 6.1.99 xhci-hcd
[   12.471066] usb usb8: SerialNumber: xhci-hcd.8.auto
[   12.471282] hub 8-0:1.0: USB hub found
[   12.471304] hub 8-0:1.0: 1 port detected
[   12.494000] <<-GTP-ERROR->> I2C Read: 0x8000, 10 bytes failed, errcode: -6! Process reset.
[   12.590671] <<-GTP-ERROR->> I2C Read: 0x8000, 10 bytes failed, errcode: -6! Process reset.
[   12.602618] usb 6-1.1: New USB device found, idVendor=25a7, idProduct=fa61, bcdDevice= 6.17
[   12.602662] usb 6-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[   12.602690] usb 6-1.1: Product: 2.4G Receiver
[   12.602711] usb 6-1.1: Manufacturer: Compx
[   12.686640] <<-GTP-ERROR->> I2C read 0x8000, 10 bytes, double check failed!
[   12.686652] <<-GTP-ERROR->> Failed to get chip-type, set chip type default: GOODIX_GT9
[   12.687362] <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -6! Process reset.
[   12.783307] <<-GTP-ERROR->> GTP i2c test failed time 1.
[   12.800666] <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -6! Process reset.
[   12.896641] <<-GTP-ERROR->> GTP i2c test failed time 2.
[   12.913999] <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -6! Process reset.
[   13.009970] <<-GTP-ERROR->> GTP i2c test failed time 3.
[   13.027333] <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -6! Process reset.
[   13.123308] <<-GTP-ERROR->> GTP i2c test failed time 4.
[   13.140667] <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -6! Process reset.
[   13.236649] <<-GTP-ERROR->> GTP i2c test failed time 5.
[   13.253303] <goodix_ts_probe>_2788    I2C communication ERROR!
[   13.253314]    <goodix_ts_probe>_2865  prob error !!!!!!!!!!!!!!!
[   13.280604] platform csi2-dphy0: Fixed dependency cycle(s) with /i2c@feca0000/imx415@1a
[   13.280674] i2c 8-001a: Fixed dependency cycle(s) with /csi2-dphy0
[   13.280828] platform csi2-dphy0: Fixed dependency cycle(s) with /i2c@feca0000/os08a10@36
[   13.280887] i2c 8-0036: Fixed dependency cycle(s) with /csi2-dphy0
[   13.281396] dw9714 3-000c: probing...
[   13.281409] dw9714 3-000c: could not get module rockchip,vcm-max-current from dts!
[   13.281422] dw9714 3-000c: could not get module rockchip,vcm-dlc-enable from dts!
[   13.281433] dw9714 3-000c: could not get module rockchip,vcm-mclk from dts!
[   13.281443] dw9714 3-000c: could not get module rockchip,vcm-t-src from dts!
[   13.281453] dw9714 3-000c: could not get module rockchip,vcm-adcanced-mode from dts!
[   13.281464] dw9714 3-000c: could not get module rockchip,vcm-sac-mode from dts!
[   13.281475] dw9714 3-000c: could not get module rockchip,vcm-sac-time from dts!
[   13.281486] dw9714 3-000c: could not get module rockchip,vcm-prescl from dts!
[   13.281496] dw9714 3-000c: could not get module rockchip,vcm-nrc-en from dts!
[   13.281506] dw9714 3-000c: could not get module rockchip,vcm-nrc-mode from dts!
[   13.281517] dw9714 3-000c: could not get module rockchip,vcm-nrc-preset from dts!
[   13.281528] dw9714 3-000c: could not get module rockchip,vcm-nrc-infl from dts!
[   13.281538] dw9714 3-000c: could not get module rockchip,vcm-nrc-time from dts!
[   13.281560] dw9714 3-000c: Failed to get xsd-gpios
[   13.281600] dw9714 3-000c: supply avdd not found, using dummy regulator
[   13.281671] dw9714 3-000c: dw9714_set_power(1048) on(1)
[   13.294436] dw9714 3-000c: retrying I2C... 0
[   13.320218] dw9714 3-000c: retrying I2C... 1
[   13.346885] dw9714 3-000c: retrying I2C... 2
[   13.373549] dw9714 3-000c: retrying I2C... 3
[   13.400217] dw9714 3-000c: retrying I2C... 4
[   13.426638] dw9714 3-000c: i2c write to failed with error -6
[   13.426650] dw9714 3-000c: dw9714 not connect!
[   13.426658] dw9714 3-000c: dw9714_set_power(1048) on(0)
[   13.426671] dw9714 3-000c: Probe failed: -6
[   13.426862] dw9714 4-000c: probing...
[   13.426874] dw9714 4-000c: could not get module rockchip,vcm-max-current from dts!
[   13.426887] dw9714 4-000c: could not get module rockchip,vcm-dlc-enable from dts!
[   13.426898] dw9714 4-000c: could not get module rockchip,vcm-mclk from dts!
[   13.426908] dw9714 4-000c: could not get module rockchip,vcm-t-src from dts!
[   13.426918] dw9714 4-000c: could not get module rockchip,vcm-adcanced-mode from dts!
[   13.426929] dw9714 4-000c: could not get module rockchip,vcm-sac-mode from dts!
[   13.426940] dw9714 4-000c: could not get module rockchip,vcm-sac-time from dts!
[   13.426951] dw9714 4-000c: could not get module rockchip,vcm-prescl from dts!
[   13.426961] dw9714 4-000c: could not get module rockchip,vcm-nrc-en from dts!
[   13.426971] dw9714 4-000c: could not get module rockchip,vcm-nrc-mode from dts!
[   13.426982] dw9714 4-000c: could not get module rockchip,vcm-nrc-preset from dts!
[   13.426992] dw9714 4-000c: could not get module rockchip,vcm-nrc-infl from dts!
[   13.427003] dw9714 4-000c: could not get module rockchip,vcm-nrc-time from dts!
[   13.427023] dw9714 4-000c: Failed to get xsd-gpios
[   13.427055] dw9714 4-000c: supply avdd not found, using dummy regulator
[   13.427115] dw9714 4-000c: dw9714_set_power(1048) on(1)
[   13.439885] dw9714 4-000c: retrying I2C... 0
[   13.447603] rockchip-vop2 fdd90000.vop: [drm:vop2_crtc_atomic_enable] Update mode to 1920x1080p60, type: 10(if:DP0, flag:0x0) for vp2 dclk: 148500000
[   13.448194] rockchip-vop2 fdd90000.vop: [drm:vop2_crtc_atomic_enable] dclk_out2 div: 2 dclk_core2 div: 2
[   13.448647] rockchip-vop2 fdd90000.vop: [drm:vop2_crtc_atomic_enable] set dclk_vop2 to 148500000, get 148500000
[   13.462588] dw-dp fde50000.dp: full-training link: 4 lanes at 2700 MHz
[   13.463554] dw9714 4-000c: retrying I2C... 1
[   13.466986] dw-dp fde50000.dp: clock recovery succeeded
[   13.469004] dw-dp fde50000.dp: channel equalization succeeded
[   13.482014] rockchip-vop2 fdd90000.vop: [drm] vop enable intf:200
[   13.490219] dw9714 4-000c: retrying I2C... 2
[   13.516884] dw9714 4-000c: retrying I2C... 3
[   13.528255] Console: switching to colour frame buffer device 240x67
[   13.543551] dw9714 4-000c: retrying I2C... 4
[   13.545873] rockchip-drm display-subsystem: [drm] fb0: rockchipdrmfb frame buffer device
[   13.569971] dw9714 4-000c: i2c write to failed with error -6
[   13.570006] dw9714 4-000c: dw9714 not connect!
[   13.570029] dw9714 4-000c: dw9714_set_power(1048) on(0)
[   13.570058] dw9714 4-000c: Probe failed: -6
[   13.570202] dw9714 8-000c: probing...
[   13.570227] dw9714 8-000c: could not get module rockchip,vcm-max-current from dts!
[   13.570262] dw9714 8-000c: could not get module rockchip,vcm-dlc-enable from dts!
[   13.570296] dw9714 8-000c: could not get module rockchip,vcm-mclk from dts!
[   13.570328] dw9714 8-000c: could not get module rockchip,vcm-t-src from dts!
[   13.570361] dw9714 8-000c: could not get module rockchip,vcm-adcanced-mode from dts!
[   13.570396] dw9714 8-000c: could not get module rockchip,vcm-sac-mode from dts!
[   13.570429] dw9714 8-000c: could not get module rockchip,vcm-sac-time from dts!
[   13.570462] dw9714 8-000c: could not get module rockchip,vcm-prescl from dts!
[   13.570495] dw9714 8-000c: could not get module rockchip,vcm-nrc-en from dts!
[   13.570527] dw9714 8-000c: could not get module rockchip,vcm-nrc-mode from dts!
[   13.570560] dw9714 8-000c: could not get module rockchip,vcm-nrc-preset from dts!
[   13.570594] dw9714 8-000c: could not get module rockchip,vcm-nrc-infl from dts!
[   13.570627] dw9714 8-000c: could not get module rockchip,vcm-nrc-time from dts!
[   13.570669] dw9714 8-000c: Failed to get xsd-gpios
[   13.570715] dw9714 8-000c: supply avdd not found, using dummy regulator
[   13.570793] dw9714 8-000c: dw9714_set_power(1048) on(1)
[   13.583547] dw9714 8-000c: retrying I2C... 0
[   13.610218] dw9714 8-000c: retrying I2C... 1
[   13.636884] dw9714 8-000c: retrying I2C... 2
[   13.663552] dw9714 8-000c: retrying I2C... 3
[   13.690217] dw9714 8-000c: retrying I2C... 4
[   13.716637] dw9714 8-000c: i2c write to failed with error -6
[   13.716667] dw9714 8-000c: dw9714 not connect!
[   13.716690] dw9714 8-000c: dw9714_set_power(1048) on(0)
[   13.716719] dw9714 8-000c: Probe failed: -6
[   13.718558] rkcifhw fdce0000.rkcif: Adding to iommu group 17
[   13.720435] rkcifhw fdce0000.rkcif: No reserved memory region assign to CIF
[   13.721612] rkcif rkcif-mipi-lvds: Adding to iommu group 17
[   13.722690] rkcif rkcif-mipi-lvds: rkcif driver version: v00.02.00
[   13.723838] rkcif rkcif-mipi-lvds: attach to cif hw node
[   13.724895] rkcif rkcif-mipi-lvds: rkcif wait line 0
[   13.725936] rkcif rkcif-mipi-lvds: rkcif fastboot reserve bufs num 3
[   13.726976] : terminal subdev does not exist
[   13.727998] : terminal subdev does not exist
[   13.728998] : terminal subdev does not exist
[   13.729981] : terminal subdev does not exist
[   13.730959] : get_remote_sensor: video pad[0] is null
[   13.731946] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.732941] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.733933] : get_remote_sensor: video pad[0] is null
[   13.734907] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.735886] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.736861] : get_remote_sensor: video pad[0] is null
[   13.737819] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.738783] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.739746] : get_remote_sensor: video pad[0] is null
[   13.740710] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.741684] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.743606] rkcif rkcif-mipi-lvds: No memory-region-thunderboot specified
[   13.744711] rkcif rkcif-mipi-lvds1: Adding to iommu group 17
[   13.745675] rkcif rkcif-mipi-lvds1: rkcif driver version: v00.02.00
[   13.746688] rkcif rkcif-mipi-lvds1: attach to cif hw node
[   13.747618] rkcif rkcif-mipi-lvds1: rkcif wait line 0
[   13.748534] rkcif rkcif-mipi-lvds1: rkcif fastboot reserve bufs num 3
[   13.749452] : terminal subdev does not exist
[   13.750375] : terminal subdev does not exist
[   13.751278] : terminal subdev does not exist
[   13.752166] : terminal subdev does not exist
[   13.753051] : get_remote_sensor: video pad[0] is null
[   13.753939] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.754834] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.755717] : get_remote_sensor: video pad[0] is null
[   13.756588] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.757481] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.758373] : get_remote_sensor: video pad[0] is null
[   13.759267] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.760188] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.761101] : get_remote_sensor: video pad[0] is null
[   13.762015] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.762951] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.764776] rkcif rkcif-mipi-lvds1: No memory-region-thunderboot specified
[   13.765869] rkcif rkcif-mipi-lvds2: Adding to iommu group 17
[   13.766856] rkcif rkcif-mipi-lvds2: rkcif driver version: v00.02.00
[   13.767873] rkcif rkcif-mipi-lvds2: attach to cif hw node
[   13.768844] rkcif rkcif-mipi-lvds2: rkcif wait line 0
[   13.769817] rkcif rkcif-mipi-lvds2: rkcif fastboot reserve bufs num 3
[   13.770804] : terminal subdev does not exist
[   13.771790] : terminal subdev does not exist
[   13.772771] : terminal subdev does not exist
[   13.773755] : terminal subdev does not exist
[   13.774722] : get_remote_sensor: video pad[0] is null
[   13.775688] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.776673] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.777658] : get_remote_sensor: video pad[0] is null
[   13.778649] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.779665] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.780694] : get_remote_sensor: video pad[0] is null
[   13.781727] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.782777] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.783832] : get_remote_sensor: video pad[0] is null
[   13.784887] : rkcif_update_sensor_info: stream[0] get remote sensor_sd failed!
[   13.785960] : rkcif_scale_set_fmt: req(40, 30) src out(0, 0)
[   13.787927] rkcif rkcif-mipi-lvds2: No memory-region-thunderboot specified
[   13.790232] rockchip-mipi-csi2-hw fdd10000.mipi0-csi2-hw: enter mipi csi2 hw probe!
[   13.791429] rockchip-mipi-csi2-hw fdd10000.mipi0-csi2-hw: probe success, v4l2_dev:mipi0-csi2-hw!
[   13.792557] rockchip-mipi-csi2-hw fdd20000.mipi1-csi2-hw: enter mipi csi2 hw probe!
[   13.793735] rockchip-mipi-csi2-hw fdd20000.mipi1-csi2-hw: probe success, v4l2_dev:mipi1-csi2-hw!
[   13.794867] rockchip-mipi-csi2-hw fdd30000.mipi2-csi2-hw: enter mipi csi2 hw probe!
[   13.796039] rockchip-mipi-csi2-hw fdd30000.mipi2-csi2-hw: probe success, v4l2_dev:mipi2-csi2-hw!
[   13.797175] rockchip-mipi-csi2-hw fdd40000.mipi3-csi2-hw: enter mipi csi2 hw probe!
[   13.798361] rockchip-mipi-csi2-hw fdd40000.mipi3-csi2-hw: probe success, v4l2_dev:mipi3-csi2-hw!
[   13.799510] rockchip-mipi-csi2-hw fdd50000.mipi4-csi2-hw: enter mipi csi2 hw probe!
[   13.800716] rockchip-mipi-csi2-hw fdd50000.mipi4-csi2-hw: probe success, v4l2_dev:mipi4-csi2-hw!
[   13.801881] rockchip-mipi-csi2-hw fdd60000.mipi5-csi2-hw: enter mipi csi2 hw probe!
[   13.803072] rockchip-mipi-csi2-hw fdd60000.mipi5-csi2-hw: probe success, v4l2_dev:mipi5-csi2-hw!
[   13.804674] rockchip-mipi-csi2 mipi0-csi2: attach to csi2 hw node
[   13.805817] rkcif rkcif-mipi-lvds: Entity type for entity rockchip-mipi-csi2 was not initialized!
[   13.806960] rockchip-mipi-csi2: Async registered subdev
[   13.808088] rockchip-mipi-csi2: probe success, v4l2_dev:rkcif-mipi-lvds!
[   13.809425] rockchip-mipi-csi2 mipi1-csi2: attach to csi2 hw node
[   13.810575] rkcif rkcif-mipi-lvds1: Entity type for entity rockchip-mipi-csi2 was not initialized!
[   13.811717] rockchip-mipi-csi2: Async registered subdev
[   13.812853] rockchip-mipi-csi2: probe success, v4l2_dev:rkcif-mipi-lvds1!
[   13.814181] rockchip-mipi-csi2 mipi2-csi2: attach to csi2 hw node
[   13.815329] rkcif rkcif-mipi-lvds2: Entity type for entity rockchip-mipi-csi2 was not initialized!
[   13.816477] rockchip-mipi-csi2: Async registered subdev
[   13.817626] rockchip-mipi-csi2: probe success, v4l2_dev:rkcif-mipi-lvds2!
[   13.819911] rkisp_hw fdcb0000.rkisp: Adding to iommu group 15
[   13.821222] rkisp_hw fdcb0000.rkisp: is_thunderboot: 0
[   13.822386] rkisp_hw fdcb0000.rkisp: Missing rockchip,grf property
[   13.823565] rkisp_hw fdcb0000.rkisp: max input:0x0@0fps
[   13.824822] rkisp_hw fdcb0000.rkisp: no find phandle sram
[   13.826110] rkisp_hw fdcc0000.rkisp: Adding to iommu group 16
[   13.827426] rkisp_hw fdcc0000.rkisp: is_thunderboot: 0
[   13.828600] rkisp_hw fdcc0000.rkisp: Missing rockchip,grf property
[   13.829779] rkisp_hw fdcc0000.rkisp: max input:0x0@0fps
[   13.831045] rkisp_hw fdcc0000.rkisp: no find phandle sram
[   13.832466] rkisp rkisp0-vir0: rkisp driver version: v02.09.00
[   13.833695] rkisp rkisp0-vir0: No memory-region-thunderboot specified
[   13.834923] rkisp rkisp0-vir0: Entity type for entity rkisp-isp-subdev was not initialized!
[   13.836866] rkisp rkisp0-vir1: rkisp driver version: v02.09.00
[   13.838063] rkisp rkisp0-vir1: No memory-region-thunderboot specified
[   13.839280] rkisp rkisp0-vir1: Entity type for entity rkisp-isp-subdev was not initialized!
[   13.841196] rkisp rkisp1-vir0: rkisp driver version: v02.09.00
[   13.842410] rkisp rkisp1-vir0: No memory-region-thunderboot specified
[   13.843634] rkisp rkisp1-vir0: Entity type for entity rkisp-isp-subdev was not initialized!
[   13.846705] usbcore: registered new interface driver uvcvideo
[   13.849768] cpu cpu0: bin=0
[   13.851106] cpu cpu0: leakage=15
[   13.853715] cpu cpu0: pvtm=1470
[   13.855027] cpu cpu0: pvtm-volt-sel=3
[   13.858150] cpu cpu4: bin=0
[   13.859450] cpu cpu4: leakage=11
[   13.867033] cpu cpu4: pvtm=1699
[   13.871602] cpu cpu4: pvtm-volt-sel=4
[   13.875449] cpu cpu6: bin=0
[   13.876747] cpu cpu6: leakage=12
[   13.884330] cpu cpu6: pvtm=1708
[   13.889354] cpu cpu6: pvtm-volt-sel=4
[   13.892434] cpu cpu0: avs=0
[   13.893541] cpu cpu0: rockchip_pvtpll_set_volt_sel: error cfg clk_id=0 voltsel (-1)
[   13.895847] cpu cpu4: avs=0
[   13.896946] cpu cpu4: rockchip_pvtpll_set_volt_sel: error cfg clk_id=2 voltsel (-1)
[   13.899093] cpu cpu6: avs=0
[   13.900196] cpu cpu6: rockchip_pvtpll_set_volt_sel: error cfg clk_id=3 voltsel (-1)
[   13.901388] cpu cpu0: l=15000 h=85000 hyst=5000 l_limit=0 h_limit=1608000000 h_table=0
[   13.902855] cpu cpu0: EM: OPP:816000 is inefficient
[   13.902951] cpu cpu0: EM: created perf domain
[   13.904742] cpu cpu4: l=15000 h=85000 hyst=5000 l_limit=0 h_limit=2208000000 h_table=0
[   13.914091] cpu cpu4: EM: OPP:1008000 is inefficient
[   13.914098] cpu cpu4: EM: OPP:816000 is inefficient
[   13.914277] cpu cpu4: EM: created perf domain
[   13.916747] cpu cpu6: l=15000 h=85000 hyst=5000 l_limit=0 h_limit=2208000000 h_table=0
[   13.934416] cpu cpu6: EM: OPP:1008000 is inefficient
[   13.934420] cpu cpu6: EM: OPP:816000 is inefficient
[   13.934505] cpu cpu6: EM: created perf domain
[   13.935892] sdhci: Secure Digital Host Controller Interface driver
[   13.936517] sdhci: Copyright(c) Pierre Ossman
[   13.937137] Synopsys Designware Multimedia Card Interface Driver
[   13.937946] sdhci-pltfm: SDHCI platform and OF driver helper
[   13.939673] arm-scmi firmware:scmi: Failed. SCMI protocol 17 not active.
[   13.940470] SMCCC: SOC_ID: ARCH_SOC_ID not implemented, skipping ....
[   13.941029] mmc0: CQHCI version 5.10
[   13.941721] cryptodev: driver 1.12 loaded.
[   13.945134] hid: raw HID events driver (C) Jiri Kosina
[   13.948597] input: Compx 2.4G Receiver as /devices/platform/fc800000.usb/usb6/6-1/6-1.1/6-1.1:1.0/0003:25A7:FA61.0001/input/input4
[   13.975317] mmc0: SDHCI controller on fe2e0000.mmc [fe2e0000.mmc] using ADMA
[   14.007573] hid-generic 0003:25A7:FA61.0001: input,hidraw0: USB HID v1.10 Keyboard [Compx 2.4G Receiver] on usb-fc800000.usb-1.1/input0
[   14.013686] input: Compx 2.4G Receiver Mouse as /devices/platform/fc800000.usb/usb6/6-1/6-1.1/6-1.1:1.1/0003:25A7:FA61.0002/input/input5
[   14.017043] input: Compx 2.4G Receiver as /devices/platform/fc800000.usb/usb6/6-1/6-1.1/6-1.1:1.1/0003:25A7:FA61.0002/input/input6
[   14.027676] input: Compx 2.4G Receiver Consumer Control as /devices/platform/fc800000.usb/usb6/6-1/6-1.1/6-1.1:1.1/0003:25A7:FA61.0002/input/input7
[   14.054798] mmc0: Command Queue Engine enabled
[   14.056818] mmc0: new HS400 Enhanced strobe MMC card at address 0001
[   14.059376] mmcblk0: mmc0:0001 CJTD4R 58.2 GiB 
[   14.068037]  mmcblk0: p1 p2
[   14.072346] mmcblk0boot0: mmc0:0001 CJTD4R 4.00 MiB 
[   14.076468] mmcblk0boot1: mmc0:0001 CJTD4R 4.00 MiB 
[   14.078957] mmcblk0rpmb: mmc0:0001 CJTD4R 4.00 MiB, chardev (236:0)
[   14.093571] input: Compx 2.4G Receiver System Control as /devices/platform/fc800000.usb/usb6/6-1/6-1.1/6-1.1:1.1/0003:25A7:FA61.0002/input/input8
[   14.096061] hid-generic 0003:25A7:FA61.0002: input,hiddev96,hidraw1: USB HID v1.10 Mouse [Compx 2.4G Receiver] on usb-fc800000.usb-1.1/input1
[   14.098183] usbcore: registered new interface driver usbhid
[   14.100248] usbhid: USB HID core driver
[   14.107634] optee: probing for conduit method.
[   14.109700] optee: revision 3.13 (57604957)
[   14.109906] optee: dynamic shared memory is enabled
[   14.114319] optee: initialized driver
[   14.117742] usbcore: registered new interface driver snd-usb-audio
[   14.122421] es8316 3-0010: ES8316 doesn't exist, exit of probe!
[   14.130484] rockchip-i2s-tdm fddf0000.i2s: CLK-ALWAYS-ON: mclk: 12288000, bclk: 3072000, fsync: 48000
[   14.134165] rockchip-i2s-tdm fe470000.i2s: Register PCM for TRCM mode
[   14.140706] debugfs: File 'Capture' in directory 'dapm' already present!
[   14.144108] input: rockchip-dp0 rockchip-dp0 as /devices/platform/dp0-sound/sound/card0/input10
[   14.146706] input: rockchip-hdmi0 rockchip-hdmi0 as /devices/platform/hdmi0-sound/sound/card1/input11
[   14.149609] NET: Registered PF_PACKET protocol family
[   14.153414] can: controller area network core
[   14.157266] NET: Registered PF_CAN protocol family
[   14.159753] can: raw protocol
[   14.162137] can: broadcast manager protocol
[   14.164501] can: netlink gateway - max_hops=1
[   14.167146] [BT_RFKILL]: Enter rfkill_rk_init
[   14.169508] [WLAN_RFKILL]: Enter rfkill_wlan_init
[   14.172210] [WLAN_RFKILL]: Enter rfkill_wlan_probe
[   14.174360] [WLAN_RFKILL]: can't find rockchip,grf property
[   14.176486] [WLAN_RFKILL]: wlan_platdata_parse_dt: wifi_chip_type = ap6275p
[   14.178642] [WLAN_RFKILL]: wlan_platdata_parse_dt: enable wifi power control.
[   14.180806] [WLAN_RFKILL]: wlan_platdata_parse_dt: wifi power controled by gpio.
[   14.183037] [WLAN_RFKILL]: wlan_platdata_parse_dt: WIFI,host_wake_irq = 0, flags = 0.
[   14.185235] [WLAN_RFKILL]: wlan_platdata_parse_dt: The ref_wifi_clk not found !
[   14.187450] [WLAN_RFKILL]: rfkill_wlan_probe: init gpio
[   14.188543] [WLAN_RFKILL]: rfkill_set_wifi_bt_power: 1
[   14.189630] [WLAN_RFKILL]: Exit rfkill_wlan_probe
[   14.191038] [BT_RFKILL]: bluetooth_platdata_parse_dt: get property: uart_rts_gpios = 122.
[   14.192160] [BT_RFKILL]: bluetooth_platdata_parse_dt: get property: BT,power_gpio = 28.
[   14.193310] [BT_RFKILL]: init ok
[   14.220049] [BT_RFKILL]: bt shut off power
[   14.246806] [BT_RFKILL]: bt_default device registered.
[   14.248002] input: bt-powerkey as /devices/platform/wireless-bluetooth/input/input12
[   14.249365] Key type dns_resolver registered
[   14.251382] imx415 3-001a: driver version: 00.01.08
[   14.255239] imx415 3-001a:  Get hdr mode failed! no hdr default
[   14.257510] vendor storage:20190527 ret = 0
[   14.258994] imx415 3-001a: detect imx415 lane 2
[   14.265214] imx415 3-001a: could not get default pinstate
[   14.267940] imx415 3-001a: could not get sleep pinstate
[   14.270679] imx415 3-001a: supply dvdd not found, using dummy regulator
[   14.273527] imx415 3-001a: supply dovdd not found, using dummy regulator
[   14.276258] imx415 3-001a: supply avdd not found, using dummy regulator
[   14.340797] imx415 3-001a: Unexpected sensor id(000000), ret(-5)
[   14.344700] imx415 4-001a: driver version: 00.01.08
[   14.347759] imx415 4-001a:  Get hdr mode failed! no hdr default
[   14.350821] imx415 4-001a: detect imx415 lane 2
[   14.353458] imx415 4-001a: could not get default pinstate
[   14.355480] imx415 4-001a: could not get sleep pinstate
[   14.357475] imx415 4-001a: supply dvdd not found, using dummy regulator
[   14.359507] imx415 4-001a: supply dovdd not found, using dummy regulator
[   14.361459] imx415 4-001a: supply avdd not found, using dummy regulator
[   14.434309] imx415 4-001a: Unexpected sensor id(000000), ret(-5)
[   14.438297] imx415 8-001a: driver version: 00.01.08
[   14.441514] imx415 8-001a:  Get hdr mode failed! no hdr default
[   14.444710] imx415 8-001a: detect imx415 lane 4
[   14.447969] imx415 8-001a: could not get default pinstate
[   14.451142] imx415 8-001a: could not get sleep pinstate
[   14.454355] imx415 8-001a: supply dvdd not found, using dummy regulator
[   14.457693] imx415 8-001a: supply dovdd not found, using dummy regulator
[   14.460954] imx415 8-001a: supply avdd not found, using dummy regulator
[   14.535406] imx415 8-001a: Unexpected sensor id(000000), ret(-5)
[   14.542173] os08a10 3-0036: driver version: 00.01.00
[   14.547465] os08a10 3-0036: supply avdd not found, using dummy regulator
[   14.552826] os08a10 3-0036: supply dovdd not found, using dummy regulator
[   14.558096] os08a10 3-0036: supply dvdd not found, using dummy regulator
[   14.563362] os08a10 3-0036: lane_num(2)  pixel_rate(360000000)
[   14.568544] os08a10 3-0036: could not get default pinstate
[   14.573717] os08a10 3-0036: could not get sleep pinstate
[   14.600114] os08a10 3-0036: Unexpected sensor id(000000), ret(-5)
[   14.605256] os08a10 3-0036: os08a10_probe(1719) Check id  failed,
               check following information:
               Power/PowerDown/Reset/Mclk/I2cBus !!
[   14.621022] os08a10 4-0036: driver version: 00.01.00
[   14.626098] os08a10 4-0036: supply avdd not found, using dummy regulator
[   14.631147] os08a10 4-0036: supply dovdd not found, using dummy regulator
[   14.634002] os08a10 4-0036: supply dvdd not found, using dummy regulator
[   14.636839] os08a10 4-0036: lane_num(2)  pixel_rate(360000000)
[   14.639618] os08a10 4-0036: could not get default pinstate
[   14.642395] os08a10 4-0036: could not get sleep pinstate
[   14.668185] os08a10 4-0036: Unexpected sensor id(000000), ret(-5)
[   14.670994] os08a10 4-0036: os08a10_probe(1719) Check id  failed,
               check following information:
               Power/PowerDown/Reset/Mclk/I2cBus !!
[   14.679854] os08a10 8-0036: driver version: 00.01.00
[   14.682775] os08a10 8-0036: supply avdd not found, using dummy regulator
[   14.685727] os08a10 8-0036: supply dovdd not found, using dummy regulator
[   14.688632] os08a10 8-0036: supply dvdd not found, using dummy regulator
[   14.691520] os08a10 8-0036: lane_num(4)  pixel_rate(360000000)
[   14.694370] os08a10 8-0036: could not get default pinstate
[   14.697205] os08a10 8-0036: could not get sleep pinstate
[   14.723445] os08a10 8-0036: Unexpected sensor id(000000), ret(-5)
[   14.726274] os08a10 8-0036: os08a10_probe(1719) Check id  failed,
               check following information:
               Power/PowerDown/Reset/Mclk/I2cBus !!
[   14.736737] Loading compiled-in X.509 certificates
[   14.739655] Key type .fscrypt registered
[   14.742464] Key type fscrypt-provisioning registered
[   14.745839] pstore: Using crash dump compression: deflate
[   14.760196] rga3 fdb60000.rga: Adding to iommu group 2
[   14.763216] rga3 fdb60000.rga: probe successfully, irq = 40, hw_version:3.0.76831
[   14.765827] rga3 fdb70000.rga: Adding to iommu group 3
[   14.768777] rga3 fdb70000.rga: probe successfully, irq = 41, hw_version:3.0.76831
[   14.772325] rga2 fdb80000.rga: probe successfully, irq = 122, hw_version:3.2.63318
[   14.774452] rga: IOMMU binding successfully, default mapping core[0x1]
[   14.776383] rga: Module initialized. v1.3.7
[   14.807949] rockchip-csi2-dphy csi2-dcphy0: csi2 dphy0 probe successfully!
[   14.810139] rockchip-csi2-dphy csi2-dcphy1: csi2 dphy0 probe successfully!
[   14.812248] rockchip-csi2-dphy csi2-dphy0: csi2 dphy0 probe successfully!
[   14.814184] mpp_vdpu1 fdb51000.avsd-plus: Adding to iommu group 1
[   14.816194] mpp_vdpu1 fdb51000.avsd-plus: probe device
[   14.818015] mpp_vdpu1 fdb51000.avsd-plus: reset_group->rw_sem_on=0
[   14.819633] mpp_vdpu1 fdb51000.avsd-plus: reset_group->rw_sem_on=0
[   14.821339] mpp_vdpu1 fdb51000.avsd-plus: probing finish
[   14.824413] mpp_vdpu2 fdb50400.vdpu: Adding to iommu group 1
[   14.827324] mpp_vdpu2 fdb50400.vdpu: probe device
[   14.830330] mpp_vdpu2 fdb50400.vdpu: reset_group->rw_sem_on=0
[   14.833099] mpp_vdpu2 fdb50400.vdpu: reset_group->rw_sem_on=0
[   14.835933] mpp_vdpu2 fdb50400.vdpu: probing finish
[   14.838458] mpp_vepu2 fdb50000.vepu: Adding to iommu group 1
[   14.840452] mpp_vepu2 fdb50000.vepu: probing start
[   14.842540] mpp_vepu2 fdb50000.vepu: reset_group->rw_sem_on=0
[   14.844319] mpp_vepu2 fdb50000.vepu: reset_group->rw_sem_on=0
[   14.845872] mpp_vepu2 fdb50000.vepu: probing finish
[   14.847653] mpp_vepu2 fdba0000.jpege-core: Adding to iommu group 5
[   14.849295] mpp_vepu2 fdba0000.jpege-core: probing start
[   14.851010] mpp_vepu2 fdba0000.jpege-core: attach ccu success
[   14.852549] mpp_vepu2 fdba0000.jpege-core: probing finish
[   14.854257] mpp_vepu2 fdba4000.jpege-core: Adding to iommu group 6
[   14.855835] mpp_vepu2 fdba4000.jpege-core: probing start
[   14.857485] mpp_vepu2 fdba4000.jpege-core: attach ccu success
[   14.858974] mpp_vepu2 fdba4000.jpege-core: probing finish
[   14.860630] mpp_vepu2 fdba8000.jpege-core: Adding to iommu group 7
[   14.862171] mpp_vepu2 fdba8000.jpege-core: probing start
[   14.864084] mpp_vepu2 fdba8000.jpege-core: attach ccu success
[   14.866470] mpp_vepu2 fdba8000.jpege-core: probing finish
[   14.869113] mpp_vepu2 fdbac000.jpege-core: Adding to iommu group 8
[   14.871578] mpp_vepu2 fdbac000.jpege-core: probing start
[   14.874174] mpp_vepu2 fdbac000.jpege-core: attach ccu success
[   14.876477] mpp_vepu2 fdbac000.jpege-core: probing finish
[   14.879074] mpp-iep2 fdbb0000.iep: Adding to iommu group 9
[   14.881493] mpp-iep2 fdbb0000.iep: probe device
[   14.884029] mpp-iep2 fdbb0000.iep: probing finish
[   14.886586] mpp_jpgdec fdb90000.jpegd: Adding to iommu group 4
[   14.887589] mpp_jpgdec fdb90000.jpegd: probe device
[   14.888439] mpp_jpgdec fdb90000.jpegd: probing finish
[   14.889304] mpp_rkvdec2 fdc38100.rkvdec-core: Adding to iommu group 12
[   14.890282] mpp_rkvdec2 fdc38100.rkvdec-core: rkvdec-core, probing start
[   14.891129] mpp_rkvdec2 fdc38100.rkvdec-core: shared_niu_a is not found!
[   14.891817] rkvdec2_init:1198: No niu aclk reset resource define
[   14.892509] mpp_rkvdec2 fdc38100.rkvdec-core: shared_niu_h is not found!
[   14.893203] rkvdec2_init:1201: No niu hclk reset resource define
[   14.893924] mpp_rkvdec2 fdc38100.rkvdec-core: no regulator, devfreq is disabled
[   14.894587] mpp_rkvdec2 fdc38100.rkvdec-core: core_mask=00010001
[   14.895205] mpp_rkvdec2 fdc38100.rkvdec-core: attach ccu as core 0
[   14.895932] mpp_rkvdec2 fdc38100.rkvdec-core: sram_start 0x00000000ff001000
[   14.896546] mpp_rkvdec2 fdc38100.rkvdec-core: rcb_iova 0x00000000fff00000
[   14.897167] mpp_rkvdec2 fdc38100.rkvdec-core: sram_size 491520
[   14.897776] mpp_rkvdec2 fdc38100.rkvdec-core: rcb_size 1048576
[   14.898382] mpp_rkvdec2 fdc38100.rkvdec-core: min_width 512
[   14.898981] mpp_rkvdec2 fdc38100.rkvdec-core: rcb_info_count 20
[   14.899578] mpp_rkvdec2 fdc38100.rkvdec-core: [136, 24576]
[   14.900172] mpp_rkvdec2 fdc38100.rkvdec-core: [137, 49152]
[   14.900758] mpp_rkvdec2 fdc38100.rkvdec-core: [141, 90112]
[   14.901339] mpp_rkvdec2 fdc38100.rkvdec-core: [140, 49152]
[   14.901897] mpp_rkvdec2 fdc38100.rkvdec-core: [139, 180224]
[   14.902438] mpp_rkvdec2 fdc38100.rkvdec-core: [133, 49152]
[   14.902973] mpp_rkvdec2 fdc38100.rkvdec-core: [134, 8192]
[   14.903502] mpp_rkvdec2 fdc38100.rkvdec-core: [135, 4352]
[   14.904022] mpp_rkvdec2 fdc38100.rkvdec-core: [138, 13056]
[   14.904507] mpp_rkvdec2 fdc38100.rkvdec-core: [142, 291584]
[   14.905001] mpp_rkvdec2 fdc38100.rkvdec-core: probing finish
[   14.905576] mpp_rkvdec2 fdc48100.rkvdec-core: Adding to iommu group 13
[   14.906196] mpp_rkvdec2 fdc48100.rkvdec-core: rkvdec-core, probing start
[   14.906759] mpp_rkvdec2 fdc48100.rkvdec-core: shared_niu_a is not found!
[   14.907226] rkvdec2_init:1198: No niu aclk reset resource define
[   14.907689] mpp_rkvdec2 fdc48100.rkvdec-core: shared_niu_h is not found!
[   14.908158] rkvdec2_init:1201: No niu hclk reset resource define
[   14.908646] mpp_rkvdec2 fdc48100.rkvdec-core: no regulator, devfreq is disabled
[   14.909160] mpp_rkvdec2 fdc48100.rkvdec-core: core_mask=00020002
[   14.909658] mpp_rkvdec2 fdc48100.rkvdec-core: attach ccu as core 1
[   14.910273] mpp_rkvdec2 fdc48100.rkvdec-core: sram_start 0x00000000ff079000
[   14.910762] mpp_rkvdec2 fdc48100.rkvdec-core: rcb_iova 0x00000000ffe00000
[   14.911249] mpp_rkvdec2 fdc48100.rkvdec-core: sram_size 487424
[   14.911738] mpp_rkvdec2 fdc48100.rkvdec-core: rcb_size 1048576
[   14.912225] mpp_rkvdec2 fdc48100.rkvdec-core: min_width 512
[   14.912710] mpp_rkvdec2 fdc48100.rkvdec-core: rcb_info_count 20
[   14.913194] mpp_rkvdec2 fdc48100.rkvdec-core: [136, 24576]
[   14.913680] mpp_rkvdec2 fdc48100.rkvdec-core: [137, 49152]
[   14.914163] mpp_rkvdec2 fdc48100.rkvdec-core: [141, 90112]
[   14.914641] mpp_rkvdec2 fdc48100.rkvdec-core: [140, 49152]
[   14.915064] mpp_rkvdec2 fdc48100.rkvdec-core: [139, 180224]
[   14.915484] mpp_rkvdec2 fdc48100.rkvdec-core: [133, 49152]
[   14.915903] mpp_rkvdec2 fdc48100.rkvdec-core: [134, 8192]
[   14.916321] mpp_rkvdec2 fdc48100.rkvdec-core: [135, 4352]
[   14.916738] mpp_rkvdec2 fdc48100.rkvdec-core: [138, 13056]
[   14.917151] mpp_rkvdec2 fdc48100.rkvdec-core: [142, 291584]
[   14.917581] mpp_rkvdec2 fdc48100.rkvdec-core: probing finish
[   14.918091] mpp_rkvenc2 fdbd0000.rkvenc-core: Adding to iommu group 10
[   14.918608] mpp_rkvenc2 fdbd0000.rkvenc-core: probing start
[   14.919394] mpp_rkvenc2 fdbd0000.rkvenc-core: bin=0
[   14.920015] mpp_rkvenc2 fdbd0000.rkvenc-core: leakage=18
[   14.920430] mpp_rkvenc2 fdbd0000.rkvenc-core: leakage-volt-sel=1
[   14.921831] mpp_rkvenc2 fdbd0000.rkvenc-core: avs=0
[   14.922284] mpp_rkvenc2 fdbd0000.rkvenc-core: l=-2147483648 h=2147483647 hyst=0 l_limit=0 h_limit=0 h_table=0
[   14.928440] mpp_rkvenc2 fdbd0000.rkvenc-core: attach ccu as core 0
[   14.929009] mpp_rkvenc2 fdbd0000.rkvenc-core: probing finish
[   14.929663] mpp_rkvenc2 fdbe0000.rkvenc-core: Adding to iommu group 11
[   14.930344] mpp_rkvenc2 fdbe0000.rkvenc-core: probing start
[   14.931273] mpp_rkvenc2 fdbe0000.rkvenc-core: bin=0
[   14.931983] mpp_rkvenc2 fdbe0000.rkvenc-core: leakage=18
[   14.932508] mpp_rkvenc2 fdbe0000.rkvenc-core: leakage-volt-sel=1
[   14.933749] mpp_rkvenc2 fdbe0000.rkvenc-core: avs=0
[   14.934346] mpp_rkvenc2 fdbe0000.rkvenc-core: l=-2147483648 h=2147483647 hyst=0 l_limit=0 h_limit=0 h_table=0
[   14.940725] mpp_rkvenc2 fdbe0000.rkvenc-core: attach ccu as core 1
[   14.941401] mpp_rkvenc2 fdbe0000.rkvenc-core: probing finish
[   14.942158] mpp_av1dec fdc70000.av1d: Adding to iommu group 14
[   14.943005] mpp_av1dec fdc70000.av1d: probing start
[   14.943810] mpp_av1dec fdc70000.av1d: probing finish
[   14.944860] input: adc-keys as /devices/platform/adc-keys/input/input13
[   14.944908] mali fb000000.gpu: Kernel DDK version g25p0-00eac0
[   14.946387] rockchip-dmc dmc: bin=3
[   14.946728] mali fb000000.gpu: GPU metrics tracepoint support enabled
[   14.946838] dwmmc_rockchip fe2c0000.mmc: No normal pinctrl state
[   14.946842] dwmmc_rockchip fe2c0000.mmc: No idle pinctrl state
[   14.946881] dwmmc_rockchip fe2c0000.mmc: IDMAC supports 32-bit address mode.
[   14.946892] dwmmc_rockchip fe2c0000.mmc: Using internal DMA controller.
[   14.946896] dwmmc_rockchip fe2c0000.mmc: Version ID is 270a
[   14.946916] dwmmc_rockchip fe2c0000.mmc: DW MMC controller at irq 139,32 bit host data width,256 deep fifo
[   14.947435] rockchip-dmc dmc: leakage=46
[   14.948935] mali fb000000.gpu: bin=0
[   14.949079] rockchip-dmc dmc: leakage-volt-sel=2
[   14.950447] mali fb000000.gpu: leakage=21
[   14.950917] rockchip-dmc dmc: soc version=3, speed=2
[   14.952139] debugfs: Directory 'fb000000.gpu-mali' with parent 'vdd_gpu_s0' already present!
[   14.954094] rockchip-dmc dmc: avs=0
[   14.959395] rockchip-dmc dmc: current ATF version 0x100
[   14.960255] rockchip-dmc dmc: there is no available frequencies!
[   14.960333] mmc_host mmc1: Bus speed (slot 0) = 400000Hz (slot req 400000Hz, actual 400000HZ div = 0)
[   14.960869] rockchip-dmc dmc: cannot get frequency info
[   14.960872] rockchip-dmc: probe of dmc failed with error -1
[   14.961440] mali fb000000.gpu: pvtm=869
[   14.961536] mali fb000000.gpu: pvtm-volt-sel=3
[   14.961576] debugfs: Directory 'fb000000.gpu-mali' with parent 'vdd_gpu_s0' already present!
[   14.962848] mali fb000000.gpu: avs=0
[   14.970372] mali fb000000.gpu: rockchip_pvtpll_set_volt_sel: error cfg clk_id=5 voltsel (-1)
[   14.971920] W : [File] : drivers/gpu/arm/bifrost/platform/rk/mali_kbase_config_rk.c; [Line] : 144; [Func] : kbase_platform_rk_init(); power-off-delay-ms not available.
[   14.976056] rkcif rkcif-mipi-lvds: clear unready subdev num: 2
[   14.978371] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   14.980230] rkcif-mipi-lvds: Async subdev notifier completed
[   14.982094] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   14.983984] rkcif-mipi-lvds: There is not terminal subdev, not synchronized with ISP
[   14.985892] rkcif rkcif-mipi-lvds1: clear unready subdev num: 2
[   14.988318] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   14.990064] mali fb000000.gpu: Register LUT 000a0800 initialized for GPU arch 0x000a0806
[   14.990338] rkcif-mipi-lvds1: Async subdev notifier completed
[   14.992617] mali fb000000.gpu: r0p0 status 5 not found in HW issues table;
[   14.994920] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   14.997247] mali fb000000.gpu: falling back to closest match: r0p0 status 0
[   14.999632] rkcif-mipi-lvds1: There is not terminal subdev, not synchronized with ISP
[   14.999639] rkcif rkcif-mipi-lvds2: clear unready subdev num: 2
[   15.000214] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   15.002090] mali fb000000.gpu: Execution proceeding normally with fallback match
[   15.004574] rkcif-mipi-lvds2: Async subdev notifier completed
[   15.007067] mali fb000000.gpu: GPU identified as 0x7 arch 10.8.6 r0p0 status 0
[   15.009623] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   15.012433] mali fb000000.gpu: CSF_GPU_RESET_TIMEOUT is capped from 20666ms to 4500ms
[   15.014990] rkcif-mipi-lvds2: There is not terminal subdev, not synchronized with ISP
[   15.015006] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   15.015932] RKNPU fdab0000.npu: Adding to iommu group 0
[   15.016082] RKNPU fdab0000.npu: RKNPU: rknpu iommu is enabled, using iommu mode
[   15.017849] mali fb000000.gpu: KBASE_PRFCNT_ACTIVE_TIMEOUT is capped from 40000ms to 4500ms
[   15.018917] rkcif-mipi-lvds2: There is not terminal subdev, not synchronized with ISP
[   15.018937] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   15.021832] mali fb000000.gpu: KBASE_AS_INACTIVE_TIMEOUT is capped from 40000ms to 4500ms
[   15.024777] rkcif-mipi-lvds: There is not terminal subdev, not synchronized with ISP
[   15.027772] mali fb000000.gpu: CSF_FIRMWARE_STOP_TIMEOUT is capped from 40000ms to 4500ms
[   15.030879] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   15.033943] mali fb000000.gpu: No priority control manager is configured
[   15.036080] rkcif-mipi-lvds1: There is not terminal subdev, not synchronized with ISP
[   15.037267] mali fb000000.gpu: Large page allocation set to false after hardware feature check
[   15.048542] mali fb000000.gpu: No memory group manager is configured
[   15.049827] mali fb000000.gpu: Protected memory allocator not available
[   15.052036] mali fb000000.gpu: EM: OPP:600000 is inefficient
[   15.052042] mali fb000000.gpu: EM: OPP:500000 is inefficient
[   15.052046] mali fb000000.gpu: EM: OPP:400000 is inefficient
[   15.052049] mali fb000000.gpu: EM: OPP:300000 is inefficient
[   15.052146] mali fb000000.gpu: EM: created perf domain
[   15.052210] RKNPU fdab0000.npu: can't request region for resource [mem 0xfdab0000-0xfdabffff]
[   15.053651] mali fb000000.gpu: l=15000 h=85000 hyst=5000 l_limit=0 h_limit=800000000 h_table=0
[   15.057067] RKNPU fdab0000.npu: can't request region for resource [mem 0xfdac0000-0xfdacffff]
[   15.061841] RKNPU fdab0000.npu: can't request region for resource [mem 0xfdad0000-0xfdadffff]
[   15.062908] mali fb000000.gpu: * MALI kbase_mmap_min_addr compiled to CONFIG_DEFAULT_MMAP_MIN_ADDR, no runtime update possible! *
[   15.066135] [drm] Initialized rknpu 0.9.8 20240828 for fdab0000.npu on minor 1
[   15.069440] mali fb000000.gpu: Probed as mali0
[   15.080599] RKNPU fdab0000.npu: RKNPU: bin=0
[   15.085276] RKNPU fdab0000.npu: leakage=11
[   15.089773] debugfs: Directory 'fdab0000.npu-rknpu' with parent 'vdd_npu_s0' already present!
[   15.101925] RKNPU fdab0000.npu: pvtm=885
[   15.111191] RKNPU fdab0000.npu: pvtm-volt-sel=3
[   15.115729] debugfs: Directory 'fdab0000.npu-rknpu' with parent 'vdd_npu_s0' already present!
[   15.123042] RKNPU fdab0000.npu: avs=0
[   15.127590] RKNPU fdab0000.npu: rockchip_pvtpll_set_volt_sel: error cfg clk_id=6 voltsel (-1)
[   15.132325] RKNPU fdab0000.npu: l=15000 h=85000 hyst=5000 l_limit=0 h_limit=800000000 h_table=0
[   15.154262] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[   15.165849] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[   15.170587] cfg80211: Loaded X.509 cert 'wens: 61c038651aabdcf94bd0ac7ff06c7248db18c600'
[   15.177154] clk: Disabling unused clocks
[   15.182539] rockchip-pm rockchip-suspend: not set pwm-regulator-config
[   15.187043] rockchip-suspend not set sleep-mode-config for mem-lite
[   15.190897] rockchip-suspend not set wakeup-config for mem-lite
[   15.194343] rockchip-suspend not set sleep-mode-config for mem-ultra
[   15.197679] rockchip-suspend not set wakeup-config for mem-ultra
[   15.202395] I : [File] : drivers/gpu/arm/mali400/mali/linux/mali_kernel_linux.c; [Line] : 407; [Func] : mali_module_init(); svn_rev_string_from_arm of this mali_ko is '', rk_ko_ver is '5', built at '11:36:55', on 'Apr 23 2025'.
[   15.206303] Mali: 
[   15.206306] Mali device driver loaded
[   15.211872] rkisp rkisp0-vir0: clear unready subdev num: 1
[   15.214868] rkisp0-vir0: Async subdev notifier completed
[   15.216209] rkisp rkisp0-vir1: clear unready subdev num: 1
[   15.217707] rkisp0-vir1: Async subdev notifier completed
[   15.219031] rkisp rkisp1-vir0: clear unready subdev num: 1
[   15.220567] rkisp1-vir0: Async subdev notifier completed
[   15.221881] ALSA device list:
[   15.223163]   #0: rockchip-dp0
[   15.224438]   #1: rockchip-hdmi0
[   15.225686]   #2: rockchip,sound-micarray
[   15.229626] Freeing unused kernel memory: 7168K
[   15.230988] Run /init as init process
[   15.232210]   with arguments:
[   15.232214]     /init
[   15.232217]   with environment:
[   15.232219]     HOME=/
[   15.232222]     TERM=linux
[   15.232224]     storagemedia=emmc
[   15.232227]     khadas_board=Edge2
[   15.232229]     partition_type=generic
[   15.232232]     fan=auto
[   15.232234]     lcd_panel=null
[   15.232237]     hwver=EDGE2.V12
[   15.243339] usb 7-1: new full-speed USB device number 2 using xhci-hcd
[   15.391648] usb 7-1: New USB device found, idVendor=35ca, idProduct=101d, bcdDevice= 2.00
[   15.394135] usb 7-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[   15.396510] usb 7-1: Product: VITURE Pro XR Glasses
[   15.398897] usb 7-1: Manufacturer: VITURE Pro
[   15.401240] usb 7-1: SerialNumber: 205C396D4642
[   15.502799] hid-generic 0003:35CA:101D.0003: hiddev97,hidraw2: USB HID v1.11 Device [VITURE Pro VITURE Pro XR Glasses] on usb-xhci-hcd.8.auto-1/input0
[   15.506765] hid-generic 0003:35CA:101D.0004: hiddev98,hidraw3: USB HID v1.11 Device [VITURE Pro VITURE Pro XR Glasses] on usb-xhci-hcd.8.auto-1/input1
[   15.510084] cdc_acm 7-1:1.2: ttyACM0: USB ACM device
[   15.693295] raid6: neonx8   gen() 11052 MB/s
[   15.749962] raid6: neonx4   gen() 11379 MB/s
[   15.806627] raid6: neonx2   gen()  9533 MB/s
[   15.863296] raid6: neonx1   gen()  7686 MB/s
[   15.919968] raid6: int64x8  gen()  2613 MB/s
[   15.976629] raid6: int64x4  gen()  3457 MB/s
[   16.033298] raid6: int64x2  gen()  4553 MB/s
[   16.089963] raid6: int64x1  gen()  3726 MB/s
[   16.090547] raid6: using algorithm neonx4 gen() 11379 MB/s
[   16.146628] raid6: .... xor() 8811 MB/s, rmw enabled
[   16.147205] raid6: using neon recovery algorithm
[   16.149335] xor: measuring software checksum speed
[   16.157405]    8regs           :  2081 MB/sec
[   16.164252]    32regs          :  2720 MB/sec
[   16.170398]    arm64_neon      :  3329 MB/sec
[   16.173525] xor: using function: arm64_neon (3329 MB/sec)
[   16.202789] Btrfs loaded, crc32c=crc32c-generic, assert=on, ref-verify=on, zoned=no, fsverity=no
[   16.322769] EXT4-fs (mmcblk0p2): mounted filesystem with writeback data mode. Quota mode: none.
[   16.605658] NET: Registered PF_INET6 protocol family
[   16.610485] Segment Routing with IPv6
[   16.614088] In-situ OAM (IOAM) with IPv6
[   16.642483] systemd[1]: systemd 255.4-1ubuntu8.6 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT -GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY +P11KIT +QRENCODE +TPM2 +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -BPF_FRAMEWORK -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
[   16.647210] systemd[1]: Detected architecture arm64.
[   16.664339] systemd[1]: Hostname set to <Khadas>.
[   17.208189] systemd[1]: Queued start job for default target graphical.target.
[   17.245040] systemd[1]: Created slice system-modprobe.slice - Slice /system/modprobe.
[   17.248375] systemd[1]: Created slice system-serial\x2dgetty.slice - Slice /system/serial-getty.
[   17.251466] systemd[1]: Created slice system-systemd\x2dfsck.slice - Slice /system/systemd-fsck.
[   17.254347] systemd[1]: Created slice user.slice - User and Session Slice.
[   17.256941] systemd[1]: Started systemd-ask-password-wall.path - Forward Password Requests to Wall Directory Watch.
[   17.259830] systemd[1]: Set up automount proc-sys-fs-binfmt_misc.automount - Arbitrary Executable File Formats File System Automount Point.
[   17.262527] systemd[1]: Expecting device dev-disk-by\x2duuid-53f48923\x2d625f\x2d41bd\x2da75f\x2d996dc0408a6e.device - /dev/disk/by-uuid/53f48923-625f-41bd-a75f-996dc0408a6e...
[   17.265298] systemd[1]: Expecting device dev-ttyFIQ0.device - /dev/ttyFIQ0...
[   17.268131] systemd[1]: Reached target integritysetup.target - Local Integrity Protected Volumes.
[   17.271050] systemd[1]: Reached target nss-user-lookup.target - User and Group Name Lookups.
[   17.273953] systemd[1]: Reached target remote-fs.target - Remote File Systems.
[   17.276851] systemd[1]: Reached target slices.target - Slice Units.
[   17.279796] systemd[1]: Reached target snapd.mounts-pre.target - Mounting snaps.
[   17.282818] systemd[1]: Reached target snapd.mounts.target - Mounted snaps.
[   17.285814] systemd[1]: Reached target swap.target - Swaps.
[   17.288661] systemd[1]: Reached target time-set.target - System Time Set.
[   17.291499] systemd[1]: Reached target veritysetup.target - Local Verity Protected Volumes.
[   17.294249] systemd[1]: Listening on syslog.socket - Syslog Socket.
[   17.296968] systemd[1]: Listening on systemd-fsckd.socket - fsck to fsckd communication Socket.
[   17.299663] systemd[1]: Listening on systemd-initctl.socket - initctl Compatibility Named Pipe.
[   17.302369] systemd[1]: Listening on systemd-journald-dev-log.socket - Journal Socket (/dev/log).
[   17.305036] systemd[1]: Listening on systemd-journald.socket - Journal Socket.
[   17.307496] systemd[1]: systemd-pcrextend.socket - TPM2 PCR Extension (Varlink) was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
[   17.308863] systemd[1]: Listening on systemd-udevd-control.socket - udev Control Socket.
[   17.311551] systemd[1]: Listening on systemd-udevd-kernel.socket - udev Kernel Socket.
[   17.314277] systemd[1]: dev-hugepages.mount - Huge Pages File System was skipped because of an unmet condition check (ConditionPathExists=/sys/kernel/mm/hugepages).
[   17.333599] systemd[1]: Mounting dev-mqueue.mount - POSIX Message Queue File System...
[   17.337722] systemd[1]: Mounting sys-kernel-debug.mount - Kernel Debug File System...
[   17.341735] systemd[1]: Mounting sys-kernel-tracing.mount - Kernel Trace File System...
[   17.346923] systemd[1]: Starting systemd-journald.service - Journal Service...
[   17.351770] systemd[1]: Starting fake-hwclock-load.service - Restore the current clock...
[   17.356059] systemd[1]: Starting keyboard-setup.service - Set the console keyboard layout...
[   17.360484] systemd[1]: Starting kmod-static-nodes.service - Create List of Static Device Nodes...
[   17.365107] systemd[1]: Starting modprobe@configfs.service - Load Kernel Module configfs...
[   17.365235] (-hwclock)[377]: fake-hwclock-load.service: Referenced but unset environment variable evaluates to an empty string: FORCE
[   17.374250] systemd[1]: Starting modprobe@dm_mod.service - Load Kernel Module dm_mod...
[   17.381312] systemd[1]: Starting modprobe@drm.service - Load Kernel Module drm...
[   17.385573] systemd-journald[375]: Collecting audit messages is disabled.
[   17.392696] systemd[1]: Starting modprobe@efi_pstore.service - Load Kernel Module efi_pstore...
[   17.395672] device-mapper: uevent: version 1.0.3
[   17.395914] device-mapper: ioctl: 4.47.0-ioctl (2022-07-28) initialised: dm-devel@redhat.com
[   17.401514] systemd[1]: Starting modprobe@fuse.service - Load Kernel Module fuse...
[   17.406666] systemd[1]: Starting modprobe@loop.service - Load Kernel Module loop...
[   17.410244] systemd[1]: systemd-fsck-root.service - File System Check on Root Device was skipped because of an unmet condition check (ConditionPathIsReadWrite=!/).
[   17.413933] systemd[1]: Starting systemd-modules-load.service - Load Kernel Modules...
[   17.417340] systemd[1]: systemd-pcrmachine.service - TPM2 PCR Machine ID Measurement was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
[   17.420548] systemd[1]: Starting systemd-remount-fs.service - Remount Root and Kernel File Systems...
[   17.424079] systemd[1]: systemd-tpm2-setup-early.service - TPM2 SRK Setup (Early) was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
[   17.426459] fuse: init (API version 7.37)
[   17.427451] systemd[1]: Starting systemd-udev-trigger.service - Coldplug All udev Devices...
[   17.436140] systemd[1]: Mounted dev-mqueue.mount - POSIX Message Queue File System.
[   17.439505] systemd[1]: Mounted sys-kernel-debug.mount - Kernel Debug File System.
[   17.442335] systemd[1]: Mounted sys-kernel-tracing.mount - Kernel Trace File System.
[   17.445312] systemd[1]: fake-hwclock-load.service: Deactivated successfully.
[   17.446616] systemd[1]: Finished fake-hwclock-load.service - Restore the current clock.
[   17.449453] systemd[1]: Finished kmod-static-nodes.service - Create List of Static Device Nodes.
[   17.449607] EXT4-fs (mmcblk0p2): re-mounted. Quota mode: none.
[   17.454061] systemd[1]: modprobe@configfs.service: Deactivated successfully.
[   17.455364] systemd[1]: Finished modprobe@configfs.service - Load Kernel Module configfs.
[   17.458000] systemd[1]: modprobe@dm_mod.service: Deactivated successfully.
[   17.459194] systemd[1]: Finished modprobe@dm_mod.service - Load Kernel Module dm_mod.
[   17.461699] systemd[1]: modprobe@drm.service: Deactivated successfully.
[   17.462886] systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
[   17.465411] systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
[   17.466566] systemd[1]: Finished modprobe@efi_pstore.service - Load Kernel Module efi_pstore.
[   17.469452] systemd[1]: Finished keyboard-setup.service - Set the console keyboard layout.
[   17.471751] systemd[1]: modprobe@fuse.service: Deactivated successfully.
[   17.472618] [dhd] _dhd_module_init: in Dongle Host Driver, version 101.10.591.52.27 (20240409-1)(20240411-2)(d83d8d7)
               drivers/net/wireless/rockchip_wlan/rkwifi/bcmdhd compiled on Apr 23 2025 at 11:37:00

[   17.472796] systemd[1]: Finished modprobe@fuse.service - Load Kernel Module fuse.
[   17.475245] [dhd] STATIC-MSG) dhd_static_buf_init : 101.10.361.36 (wlan=r892223-20231107-1)
[   17.477164] [dhd] STATIC-MSG) dhd_init_wlan_mem : prealloc ok for index 0: 2371584(2316K)
[   17.477168] [WLAN_RFKILL]: rockchip_wifi_get_oob_irq: Enter
[   17.477207] [dhd] dhd_wlan_init_gpio: WL_HOST_WAKE=-1, oob_irq=141, oob_irq_flags=0x4
[   17.477210] [dhd] dhd_wlan_init_gpio: WL_REG_ON=-1
[   17.477211] [dhd] dhd_wifi_platform_load: Enter
[   17.477213] [dhd] wifi_platform_bus_enumerate device present 1
[   17.477214] [dhd] ======== Card detection to detect PCIE card! ========
[   17.477368] [dhd] dhdpcie_pci_probe : no mutex held
[   17.477371] [dhd] dhdpcie_pci_probe : set mutex lock
[   17.477372] [dhd] PCI_PROBE:  bus 0x41, slot 0x0,vendor 0x14E4, device 0x449D(good PCI location)
[   17.477375] [dhd] dhdpcie_init: found adapter info 'DHD generic adapter'
[   17.477377] [dhd] STATIC-MSG) dhd_wlan_mem_prealloc : section 3, size 139264
[   17.477385] [dhd] succeed to alloc static buf
[   17.477387] [dhd] STATIC-MSG) dhd_wlan_mem_prealloc : section 4, size 0
[   17.477423] pcieh 0004:41:00.0: enabling device (0000 -> 0002)
[   17.477755] [dhd] Disable CTO
[   17.478507] [dhd] DHD: dongle ram size is set to 1310720(orig 1310720) at 0x170000
[   17.492188] [dhd] dhdpcie_bar1_window_switch_enab: bar1_switch_enab=0 ramstart=0x170000 ramend=0x2affff bar1_size=0x0
[   17.492217] [dhd] STATIC-MSG) dhd_wlan_mem_prealloc : section 7, size 43840
[   17.493912] [dhd] dhd_conf_set_chiprev : devid=0x449d, chip=0xaae8, chiprev=2, svid=0x14e4, ssid=0xaae8
[   17.494312] systemd[1]: modprobe@loop.service: Deactivated successfully.
[   17.494944] [dhd] dhd_check_htput_chip: htput_support:1
[   17.495697] systemd[1]: Finished modprobe@loop.service - Load Kernel Module loop.
[   17.496342] [dhd] STATIC-MSG) dhd_wlan_mem_prealloc : section 0, size 5152
[   17.499361] systemd[1]: Finished systemd-modules-load.service - Load Kernel Modules.
[   17.501610] systemd[1]: Finished systemd-remount-fs.service - Remount Root and Kernel File Systems.
[   17.503060] [dhd] dhd_ioctl_entry_local invalid parameter net 0000000000000000 dev_priv 00000000ce6360b6
[   17.503064] [dhd] CFG80211-ERROR) wl_is_fils_supported : FILS NOT supported, err -22
[   17.503193] [dhd] STATIC-MSG) dhd_wlan_mem_prealloc : section 5, size 65536
[   17.504760] [dhd] CFG80211-ERROR) wl_is_fils_supported : FILS NOT supported, err -19
[   17.506504] [dhd] STATIC-MSG) dhd_wlan_mem_prealloc : section 19, size 65688
[   17.507360] [dhd] dhd_attach(): thread:dhd_watchdog_thread:197 started
[   17.508119] [dhd] dhd_deferred_work_init: work queue initialized
[   17.508859] [dhd] dhd_tcpack_suppress_set: TCP ACK Suppress mode 0 -> mode 3
[   17.509597] [dhd] dhd_tcpack_suppress_set: TCPACK_INFO_MAXNUM=40, TCPDATA_INFO_MAXNUM=40
[   17.510353] [dhd] dhd_cpumasks_init CPU masks primary(big)=0xf0 secondary(little)=0xe
[   17.511111] [dhd] dhd_cpu_startup_callback(): LB data is not initialized yet.
[   17.513834] [dhd] dhd_cpu_startup_callback(): LB data is not initialized yet.
[   17.516449] [dhd] dhd_cpu_startup_callback(): LB data is not initialized yet.
[   17.519020] [dhd] dhd_cpu_startup_callback(): LB data is not initialized yet.
[   17.521531] [dhd] dhd_cpu_startup_callback(): LB data is not initialized yet.
[   17.522345] [dhd] dhd_cpu_startup_callback(): LB data is not initialized yet.
[   17.523115] [dhd] dhd_cpu_startup_callback(): LB data is not initialized yet.
[   17.523869] [dhd] dhd_cpu_startup_callback(): LB data is not initialized yet.
[   17.524658] [dhd] dhdpcie_bus_attach: making DHD_BUS_DOWN
[   17.525464] [dhd] dhdpcie_init: rc_dev from dev->bus->self (1d87:3588) is 00000000b5ddc01d
[   17.525565] [dhd] dhdpcie_init: rc_ep_aspm_cap: 1 rc_ep_l1ss_cap: 1
[   17.528606] [dhd] dhdpcie_request_irq: INTx enabled, irq=84
[   17.529407] [dhd] dhdpcie_bar1_window_switch_enab: bar1_switch_enab=0 ramstart=0x170000 ramend=0x2affff bar1_size=0x400000
[   17.530203] [dhd] dhd_bus_download_firmware: firmware path=/lib/firmware/brcm/fw_bcmdhd.bin, nvram path=/lib/firmware/brcm/nvram.txt
[   17.531006] [dhd] dhd_conf_set_path_params : Final fw_path=/lib/firmware/brcm/fw_bcm43752a2_pcie_ag.bin
[   17.531796] [dhd] dhd_conf_set_path_params : Final nv_path=/lib/firmware/brcm/nvram_ap6275p.txt
[   17.532577] [dhd] dhd_conf_set_path_params : Final clm_path=/lib/firmware/brcm/clm_bcm43752a2_pcie_ag.blob
[   17.533362] [dhd] dhd_conf_set_path_params : Final conf_path=/lib/firmware/brcm/config_bcm43752a2_pcie_ag.txt
[   17.535611] [dhd] dhd_os_open_image1: /lib/firmware/brcm/config_bcm43752a2_pcie_ag.txt (30 bytes) open success
[   17.536743] [dhd] dhd_conf_read_others : wl_preinit = pm2_sleep_ret=2000
[   17.537532] [dhd] d2h_intr_method -> PCIE_INTX(0); d2h_intr_control -> D2H_INTMASK(0)
[   17.538404] [dhd] dhdpcie_download_code_file: dhd_tcm_test_enable 0, dhd_tcm_test_status 0
[   17.539173] [dhd] dhdpcie_download_code_file: download firmware /lib/firmware/brcm/fw_bcm43752a2_pcie_ag.bin
[   17.539958] [dhd] dhd_os_open_image1: /lib/firmware/brcm/fw_bcm43752a2_pcie_ag.bin (942297 bytes) open success
[   17.541109] [dhd] dhd_os_open_image1: /lib/firmware/brcm/fw_bcm43752a2_pcie_ag.bin (942297 bytes) open success
[   17.541872] [dhd] dhdpcie_download_code_file Using SINGLE image (size 942297)
[   17.543788] systemd[1]: Mounting sys-fs-fuse-connections.mount - FUSE Control File System...
[   17.546586] systemd[1]: Mounting sys-kernel-config.mount - Kernel Configuration File System...
[   17.550164] systemd[1]: systemd-hwdb-update.service - Rebuild Hardware Database was skipped because of an unmet condition check (ConditionNeedsUpdate=/etc).
[   17.552392] systemd[1]: Starting systemd-pstore.service - Platform Persistent Storage Archival...
[   17.555662] systemd[1]: Starting systemd-random-seed.service - Load/Save OS Random Seed...
[   17.557853] systemd[1]: systemd-repart.service - Repartition Root Disk was skipped because no trigger condition checks were met.
[   17.560043] systemd[1]: Starting systemd-sysctl.service - Apply Kernel Variables...
[   17.563304] systemd[1]: Starting systemd-tmpfiles-setup-dev-early.service - Create Static Device Nodes in /dev gracefully...
[   17.565560] systemd[1]: systemd-tpm2-setup.service - TPM2 SRK Setup was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
[   17.567416] systemd[1]: Mounted sys-fs-fuse-connections.mount - FUSE Control File System.
[   17.569577] systemd[1]: Mounted sys-kernel-config.mount - Kernel Configuration File System.
[   17.593309] systemd[1]: Finished systemd-pstore.service - Platform Persistent Storage Archival.
[   17.596036] systemd[1]: Finished systemd-random-seed.service - Load/Save OS Random Seed.
[   17.600238] systemd[1]: Finished systemd-tmpfiles-setup-dev-early.service - Create Static Device Nodes in /dev gracefully.
[   17.602124] systemd[1]: systemd-sysusers.service - Create System Users was skipped because no trigger condition checks were met.
[   17.603987] systemd[1]: Starting systemd-tmpfiles-setup-dev.service - Create Static Device Nodes in /dev...
[   17.606465] systemd[1]: Finished systemd-sysctl.service - Apply Kernel Variables.
[   17.636953] systemd[1]: Finished systemd-tmpfiles-setup-dev.service - Create Static Device Nodes in /dev.
[   17.638292] systemd[1]: Reached target local-fs-pre.target - Preparation for Local File Systems.
[   17.638871] [dhd] dhd_os_open_image1: /lib/firmware/brcm/nvram_ap6275p.txt (7335 bytes) open success
[   17.639243] [dhd] dhdpcie_download_nvram: dhd_get_download_buffer len 7335
[   17.639246] [dhd] # AP6275P_NVRAM_V1.1_20200702 
[   17.639278] [dhd] dhdpcie_download_nvram: process_nvram_vars len 5860
[   17.640774] systemd[1]: Mounting tmp.mount - /tmp...
[   17.643890] systemd[1]: Starting systemd-udevd.service - Rule-based Manager for Device Events and Files...
[   17.651025] systemd[1]: Mounted tmp.mount - /tmp.
[   17.656997] [dhd] dhdpcie_bus_write_vars: Download, Upload and compare of NVRAM succeeded.
[   17.657001] [dhd] dhdpcie_bus_write_vars: New varsize is 5864, length token(nvram_csm)=0xfa4505ba
[   17.657415] [dhd] Download and compare of TLV 0xfeedc0de succeeded (size 128, addr 2ae88c).
[   17.657526] [dhd] dhdpcie_bus_download_state: Took ARM out of Reset
[   17.657545] [dhd] dhd_bus_aer_config: Configure AER registers for EP
[   17.657583] [dhd] dhd_bus_aer_config: Configure AER registers for RC
[   17.699444] systemd[1]: Finished systemd-udev-trigger.service - Coldplug All udev Devices.
[   17.702474] systemd[1]: Starting ifupdown-pre.service - Helper to synchronize boot up for ifupdown...
[   17.719940] systemd[1]: Finished ifupdown-pre.service - Helper to synchronize boot up for ifupdown.
[   17.741255] systemd[1]: Started systemd-udevd.service - Rule-based Manager for Device Events and Files.
[   17.745069] systemd[1]: plymouth-start.service - Show Plymouth Boot Screen was skipped because of an unmet condition check (ConditionKernelCommandLine=splash).
[   17.745334] systemd[1]: Started systemd-ask-password-console.path - Dispatch Password Requests to Console Directory Watch.
[   17.749020] [dhd] dhdpcie_readshared: addr=0x20c8f4 nvram_csm=0xfa4505ba
[   17.749027] [dhd] ### Total time ARM OOR to Readshared pass took 91556 usec ###
[   17.749030] [dhd] dhdpcie_readshared: PCIe shared addr (0x0020c8f4) read took 90000 usec before dongle is ready
[   17.749132] systemd[1]: systemd-ask-password-plymouth.path - Forward Password Requests to Plymouth Directory Watch was skipped because of an unmet condition check (ConditionPathExists=/run/plymouth/pid).
[   17.749196] systemd[1]: Reached target cryptsetup.target - Local Encrypted Volumes.
[   17.749294] [dhd] FW supports DAR ? N
[   17.749321] [dhd] dhdpcie_readshared: max H2D queues 64
[   17.749323] [dhd] FW supports debug buf dest ? N 
[   17.749325] [dhd] FW supports MD ring ? N
[   17.749349] [dhd] dhd_bus_init: Enabling bus->intr_enabled
[   17.749352] [dhd] dhdpcie_oob_intr_register OOB irq=141 flags=0x4
[   17.749387] [dhd] dhdpcie_oob_intr_register: enable_irq_wake
[   17.749408] [dhd] STATIC-MSG) dhd_wlan_mem_prealloc : section 9, size 32896
[   17.749416] [dhd] dhd_prot_init:4146: h2d_max_txpost = 512
[   17.749418] [dhd] dhd_prot_init:4152: h2d_htput_max_txpost = 2048
[   17.749536] [dhd] dhd_prot_init: max_rxbufpost:511 rx_buf_burst:64 rx_bufpost_threshold:64
[   17.749539] [dhd] ENABLING DW:0
[   17.749541] [dhd] IDMA not enabled in FW !!
[   17.749542] [dhd] IFRM not enabled in FW !!
[   17.749543] [dhd] DAR not enabled in FW !!
[   17.749544] [dhd] Enable hostcap: EXTD TXS in txcpl
[   17.749585] [dhd] dhd_prot_d2h_sync_init(): D2H sync mechanism is XORCSUM 
[   17.749597] [dhd] dhd_bus_hostready : Read PCICMD Reg: 0x00100006
[   17.749613] [dhd] dhd_bus_hostready: Ring Hostready:1
[   17.749615] [dhd] Attach flowrings pool for 64 rings
[   17.749892] [dhd] trying to send create d2h info ring: id 70
[   17.749894] [dhd] dhd_send_d2h_ringcreate ringid: 3 idx: 70 max_h2d: 67
[   17.749897] [dhd] trying to send create h2d info ring id 69
[   17.750838] [dhd] dhd_prot_process_d2h_ring_create_complete ring create Response status = 0 ring 3, id 0xfffc
[   17.750946] [dhd] info buffer post after ring create
[   17.752847] [dhd] wlc_ver_major 12, wlc_ver_minor 1
[   17.756404] [dhd] dhd_sync_with_dongle: GET_REVINFO device 0x449d, vendor 0x14e4, chipnum 0xaae8
[   17.758537] [dhd] dhd_sync_with_dongle: RxBuf Post : 2048
[   17.758546] [dhd] dhd_sync_with_dongle: RxBuf Post Alloc : 2048
[   17.762326] [dhd] dhd_preinit_ioctls: preinit_status IOVAR not supported, use legacy preinit
[   17.762332] [dhd] dhd_tcpack_suppress_set 378: already set to 3
[   17.765311] [dhd] dhd_legacy_preinit_ioctls: hostwake_oob enabled
[   17.766722] [dhd] dhd_legacy_preinit_ioctls: use firmware generated mac_address 70:f7:54:b8:cc:cd
[   17.766762] [dhd] dhd_os_open_image1: /lib/firmware/brcm/clm_bcm43752a2_pcie_ag.blob (29225 bytes) open success
[   17.768158] [dhd] dhd_check_current_clm_data: ----- This FW is not included CLM data -----
[   17.768925] systemd[1]: Found device dev-ttyFIQ0.device - /dev/ttyFIQ0.
[   17.806669] [dhd] dhd_apply_default_clm: CLM download succeeded 
[   17.808873] [dhd] dhd_check_current_clm_data: ----- This FW is included CLM data -----
[   17.815332] [dhd] Firmware up: op_mode=0x0005, MAC=70:f7:54:b8:cc:cd
[   17.825213] systemd[1]: Found device dev-disk-by\x2duuid-53f48923\x2d625f\x2d41bd\x2da75f\x2d996dc0408a6e.device - /dev/disk/by-uuid/53f48923-625f-41bd-a75f-996dc0408a6e.
[   17.837128] [dhd] dhd_legacy_preinit_ioctls: event_log_max_sets: 26 ret: 0
[   17.851111] [dhd] arp_enable:1 arp_ol:0
[   17.853558] systemd[1]: Starting systemd-fsck@dev-disk-by\x2duuid-53f48923\x2d625f\x2d41bd\x2da75f\x2d996dc0408a6e.service - File System Check on /dev/disk/by-uuid/53f48923-625f-41bd-a75f-996dc0408a6e...
[   17.862531] systemd[1]: Created slice system-systemd\x2dbacklight.slice - Slice /system/systemd-backlight.
[   17.865838] systemd[1]: Starting systemd-backlight@backlight:backlight-mipi0.service - Load/Save Screen Backlight Brightness of backlight:backlight-mipi0...
[   17.872319] [dhd]   Driver: 101.10.591.52.27 (20240409-1)(20240411-2)
               [dhd]   Firmware: wl0: Dec  6 2023 16:58:26 version 18.35.387.23.215 (g7861e478) FWID 01-efcb6b79
               [dhd]   CLM: 9.9.8_SS (2021-05-10 15:05:58) 
[   17.877524] [dhd] dhd_legacy_preinit_ioctls: Monitor mode is enabled in FW cap
[   17.881328] systemd[1]: Started systemd-fsckd.service - File System Check Daemon to report status.
[   17.898804] systemd[1]: Finished systemd-backlight@backlight:backlight-mipi0.service - Load/Save Screen Backlight Brightness of backlight:backlight-mipi0.
[   17.917806] systemd[1]: dev-hugepages.mount - Huge Pages File System was skipped because of an unmet condition check (ConditionPathExists=/sys/kernel/mm/hugepages).
[   17.918916] systemd[1]: Starting fake-hwclock-load.service - Restore the current clock...
[   17.921413] systemd[1]: Starting modprobe@dm_mod.service - Load Kernel Module dm_mod...
[   17.923694] systemd[1]: Starting modprobe@loop.service - Load Kernel Module loop...
[   17.924891] systemd[1]: plymouth-start.service - Show Plymouth Boot Screen was skipped because of an unmet condition check (ConditionKernelCommandLine=splash).
[   17.924933] systemd[1]: systemd-ask-password-plymouth.path - Forward Password Requests to Plymouth Directory Watch was skipped because of an unmet condition check (ConditionPathExists=/run/plymouth/pid).
[   17.925009] systemd[1]: systemd-fsck-root.service - File System Check on Root Device was skipped because of an unmet condition check (ConditionPathIsReadWrite=!/).
[   17.925100] systemd[1]: systemd-hwdb-update.service - Rebuild Hardware Database was skipped because of an unmet condition check (ConditionNeedsUpdate=/etc).
[   17.925131] systemd[1]: systemd-pcrmachine.service - TPM2 PCR Machine ID Measurement was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
[   17.925193] systemd[1]: systemd-sysusers.service - Create System Users was skipped because no trigger condition checks were met.
[   17.925221] systemd[1]: systemd-tpm2-setup-early.service - TPM2 SRK Setup (Early) was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
[   17.925235] systemd[1]: systemd-tpm2-setup.service - TPM2 SRK Setup was skipped because of an unmet condition check (ConditionSecurity=measured-uki).
[   17.925724] systemd[1]: Finished systemd-fsck@dev-disk-by\x2duuid-53f48923\x2d625f\x2d41bd\x2da75f\x2d996dc0408a6e.service - File System Check on /dev/disk/by-uuid/53f48923-625f-41bd-a75f-996dc0408a6e.
[   17.929626] systemd[1]: Mounting boot.mount - /boot...
[   17.930318] [dhd] dhd_legacy_preinit_ioctls: d3_hostwake_delay IOVAR not present, proceed
[   17.931124] systemd[1]: modprobe@loop.service: Deactivated successfully.
[   17.931320] systemd[1]: Finished modprobe@loop.service - Load Kernel Module loop.
[   17.936568] systemd[1]: modprobe@dm_mod.service: Deactivated successfully.
[   17.936931] systemd[1]: Finished modprobe@dm_mod.service - Load Kernel Module dm_mod.
[   17.938539] systemd[1]: systemd-repart.service - Repartition Root Disk was skipped because no trigger condition checks were met.
[   17.938976] (-hwclock)[513]: fake-hwclock-load.service: Referenced but unset environment variable evaluates to an empty string: FORCE
[   17.942277] EXT4-fs (mmcblk0p1): mounted filesystem with ordered data mode. Quota mode: none.
[   17.944888] systemd[1]: Mounted boot.mount - /boot.
[   17.946392] systemd[1]: Reached target local-fs.target - Local File Systems.
[   17.949062] systemd[1]: Listening on systemd-sysext.socket - System Extension Image Management (Varlink).
[   17.950338] systemd[1]: apparmor.service - Load AppArmor profiles was skipped because of an unmet condition check (ConditionSecurity=apparmor).
[   17.952512] systemd[1]: Starting console-setup.service - Set console font and keymap...
[   17.953188] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.953192] stream_cif_mipi_id0: update sensor info failed -19
[   17.955150] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.955154] stream_cif_mipi_id2: update sensor info failed -19
[   17.957251] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   17.959165] stream_cif_mipi_id3: update sensor info failed -19
[   17.959814] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   17.960695] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.961077] rkcif_scale_ch3: update sensor info failed -19
[   17.961362] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.961365] rkcif_scale_ch2: update sensor info failed -19
[   17.961520] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.961525] rkcif_scale_ch1: update sensor info failed -19
[   17.961619] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   17.961622] rkcif_scale_ch3: update sensor info failed -19
[   17.961678] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   17.961684] stream_cif_mipi_id3: update sensor info failed -19
[   17.961954] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.961957] rkcif_scale_ch2: update sensor info failed -19
[   17.961998] stream_cif_mipi_id0: update sensor info failed -19
[   17.962056] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.962058] rkcif_tools_id1: update sensor info failed -19
[   17.962264] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.962267] stream_cif_mipi_id1: update sensor info failed -19
[   17.962865] [dhd] dhd_update_interface_flow_info: ifindex:0 previous role:0 new role:0
[   17.962878] [dhd] dhd_rx_frame: net device is NOT registered. drop event packet
[   17.963071] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.963385] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.963388] stream_cif_mipi_id0: update sensor info failed -19
[   17.964419] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.964749] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.964755] stream_cif_mipi_id2: update sensor info failed -19
[   17.966228] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.966235] rkcif_scale_ch0: update sensor info failed -19
[   17.966274] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.966277] rkcif_tools_id2: update sensor info failed -19
[   17.967271] stream_cif_mipi_id1: update sensor info failed -19
[   17.968186] rkcif_scale_ch0: update sensor info failed -19
[   17.968468] [dhd] dhd_conf_set_country : set country CN, revision 0
[   17.969316] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.969320] rkcif_scale_ch1: update sensor info failed -19
[   17.970416] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.970419] stream_cif_mipi_id1: update sensor info failed -19
[   17.970878] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   17.970882] rkcif_scale_ch3: update sensor info failed -19
[   17.971042] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.971046] rkcif_tools_id2: update sensor info failed -19
[   17.971380] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.971383] rkcif_tools_id1: update sensor info failed -19
[   17.971621] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.971624] rkcif_scale_ch1: update sensor info failed -19
[   17.972581] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.972780] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.972783] rkcif_scale_ch0: update sensor info failed -19
[   17.973827] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.973830] rkcif_tools_id0: update sensor info failed -19
[   17.975088] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   17.976055] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.976058] rkcif_tools_id2: update sensor info failed -19
[   17.978439] stream_cif_mipi_id2: update sensor info failed -19
[   17.979002] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.980707] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   17.980710] rkcif_tools_id0: update sensor info failed -19
[   17.982108] rkcif_tools_id1: update sensor info failed -19
[   17.985161] rkcif_tools_id0: update sensor info failed -19
[   17.985447] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   17.985454] stream_cif_mipi_id3: update sensor info failed -19
[   17.985523] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   17.985525] rkcif_scale_ch2: update sensor info failed -19
[   18.006264] [dhd] dhd_conf_set_country : Country code: CN (CN/0)
[   18.146986] [dhd] Dongle Host Driver, version 101.10.591.52.27 (20240409-1)(20240411-2)(d83d8d7)
               drivers/net/wireless/rockchip_wlan/rkwifi/bcmdhd compiled on Apr 23 2025 at 11:37:00

[   18.151138] [dhd] Register interface [wlan0]  MAC: 70:f7:54:b8:cc:cd

[   18.151218] [dhd] dhd_tcpack_suppress_set: TCP ACK Suppress mode 3 -> mode 0
[   18.151225] [dhd] dhd_tcpack_suppress_set: TCPACK_INFO_MAXNUM=40, TCPDATA_INFO_MAXNUM=40
[   18.151233] [dhd] [wlan0] wl_android_wifi_off :  g_wifi_on=1 force_off=1
[   18.151236] [dhd] dhd_bus_devreset: == Power OFF ==
[   18.151238] [dhd] dhdpcie_advertise_bus_cleanup: DB7 Not sent!!!
[   18.151252] [dhd] dhd_bus_stop: making DHD_BUS_DOWN
[   18.151383] [dhd] dhd_dpc_kill: tasklet disabled
[   18.152504] [dhd] dhd_bus_devreset: making DHD_BUS_DOWN
[   18.152506] [dhd] dhd_bus_devreset:  WLAN OFF Done
[   18.152508] [dhd] wifi_platform_set_power = 0, delay: 10 msec
[   18.152511] [dhd] ======== PULL WL_REG_ON(-1) LOW! ========
[   18.152512] [WLAN_RFKILL]: rockchip_wifi_power: 0
[   18.152515] [WLAN_RFKILL]: rockchip_wifi_power: toggle = false
[   18.152517] [WLAN_RFKILL]: rockchip_wifi_power: toggle = false
[   18.152518] [WLAN_RFKILL]: wifi shut off power [GPIO-1-1]
[   18.156437] systemd[1]: Started edge2-station.service - station control.
[   18.163410] [dhd] wifi_platform_set_power = 0, sleep done: 10 msec
[   18.163415] [dhd] [wlan0] wl_android_wifi_off : out
[   18.163662] [dhd] Register interface [wlan1]  MAC: 72:f7:54:b8:cc:cd

[   18.163667] [dhd] wl_android_post_init: 0
[   18.163669] [dhd] dhdpcie_pci_probe : mutex is released.
[   18.163728] [dhd] _dhd_module_init: Exit err=0
[   18.220521] systemd[1]: Started fan.service - FAN control.
[   18.227624] systemd[1]: Starting fenix-zram-config.service - Fenix ZRAM config...
[   18.231211] systemd[1]: ldconfig.service - Rebuild Dynamic Linker Cache was skipped because no trigger condition checks were met.
[   18.234294] systemd[1]: Starting plymouth-read-write.service - Tell Plymouth To Write Out Runtime Data...
[   18.237686] systemd[1]: snapd.apparmor.service - Load AppArmor profiles managed internally by snapd was skipped because of an unmet condition check (ConditionSecurity=apparmor).
[   18.240591] systemd[1]: Started system-check.service - System check.
[   18.248191] systemd[1]: Starting systemd-binfmt.service - Set Up Additional Binary Formats...
[   18.256807] systemd[1]: Starting ufw.service - Uncomplicated firewall...
[   18.264857] systemd[1]: Started systemd-journald.service - Journal Service.
[   18.350055] zram: Added device: zram0
[   18.350605] zram: Added device: zram1
[   18.351787] zram: Added device: zram2
[   18.352276] zram: Added device: zram3
[   18.352688] zram: Added device: zram4
[   18.354036] zram: Added device: zram5
[   18.370764] zram1: detected capacity change from 0 to 4018608
[   18.384858] Adding 2009300k swap on /dev/zram1.  Priority:5 extents:1 across:2009300k SS
[   18.388027] zram2: detected capacity change from 0 to 4018608
[   18.395072] Adding 2009300k swap on /dev/zram2.  Priority:5 extents:1 across:2009300k SS
[   18.397522] zram3: detected capacity change from 0 to 4018608
[   18.402404] systemd-journald[375]: Received client request to flush runtime journal.
[   18.409505] Adding 2009300k swap on /dev/zram3.  Priority:5 extents:1 across:2009300k SS
[   18.411725] zram4: detected capacity change from 0 to 4018608
[   18.419255] Adding 2009300k swap on /dev/zram4.  Priority:5 extents:1 across:2009300k SS
[   18.503329] [BT_RFKILL]: ENABLE UART_RTS
[   18.609982] [BT_RFKILL]: DISABLE UART_RTS
[   18.610014] [BT_RFKILL]: bt turn on power
[   18.823314] [BT_RFKILL]: bt shut off power
[   18.848682] rockchip-vop2 fdd90000.vop: [drm] vop disable intf:200
[   18.849773] rockchip-vop2 fdd90000.vop: [drm:vop2_crtc_atomic_disable] Crtc atomic disable vp2
[   19.033708] rd 0-7: Disabling EAS, schedutil is mandatory
[   19.261026] [dhd] CFG80211-ERROR) wl_cfg80211_dump_station : WLC_GET_ASSOCLIST error -19
[   19.261554] [dhd] dhd_ioctl_entry_local bad ifidx
[   19.261565] [dhd] CFG80211-ERROR) wl_cfg80211_dump_station : WLC_GET_ASSOCLIST error -19
[   19.288950] loop0: detected capacity change from 0 to 8
[   19.876460] [dhd] dhd_pri_open : no mutex held
[   19.876474] [dhd] dhd_pri_open : set mutex lock
[   19.876479] [dhd] [wlan0] dhd_open : Enter
[   19.876483] [dhd] Dongle Host Driver, version 101.10.591.52.27 (20240409-1)(20240411-2)(d83d8d7)
               drivers/net/wireless/rockchip_wlan/rkwifi/bcmdhd compiled on Apr 23 2025 at 11:37:00

[   19.876492] [dhd] dhd_open: ######### called for ifidx=0 #########
[   19.876502] [dhd] [wlan0] wl_android_wifi_on : in g_wifi_on=0
[   19.876508] [dhd] wifi_platform_set_power = 1, delay: 200 msec
[   19.876514] [dhd] ======== PULL WL_REG_ON(-1) HIGH! ========
[   19.876518] [WLAN_RFKILL]: rockchip_wifi_power: 1
[   19.876523] [WLAN_RFKILL]: rockchip_wifi_power: toggle = false
[   19.876528] [WLAN_RFKILL]: wifi turn on power [GPIO-1-0]
[   19.879997] [BT_RFKILL]: ENABLE UART_RTS
[   19.986702] [BT_RFKILL]: DISABLE UART_RTS
[   19.986750] [BT_RFKILL]: bt turn on power
[   20.080029] [dhd] wifi_platform_set_power = 1, sleep done: 200 msec
[   20.080042] [dhd] dhd_bus_devreset: == Power ON ==
[   20.085745] rk-pcie fe190000.pcie: can't get current limit.
[   20.288008] rk-pcie fe190000.pcie: PCIe Linking... LTSSM is 0x2
[   20.363361] rk-pcie fe190000.pcie: PCIe Link up, LTSSM is 0x30011
[   20.363371] rk-pcie fe190000.pcie: rockchip_dw_pcie_pm_ctrl_for_user ltssm=30011
[   20.363378] [dhd] dhd_bus_devreset: dhdpcie_bus_start_host_dev OK
[   20.363813] [dhd] ******** Perform FLR ********
[   20.363828] [dhd] config space 0x88 is 0x8080
[   20.363832] [dhd] ******** device not in FLR ********
[   20.364128] [dhd] ******** device force FLR only not set ********
[   20.364132] [dhd] Delay of 70 msec
[   20.440041] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440095] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440144] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440193] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440242] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440291] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440341] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440390] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440439] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440488] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440537] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440586] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440635] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440684] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440733] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440782] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440831] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440881] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440930] [dhd] read_config: reg=0x88 read val=0xb080
[   20.440979] [dhd] read_config: reg=0x88 read val=0xb080
[   20.441028] [dhd] read_config: reg=0x88 read val=0xb080
[   20.441077] [dhd] read_config: reg=0x88 read val=0xb080
[   20.441126] [dhd] read_config: reg=0x88 read val=0xb080
[   20.441176] [dhd] read_config: reg=0x88 read val=0x8080
[   20.441566] [dhd] ******** FLR Succedeed ********
[   20.441675] [dhd] Disable CTO
[   20.442636] [dhd] dhd_dump_pcie_slave_wrapper_regs pcie slave wrapper base not populated
[   20.442874] [dhd] DHD: dongle ram size is set to 1310720(orig 1310720) at 0x170000
[   20.442880] [dhd] dhdpcie_bar1_window_switch_enab: bar1_switch_enab=0 ramstart=0x170000 ramend=0x2affff bar1_size=0x400000
[   20.442961] [dhd] dhdpcie_request_irq: INTx enabled, irq=84
[   20.442986] [dhd] dhd_bus_download_firmware: firmware path=/lib/firmware/brcm/fw_bcmdhd.bin, nvram path=/lib/firmware/brcm/nvram.txt
[   20.443005] [dhd] dhd_conf_set_path_params : Final fw_path=/lib/firmware/brcm/fw_bcm43752a2_pcie_ag.bin
[   20.443010] [dhd] dhd_conf_set_path_params : Final nv_path=/lib/firmware/brcm/nvram_ap6275p.txt
[   20.443013] [dhd] dhd_conf_set_path_params : Final clm_path=/lib/firmware/brcm/clm_bcm43752a2_pcie_ag.blob
[   20.443017] [dhd] dhd_conf_set_path_params : Final conf_path=/lib/firmware/brcm/config_bcm43752a2_pcie_ag.txt
[   20.443042] [dhd] dhd_os_open_image1: /lib/firmware/brcm/config_bcm43752a2_pcie_ag.txt (30 bytes) open success
[   20.443066] [dhd] dhd_conf_read_others : wl_preinit = pm2_sleep_ret=2000
[   20.443072] [dhd] d2h_intr_method -> PCIE_INTX(0); d2h_intr_control -> D2H_INTMASK(0)
[   20.443261] [dhd] dhdpcie_download_code_file: dhd_tcm_test_enable 0, dhd_tcm_test_status 0
[   20.443266] [dhd] dhdpcie_download_code_file: download firmware /lib/firmware/brcm/fw_bcm43752a2_pcie_ag.bin
[   20.443280] [dhd] dhd_os_open_image1: /lib/firmware/brcm/fw_bcm43752a2_pcie_ag.bin (942297 bytes) open success
[   20.443286] [dhd] dhdpcie_download_code_file Using SINGLE image (size 942297)
[   20.537497] [dhd] dhd_os_open_image1: /lib/firmware/brcm/nvram_ap6275p.txt (7335 bytes) open success
[   20.537506] [dhd] dhdpcie_download_nvram: dhd_get_download_buffer len 7335
[   20.537509] [dhd] # AP6275P_NVRAM_V1.1_20200702 
[   20.537540] [dhd] dhdpcie_download_nvram: process_nvram_vars len 5860
[   20.555116] [dhd] dhdpcie_bus_write_vars: Download, Upload and compare of NVRAM succeeded.
[   20.555118] [dhd] dhdpcie_bus_write_vars: New varsize is 5864, length token(nvram_csm)=0xfa4505ba
[   20.555523] [dhd] Download and compare of TLV 0xfeedc0de succeeded (size 128, addr 2ae88c).
[   20.555615] [dhd] dhdpcie_bus_download_state: Took ARM out of Reset
[   20.555633] [dhd] dhd_bus_aer_config: Configure AER registers for EP
[   20.555652] [dhd] dhd_bus_aer_config: Configure AER registers for RC
[   20.646005] [dhd] dhdpcie_readshared: addr=0x20c8f4 nvram_csm=0xfa4505ba
[   20.646009] [dhd] ### Total time ARM OOR to Readshared pass took 90430 usec ###
[   20.646010] [dhd] dhdpcie_readshared: PCIe shared addr (0x0020c8f4) read took 90000 usec before dongle is ready
[   20.646270] [dhd] FW supports DAR ? N
[   20.646297] [dhd] dhdpcie_readshared: max H2D queues 64
[   20.646298] [dhd] FW supports debug buf dest ? N 
[   20.646300] [dhd] FW supports MD ring ? N
[   20.646320] [dhd] dhd_bus_init: Enabling bus->intr_enabled
[   20.646323] [dhd] dhdpcie_oob_intr_register OOB irq=141 flags=0x4
[   20.646340] [dhd] dhdpcie_oob_intr_register: enable_irq_wake
[   20.646361] [dhd] STATIC-MSG) dhd_wlan_mem_prealloc : section 9, size 32896
[   20.647057] [dhd] dhd_prot_init:4146: h2d_max_txpost = 512
[   20.647060] [dhd] dhd_prot_init:4152: h2d_htput_max_txpost = 2048
[   20.647064] [dhd] dhd_prot_init: max_rxbufpost:511 rx_buf_burst:64 rx_bufpost_threshold:64
[   20.647067] [dhd] ENABLING DW:0
[   20.647069] [dhd] IDMA not enabled in FW !!
[   20.647071] [dhd] IFRM not enabled in FW !!
[   20.647072] [dhd] DAR not enabled in FW !!
[   20.647073] [dhd] Enable hostcap: EXTD TXS in txcpl
[   20.647115] [dhd] dhd_prot_d2h_sync_init(): D2H sync mechanism is XORCSUM 
[   20.647126] [dhd] dhd_bus_hostready : Read PCICMD Reg: 0x00100006
[   20.647142] [dhd] dhd_bus_hostready: Ring Hostready:1
[   20.647246] [dhd] trying to send create d2h info ring: id 70
[   20.647248] [dhd] dhd_send_d2h_ringcreate ringid: 3 idx: 70 max_h2d: 67
[   20.647250] [dhd] trying to send create h2d info ring id 69
[   20.648123] [dhd] dhd_prot_process_d2h_ring_create_complete ring create Response status = 0 ring 3, id 0xfffc
[   20.648142] [dhd] info buffer post after ring create
[   20.649893] [dhd] wlc_ver_major 12, wlc_ver_minor 1
[   20.650251] [dhd] dhd_sync_with_dongle: GET_REVINFO device 0x449d, vendor 0x14e4, chipnum 0xaae8
[   20.650686] [dhd] dhd_sync_with_dongle: RxBuf Post : 2048
[   20.650688] [dhd] dhd_sync_with_dongle: RxBuf Post Alloc : 2048
[   20.652277] [dhd] dhd_preinit_ioctls: preinit_status IOVAR not supported, use legacy preinit
[   20.652280] [dhd] dhd_tcpack_suppress_set: TCP ACK Suppress mode 0 -> mode 3
[   20.652282] [dhd] dhd_tcpack_suppress_set: TCPACK_INFO_MAXNUM=40, TCPDATA_INFO_MAXNUM=40
[   20.653140] [dhd] dhd_legacy_preinit_ioctls: hostwake_oob enabled
[   20.654452] [dhd] dhd_legacy_preinit_ioctls: use firmware generated mac_address 70:f7:54:b8:cc:cd
[   20.654467] [dhd] dhd_os_open_image1: /lib/firmware/brcm/clm_bcm43752a2_pcie_ag.blob (29225 bytes) open success
[   20.655009] [dhd] dhd_check_current_clm_data: ----- This FW is not included CLM data -----
[   20.670215] [dhd] dhd_apply_default_clm: CLM download succeeded 
[   20.670781] [dhd] dhd_check_current_clm_data: ----- This FW is included CLM data -----
[   20.672991] [dhd] Firmware up: op_mode=0x0005, MAC=70:f7:54:b8:cc:cd
[   20.707948] [dhd] dhd_legacy_preinit_ioctls: event_log_max_sets: 26 ret: 0
[   20.711979] [dhd] arp_enable:1 arp_ol:0
[   20.714589] [dhd]   Driver: 101.10.591.52.27 (20240409-1)(20240411-2)
               [dhd]   Firmware: wl0: Dec  6 2023 16:58:26 version 18.35.387.23.215 (g7861e478) FWID 01-efcb6b79
               [dhd]   CLM: 9.9.8_SS (2021-05-10 15:05:58) 
[   20.716632] [dhd] dhd_legacy_preinit_ioctls: Monitor mode is enabled in FW cap
[   20.731311] [dhd] dhd_legacy_preinit_ioctls: d3_hostwake_delay IOVAR not present, proceed
[   20.732296] [dhd] dhd_update_interface_flow_info: ifindex:0 previous role:0 new role:0
[   20.732323] [dhd] dhd_rx_frame: net device is NOT registered. drop event packet
[   20.733181] [dhd] dhd_conf_same_country : country code = CN/0 is already configured
[   20.739600] [dhd] dhd_bus_devreset: WLAN Power On Done
[   20.739602] [dhd] [wlan0] wl_android_wifi_on : Success
[   20.764601] [dhd] dhd_update_interface_flow_info: ifindex:0 previous role:0 new role:0
[   20.764626] [dhd] dhd_rx_frame: net device is NOT registered. drop event packet
[   20.778806] [dhd] [wlan0] wl_cfg80211_up : Roam channel cache enabled
[   20.780807] [dhd] [wlan0] dhd_open : Exit ret=0
[   20.780810] [dhd] [wlan0] dhd_pri_open : tx queue started
[   20.780826] [dhd] [wlan0] custom_xps_map_set : Done. mapping cpu
[   20.780828] [dhd] dhd_pri_open : mutex is released.
[   20.786810] [dhd] dhd_ioctl_entry_local bad ifidx
[   20.788388] [dhd] dhd_static_if_open : no mutex held
[   20.788392] [dhd] dhd_static_if_open : set mutex lock
[   20.788394] [dhd] [wlan1] dhd_static_if_open : Enter
[   20.788397] [dhd] [wlan0] dhd_open : Primary net_device is already up
[   20.788401] [dhd] CFG80211-ERROR) wl_cfg80211_deinit_p2p_discovery : Disabling P2P Discovery Interface 
[   20.788404] [dhd] CFGP2P-ERROR) wl_cfgp2p_disable_discovery :  do nothing, not initialized
[   20.790984] [dhd] dhd_update_interface_flow_info: ifindex:1 previous role:0 new role:0
[   20.800378] [dhd] dhd_clear_del_in_progress
[   20.800383] [dhd] [wlan1] dhd_static_if_open : Exit ret=0
[   20.800385] [dhd] dhd_static_if_open : mutex is released.
[   20.880972] rockchip-vop2 fdd90000.vop: [drm:vop2_crtc_atomic_enable] Update mode to 1920x1080p60, type: 10(if:DP0, flag:0x0) for vp2 dclk: 148500000
[   20.881550] rockchip-vop2 fdd90000.vop: [drm:vop2_crtc_atomic_enable] dclk_out2 div: 2 dclk_core2 div: 2
[   20.881578] rockchip-vop2 fdd90000.vop: [drm:vop2_crtc_atomic_enable] set dclk_vop2 to 148500000, get 148500000
[   20.890516] [dhd] P2P interface registered
[   20.895821] dw-dp fde50000.dp: full-training link: 4 lanes at 2700 MHz
[   20.900457] dw-dp fde50000.dp: clock recovery succeeded
[   20.904188] dw-dp fde50000.dp: channel equalization succeeded
[   20.906813] [dhd] CFGP2P-ERROR) wl_cfgp2p_set_discovery : p2p_disc 1 error -16
[   20.906819] [dhd] CFGP2P-ERROR) wl_cfgp2p_init_discovery : set discover error
[   20.913804] [dhd] CFGP2P-ERROR) wl_cfgp2p_enable_discovery :  init discovery error -16
[   20.913814] [dhd] CFGP2P-ERROR) wl_cfgp2p_disable_discovery :  do nothing, not initialized
[   20.914940] rockchip-vop2 fdd90000.vop: [drm] vop enable intf:200
[   20.920825] [dhd] CFGP2P-ERROR) wl_cfgp2p_start_p2p_device : P2P enable discovery failed, ret=-16
[   20.921586] [dhd] CFGP2P-ERROR) wl_cfgp2p_disable_discovery :  do nothing, not initialized
[   20.950008] [dhd] CFGP2P-ERROR) wl_cfgp2p_del_p2p_disc_if : P2P interface unregistered
[   20.973808] [dhd] CFG80211-ERROR) wl_cfg80211_flush_pmksa : Not supporting Flushing pmklist on virtual interfaces than primary interface, primary_dev wlan0 dev wlan1
[   20.990511] of_dma_request_slave_channel: dma-names property of node '/serial@febc0000' missing or empty
[   20.990552] dw-apb-uart febc0000.serial: failed to request DMA, use interrupt mode
[   20.996884] [dhd] P2P interface registered
[   21.010855] [dhd] CFGP2P-ERROR) wl_cfgp2p_set_discovery : p2p_disc 1 error -16
[   21.010867] [dhd] CFGP2P-ERROR) wl_cfgp2p_init_discovery : set discover error
[   21.017608] [dhd] CFGP2P-ERROR) wl_cfgp2p_enable_discovery :  init discovery error -16
[   21.017616] [dhd] CFGP2P-ERROR) wl_cfgp2p_disable_discovery :  do nothing, not initialized
[   21.023655] [dhd] CFGP2P-ERROR) wl_cfgp2p_start_p2p_device : P2P enable discovery failed, ret=-16
[   21.024013] [dhd] CFGP2P-ERROR) wl_cfgp2p_disable_discovery :  do nothing, not initialized
[   21.060081] [dhd] CFGP2P-ERROR) wl_cfgp2p_del_p2p_disc_if : P2P interface unregistered
[   21.802329] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.802368] stream_cif_mipi_id0: update sensor info failed -19
[   21.802434] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.802454] stream_cif_mipi_id1: update sensor info failed -19
[   21.802492] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.802511] rkcif_tools_id2: update sensor info failed -19
[   21.802545] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.802564] stream_cif_mipi_id2: update sensor info failed -19
[   21.802598] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   21.802617] stream_cif_mipi_id3: update sensor info failed -19
[   21.802650] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.802669] rkcif_scale_ch0: update sensor info failed -19
[   21.802701] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.802721] rkcif_scale_ch1: update sensor info failed -19
[   21.802754] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.802774] rkcif_scale_ch2: update sensor info failed -19
[   21.802807] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   21.802827] rkcif_scale_ch3: update sensor info failed -19
[   21.802859] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.802878] rkcif_tools_id0: update sensor info failed -19
[   21.802911] rkcif-mipi-lvds: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.802930] rkcif_tools_id1: update sensor info failed -19
[   21.802973] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.802993] stream_cif_mipi_id0: update sensor info failed -19
[   21.803028] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.803048] stream_cif_mipi_id1: update sensor info failed -19
[   21.803080] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.803099] stream_cif_mipi_id2: update sensor info failed -19
[   21.803131] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   21.803151] stream_cif_mipi_id3: update sensor info failed -19
[   21.803182] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.803201] rkcif_scale_ch0: update sensor info failed -19
[   21.803233] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.803253] rkcif_scale_ch1: update sensor info failed -19
[   21.803285] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.803304] rkcif_scale_ch2: update sensor info failed -19
[   21.803360] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   21.803380] rkcif_scale_ch3: update sensor info failed -19
[   21.803415] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.803435] rkcif_tools_id0: update sensor info failed -19
[   21.803469] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.803488] rkcif_tools_id1: update sensor info failed -19
[   21.803522] rkcif-mipi-lvds1: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.803541] rkcif_tools_id2: update sensor info failed -19
[   21.803588] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.803608] stream_cif_mipi_id0: update sensor info failed -19
[   21.803640] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.803660] stream_cif_mipi_id1: update sensor info failed -19
[   21.804413] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.805131] stream_cif_mipi_id2: update sensor info failed -19
[   21.805874] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   21.806606] stream_cif_mipi_id3: update sensor info failed -19
[   21.807375] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.808123] rkcif_scale_ch0: update sensor info failed -19
[   21.808897] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.809657] rkcif_scale_ch1: update sensor info failed -19
[   21.810458] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.811224] rkcif_scale_ch2: update sensor info failed -19
[   21.812005] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[3] get remote terminal sensor failed!
[   21.812772] rkcif_scale_ch3: update sensor info failed -19
[   21.813567] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[0] get remote terminal sensor failed!
[   21.814338] rkcif_tools_id0: update sensor info failed -19
[   21.815136] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[1] get remote terminal sensor failed!
[   21.815923] rkcif_tools_id1: update sensor info failed -19
[   21.816742] rkcif-mipi-lvds2: rkcif_update_sensor_info: stream[2] get remote terminal sensor failed!
[   21.817543] rkcif_tools_id2: update sensor info failed -19
[   26.271481] [dhd] [wlan0] wl_ext_set_chanspec : channel 5g-149(0xe09b 80MHz)
[   26.272701] [dhd] [wlan0] wl_conn_debug_info : Connecting with 58:cb:52:bf:6e:c0 ssid "anso", len (4), channel=5g-149(chan_cnt=1), sec=wpa2/psk/mfpc/aes, rssi=-60
[   26.353513] [dhd] dhd_update_interface_flow_info: ifindex:0 previous role:0 new role:0
[   26.353524] [dhd] dhd_update_multicilent_flow_rings: ifindex 0
[   26.371194] [dhd] [wlan0] wl_iw_event : Link UP with 58:cb:52:bf:6e:c0
[   26.371208] [dhd] [wlan0] wl_ext_iapsta_link : [S] Link UP with 58:cb:52:bf:6e:c0
[   26.374587] [dhd] [wlan0] wl_bss_connect_done : Report connect result - connection succeeded
[   26.384881] [dhd] dhd_prot_flow_ring_create: Send Flow Create Req flow ID 61 for peer 58:cb:52:bf:6e:c0 prio 3 ifindex 0 items 512
[   26.385233] [dhd] dhd_prot_flow_ring_create_response_process: Flow Create Response status = 0 Flow 61
[   26.390974] [dhd] [wlan0] wl_add_keyext : key index (0) for 58:cb:52:bf:6e:c0
[   26.411086] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready
[   26.413733] [dhd] [wlan0] wl_cfg80211_set_suspend_bcn_li_dtim : bcn_li_dtim:0 lpas:0 bcn_to_dly:0
[   26.415587] [dhd] dhd_prot_flow_ring_create: Send Flow Create Req flow ID 65 for peer ff:ff:ff:ff:ff:ff prio 0 ifindex 0 items 2048
[   26.416101] [dhd] dhd_prot_flow_ring_create_response_process: Flow Create Response status = 0 Flow 65
[   28.197173] platform bt-sound: deferred probe pending
[   28.197177] platform es8316-sound: deferred probe pending
[   29.165875] Bluetooth: Core ver 2.22
[   29.165946] NET: Registered PF_BLUETOOTH protocol family
[   29.165952] Bluetooth: HCI device and connection manager initialized
[   29.165965] Bluetooth: HCI socket layer initialized
[   29.165971] Bluetooth: L2CAP socket layer initialized
[   29.165987] Bluetooth: SCO socket layer initialized
[   29.167894] Bluetooth: HCI UART driver ver 2.3
[   29.167899] Bluetooth: HCI UART protocol H4 registered
[   29.167901] Bluetooth: HCI UART protocol ATH3K registered
[   29.272565] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
[   29.272581] Bluetooth: BNEP filters: protocol multicast
[   29.272594] Bluetooth: BNEP socket layer initialized
[   29.275781] Bluetooth: MGMT ver 1.22
[   29.281221] NET: Registered PF_ALG protocol family
[   29.299036] Bluetooth: RFCOMM TTY layer initialized
[   29.299058] Bluetooth: RFCOMM socket layer initialized
[   29.299073] Bluetooth: RFCOMM ver 1.11
[   46.986875] vcc3v3_lcd1_en: disabling
[   46.986888] vcc3v3_lcd2_en: disabling
[  138.448960] mali fb000000.gpu: use 'driver built-in firmware' directly
[  138.448965] mali fb000000.gpu: Loading Mali firmware 0x1010000
[  138.449888] mali fb000000.gpu: Mali firmware git_sha: 8e5cfcfec20cc8aff8509d37e72babc935d34a3b 
[  138.452662] mali fb000000.gpu: CSF_SCHED_PROTM_PROGRESS_TIMEOUT is capped from 8738ms to 4500ms
[  138.459393] mali fb000000.gpu: Clearing BASE_MEM_UNCACHED_GPU flag to avoid MMA violation

```