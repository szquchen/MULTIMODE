# MULTIMODE

## Indroduction

MULTIMODE is a general code that obtains the ro-vibrational eigenvalues and eigenfunctions of the “Watson Hamilonian” using vibrational self-consistent field and configuration interaction.

## Requirements
* The users need to supply their own potential energy surface, written in Fortran (Or machine-learned potentials that make use of Atomic Simulation Environment, using an interface to be released in the near future)
* The equilibrium structure of the molecule (must be a minimum, optimized with the potential energy surface)
* A Fortran compiler. The version on this site has been tested with Intel and GNU Fortran compiler.

## A Quick Usage Guide -- Command Line version
The source codes are in `mm/src`. A sample potential energy surface for H<sub>2</sub>CO (`h2co_pes.f90` and `user.h2co.f`) are provided.

* Go to `mm/src` and compile the program using the Makefile. To link another potential, use `user.h2co.f` as a template and modify subroutines `USERIN` and `GETPOT`
* Use the MM Helper GUI, `mm/mmhelper.py`, to generate the input file `fort.1`. Below is a screen shot of the GUI. Two sample inputs are provided in `examples`, one uses all the normal modes, and the other uses a subset of normal modes in a reduced-dimensional calculation. Users may also consult `notes/Quick_Start_Guide.pdf` to further modify the input file
* Copy the executable `mm.x` and the input file `fort.1` to directory `mm`, and execute `./mm.x fort.1 fort.2`, where `fort.2` is the name of the output file.
* Wait for program to end and get the result. It will take <1 min to run the H<sub>2</sub>CO example, but may take substantially longer with larger molecules.

<p align="center">
    <img src="https://github.com/szquchen/MULTIMODE/blob/main/mm/mmhelper.png" alt="MM Helper" width="400" height="550">
</p>

## TO-DO-LIST
### Essential

- [ ] Release the interface for Python MLPs

### Optional

- [ ] [Choose a liscence for MM](https://choosealicense.com)

## Credit

### Theory
* Joel M. Bowman
* Stuart Carter

### MM orginial package and documentation
* Stuart Carter

### User-friendly Realization
* Kee (Qingfeng) Wang (https://github.com/Kee-Wang)
* Chen Qu
