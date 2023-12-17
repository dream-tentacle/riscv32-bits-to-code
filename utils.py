# rule example:
# rules = [
#     {"pattern":"?????????????????????????0110111", # no space
#      "instr_name":"lui",
#      "instr_type":"U",
#      "instr_content":"R(rd)=imm"
#     }
# ]
def getrules(codes):
    lines = codes.replace("\n", "").replace(" ", "").split("INSTPAT")
    rules = []
    for line in lines:
        if len(line.split(",")) < 4:
            continue
        rules.append({})
        rule = rules[-1]
        objects = line.split(",")
        rule["pattern"] = objects[0].split('"')[1].replace(" ", "")
        rule["instr_name"] = objects[1].strip()
        rule["instr_type"] = objects[2].strip()
        rule["instr_content"] = ")".join(",".join(objects[3:]).split(")")[:-1])
    return rules


def explain(rules, x, base=16):
    x = int(x, base=base)
    x = str(bin(x))[2:]
    x = (32 - len(x)) * "0" + x
    for rule in rules:
        flag = True
        for bit in range(len(x)):
            if rule["pattern"][bit] != "?" and rule["pattern"][bit] != x[bit]:
                flag = False
                break
        if not flag:
            continue
        rd = hex(int(x[20:25], base=2))
        rs1 = hex(int(x[12:17], base=2))
        rs2 = hex(int(x[7:12], base=2))
        imm = ""
        if rule["instr_type"] == "I":
            imm = x[0:12]
        elif rule["instr_type"] == "U":
            imm = x[0:20] + "0" * 12
        elif rule["instr_type"] == "S":
            imm = x[0:7] + x[20:25]
        elif rule["instr_type"] == "J":
            imm = x[0] + x[12:20] + x[11] + x[1:11] + "0"
        elif rule["instr_type"] == "B":
            imm = x[0] + x[24] + x[1:7] + x[20:24] + "0"
        if imm != "":
            # 如果字符串以 "1" 开头，表示是负数的补码
            if imm[0] == "1":
                # 计算负数的补码
                imm = bin(int(imm, 2) - (1 << len(imm)))
                # 将二进制补码字符串转换为整数
            imm = int(imm, 2)
            imm = hex(imm)
        else:
            imm = "type_error"
        replace_list = [
            ["(rd)", f"({rd})"],
            ["rs1", f"{rs1}"],
            ["rs2", f"{rs2}"],
            ["src1", f"R({rs1})"],
            ["src2", f"R({rs2})"],
            ["imm", f"imm(={imm})"],
        ]
        re = rule["instr_content"]
        for replace_item in replace_list:
            re = re.replace(replace_item[0], replace_item[1])
        return rule["instr_name"] + ", " + re
    return "NO PATTERN"


try:
    with open("./nemu_instr.txt", "r") as file:
        codes = file.read()
except:
    print(
        "Error: unable to read the file ./nemu_instr.txt. Make sure you add your code into this file"
    )
