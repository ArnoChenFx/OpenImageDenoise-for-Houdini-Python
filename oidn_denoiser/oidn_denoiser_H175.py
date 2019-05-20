#conding:utf-8
import ctypes
import os
import ctypes
from ctypes import *


pth = os.path.split(os.path.realpath(__file__))[0]
pth = pth.replace("\\","/")
lib = pth+"/lib"
os.environ['path'] += ';'+lib
dnser = ctypes.CDLL("oidn_denoiser_H175.dll")

class denoiser():
    def __init__(self):
        self.beauty = None
        self.albedo = None
        self.normal = None
        self.output = None
        self.use_hdr=False
        self.use_srgb=False
        self.use_affinity=False
        self.num_threads=0
        self.debug_mode = False

    def run(self):
        str_c1 = c_char_p(bytes(self.beauty))
        str_c2 = c_char_p(bytes(self.albedo))
        str_c3 = c_char_p(bytes(self.normal))
        str_c4 = c_char_p(bytes(self.output))
        c_a = [str_c1, str_c2, str_c3, str_c4]
        c_arr = (c_char_p*4)(*c_a)

        _use_hdr = c_bool(self.use_hdr)
        _use_srgb = c_bool(self.use_hdr)
        _use_affinity = c_bool(self.use_hdr)
        _num_threads = c_int(self.num_threads)
        _debug_mode = c_int(self.debug_mode)
        dnser.denoise(c_arr,_use_hdr,_use_srgb,_use_affinity,_num_threads,_debug_mode)
        
        print "denoise finished"
        
    def set_use_hdr(self,a):
        self.use_hdr = a

    def set_use_srgb(self,a):
        self.use_srgb = a

    def set_use_affinity(self,a):
        self.use_affinity = a

    def set_debug_mode(self,a):
        self.debug_mode = a

    def set_num_threads(self,num):
        self.num_threads = num


