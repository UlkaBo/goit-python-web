from abc import abstractclassmethod, ABCMeta
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def serialize(self):
        pass

    @abstractclassmethod
    def deserialize(self):
        pass


class SerializationJson(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)


class SerializationBin(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


data = [7, 8, 'json', True]
packed_data = SerializationJson().serialize(data)
print(packed_data)
data_after_json = SerializationJson().deserialize(packed_data)
print(data_after_json)

packed_data = SerializationBin().serialize(data)
print(packed_data)
data_after_bin = SerializationBin().deserialize(packed_data)
print(data_after_bin)
