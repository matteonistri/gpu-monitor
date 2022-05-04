#! /bin/sh

 nsys launch -w true -t cuda,nvtx,cublas,cublas-verbose,cusparse,cusparse-verbose,cudnn,opengl,opengl-annotations,openacc,openmp,osrt,mpi,nvvideo,vulkan,vulkan-annotations,oshmem,ucx python -u pytorch_ART.py --attacks_library ./SAIS/ --home $HOME/gpu-monitor/ --full_iterations 1