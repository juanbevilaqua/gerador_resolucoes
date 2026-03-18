import yaml
import os
import sys

def _base_path():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.getcwd()

def carregar_config():
    base_path = _base_path()

    config_path = os.path.join(base_path, "src", "config", "configs.yaml")

    with open(config_path, "r", encoding="utf-8") as file:
        file_parts = list(yaml.safe_load_all(file))

    # resolve automaticamente o modelo base
    file_parts[0]['timbre_res'] = os.path.join(
        base_path,
        file_parts[0]['timbre_res']
    )

    return file_parts