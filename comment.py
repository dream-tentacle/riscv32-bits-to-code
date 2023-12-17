from utils import getrules, explain, codes

rules = getrules(codes)

import os

load_path = "./src/"
save_path = "./output/"
for filename in os.listdir(load_path):
    file_path = load_path + filename
    if os.path.isfile(file_path) and not (
        file_path[-5] <= "9" and file_path[-5] >= "0"
    ):
        f = open(file_path, "r")
        content = f.readlines()
        f.close()
        f = open(save_path + filename, "w")
        current_line = 0
        for line in content:
            if line[0] == "@":
                f.write(line)
                current_line = int(line[1:], base=16)
                continue
            wr = f"{line[:-1]}  // 0x{hex(current_line)} {explain(rules, line)}"
            current_line += 4
            f.write(wr + "\n")
