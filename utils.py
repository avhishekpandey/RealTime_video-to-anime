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
        return []

    checkpoints = os.listdir(checkpoints_dir)
    return [os.path.join(checkpoints_dir, checkpoint) for checkpoint in checkpoints]


