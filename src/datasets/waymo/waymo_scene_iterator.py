from __future__ import annotations

from src.datasets.dataset import Dataset
from src.datasets.frame_descriptor import FrameDescriptor


class WaymoSceneIterator(Dataset.SceneIterator):
    """Iterator over frames in a NuScenes scene.
    """

    def __init__(self,
                 scene_id: str,
                 scene_descriptors: list):
        self.__scene_id = scene_id
        self.__scene_descriptors = scene_descriptors
        self.__current_frame = 0

    def __iter__(self) -> WaymoSceneIterator:
        """Reset iterator and returns itself.
        """
        self.__current_frame = 0
        return self

    def __next__(self) -> tuple[str, FrameDescriptor]:
        """Returns next frame.

        :return: tuple[str, dict[str, any]]
            Returns a tuple of frame id to frame meta-information
        """

        if self.__current_frame >= len(self.__scene_descriptors):
            raise StopIteration()

        frame_metadata = self.__scene_descriptors[self.__current_frame]

        frame_id = frame_metadata['frame_id']

        instance_ids = frame_metadata['annotations']['ids']

        self.__current_frame += 1

        return frame_id, FrameDescriptor(frame_id=frame_id, instances_ids=instance_ids)
