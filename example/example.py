import oidn_denoiser
reload(oidn_denoiser)


beauty = "car_beauty.jpg"
albedo = "car_albedo.jpg"
normal = "car_normal.jpg"
output = "car_denoised.png"


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
