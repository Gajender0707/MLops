import os 
from pathlib import Path

list_of_files=[

    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaulation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "init_setup.sh",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"

]

for files in list_of_files:
    files=Path(files)
    filedir,filename=os.path.split(files)
    # print(os.path.split(files))

    if filedir!="":
        print(filedir)
        os.makedirs(filedir,exist_ok=True)

    if not os.path.exists(files):
        with open(files,"w") as f:
            pass
