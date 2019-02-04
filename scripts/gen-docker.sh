python generator/generate.py docker/Dockerfile.tensorflow-py36-cpu tensorflow python==3.6
python generator/generate.py docker/Dockerfile.keras-py36-cpu keras python==3.6
python generator/generate.py docker/Dockerfile.pytorch-py36-cpu pytorch python==3.6
python generator/generate.py docker/Dockerfile.caffe-py36-cpu caffe python==3.6
python generator/generate.py docker/Dockerfile.torch-py36-cpu torch python==3.6
python generator/generate.py docker/Dockerfile.all-jupyter-py36-cpu tensorflow keras pytorch caffe torch python==3.6 gdal_shapely pymssql pyhive
python generator/generate.py docker/Dockerfile.tensorflow-py36-cu90 tensorflow python==3.6 --cuda-ver 9.0 --cudnn-ver 7
python generator/generate.py docker/Dockerfile.keras-py36-cu90 keras python==3.6 --cuda-ver 9.0 --cudnn-ver 7
python generator/generate.py docker/Dockerfile.pytorch-py36-cu90 pytorch python==3.6 --cuda-ver 9.0 --cudnn-ver 7
python generator/generate.py docker/Dockerfile.caffe-py36-cu90 caffe python==3.6 --cuda-ver 9.0 --cudnn-ver 7
python generator/generate.py docker/Dockerfile.torch-py36-cu90 torch python==3.6 --cuda-ver 9.0 --cudnn-ver 7
python generator/generate.py docker/Dockerfile.all-jupyter-py36-cu90 tensorflow keras pytorch caffe torch python==3.6 gdal_shapely pymssql pyhive --cuda-ver 9.0 --cudnn-ver 7
