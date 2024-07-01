# Model snitch in Stream
```
# WORKFLOW 
# create conda environment:
# conda create -n stream 

# then install requirements:
# conda activate stream
# pip install -r requirements.txt

# "first run"
# cd stream
# python main_stream.py

# to deactivate environment:
# conda deactivate zigzag-yaml
```

## Error running api.py

```
cd stream; python api.py
```

Give the error:

```
(stream) [hoppip@inf-205-102 stream]$ python api.py
Traceback (most recent call last):
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/api.py", line 2, in <module>
    from stream.classes.stages import *
  File "/home/hoppip/.local/lib/python3.12/site-packages/stream/classes/stages/__init__.py", line 1, in <module>
    from .GenerateCNWorkloadHybridStage import GenerateCNWorkloadHybridStage
  File "/home/hoppip/.local/lib/python3.12/site-packages/stream/classes/stages/GenerateCNWorkloadHybridStage.py", line 15, in <module>
    from zigzag.classes.mapping.temporal.temporal_loop import TemporalLoop
ModuleNotFoundError: No module named 'zigzag.classes'

```

Tried to fix with:

```
python -m pip install --no-cache-dir --force-reinstall  zigzag-dse
```

but no luck.

## Error running main_stream.py

```
python main_stream.py
```

Runs for a while and then gives error:

```
2024-07-01 10:47:48,559 - stream.classes.stages.InterCoreMappingStage.run +141 - INFO - Running Inter-Core Allocation Optimization with Genetic Algorithm.
Traceback (most recent call last):
  File "/home/hoppip/stream-zigzag-input-output-linalg/main_stream.py", line 94, in <module>
    scme, _ = mainstage.run()
              ^^^^^^^^^^^^^^^
  File "/home/hoppip/.local/lib/python3.12/site-packages/zigzag/stages/MainStage.py", line 17, in run
    for cme, extra_info in self.list_of_callables[0](self.list_of_callables[1:], **self.kwargs).run():
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/stages/AcceleratorParserStage.py", line 26, in run
    for cme, extra_info in sub_stage.run():
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/stages/ModelParserStage.py", line 43, in run
    for cme, extra_info in sub_stage.run():
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/stages/GenerateCNWorkloadHybridStage.py", line 131, in run
    for cme, extra_info in sub_stage.run():
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/stages/IntraCoreMappingStage.py", line 170, in run
    for cme, extra_info in sub_stage.run():
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/stages/DetermineSchedulingOrderStage.py", line 40, in run
    for cme, extra_info in sub_stage.run():
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/stages/InterCoreMappingStage.py", line 151, in run
    pop, hof = self.genetic_algorithm.run()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/opt/allocation/genetic_algorithm/genetic_algorithm.py", line 125, in run
    logbook = algorithms.eaMuPlusLambda(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hoppip/.local/lib/python3.12/site-packages/deap/algorithms.py", line 302, in eaMuPlusLambda
    for ind, fit in zip(invalid_ind, fitnesses):
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/opt/allocation/genetic_algorithm/fitness_evaluator.py", line 63, in get_fitness
    scme.run()
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/cost_model/cost_model.py", line 51, in run
    results = schedule_graph(
              ^^^^^^^^^^^^^^^
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/cost_model/scheduler.py", line 287, in schedule_graph
    best_candidate, preds_end = get_best_candidate(candidates, scheduling_order)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hoppip/stream-zigzag-input-output-linalg/stream/classes/cost_model/scheduler.py", line 84, in get_best_candidate
    idxs = [scheduling_order.index((n.id, n.sub_id)) for n in cn_candidates]
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: (0, 0) is not in list
```

- Why?
- Got different error on this fork [here](https://github.com/EmilySillars/stream-zigzag-input-output-linalg/tree/add-linalg-as-output-from-stream/linalg-input-output)

## miscellaneous notes

```
from pprint import pprint
pprint(vars(scme))
```

