# riscv32-bit-to-code
### Translation Method
To utilize this project, you have to put your `INSTPAT` codes into `./nemu_instr.txt`. If you don't have one, please contact me.
Only the following format content should be added into the file:
```
INSTPAT("??????? ????? ????? ??? ????? 01101 11", lui, U, R(rd) = imm);
```
### comment.py
Add your riscv files (.txt or .hex) to `./src/`, run the code `comment.py`, and you get all the files with comments in `./output/`.

NOTE: This project is built for the digital logic and computer organization course in Nanjing University (NJU). We received some `.hex` files of riscv machine instructions from the teacher.\
There is an example file `./src/add.txt`. You can check whether your file is in the same format. The `@0` in the first line doesn't matter, i.e., you don't need to have this line in your file.

### ask.py
Run this code, type a hex number and click Enter to get the translation of the hex number. Click Enter again to stop, or just enter another hex number.
If you want to change the input base, just modify the `base` variable in the function `explain()`.
