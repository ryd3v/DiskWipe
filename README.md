# Disk Wipe

![ALT](https://github.com/ryd3v/DiskWipe/blob/main/Screenshot.png)

Disk Wipe is a versatile tool designed for the secure erasure of storage media on both Windows and Linux operating
systems. By employing robust wiping methods, it ensures that the data on the specified disk is irretrievably deleted,
making it an effective solution for anti-forensic processes. This application offers a user-friendly interface and
real-time progress tracking, making data sanitization accessible and transparent. Please note that the use of Disk Wipe
is at the user's own risk and discretion. It is highly recommended to backup any important data before proceeding with
the wipe operation, as the process is irreversible and could result in permanent data loss.

```bash
pip install -r requirments.txt
```

```bash
pyinstaller --onefile DiskWipe.py
```

## Linux

On Linux it's best to launch from the commandline as your sudo password is required for dc3dd.

----

## DISCLAIMER:

This program is intended for educational purposes and legitimate, authorized disk wiping only. It is provided 'as is',
without warranty of any kind. The author, Ryan Collins, accepts no responsibility or liability for any data loss or
damage that may occur as a result of using this program.

# WARNING:

This program will permanently erase data from the disk specified by the user. Once data has been erased, it may not be
recoverable. Please ensure that you have made adequate backups of any data you wish to keep and have correctly
identified the disk you wish to wipe before proceeding.

By using this program, you acknowledge and accept that:

1. You understand the function of this program and the potential risks involved.
2. You accept full responsibility for any data loss or system damage that may occur as a result of using this program.
3. You will not hold the author, Ryan Collins, or any other parties involved in the creation, distribution, or
   maintenance of this program liable for any data loss or system damage that may occur as a result of using this
   program.
