# linalg --> stream/zigzag --> linalg



# Hackathon In-Progress Work (will refine this section later)

```
Matrix Multiplication as linalg ---> Stream ---> Stream Output ---> Manually Transformed linalg
```

Input linalg: [matmul.mlir](matmul.mlir)

Input python workload: [workload.py](inputs/workload/workload.py)

**Running on Stream Errors:**

1) tried `python main_stream.py` but getting error from workload definition
```
2024-04-04 10:24:24,586 - zigzag.classes.io.accelerator.parser.parse_accelerator_from_path +52 - INFO - Parsed accelerator with cores [1].
2024-04-04 10:24:24,587 - stream.classes.workload.dnn_workload.__init__ +67 - INFO - Parsed layer node default_0 | INPUT ['the_first_input'] | OUTPUT ['default_0_output']
Traceback (most recent call last):
  File "/home/emily/stream-zigzag-input-output-linalg/main_stream.py", line 99, in <module>
    scme, _ = mainstage.run()
  File "/home/emily/.local/lib/python3.10/site-packages/zigzag/classes/stages/Stage.py", line 49, in run
    for cme, extra_info in self.list_of_callables[0](
  File "/home/emily/.local/lib/python3.10/site-packages/zigzag/classes/stages/MainInputParserStages.py", line 21, in run
    for cme, extra_info in sub_stage.run():
  File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/stages/ModelParserStage.py", line 83, in run
    workload = parse_workload_from_path(
  File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/stages/ModelParserStage.py", line 65, in parse_workload_from_path
    workload = DNNWorkload(workload, mapping, accelerator)
  File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/workload/dnn_workload.py", line 73, in __init__
    layer_node = ComputationNode(
  File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/workload/computation_node.py", line 44, in __init__
    LayerNode.__init__(self, node_id, node_attrs, node_name)
  File "/home/emily/.local/lib/python3.10/site-packages/zigzag/classes/workload/layer_node.py", line 111, in __init__
    self.memory_operand_links = memory_operand_links.copy()
AttributeError: 'NoneType' object has no attribute 'copy'
```
2. Tried `python main_stream.py` with `workload_path = "stream.inputs.testing.workload.testing_workload_for_1_core"` but getting error from accelerator/hardware definition

   ```
   emily@ProfessorPlum:~/stream-zigzag-input-output-linalg$ python main_stream.py
   2024-04-04 10:40:47,134 - zigzag.classes.io.accelerator.parser.parse_accelerator_from_path +52 - INFO - Parsed accelerator with cores [1].
   2024-04-04 10:40:47,135 - stream.classes.workload.dnn_workload.__init__ +67 - INFO - Parsed layer node layer_on_core0_0 | INPUT ['the_first_input'] | OUTPUT ['layer_on_core0_0_output']
   2024-04-04 10:40:47,135 - stream.classes.workload.dnn_workload.__init__ +67 - INFO - Parsed layer node layer_on_core0_1 | INPUT ['layer_on_core0_0_output'] | OUTPUT ['layer_on_core0_1_output']
   2024-04-04 10:40:47,135 - stream.classes.workload.dnn_workload.__init__ +67 - INFO - Parsed layer node layer_on_core0_2 | INPUT ['layer_on_core0_1_output'] | OUTPUT ['layer_on_core0_2_output']
   2024-04-04 10:40:47,136 - stream.classes.workload.dnn_workload.__init__ +67 - INFO - Parsed layer node layer_on_core0_3 | INPUT ['layer_on_core0_2_output'] | OUTPUT ['layer_on_core0_3_output']
   2024-04-04 10:40:47,136 - stream.classes.stages.ModelParserStage.parse_workload_from_path +66 - INFO - Created workload graph with 4 nodes and 3 edges.
   2024-04-04 10:40:47,136 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +89 - INFO - ComputationNode(0,): Outer loops [TemporalLoop(OY,7)].
   2024-04-04 10:40:47,136 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +90 - INFO - ComputationNode(0,): Generated 7 finer nodes.
   2024-04-04 10:40:47,137 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +89 - INFO - ComputationNode(1,): Outer loops [TemporalLoop(OY,5)].
   2024-04-04 10:40:47,137 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +90 - INFO - ComputationNode(1,): Generated 5 finer nodes.
   2024-04-04 10:40:47,137 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +89 - INFO - ComputationNode(2,): Outer loops [TemporalLoop(OY,5)].
   2024-04-04 10:40:47,138 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +90 - INFO - ComputationNode(2,): Generated 5 finer nodes.
   2024-04-04 10:40:47,138 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +89 - INFO - ComputationNode(3,): Outer loops [TemporalLoop(OY,5)].
   2024-04-04 10:40:47,138 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +90 - INFO - ComputationNode(3,): Generated 5 finer nodes.
   2024-04-04 10:40:47,139 - stream.classes.stages.GenerateCNWorkloadHybridStage.run +123 - INFO - Finer graph: DiGraph with 22 nodes and 43 edges.
   2024-04-04 10:40:47,140 - stream.classes.stages.IntraCoreMappingStage.run +81 - INFO - Start IntraCoreMappingStage.
   2024-04-04 10:40:47,141 - stream.classes.stages.IntraCoreMappingStage.run +181 - INFO - Finished IntraCoreMappingStage.
   Traceback (most recent call last):
     File "/home/emily/stream-zigzag-input-output-linalg/main_stream.py", line 99, in <module>
       scme, _ = mainstage.run()
     File "/home/emily/.local/lib/python3.10/site-packages/zigzag/classes/stages/Stage.py", line 49, in run
       for cme, extra_info in self.list_of_callables[0](
     File "/home/emily/.local/lib/python3.10/site-packages/zigzag/classes/stages/MainInputParserStages.py", line 21, in run
       for cme, extra_info in sub_stage.run():
     File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/stages/ModelParserStage.py", line 91, in run
       for cme, extra_info in sub_stage.run():
     File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/stages/GenerateCNWorkloadHybridStage.py", line 133, in run
       for cme, extra_info in sub_stage.run():
     File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/stages/IntraCoreMappingStage.py", line 183, in run
       for cme, extra_info in sub_stage.run():
     File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/stages/DetermineSchedulingOrderStage.py", line 39, in run
       sub_stage = self.list_of_callables[0](
     File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/stages/InterCoreMappingStage.py", line 102, in __init__
       self.set_hw_performance_non_flexible_nodes()
     File "/home/emily/stream-zigzag-input-output-linalg/stream/classes/stages/InterCoreMappingStage.py", line 210, in set_hw_performance_non_flexible_nodes
       offchip_core = self.accelerator.get_core(self.accelerator.offchip_core_id)
   AttributeError: 'Accelerator' object has no attribute 'offchip_core_id'
   ```

   
## misc notes below

```
python main_stream.py --model inputs.workload.convolution-for-zigzag2 --accelerator inputs.hardware.c_k --mapping inputs.mapping.mapping_c_k
```

```
python optimal-latency.py --model inputs.workload.convolution-for-zigzag2 --accelerator inputs.hardware.c_k --mapping inputs.mapping.mapping_c_k


```

feed output of tool into stream

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

