
import os, sys
import yaml

def read_config(cfg_dir):
    print('\n Reading configurations...', flush=True)

    io_setting    = os.path.join(cfg_dir, "IO.yml")
    param_setting = os.path.join(cfg_dir, "param_meta.yml")
    tf_setting    = os.path.join(cfg_dir, "tf_coef.yml")

    with open(io_setting, "r") as ymlfile:
        io_cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    with open(param_setting, "r") as ymlfile:
        par_cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    with open(tf_setting, "r") as ymlfile:
        tf_cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    # some checking consistency among operations. e.g.,  if not compute, obviously not write not scale
    for key, dic in par_cfg['param'].items():
        if not dic['compute']:
            par_cfg['param'][key]['write'] = False
            par_cfg['param'][key]['vertical_scale'] = False
            par_cfg['param'][key]['horizontal_scale'] = False

    return io_cfg, par_cfg, tf_cfg
