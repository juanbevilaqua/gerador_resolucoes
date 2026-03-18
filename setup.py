import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os",
                                "docx",
                                "pdf2docx",
                                "PyPDF2",
                                "customtkinter",
                                "yaml",
                                "PIL",
                                "pywinstyles",
                                  "src",
                                "src.modelos"],
                     "includes": ["src.modelos.CalendarioReunioes"],

                     "include_files": [("themes", "themes"), ("src/static/img", "src/static/img"),
                                       ("src/database", "src/database"), ("src/config", "src/config"),
                                        ("MODELO papel timbrado FACET.docx", "MODELO papel timbrado FACET.docx")
                                       ]

                     }

# GUI applications require a different base on Windows (the default is for a console application).
base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(
    name="Gerador de Resoluções",
    version="0.1",
    description="Geraador de Resoluções para o PPGCTA/UFGD",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)