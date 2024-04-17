import os
base_path = './GPT_SoVITS'
os.system(f'git clone https://code.openxlab.org.cn/alexw/pretrained_models.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
os.system('streamlit run app.py')
