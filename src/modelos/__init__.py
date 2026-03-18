import os
import importlib
import sys

# IMPORTAÇÃO AUTOMÁTICA DE TODOS OS MODELOS DISPONÍVEIS

# pega o diretório atual (pasta "modelos")
package_dir = os.path.dirname(__file__)
package_name = __name__

for filename in os.listdir(package_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]  # tira o ".py"

        full_module_name = f"{package_name}.{module_name}"
        module = importlib.import_module(full_module_name)

        #globals()[module_name] = module
        setattr(sys.modules[package_name], module_name, module)
