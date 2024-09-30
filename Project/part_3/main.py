import torch

# 检查CUDA（即GPU）是否可用
if torch.cuda.is_available():
    print("CUDA (GPU) 可用！")
    # 获取GPU数量和型号名称
    print(f"GPU数量: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA (GPU) 不可用。")
