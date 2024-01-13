import subprocess

'''安装数据集所需全部solc版本'''
def install_all_version(all_versions_list):
    
    for version in  all_versions_list:
        command = f"solc-select install {version}"
        subprocess.run(command, shell=True)

all_versions_list = ['0.5.8', '0.5.1', '0.4.22', '0.5.2', '0.4.23', '0.5.11', '0.5.0', '0.5.10', '0.5.00', '0.5.7', '0.4.21', '0.5.9', '0.5.6']

install_all_version(all_versions_list)