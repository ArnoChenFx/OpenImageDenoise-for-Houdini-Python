import oidn_denoiser
import os

path = os.path.split(os.path.realpath(__file__))[0]
path = path.replace("\\","/") + "/"

beauty = path + "car_beauty.jpg"
albedo = path + "car_albedo.jpg"
normal = path + "car_normal.jpg"
output = path + "car_denoised.png"


denoiser = oidn_denoiser.denoiser()

denoiser.beauty = beauty
denoiser.albedo = albedo
denoiser.normal = normal
denoiser.output = output

denoiser.set_use_srgb(True)
denoiser.set_use_hdr(False)
denoiser.set_use_affinity(True)
denoiser.set_num_threads(16)
denoiser.set_debug_mode(True)

denoiser.run()
