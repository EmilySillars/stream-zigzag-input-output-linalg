# modifed from https://github.com/KULeuven-MICAS/zigzag/blob/tutorial/lab3/inputs/mapping/mapping_c_k.py
mapping = {
    "default": {
        "core_allocation": 0,
       # "spatial_mapping": {"D1": ("C", 32), "D2": ("K", 32)}, 
       # ^above line commented out so that ZigZag looks for optimal spatial mapping
        "memory_operand_links": {"O": "O", "W": "I2", "I": "I1"},
    },
}