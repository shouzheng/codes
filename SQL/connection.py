import yaml
import os

# 加载 YAML 文件
def load_yaml_to_env(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)

    # 遍历 YAML 文件内容，将值注册到环境变量
    for section, values in config.items():
        for key, value in values.items():
            env_key = f"{section.upper()}_{key.upper()}"
            os.environ[env_key] = str(value)

# 调用函数加载 YAML 文件并注册到环境变量，这个文件不会上传，可以参考 .env.yaml.template 文件配置自己的环境变量
load_yaml_to_env('./.env.yaml')

# 创建连接字符串（替换为你的数据库信息）
connection_string = f"postgresql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/{os.environ['DATABASE_DBNAME']}"
