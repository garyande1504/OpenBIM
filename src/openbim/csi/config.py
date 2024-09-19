

def reshape(apply):
    """
    apply is a list of dictionaries describing changes to apply to a model. 
    This function reshapes this list into a form that is more efficient for processing. 

    In particular, we want something like:

    {
        "Frame": {
            <name>: [<applied changes>]
        },
        "Shell": {},
        "Solid": {}
    }
    """

    
    reshaped = {
        "Frame": {},
        "Shell": {},
        "Solid": {}
    }

    for change in apply:
        typ = change["type"]
        type_dict = reshaped[typ]
        name = change["name"]
        if name in type_dict:
            type_dict[name].extend(change["apply"])
        else :
            type_dict[name] = change["apply"]

    return reshaped


if __name__ == "__main__":

    apply = [
        {"type": "Frame", "name": 32, "apply": ["Geometry.PDelta"]},
        {"type": "Frame", "name": 32, "apply": ["Material.Plasticity"]},
        {"type": "Shell", "name": 33, "apply": ["Material.Plasticity"]},
        {"type": "Frame", "name": 33, "apply": ["Geometry.PDelta"]},
        {"type": "Frame", "name": 33, "apply": ["Material.Plasticity", "Geometry.PDelta"]}
    ]

    reshaped = reshape(apply)

    print(reshaped)



