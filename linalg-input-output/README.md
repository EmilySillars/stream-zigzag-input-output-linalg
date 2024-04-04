# linalg --> stream/zigzag --> linalg



# Hackathon In-Progress Work (will refine this section later)

```
Matrix Multiplication as linalg ---> Stream ---> Stream Output ---> Manually Transformed linalg
```

Input linalg: [matmul.mlir](matmul.mlir)

Input python workload: [matmul-as-python-workload.py](inputs/workload/matmul-as-python-workload.py)

Run on Stream:

```
python main_stream.py --model inputs.workload.convolution-for-zigzag2 --accelerator inputs.hardware.c_k --mapping inputs.mapping.mapping_c_k
```

```
python optimal-latency.py --model inputs.workload.convolution-for-zigzag2 --accelerator inputs.hardware.c_k --mapping inputs.mapping.mapping_c_k


```

## feed output of tool into stream

```
python
import stream
accelerator = "inputs.testing.hardware.dual_testing_core_offchip"
workload = "inputs.testing.workload.testing_workload_for_2_cores"
mapping = "inputs.testing.mapping.testing_mapping"
stream.api.get_hardware_performance_stream("inputs.hardware.snax_gemm", "workload","inputs.hardware.mapping_c_k",0,0,0) 

[("OY", "all")]

stream.api.get_hardware_performance_stream("inputs.hardware.snax_gemm", "workload","inputs.hardware.mapping_c_k",1,[],"blah")

stream.api.get_hardware_performance_stream("inputs.hardware.snax_gemm", "workload","inputs.hardware.mapping_c_k",1,[("OY", "all")],"blah")

linalg-input-output/inputs/examples/hardware/snax_gemm.py

stream.api.get_hardware_performance_stream("inputs/examples/hardware/snax_gemm", "workload","inputs.hardware.mapping_c_k",1,[("OY", "all")],"blah")

```





```
python xdsl_opt_main.py tests/matmul.mlir -p linalg-to-stream &&
python main_stream.py --model workload --accelerator inputs.hardware.snax_gemm --mapping inputs.mapping_c_k
```



```
python main_stream.py --model inputs.workload.convolution-for-zigzag2 --accelerator inputs.hardware.c_k --mapping inputs.mapping.mapping_c_k
```

