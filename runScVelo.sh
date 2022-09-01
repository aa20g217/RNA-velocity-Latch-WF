module load Anaconda3
source activate velocyto

#"Radial glia 1,Radial glia 2,Neuroblast,Immature Neuron 1,Immature Neuron 2,Neuron 1,Neuron 2"
papermill runScVelo.ipynb Report.ipynb -p fieName $1 -p clusters "$2" -p basis $3 
jupyter nbconvert --no-input --to html Report.ipynb 
cp Report.html ./figures/
