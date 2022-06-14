import sys 

def mask_valid(mask_nums):
    bin_str = ''
    for n in mask_nums:
        bin_str += bin(n)[2:].rjust(8, '0')
#     print(mask_nums, bin_str)
    if "01" in bin_str or "1" not in bin_str or '0' not in bin_str:
        return False
    return True

def process_ip(line, cnts):
    ip,mask = line.split("~")
    
    if ip.startswith("0") or ip.startswith("127"):
        return 0
    if '' in ip.split('.') or '' in mask.split('.'):
        cnts[5] += 1
        return 0
    ip_nums = list(map(int,ip.split(".")))
    mask_nums = list(map(int, mask.split(".")))
    if not mask_valid(mask_nums):
        cnts[5] += 1
        return 0
    if 1 <= ip_nums[0] <= 126:
        cnts[0] += 1
        if ip_nums[0] == 10:
            cnts[6] += 1
    elif 128 <= ip_nums[0] <= 191:
        cnts[1] += 1
        if ip_nums[0] == 172 and 16 <= ip_nums[1] <=31:
            cnts[6] += 1
    elif 192 <= ip_nums[0] <= 223:
        cnts[2] += 1
        if ip_nums[0] == 192 and ip_nums[1] == 168:
            cnts[6] += 1
    elif 224 <= ip_nums[0] <= 239:
        cnts[3] += 1
    elif 240 <= ip_nums[0] <= 255:
        cnts[4] += 1
    else:
        cnts[5] += 1
    
    return 0
    
cnts = [0]*7
for line in sys.stdin:
    a = line.split()
    # test in local, uncomment the following two line
    # if line.startswith("#"):
    #     break
    process_ip(line, cnts)

for c in cnts:
    print(c, end=" ")