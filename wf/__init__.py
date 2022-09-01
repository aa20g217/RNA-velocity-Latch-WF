"""
RNA velocity analysis in single cells with scVelo.
"""


import subprocess
from pathlib import Path

from flytekit import LaunchPlan, workflow
from latch.types import LatchDir,LatchFile
from latch import large_task

@large_task
def runScript(inputDir: LatchFile,output_dir: LatchDir,clusterName: str="Clusters",embedding: str="umap") -> LatchDir:
    subprocess.run(
        [
            "sh",
            "runScVelo.sh",
            inputDir.local_path,
            clusterName,
            embedding
        ]
    )
    local_output_dir = str(Path("/root/figures").resolve())

    remote_path=output_dir.remote_path
    if remote_path[-1] != "/":
        remote_path += "/"

    return LatchDir(local_output_dir,remote_path)


@workflow
def scVelo_wf(inputDir: LatchFile,output_dir: LatchDir,clusterName: str="Clusters",embedding: str="umap") -> LatchDir:
    """

    RNA velocity analysis in single cells using scVelo
    ----

    `RNA velocity analysis`  allows us to infer transcriptional dynamics that are not directly observed in a scRNA-seq experiment using a mathematical model of transcriptional kinetics. We can use RNA velocity to determine if a gene of interest is being induced or repressed in a give cell population of interest. Moreover, we can extrapolate this information to predict cell fate decision via pseudotime trajectories.

    __metadata__:
        display_name: RNA velocity analysis in single cells
        author:
            name: Akshay
            email: akshaysuhag2511@gmail.com
            github:
        repository:
        license:
            id: MIT

    Args:

        inputDir:
          Select input file. This file should contain matrices of spliced/unspliced reads (from velocyto) as well as row and column attributes.

          __metadata__:
            display_name: Input File

        clusterName:
          A column name in annotation matrix that contains clusters name.

          __metadata__:
            display_name: Column Name

        embedding:
          	Possible options are umap,tsne, and pca.

          __metadata__:
            display_name: Embedding Type

        output_dir:
          Where to save the report and plots?.

          __metadata__:
            display_name: Output Directory
    """
    return runScript(inputDir=inputDir,clusterName=clusterName,embedding=embedding,output_dir=output_dir)
