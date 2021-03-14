# 2021-3-14

#coding=utf-8

import sys
import numpy as np

def main():
    # to read standard input
    dataset1 = np.loadtxt(r'F:\校外项目\2021华为软件精英挑战赛\training-data\training-1.txt', dtype=int, comments='(')  # read the dataset
    amount_host = dataset1[0]  # The amount of the available hosts
    amount_vm = dataset1[1]  # The amount of the vm on sale
    amount_seq = dataset1[2]  # The amount of sequence in total
    amount_seq_each_day = dataset1[3:]  # The amount of sequence in each day
    print(amount_host)
    print(amount_vm)
    print(amount_seq)
    print(amount_seq_each_day)
    # process
    # to write standard output
    sys.stdout.flush()


if __name__ == "__main__":
    main()

