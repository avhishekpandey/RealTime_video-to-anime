import os

def get_modelpaths(model_name: str):
    """
    Get the paths of all the checkpoints for the given model name.

    Args:
    model_name: The name of the model.

    Returns:
    A list of paths to the checkpoints.
    """

    model_name = ".".join([model_name,"onnx"])

    model_path = os.path.abspath(os.path.join("Checkpoints",model_name))
    if not os.path.exists(model_path):
        return None


    return model_path


