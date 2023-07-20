import os

def get_modelpaths(model_name: str):
    """
    Get the paths of all the checkpoints for the given model name.

    Args:
    model_name: The name of the model.

    Returns:
    A list of paths to the checkpoints.
    """

    checkpoints_dir = os.path.join("Checkpoints", model_name)
    if not os.path.exists(checkpoints_dir):
        return None

    checkpoints = os.listdir(checkpoints_dir)
    model_paths = []
    for checkpoint in checkpoints:
        if checkpoint.endswith(".onnx"):
            model_paths.append(os.path.join(checkpoints_dir, checkpoint))
    return model_paths


