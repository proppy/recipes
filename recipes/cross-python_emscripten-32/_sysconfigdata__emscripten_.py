build_time_vars = {
    "AR": "$CONDA_EMSDK_DIR/upstream/emscripten/emar",
    "CC": "$CONDA_EMSDK_DIR/upstream/emscripten/emcc",
    "CXX": "$CONDA_EMSDK_DIR/upstream/emscripten/em++",
    "CCSHARED": "",
    "CFLAGS": "-Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g "
    "-fwrapv -O3 -Wall -g0 -g0 -fPIC -fdiagnostics-color=always",
    "LDFLAGS": "-L$PREFIX/lib ",
    "LDSHARED": "$CONDA_EMSDK_DIR/upstream/emscripten/emcc " "-L$PREFIX/lib ",
    "VERSION": "3.10",
    "HOST_GNU_TYPE": "wasm32-unknown-emscripten",
    "ABIFLAGS": "",
    "AC_APPLE_UNIVERSAL_BUILD": 0,
    "AIX_BUILDDATE": 0,
    "AIX_GENUINE_CPLUSPLUS": 0,
    "ALIGNOF_LONG": 4,
    "ALIGNOF_SIZE_T": 4,
    "ALT_SOABI": 0,
    "ANDROID_API_LEVEL": 0,
    "AR": "$CONDA_EMSDK_DIR/upstream/emscripten/emar",
    "ARFLAGS": "rcs",
    "BASECFLAGS": "-Wno-unused-result -Wsign-compare -Wunreachable-code",
    "BASECPPFLAGS": "",
    "BASEMODLIBS": "",
    "BINDIR": "$PREFIX/bin",
    "BINLIBDEST": "$PREFIX/lib/python3.10",
    "BLDLIBRARY": "libpython3.10.a",
    "BLDSHARED": "$CONDA_EMSDK_DIR/upstream/emscripten/emcc " "-L$PREFIX/lib",
    "BUILDEXE": "",
    "BUILDPYTHON": "python",
    "BUILD_GNU_TYPE": "x86_64-pc-linux-gnu",
    "BYTESTR_DEPS": "\\",
    "CC": "$CONDA_EMSDK_DIR/upstream/emscripten/emcc",
    "CCSHARED": "",
    "CFLAGS": "-Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g "
    "-fwrapv -O3 -Wall -g0 -g0 -fPIC -fdiagnostics-color=always",
    "CFLAGSFORSHARED": "",
    "CFLAGS_ALIASING": "-fno-strict-aliasing",
    "CONFIGFILES": "configure configure.ac acconfig.h pyconfig.h.in " "Makefile.pre.in",
    "CONFIGURE_CFLAGS": "-g0 -g0 -fPIC",
    "CONFIGURE_CFLAGS_NODIST": "-std=c99 -Wextra -Wno-unused-result "
    "-Wno-unused-parameter "
    "-Wno-missing-field-initializers "
    "-Wstrict-prototypes "
    "-Werror=implicit-function-declaration "
    "-fvisibility=hidden",
    "CONFIGURE_CPPFLAGS": "-I$PREFIX/include",
    "CONFIGURE_LDFLAGS": "-L$PREFIX/lib ",
    "CONFIGURE_LDFLAGS_NODIST": "",
    "CONFIG_ARGS": "'CFLAGS=-g0 -g0 -fPIC' "
    "'CPPFLAGS=-I$PREFIX/include' "
    "'LDFLAGS=-L$PREFIX/lib "
    "'--without-pymalloc' '--disable-shared' "
    "'--disable-ipv6' '--enable-big-digits=30' "
    "'--enable-optimizations' '--host=wasm32-unknown-emscripten' "
    "'--build=x86_64-pc-linux-gnu' "
    "'--prefix=/home/derthorsten/micromamba/envs/emforgetest' "
    "'build_alias=x86_64-pc-linux-gnu' "
    "'host_alias=wasm32-unknown-emscripten' "
    "'CC=$CONDA_EMSDK_DIR/upstream/emscripten/emcc' "
    "'PKG_CONFIG_PATH=' "
    "'PKG_CONFIG_LIBDIR=$CONDA_EMSDK_DIR/upstream/emscripten/cache/sysroot/local/lib/pkgconfig:$CONDA_EMSDK_DIR/upstream/emscripten/cache/sysroot/lib/pkgconfig'",
    "CONFINCLUDEDIR": "$PREFIX/include",
    "CONFINCLUDEPY": "$PREFIX/include/python3.10",
    "COREPYTHONPATH": "",
    "COVERAGE_INFO": "$PREFIX/conda-bld/python_1649414357931/work/coverage.info",
    "COVERAGE_REPORT": "$PREFIX/conda-bld/python_1649414357931/work/lcov-report",
    "COVERAGE_REPORT_OPTIONS": '--no-branch-coverage --title "CPython lcov ' 'report"',
    "CPPFLAGS": "-I. -I./Include " "-I$PREFIX/include",
    "CTYPES_FLAGS": "-DHAVE_FFI_PREP_CIF_VAR=1 -DHAVE_FFI_PREP_CLOSURE_LOC=1 "
    "-DHAVE_FFI_CLOSURE_ALLOC=1",
    "CXX": "$CONDA_EMSDK_DIR/upstream/emscripten/em++",
    "DESTDIRS": "/home/derthorsten/micromamba/envs/emforgetest "
    "$PREFIX/lib "
    "$PREFIX/lib/python3.10 "
    "$PREFIX/lib/python3.10/lib-dynload",
    "DESTLIB": "$PREFIX/lib/python3.10",
    "DESTPATH": "",
    "DESTSHARED": "$PREFIX/lib/python3.10/lib-dynload",
    "DFLAGS": "",
    "DIRMODE": 755,
    "DIST": "README.rst ChangeLog configure configure.ac acconfig.h pyconfig.h.in "
    "Makefile.pre.in Include Lib Misc Ext-dummy",
    "DISTDIRS": "Include Lib Misc Ext-dummy",
    "DISTFILES": "README.rst ChangeLog configure configure.ac acconfig.h "
    "pyconfig.h.in Makefile.pre.in",
    "DLINCLDIR": ".",
    "DLLLIBRARY": "",
    "DOUBLE_IS_ARM_MIXED_ENDIAN_IEEE754": 0,
    "DOUBLE_IS_BIG_ENDIAN_IEEE754": 0,
    "DOUBLE_IS_LITTLE_ENDIAN_IEEE754": 1,
    "DTRACE": "",
    "DTRACE_DEPS": "\\",
    "DTRACE_HEADERS": "",
    "DTRACE_OBJS": "",
    "DYNLOADFILE": "dynload_shlib.o",
    "ENABLE_IPV6": 0,
    "ENSUREPIP": "upgrade",
    "EXE": "",
    "EXEMODE": 755,
    "EXPERIMENTAL_ISOLATED_SUBINTERPRETERS": 0,
    "EXPORTSFROM": "",
    "EXPORTSYMS": "",
    "EXTRATESTOPTS": "",
    "EXTRA_CFLAGS": "",
    "EXT_SUFFIX": ".cpython-310.so",
    "FILEMODE": 644,
    "FLOAT_WORDS_BIGENDIAN": 0,
    "FLOCK_NEEDS_LIBBSD": 0,
    "GETPGRP_HAVE_ARG": 0,
    "GITBRANCH": "",
    "GITTAG": "",
    "GITVERSION": "",
    "GNULD": "no",
    "HAVE_ACCEPT4": 1,
    "HAVE_ACOSH": 1,
    "HAVE_ADDRINFO": 1,
    "HAVE_ALARM": 1,
    "HAVE_ALIGNED_REQUIRED": 1,
    "HAVE_ALLOCA_H": 1,
    "HAVE_ALTZONE": 0,
    "HAVE_ASINH": 1,
    "HAVE_ASM_TYPES_H": 0,
    "HAVE_ATANH": 1,
    "HAVE_BIND_TEXTDOMAIN_CODESET": 1,
    "HAVE_BLUETOOTH_BLUETOOTH_H": 0,
    "HAVE_BLUETOOTH_H": 0,
    "HAVE_BROKEN_MBSTOWCS": 0,
    "HAVE_BROKEN_NICE": 0,
    "HAVE_BROKEN_PIPE_BUF": 0,
    "HAVE_BROKEN_POLL": 0,
    "HAVE_BROKEN_POSIX_SEMAPHORES": 0,
    "HAVE_BROKEN_PTHREAD_SIGMASK": 0,
    "HAVE_BROKEN_SEM_GETVALUE": 1,
    "HAVE_BROKEN_UNSETENV": 0,
    "HAVE_BUILTIN_ATOMIC": 1,
    "HAVE_CHFLAGS": 0,
    "HAVE_CHOWN": 1,
    "HAVE_CHROOT": 1,
    "HAVE_CLOCK": 1,
    "HAVE_CLOCK_GETRES": 1,
    "HAVE_CLOCK_GETTIME": 1,
    "HAVE_CLOCK_SETTIME": 1,
    "HAVE_CLOSE_RANGE": 0,
    "HAVE_COMPUTED_GOTOS": 0,
    "HAVE_CONFSTR": 1,
    "HAVE_CONIO_H": 0,
    "HAVE_COPYSIGN": 1,
    "HAVE_COPY_FILE_RANGE": 0,
    "HAVE_CRYPT_H": 1,
    "HAVE_CRYPT_R": 1,
    "HAVE_CTERMID": 1,
    "HAVE_CTERMID_R": 0,
    "HAVE_CURSES_FILTER": 0,
    "HAVE_CURSES_H": 0,
    "HAVE_CURSES_HAS_KEY": 0,
    "HAVE_CURSES_IMMEDOK": 0,
    "HAVE_CURSES_IS_PAD": 0,
    "HAVE_CURSES_IS_TERM_RESIZED": 0,
    "HAVE_CURSES_RESIZETERM": 0,
    "HAVE_CURSES_RESIZE_TERM": 0,
    "HAVE_CURSES_SYNCOK": 0,
    "HAVE_CURSES_TYPEAHEAD": 0,
    "HAVE_CURSES_USE_ENV": 0,
    "HAVE_CURSES_WCHGAT": 0,
    "HAVE_DECL_ISFINITE": 1,
    "HAVE_DECL_ISINF": 1,
    "HAVE_DECL_ISNAN": 1,
    "HAVE_DECL_RTLD_DEEPBIND": 0,
    "HAVE_DECL_RTLD_GLOBAL": 1,
    "HAVE_DECL_RTLD_LAZY": 1,
    "HAVE_DECL_RTLD_LOCAL": 1,
    "HAVE_DECL_RTLD_MEMBER": 0,
    "HAVE_DECL_RTLD_NODELETE": 1,
    "HAVE_DECL_RTLD_NOLOAD": 1,
    "HAVE_DECL_RTLD_NOW": 1,
    "HAVE_DECL_TZNAME": 0,
    "HAVE_DEVICE_MACROS": 1,
    "HAVE_DEV_PTC": 0,
    "HAVE_DEV_PTMX": 0,
    "HAVE_DIRECT_H": 0,
    "HAVE_DIRENT_D_TYPE": 1,
    "HAVE_DIRENT_H": 1,
    "HAVE_DIRFD": 1,
    "HAVE_DLFCN_H": 1,
    "HAVE_DLOPEN": 1,
    "HAVE_DUP2": 1,
    "HAVE_DUP3": 1,
    "HAVE_DYLD_SHARED_CACHE_CONTAINS_PATH": 0,
    "HAVE_DYNAMIC_LOADING": 1,
    "HAVE_ENDIAN_H": 1,
    "HAVE_EPOLL": 1,
    "HAVE_EPOLL_CREATE1": 1,
    "HAVE_ERF": 1,
    "HAVE_ERFC": 1,
    "HAVE_ERRNO_H": 1,
    "HAVE_EVENTFD": 1,
    "HAVE_EXECV": 1,
    "HAVE_EXPLICIT_BZERO": 1,
    "HAVE_EXPLICIT_MEMSET": 0,
    "HAVE_EXPM1": 1,
    "HAVE_FACCESSAT": 1,
    "HAVE_FCHDIR": 1,
    "HAVE_FCHMOD": 1,
    "HAVE_FCHMODAT": 1,
    "HAVE_FCHOWN": 1,
    "HAVE_FCHOWNAT": 1,
    "HAVE_FCNTL_H": 1,
    "HAVE_FDATASYNC": 1,
    "HAVE_FDOPENDIR": 1,
    "HAVE_FDWALK": 0,
    "HAVE_FEXECVE": 1,
    "HAVE_FINITE": 1,
    "HAVE_FLOCK": 1,
    "HAVE_FORK": 1,
    "HAVE_FORKPTY": 1,
    "HAVE_FPATHCONF": 1,
    "HAVE_FSEEK64": 0,
    "HAVE_FSEEKO": 1,
    "HAVE_FSTATAT": 1,
    "HAVE_FSTATVFS": 1,
    "HAVE_FSYNC": 1,
    "HAVE_FTELL64": 0,
    "HAVE_FTELLO": 1,
    "HAVE_FTIME": 1,
    "HAVE_FTRUNCATE": 1,
    "HAVE_FUTIMENS": 1,
    "HAVE_FUTIMES": 0,
    "HAVE_FUTIMESAT": 1,
    "HAVE_GAI_STRERROR": 1,
    "HAVE_GAMMA": 0,
    "HAVE_GCC_ASM_FOR_MC68881": 0,
    "HAVE_GCC_ASM_FOR_X64": 0,
    "HAVE_GCC_ASM_FOR_X87": 0,
    "HAVE_GCC_UINT128_T": 1,
    "HAVE_GETADDRINFO": 1,
    "HAVE_GETC_UNLOCKED": 1,
    "HAVE_GETENTROPY": 1,
    "HAVE_GETGRGID_R": 1,
    "HAVE_GETGRNAM_R": 1,
    "HAVE_GETGROUPLIST": 0,
    "HAVE_GETGROUPS": 1,
    "HAVE_GETHOSTBYNAME": 0,
    "HAVE_GETHOSTBYNAME_R": 1,
    "HAVE_GETHOSTBYNAME_R_3_ARG": 0,
    "HAVE_GETHOSTBYNAME_R_5_ARG": 0,
    "HAVE_GETHOSTBYNAME_R_6_ARG": 1,
    "HAVE_GETITIMER": 1,
    "HAVE_GETLOADAVG": 1,
    "HAVE_GETLOGIN": 1,
    "HAVE_GETNAMEINFO": 1,
    "HAVE_GETPAGESIZE": 1,
    "HAVE_GETPEERNAME": 1,
    "HAVE_GETPGID": 1,
    "HAVE_GETPGRP": 1,
    "HAVE_GETPID": 1,
    "HAVE_GETPRIORITY": 1,
    "HAVE_GETPWENT": 1,
    "HAVE_GETPWNAM_R": 1,
    "HAVE_GETPWUID_R": 1,
    "HAVE_GETRANDOM": 0,
    "HAVE_GETRANDOM_SYSCALL": 0,
    "HAVE_GETRESGID": 1,
    "HAVE_GETRESUID": 1,
    "HAVE_GETSID": 1,
    "HAVE_GETSPENT": 0,
    "HAVE_GETSPNAM": 0,
    "HAVE_GETWD": 0,
    "HAVE_GLIBC_MEMMOVE_BUG": 0,
    "HAVE_GRP_H": 1,
    "HAVE_HSTRERROR": 1,
    "HAVE_HTOLE64": 1,
    "HAVE_HYPOT": 1,
    "HAVE_IEEEFP_H": 0,
    "HAVE_IF_NAMEINDEX": 0,
    "HAVE_INET_ATON": 1,
    "HAVE_INET_PTON": 1,
    "HAVE_INITGROUPS": 0,
    "HAVE_INTTYPES_H": 1,
    "HAVE_IO_H": 0,
    "HAVE_IPA_PURE_CONST_BUG": 0,
    "HAVE_KILL": 1,
    "HAVE_KILLPG": 1,
    "HAVE_KQUEUE": 0,
    "HAVE_LANGINFO_H": 1,
    "HAVE_LARGEFILE_SUPPORT": 1,
    "HAVE_LCHFLAGS": 0,
    "HAVE_LCHMOD": 1,
    "HAVE_LCHOWN": 1,
    "HAVE_LGAMMA": 1,
    "HAVE_LIBDL": 1,
    "HAVE_LIBDLD": 0,
    "HAVE_LIBIEEE": 0,
    "HAVE_LIBINTL_H": 1,
    "HAVE_LIBREADLINE": 0,
    "HAVE_LIBRESOLV": 0,
    "HAVE_LIBSENDFILE": 0,
    "HAVE_LIBUTIL_H": 0,
    "HAVE_LIBUUID": 0,
    "HAVE_LINK": 1,
    "HAVE_LINKAT": 1,
    "HAVE_LINUX_CAN_BCM_H": 0,
    "HAVE_LINUX_CAN_H": 0,
    "HAVE_LINUX_CAN_J1939_H": 0,
    "HAVE_LINUX_CAN_RAW_FD_FRAMES": 0,
    "HAVE_LINUX_CAN_RAW_H": 0,
    "HAVE_LINUX_CAN_RAW_JOIN_FILTERS": 0,
    "HAVE_LINUX_MEMFD_H": 0,
    "HAVE_LINUX_NETLINK_H": 0,
    "HAVE_LINUX_QRTR_H": 0,
    "HAVE_LINUX_RANDOM_H": 0,
    "HAVE_LINUX_TIPC_H": 0,
    "HAVE_LINUX_VM_SOCKETS_H": 1,
    "HAVE_LINUX_WAIT_H": 0,
    "HAVE_LOCKF": 1,
    "HAVE_LOG1P": 1,
    "HAVE_LOG2": 1,
    "HAVE_LONG_DOUBLE": 1,
    "HAVE_LSTAT": 1,
    "HAVE_LUTIMES": 0,
    "HAVE_MADVISE": 1,
    "HAVE_MAKEDEV": 1,
    "HAVE_MBRTOWC": 1,
    "HAVE_MEMFD_CREATE": 1,
    "HAVE_MEMORY_H": 1,
    "HAVE_MEMRCHR": 1,
    "HAVE_MKDIRAT": 1,
    "HAVE_MKFIFO": 1,
    "HAVE_MKFIFOAT": 1,
    "HAVE_MKNOD": 1,
    "HAVE_MKNODAT": 1,
    "HAVE_MKTIME": 1,
    "HAVE_MMAP": 1,
    "HAVE_MREMAP": 1,
    "HAVE_NCURSES_H": 0,
    "HAVE_NDIR_H": 0,
    "HAVE_NETPACKET_PACKET_H": 1,
    "HAVE_NET_IF_H": 1,
    "HAVE_NICE": 1,
    "HAVE_NON_UNICODE_WCHAR_T_REPRESENTATION": 0,
    "HAVE_OPENAT": 1,
    "HAVE_OPENPTY": 1,
    "HAVE_PATHCONF": 1,
    "HAVE_PAUSE": 1,
    "HAVE_PIPE2": 1,
    "HAVE_PLOCK": 0,
    "HAVE_POLL": 1,
    "HAVE_POLL_H": 1,
    "HAVE_POSIX_FADVISE": 1,
    "HAVE_POSIX_FALLOCATE": 1,
    "HAVE_POSIX_SPAWN": 1,
    "HAVE_POSIX_SPAWNP": 0,
    "HAVE_PREAD": 1,
    "HAVE_PREADV": 1,
    "HAVE_PREADV2": 0,
    "HAVE_PRLIMIT": 1,
    "HAVE_PROCESS_H": 0,
    "HAVE_PROTOTYPES": 1,
    "HAVE_PTHREAD_CONDATTR_SETCLOCK": 1,
    "HAVE_PTHREAD_DESTRUCTOR": 0,
    "HAVE_PTHREAD_GETCPUCLOCKID": 0,
    "HAVE_PTHREAD_H": 1,
    "HAVE_PTHREAD_INIT": 0,
    "HAVE_PTHREAD_KILL": 0,
    "HAVE_PTHREAD_SIGMASK": 1,
    "HAVE_PTY_H": 1,
    "HAVE_PWRITE": 1,
    "HAVE_PWRITEV": 1,
    "HAVE_PWRITEV2": 0,
    "HAVE_READLINK": 1,
    "HAVE_READLINKAT": 1,
    "HAVE_READV": 1,
    "HAVE_REALPATH": 1,
    "HAVE_RENAMEAT": 1,
    "HAVE_RL_APPEND_HISTORY": 0,
    "HAVE_RL_CATCH_SIGNAL": 0,
    "HAVE_RL_COMPLETION_APPEND_CHARACTER": 0,
    "HAVE_RL_COMPLETION_DISPLAY_MATCHES_HOOK": 0,
    "HAVE_RL_COMPLETION_MATCHES": 0,
    "HAVE_RL_COMPLETION_SUPPRESS_APPEND": 0,
    "HAVE_RL_PRE_INPUT_HOOK": 0,
    "HAVE_RL_RESIZE_TERMINAL": 0,
    "HAVE_ROUND": 1,
    "HAVE_RTPSPAWN": 0,
    "HAVE_SCHED_GET_PRIORITY_MAX": 0,
    "HAVE_SCHED_H": 1,
    "HAVE_SCHED_RR_GET_INTERVAL": 0,
    "HAVE_SCHED_SETAFFINITY": 0,
    "HAVE_SCHED_SETPARAM": 0,
    "HAVE_SCHED_SETSCHEDULER": 0,
    "HAVE_SEM_CLOCKWAIT": 0,
    "HAVE_SEM_GETVALUE": 0,
    "HAVE_SEM_OPEN": 0,
    "HAVE_SEM_TIMEDWAIT": 0,
    "HAVE_SEM_UNLINK": 0,
    "HAVE_SENDFILE": 0,
    "HAVE_SETEGID": 1,
    "HAVE_SETEUID": 1,
    "HAVE_SETGID": 1,
    "HAVE_SETGROUPS": 1,
    "HAVE_SETHOSTNAME": 0,
    "HAVE_SETITIMER": 1,
    "HAVE_SETLOCALE": 1,
    "HAVE_SETPGID": 1,
    "HAVE_SETPGRP": 1,
    "HAVE_SETPRIORITY": 1,
    "HAVE_SETREGID": 1,
    "HAVE_SETRESGID": 1,
    "HAVE_SETRESUID": 1,
    "HAVE_SETREUID": 1,
    "HAVE_SETSID": 1,
    "HAVE_SETUID": 1,
    "HAVE_SETVBUF": 1,
    "HAVE_SHADOW_H": 1,
    "HAVE_SHM_OPEN": 1,
    "HAVE_SHM_UNLINK": 1,
    "HAVE_SIGACTION": 1,
    "HAVE_SIGALTSTACK": 0,
    "HAVE_SIGFILLSET": 1,
    "HAVE_SIGINFO_T_SI_BAND": 1,
    "HAVE_SIGINTERRUPT": 1,
    "HAVE_SIGNAL_H": 1,
    "HAVE_SIGPENDING": 1,
    "HAVE_SIGRELSE": 0,
    "HAVE_SIGTIMEDWAIT": 1,
    "HAVE_SIGWAIT": 1,
    "HAVE_SIGWAITINFO": 1,
    "HAVE_SNPRINTF": 1,
    "HAVE_SOCKADDR_ALG": 0,
    "HAVE_SOCKADDR_SA_LEN": 0,
    "HAVE_SOCKADDR_STORAGE": 1,
    "HAVE_SOCKETPAIR": 1,
    "HAVE_SPAWN_H": 1,
    "HAVE_SPLICE": 0,
    "HAVE_SSIZE_T": 1,
    "HAVE_STATVFS": 1,
    "HAVE_STAT_TV_NSEC": 1,
    "HAVE_STAT_TV_NSEC2": 0,
    "HAVE_STDARG_PROTOTYPES": 1,
    "HAVE_STDINT_H": 1,
    "HAVE_STDLIB_H": 1,
    "HAVE_STD_ATOMIC": 1,
    "HAVE_STRFTIME": 1,
    "HAVE_STRINGS_H": 1,
    "HAVE_STRING_H": 1,
    "HAVE_STRLCPY": 1,
    "HAVE_STROPTS_H": 1,
    "HAVE_STRSIGNAL": 1,
    "HAVE_STRUCT_PASSWD_PW_GECOS": 1,
    "HAVE_STRUCT_PASSWD_PW_PASSWD": 1,
    "HAVE_STRUCT_STAT_ST_BIRTHTIME": 0,
    "HAVE_STRUCT_STAT_ST_BLKSIZE": 1,
    "HAVE_STRUCT_STAT_ST_BLOCKS": 1,
    "HAVE_STRUCT_STAT_ST_FLAGS": 0,
    "HAVE_STRUCT_STAT_ST_GEN": 0,
    "HAVE_STRUCT_STAT_ST_RDEV": 1,
    "HAVE_STRUCT_TM_TM_ZONE": 1,
    "HAVE_SYMLINK": 1,
    "HAVE_SYMLINKAT": 1,
    "HAVE_SYNC": 1,
    "HAVE_SYSCONF": 1,
    "HAVE_SYSEXITS_H": 1,
    "HAVE_SYS_AUDIOIO_H": 0,
    "HAVE_SYS_BSDTTY_H": 0,
    "HAVE_SYS_DEVPOLL_H": 0,
    "HAVE_SYS_DIR_H": 0,
    "HAVE_SYS_ENDIAN_H": 0,
    "HAVE_SYS_EPOLL_H": 1,
    "HAVE_SYS_EVENTFD_H": 1,
    "HAVE_SYS_EVENT_H": 0,
    "HAVE_SYS_FILE_H": 1,
    "HAVE_SYS_IOCTL_H": 1,
    "HAVE_SYS_KERN_CONTROL_H": 0,
    "HAVE_SYS_LOADAVG_H": 0,
    "HAVE_SYS_LOCK_H": 0,
    "HAVE_SYS_MEMFD_H": 0,
    "HAVE_SYS_MKDEV_H": 0,
    "HAVE_SYS_MMAN_H": 1,
    "HAVE_SYS_MODEM_H": 0,
    "HAVE_SYS_NDIR_H": 0,
    "HAVE_SYS_PARAM_H": 1,
    "HAVE_SYS_POLL_H": 1,
    "HAVE_SYS_RANDOM_H": 1,
    "HAVE_SYS_RESOURCE_H": 1,
    "HAVE_SYS_SELECT_H": 1,
    "HAVE_SYS_SENDFILE_H": 0,
    "HAVE_SYS_SOCKET_H": 1,
    "HAVE_SYS_STATVFS_H": 1,
    "HAVE_SYS_STAT_H": 1,
    "HAVE_SYS_SYSCALL_H": 1,
    "HAVE_SYS_SYSMACROS_H": 1,
    "HAVE_SYS_SYS_DOMAIN_H": 0,
    "HAVE_SYS_TERMIO_H": 0,
    "HAVE_SYS_TIMES_H": 1,
    "HAVE_SYS_TIME_H": 1,
    "HAVE_SYS_TYPES_H": 1,
    "HAVE_SYS_UIO_H": 1,
    "HAVE_SYS_UN_H": 1,
    "HAVE_SYS_UTSNAME_H": 1,
    "HAVE_SYS_WAIT_H": 1,
    "HAVE_SYS_XATTR_H": 1,
    "HAVE_TCGETPGRP": 1,
    "HAVE_TCSETPGRP": 1,
    "HAVE_TEMPNAM": 1,
    "HAVE_TERMIOS_H": 1,
    "HAVE_TERM_H": 0,
    "HAVE_TGAMMA": 1,
    "HAVE_TIMEGM": 1,
    "HAVE_TIMES": 1,
    "HAVE_TMPFILE": 1,
    "HAVE_TMPNAM": 1,
    "HAVE_TMPNAM_R": 0,
    "HAVE_TM_ZONE": 1,
    "HAVE_TRUNCATE": 1,
    "HAVE_TZNAME": 0,
    "HAVE_UCS4_TCL": 0,
    "HAVE_UNAME": 1,
    "HAVE_UNISTD_H": 1,
    "HAVE_UNLINKAT": 1,
    "HAVE_USABLE_WCHAR_T": 0,
    "HAVE_UTIL_H": 0,
    "HAVE_UTIMENSAT": 1,
    "HAVE_UTIMES": 1,
    "HAVE_UTIME_H": 1,
    "HAVE_UUID_CREATE": 0,
    "HAVE_UUID_ENC_BE": 0,
    "HAVE_UUID_GENERATE_TIME_SAFE": 0,
    "HAVE_UUID_H": 0,
    "HAVE_UUID_UUID_H": 1,
    "HAVE_VFORK": 1,
    "HAVE_WAIT3": 0,
    "HAVE_WAIT4": 0,
    "HAVE_WAITID": 1,
    "HAVE_WAITPID": 1,
    "HAVE_WCHAR_H": 1,
    "HAVE_WCSCOLL": 1,
    "HAVE_WCSFTIME": 0,
    "HAVE_WCSXFRM": 1,
    "HAVE_WMEMCMP": 1,
    "HAVE_WORKING_TZSET": 0,
    "HAVE_WRITEV": 1,
    "HAVE_ZLIB_COPY": 0,
    "HAVE__GETPTY": 0,
    "HOST_GNU_TYPE": "wasm32-unknown-emscripten",
    "INCLDIRSTOMAKE": "$PREFIX/include "
    "$PREFIX/include "
    "$PREFIX/include/python3.10 "
    "$PREFIX/include/python3.10",
    "INCLUDEDIR": "$PREFIX/include",
    "INCLUDEPY": "$PREFIX/include/python3.10",
    "INSTALL": "/usr/bin/install -c",
    "INSTALL_DATA": "/usr/bin/install -c -m 644",
    "INSTALL_PROGRAM": "/usr/bin/install -c",
    "INSTALL_SCRIPT": "/usr/bin/install -c",
    "INSTALL_SHARED": "/usr/bin/install -c -m 755",
    "INSTSONAME": "libpython3.10.a",
    "IO_H": "Modules/_io/_iomodule.h",
    "IO_OBJS": "\\",
    "LDCXXSHARED": "$CONDA_EMSDK_DIR/upstream/emscripten/emcc",
    "LDFLAGS": "-L$PREFIX/lib ",
    "LDLIBRARY": "libpython3.10.a",
    "LDLIBRARYDIR": "",
    "LDSHARED": "$CONDA_EMSDK_DIR/upstream/emscripten/emcc " "-L$PREFIX/lib ",
    "LDVERSION": "3.10",
    "LIBC": "",
    "LIBDEST": "$PREFIX/lib/python3.10",
    "LIBDIR": "$PREFIX/lib",
    "LIBFFI_INCLUDEDIR": "",
    "LIBM": "-lm",
    "LIBOBJDIR": "Python/",
    "LIBOBJS": "",
    "LIBPC": "$PREFIX/lib/pkgconfig",
    "LIBPL": "$PREFIX/lib/python3.10/config-3.10",
    "LIBPYTHON": "",
    "LIBRARY": "libpython3.10.a",
    "LIBRARY_DEPS": "libpython3.10.a",
    "LIBRARY_OBJS": "\\",
    "LIBRARY_OBJS_OMIT_FROZEN": "\\",
    "LIBS": "-ldl  -lm",
    "LIBSUBDIRS": "asyncio \\",
    "LINKCC": "$CONDA_EMSDK_DIR/upstream/emscripten/emcc",
    "LINKFORSHARED": "",
    "LIPO_32BIT_FLAGS": "",
    "LIPO_INTEL64_FLAGS": "",
    "LLVM_PROF_ERR": "no",
    "LLVM_PROF_FILE": "",
    "LLVM_PROF_MERGER": "",
    "LN": "ln",
    "LOCALMODLIBS": "-DHAVE_FFI_PREP_CIF_VAR=1 -DHAVE_FFI_PREP_CLOSURE_LOC=1 "
    "-DHAVE_FFI_CLOSURE_ALLOC=1                 -lsqlite3   -lbz2",
    "MACHDEP": "emscripten",
    "MACHDEP_OBJS": "",
    "MACHDESTLIB": "$PREFIX/lib/python3.10",
    "MACOSX_DEPLOYMENT_TARGET": "",
    "MAINCC": "$CONDA_EMSDK_DIR/upstream/emscripten/emcc",
    "MAJOR_IN_MKDEV": 0,
    "MAJOR_IN_SYSMACROS": 1,
    "MAKESETUP": "./Modules/makesetup",
    "MANDIR": "$PREFIX/share/man",
    "MKDIR_P": "/usr/bin/mkdir -p",
    "MODBUILT_NAMES": "array  audioop  math  cmath  _contextvars  _struct  "
    "_random  _bisect  _datetime  _heapq  _json  _csv  _ctypes  "
    "_ctypes_test  unicodedata  _pickle  _socket  select  "
    "_posixsubprocess  binascii  zlib  pyexpat  _sha1  _sha256  "
    "_sha512  _sha3  _md5  _blake2  _sqlite3  _crypt  _bz2  "
    "_queue  _multibytecodec  _codecs_cn  _codecs_hk  "
    "_codecs_iso2022  _codecs_jp  _codecs_kr  _codecs_tw  "
    "_lsprof  _decimal  mmap  _xxsubinterpreters  posix  errno  "
    "_sre  _codecs  _weakref  _functools  _operator  "
    "_collections  _abc  itertools  atexit  _signal  _stat  "
    "time  _thread  _locale  _io  faulthandler  _tracemalloc  "
    "_symtable  xxsubtype",
    "MODDISABLED_NAMES": "",
    "MODLIBS": "-DHAVE_FFI_PREP_CIF_VAR=1 -DHAVE_FFI_PREP_CLOSURE_LOC=1 "
    "-DHAVE_FFI_CLOSURE_ALLOC=1                 -lsqlite3   -lbz2",
    "MODOBJS": "Modules/arraymodule.o  Modules/audioop.o  Modules/mathmodule.o "
    "Modules/_math.o  Modules/cmathmodule.o  "
    "Modules/_contextvarsmodule.o  Modules/_struct.o  "
    "Modules/_randommodule.o  Modules/_bisectmodule.o  "
    "Modules/_datetimemodule.o  Modules/_heapqmodule.o  "
    "Modules/_json.o  Modules/_csv.o  Modules/_ctypes.o "
    "Modules/callbacks.o Modules/callproc.o Modules/cfield.o "
    "Modules/stgdict.o  Modules/_ctypes_test.o  Modules/unicodedata.o  "
    "Modules/_pickle.o  Modules/socketmodule.o  "
    "Modules/selectmodule.o  Modules/_posixsubprocess.o  "
    "Modules/binascii.o  Modules/zlibmodule.o  Modules/xmlparse.o "
    "Modules/xmlrole.o Modules/xmltok.o Modules/pyexpat.o  "
    "Modules/sha1module.o  Modules/sha256module.o  "
    "Modules/sha512module.o  Modules/sha3module.o  "
    "Modules/md5module.o  Modules/blake2module.o "
    "Modules/blake2b_impl.o Modules/blake2s_impl.o  Modules/cache.o "
    "Modules/connection.o Modules/cursor.o Modules/microprotocols.o "
    "Modules/module.o Modules/prepare_protocol.o Modules/row.o "
    "Modules/statement.o Modules/util.o  Modules/_cryptmodule.o  "
    "Modules/_bz2module.o  Modules/_queuemodule.o  "
    "Modules/multibytecodec.o  Modules/_codecs_cn.o  "
    "Modules/_codecs_hk.o  Modules/_codecs_iso2022.o  "
    "Modules/_codecs_jp.o  Modules/_codecs_kr.o  Modules/_codecs_tw.o  "
    "Modules/_lsprof.o Modules/rotatingtree.o  Modules/_decimal.o "
    "Modules/basearith.o Modules/constants.o Modules/context.o "
    "Modules/convolute.o Modules/crt.o Modules/difradix2.o "
    "Modules/fnt.o Modules/fourstep.o Modules/io.o Modules/mpalloc.o "
    "Modules/mpdecimal.o Modules/numbertheory.o Modules/sixstep.o "
    "Modules/transpose.o  Modules/mmapmodule.o  "
    "Modules/_xxsubinterpretersmodule.o  Modules/posixmodule.o  "
    "Modules/errnomodule.o  Modules/_sre.o  Modules/_codecsmodule.o  "
    "Modules/_weakref.o  Modules/_functoolsmodule.o  "
    "Modules/_operator.o  Modules/_collectionsmodule.o  "
    "Modules/_abc.o  Modules/itertoolsmodule.o  "
    "Modules/atexitmodule.o  Modules/signalmodule.o  Modules/_stat.o  "
    "Modules/timemodule.o  Modules/_threadmodule.o  "
    "Modules/_localemodule.o  Modules/_iomodule.o Modules/iobase.o "
    "Modules/fileio.o Modules/bytesio.o Modules/bufferedio.o "
    "Modules/textio.o Modules/stringio.o  Modules/faulthandler.o  "
    "Modules/_tracemalloc.o  Modules/symtablemodule.o  "
    "Modules/xxsubtype.o",
    "MODULE_OBJS": "\\",
    "MULTIARCH": "",
    "MULTIARCH_CPPFLAGS": "",
    "MVWDELCH_IS_EXPRESSION": 0,
    "NO_AS_NEEDED": "",
    "OBJECT_OBJS": "\\",
    "OPENSSL_INCLUDES": "-I/usr/include",
    "OPENSSL_LDFLAGS": "-L/usr/lib",
    "OPENSSL_LIBS": "-lssl -lcrypto",
    "OPENSSL_RPATH": "",
    "OPT": "-DNDEBUG -g -fwrapv -O3 -Wall",
    "OTHER_LIBTOOL_OPT": "",
    "PACKAGE_BUGREPORT": 0,
    "PACKAGE_NAME": 0,
    "PACKAGE_STRING": 0,
    "PACKAGE_TARNAME": 0,
    "PACKAGE_URL": 0,
    "PACKAGE_VERSION": 0,
    "PARSER_HEADERS": "\\",
    "PARSER_OBJS": "\\ \\ Parser/myreadline.o Parser/tokenizer.o",
    "PEGEN_HEADERS": "\\",
    "PEGEN_OBJS": "\\",
    "PGO_PROF_GEN_FLAG": "",
    "PGO_PROF_USE_FLAG": "",
    "PLATLIBDIR": "lib",
    "POBJS": "\\",
    "POSIX_SEMAPHORES_NOT_ENABLED": 0,
    "PROFILE_TASK": "-m test --pgo --timeout=1200",
    "PTHREAD_KEY_T_IS_COMPATIBLE_WITH_INT": 1,
    "PTHREAD_SYSTEM_SCHED_SUPPORTED": 0,
    "PURIFY": "",
    "PY3LIBRARY": "",
    "PYLONG_BITS_IN_DIGIT": 30,
    "PYTHON": "python",
    "PYTHONFRAMEWORK": "",
    "PYTHONFRAMEWORKDIR": "no-framework",
    "PYTHONFRAMEWORKINSTALLDIR": "",
    "PYTHONFRAMEWORKPREFIX": "",
    "PYTHONPATH": "",
    "PYTHON_FOR_BUILD": "_PYTHON_PROJECT_BASE=$PREFIX/conda-bld/python_1649414357931/work "
    "_PYTHON_HOST_PLATFORM=$(_PYTHON_HOST_PLATFORM) "
    "PYTHONPATH=$(shell test -f pybuilddir.txt && echo "
    "$PREFIX/conda-bld/python_1649414357931/work/`cat "
    "pybuilddir.txt`:)./Lib "
    "_PYTHON_SYSCONFIGDATA_NAME=_sysconfigdata__emscripten_ "
    "python3.10",
    "PYTHON_FOR_REGEN": "",
    "PYTHON_HEADERS": "\\",
    "PYTHON_OBJS": "\\",
    "PY_BUILTIN_HASHLIB_HASHES": '"md5,sha1,sha256,sha512,sha3,blake2"',
    "PY_BUILTIN_MODULE_CFLAGS": "-Wno-unused-result -Wsign-compare "
    "-Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall "
    "-g0 -g0 -fPIC -fdiagnostics-color=always "
    "-std=c99 -Wextra -Wno-unused-result "
    "-Wno-unused-parameter "
    "-Wno-missing-field-initializers "
    "-Wstrict-prototypes "
    "-Werror=implicit-function-declaration "
    "-fvisibility=hidden  -I./Include/internal -I. "
    "-I./Include "
    "-I$PREFIX/include "
    "-DPy_BUILD_CORE_BUILTIN",
    "PY_CFLAGS": "-Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG "
    "-g -fwrapv -O3 -Wall -g0 -g0 -fPIC -fdiagnostics-color=always",
    "PY_CFLAGS_NODIST": "-std=c99 -Wextra -Wno-unused-result "
    "-Wno-unused-parameter -Wno-missing-field-initializers "
    "-Wstrict-prototypes "
    "-Werror=implicit-function-declaration "
    "-fvisibility=hidden  -I./Include/internal",
    "PY_COERCE_C_LOCALE": 1,
    "PY_CORE_CFLAGS": "-Wno-unused-result -Wsign-compare -Wunreachable-code "
    "-DNDEBUG -g -fwrapv -O3 -Wall -g0 -g0 -fPIC "
    "-fdiagnostics-color=always -std=c99 -Wextra "
    "-Wno-unused-result -Wno-unused-parameter "
    "-Wno-missing-field-initializers -Wstrict-prototypes "
    "-Werror=implicit-function-declaration -fvisibility=hidden  "
    "-I./Include/internal -I. -I./Include "
    "-I$PREFIX/include "
    "-DPy_BUILD_CORE",
    "PY_CORE_LDFLAGS": "-L$PREFIX/lib ",
    "PY_CPPFLAGS": "-I. -I./Include " "-I$PREFIX/include",
    "PY_ENABLE_SHARED": 0,
    "PY_FORMAT_SIZE_T": '"z"',
    "PY_LDFLAGS": "-L$PREFIX/lib ",
    "PY_LDFLAGS_NODIST": "",
    "PY_SSL_DEFAULT_CIPHERS": 1,
    "PY_SSL_DEFAULT_CIPHER_STRING": 0,
    "PY_STDMODULE_CFLAGS": "-Wno-unused-result -Wsign-compare -Wunreachable-code "
    "-DNDEBUG -g -fwrapv -O3 -Wall -g0 -g0 -fPIC "
    "-fdiagnostics-color=always -std=c99 -Wextra "
    "-Wno-unused-result -Wno-unused-parameter "
    "-Wno-missing-field-initializers -Wstrict-prototypes "
    "-Werror=implicit-function-declaration "
    "-fvisibility=hidden  -I./Include/internal -I. "
    "-I./Include "
    "-I$PREFIX/include",
    "Py_DEBUG": 0,
    "Py_ENABLE_SHARED": 0,
    "Py_HASH_ALGORITHM": 0,
    "Py_TRACE_REFS": 0,
    "QUICKTESTOPTS": "-x test_subprocess test_io test_lib2to3 \\",
    "READELF": "true",
    "RESSRCDIR": "Mac/Resources/framework",
    "RETSIGTYPE": "void",
    "RUNSHARED": "",
    "SCRIPTDIR": "$PREFIX/lib",
    "SETPGRP_HAVE_ARG": 0,
    "SHELL": "/bin/sh",
    "SHLIBS": "-ldl  -lm",
    "SHLIB_SUFFIX": ".so",
    "SHM_NEEDS_LIBRT": 0,
    "SIGNED_RIGHT_SHIFT_ZERO_FILLS": 0,
    "SITEPATH": "",
    "SIZEOF_DOUBLE": 8,
    "SIZEOF_FLOAT": 4,
    "SIZEOF_FPOS_T": 16,
    "SIZEOF_INT": 4,
    "SIZEOF_LONG": 4,
    "SIZEOF_LONG_DOUBLE": 16,
    "SIZEOF_LONG_LONG": 8,
    "SIZEOF_OFF_T": 8,
    "SIZEOF_PID_T": 4,
    "SIZEOF_PTHREAD_KEY_T": 4,
    "SIZEOF_PTHREAD_T": 4,
    "SIZEOF_SHORT": 2,
    "SIZEOF_SIZE_T": 4,
    "SIZEOF_TIME_T": 4,
    "SIZEOF_UINTPTR_T": 4,
    "SIZEOF_VOID_P": 4,
    "SIZEOF_WCHAR_T": 4,
    "SIZEOF__BOOL": 1,
    "SOABI": "cpython-310",
    "SQLITEMODULENAME": "MODULE_NAME='\"sqlite\"'",
    "SRCDIRS": "Parser Objects Python Modules Modules/_io Programs",
    "SRC_GDB_HOOKS": "./Tools/gdb/libpython.py",
    "STATIC_LIBPYTHON": 1,
    "STDC_HEADERS": 1,
    "STRICT_SYSV_CURSES": "/* Don't use ncurses extensions */",
    "STRIPFLAG": "-s",
    "SUBDIRS": "",
    "SUBDIRSTOO": "Include Lib Misc",
    "SYSLIBS": "-lm",
    "SYS_SELECT_WITH_SYS_TIME": 1,
    "TCLTK_INCLUDES": "",
    "TCLTK_LIBS": "",
    "TESTOPTS": "",
    "TESTPATH": "",
    "TESTPYTHON": "./python",
    "TESTPYTHONOPTS": "",
    "TESTRUNNER": "./python ./Tools/scripts/run_tests.py",
    "TESTSUBDIRS": "ctypes/test \\",
    "TESTTIMEOUT": 1200,
    "TEST_MODULES": "yes",
    "THREAD_STACK_SIZE": 0,
    "TIMEMODULE_LIB": 0,
    "TIME_WITH_SYS_TIME": 1,
    "TM_IN_SYS_TIME": 0,
    "TZPATH": "/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/zoneinfo",
    "UNICODE_DEPS": "\\",
    "UNIVERSALSDK": "",
    "UPDATE_FILE": "./Tools/scripts/update_file.py",
    "USE_COMPUTED_GOTOS": 0,
    "VERSION": "3.10",
    "WHEEL_PKG_DIR": "",
    "WINDOW_HAS_FLAGS": 0,
    "WITH_DECIMAL_CONTEXTVAR": 1,
    "WITH_DOC_STRINGS": 1,
    "WITH_DTRACE": 0,
    "WITH_DYLD": 0,
    "WITH_EDITLINE": 0,
    "WITH_LIBINTL": 0,
    "WITH_NEXT_FRAMEWORK": 0,
    "WITH_PYMALLOC": 0,
    "WITH_VALGRIND": 0,
    "X87_DOUBLE_ROUNDING": 0,
    "XMLLIBSUBDIRS": "xml xml/dom xml/etree xml/parsers xml/sax",
    "abs_builddir": "$PREFIX/conda-bld/python_1649414357931/work",
    "abs_srcdir": "$PREFIX/conda-bld/python_1649414357931/work",
    "datarootdir": "$PREFIX/share",
    "exec_prefix": "/home/derthorsten/micromamba/envs/emforgetest",
    "prefix": "/home/derthorsten/micromamba/envs/emforgetest",
}
