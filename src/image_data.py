from enum import Enum
from pathlib import Path

class ImageStatus(Enum):
    NEW = "new"
    PROCESSING = "processing"
    DONE = "done"
    ERROR = "error"

class ImageVersion:
    def __init__(self, data = None, path: str = ""):
        self.data = data if data is not None else []
        self.path = path

    def __repr__(self):
        return f"ImageVersion(path='{self.path}', data_len={len(self.data)})"

    def to_dict(self):
        if len(self.path) == 0:
            return {
                "path": "",
                "size": "0"
            }
        path = Path(self.path)
        return {
            "path": str(path.absolute()),
            "size": f"{path.stat().st_size / (1024*1024):.2f} MB",
        }


class ImageData:
    def __init__(self, file: str):
        self.__name = Path(file).name
        self.__path = file
        self.__detect_data = []
        self.__image = {
            "original": ImageVersion(),
            "debug": ImageVersion(),
            "censored": ImageVersion(),
        }
        self.__status = ImageStatus.NEW
        self.__error_msg = ""

    @property
    def name(self):
        return self.__name
    @property
    def path(self):
        return self.__path
    @property
    def image(self):
        return self.__image
    @property
    def status(self):
        return self.__status
    
    def start(self):
        self.__status = ImageStatus.PROCESSING
    def finish(self):
        self.__status = ImageStatus.DONE
    def error(self, error_msg: str = ""):
        self.__status = ImageStatus.ERROR
        self.__error_msg = error_msg

    def add_detection(self, detection):
        self.__detect_data.append(detection)

    def set_image(self, version: str, data, path: str):
        if version in self.image:
            self.image[version].data = data
            self.image[version].path = path
        else:
            raise ValueError(f"Invalid: {version}")

    def to_dict(self):
        data = {
            "name": self.__name,
            "path": self.__path,
            "detect_data": self.__detect_data,
            "image": {
                key: value.to_dict() 
                for key, value in self.__image.items() 
                    if len(value.path) > 0
            },
            "status": self.__status.value
        }
        
        if self.__error_msg:
            data["error_msg"] = self.__error_msg

        return data

    def __repr__(self):
        return f"ImageData(name='{self.__name}', status='{self.status}')"