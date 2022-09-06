# RNA velocity analysis
#### **Summary**
RNA velocity analysis allows us to infer transcriptional dynamics that are not directly observed in a scRNA-seq experiment using a mathematical model of transcriptional kinetics. We can use RNA velocity to determine if a gene of interest is being induced or repressed in a give cell population of interest. Moreover, we can extrapolate this information to predict cell fate decision via pseudotime trajectories.

#### **Input**
A loom or h5ad file containing spliced/unspliced read counts matrix(from velocyto http://velocyto.org/). In addition, clustering information should be available in the annotation matrix of the given file.

#### **Output**
An HTML report with RNA velocity analysis results. In addition, a folder with publication-ready plots.

#### **Latch wf link**
https://console.latch.bio/explore/67620/info
