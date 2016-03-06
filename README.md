# pyPackageProject
Package a VHDL project as an Vivado IP. Ability to detect interfaces as AXI 4, AXI 4 Lite, ..


## Usage
    Use: python pyPackage.py [-opts] [cmd [args]]
    
    Options:
    -help   Display the options and the usage of this script.
    -top    Path of the VHDL top.
    -out    Path of the IP output.
    -tcl    Export a Vivado tcl script.

## to-do list

- [ ] Args
- [ ] Auto-detect some interfaces
- [ ] Export the TCL Script
- [ ] Execute the TCL Script
