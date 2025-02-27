# !/usr/bin/env python
# _*_ coding utf-8 _*_
# @Time: 2025/1/4 17:05
# @Author: Luke Ewin
# @Redir By Paul Yu 2025/02/27
# @Blog: https://blog.lukeewin.top

import os
from modelscope import snapshot_download

# 定义目标路径为当前目录下的 models 文件夹
target_dir = os.path.join(os.getcwd(), "models")  # 关键：目录名改为 models
os.makedirs(target_dir, exist_ok=True)  # 自动创建目录

# 下载模型并指定保存路径
model_names = [
    'iic/speech_campplus_sv_zh-cn_16k-common',
    'iic/speech_fsmn_vad_zh-cn-16k-common-pytorch',
    'iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch',
    'iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch'
]

# 直接保存到 models 目录
for name in model_names:
    model_path = snapshot_download(name, cache_dir=target_dir)
