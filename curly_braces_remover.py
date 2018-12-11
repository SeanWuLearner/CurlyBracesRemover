
import os

###################################
def remove_curly_braces(line, braces_set):
    ret_str = ''
    copy_start = 0
    for left, right in braces_set:
        ret_str += line[copy_start:left]
        ret_str += line[left+1:right+1]
        copy_start = right+2

    if copy_start < len(line):
        ret_str += line[copy_start :]
    return ret_str

###################################
def match_paired_braces(left_list, right_list):
    ret = []

    j = 0
    for i, val in enumerate(left_list):
        while (j < len(right_list)) and (right_list[j] <= val):
            j += 1

        # check if there is no illegal right braces at all.
        if j == len(right_list) and (right_list[j] <= val):
            break

        if (i+1) < len(left_list): #consider if there is another left braces followed
            if left_list[i+1] < right_list[j]:
                continue
            else:
                ret.append((val, right_list[j]))
        else:
            ret.append((val, right_list[j]))

    return ret # return a list of left-right pair

#######################################
def remove_curly_brasces(fin_name, fout_name):
    ### open input file ###
    fin = open(fin_name, 'r')
    if fin.readable() is False:
        print("open file with read mode fail")
        return False

    ### open output file ###
    if os.path.isfile(fout_name) is True:
        os.remove(fout_name)

    fout = open(fout_name, "wt")
    if fout.writable() is False:
        print("open output file with write mode fail")
        fin.close()
        return False

    ### iterate each line ###
    line_num = 0
    while True:
        line = fin.readline()
        line_num += 1
        if line == '':
            break # exit condition

        #### collect the left braces ####
        left_braces_list = []
        left_hit_idx = str(line).find('{"')
        while left_hit_idx != -1:
            left_braces_list.append(left_hit_idx)
            left_hit_idx = str(line).find('{"', left_hit_idx+1)

        #case: there is no left braces
        if not left_braces_list:
            fout.write(line)
            continue # forward to the next line

        #### collect the right braces ####
        right_braces_list = []
        right_hit_idx = str(line).find('"}')
        while right_hit_idx != -1:
            right_braces_list.append(right_hit_idx)
            right_hit_idx = str(line).find('"}', right_hit_idx+1)

        #case: there is no right braces
        if not right_braces_list:
            fout.write(line)
            continue # forward to the next line

        #### there are both left and right braces in this line ####
        enclosed_set = match_paired_braces(left_braces_list, right_braces_list)
        mod_line = remove_curly_braces(line, enclosed_set)
        fout.write(mod_line)

    print('write file complete')
    fin.close()
    fout.close()
    return True

#######################################
def main():
    fin_name = 'input_test.txt'
    fout_name = 'output.txt'
    remove_curly_brasces(fin_name, fout_name)



######### my testint code ########################
def main2():

    ### EXP: tuple access ###
    #left = [(1,2), (3,4)]
    #for a,b in left:
    #    print(f'a={a}, b={b}')

    #print(a)
    #print(b)

    ### EXP: string ###
    #str = "0123456789"
    #str2 = str[5:]
    #print(str2)
    #print(len(str))

    #str += "rrr"
    #print(str)

    ### write file test ###
    #fout = open('test.txt', 'wt')
    #fout.write('123')
    #fout.write('456')
    #fout.flush()
    #fout.close()

    ### EXP list ###
    my_list = []
    if not my_list:
        print('my list is empty')
    else:
        print('my list is not empty')

####### module entry #################
if __name__ == '__main__':
    main2()
