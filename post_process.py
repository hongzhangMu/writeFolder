#-*- coding:utf-8 -*-
import os
import sys
import numpy as np
import ConfigParser

if len(sys.argv) < 6:
    print 'case_id root_folder ori_lst seg_lst naming_lst'
    sys.exit(1)

case_id = sys.argv[1]
root_folder = sys.argv[2]
ori_lst = sys.argv[3]
seg_lst = sys.argv[4]
naming_lst = sys.argv[5]

#创建文件夹
case_folder = os.path.join(root_folder, case_id)
if False == os.path.exists(case_folder):
    os.system('mkdir -p ' + case_folder)


for line in open(naming_lst):

    line = line[0:-1]
    vessel_name = line.split('.')[0]

    vessel_folder = os.path.join(case_folder, vessel_name)

    if False == os.path.exists(vessel_folder):
        os.system('mkdir -p ' + vessel_folder)

    seg_folder = os.path.join(vessel_folder, 'seg') #
    if False == os.path.exists(seg_folder):
        os.system('mkdir -p ' + seg_folder)
        # os.system('ITKbinaryThinningImageFilter3D.exe seg.mha input.mha output.mha centerline.vtp')


    for i in range(36):
        angle_folder = os.path.join(vessel_name, 'shortaxis')
        if False == os.path.exists(angle_folder):
            os.system('mkdir -p ' + angle_folder)
        
        shortaxis_folder = os.path.join(angle_folder, 'shortaxis_', str(i * 10))
        if False == os.path.exists(shortaxis_folder):
            os.system('mkdir -p ' + shortaxis_folder)
            # os.system('ITKbinaryThinningImageFilter3D.exe seg.mha input.mha output.mha centerline.vtp')  


#os.system('ITKbinaryThinningImageFilter3D.exe input.mha output.mha centerline.vtp')      

