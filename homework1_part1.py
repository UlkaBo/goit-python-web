from abc import abstractclassmethod, ABCMeta
import json
import pickle
import math

class SerializationInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def serialize(self):
        pass

    @abstractclassmethod
    def deserialize(self):
        pass


class SerializationJsonList(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)

class SerializationJsonDict(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)

class SerializationJsonSet(SerializationInterface):
    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed_data):
        x = json.loads(packed_data)
        for i, el in enumerate(x):
            if type(el) == list:
                x[i] = tuple(el)
        print(set(x), type(x))
        return set(x)

class SerializationJsonTuple(SerializationInterface):
    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed_data):
        return tuple(json.loads(packed_data))

class SerializationBinList(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class SerializationBinList(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class SerializationBinDict(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class SerializationBinSet(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class SerializationBinTuple(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

data_list = [1, '2', math.pi, (1,2,3), False]
data_dict_bin = {1: 2, '2': '3', (1,2,3): True, '3': math.pi, '4': [1,2,3], '5': set('bin'), '6' :tuple('set'), '7': {1:2, 3:4}}
data_dict_json = {'1': 2, '2': '3', '0': True, '3': math.pi, '4': [1,2,3], '5': 'json', '6' :'json', '7': 0}
data_set = {'r', (3,4,5), 2, math.pi}
data_tuple = (1,'2', math.pi, [1,2,3], False)

print(f'serialize  - deserialize json list \n{data_list}:')
packed_data = SerializationJsonList().serialize(data_list)
print(f'serialize data - \n{packed_data}')
data_after = SerializationJsonList().deserialize(packed_data)
print(f'deserialize data \n{data_after}')
try:
    assert data_list == data_after, 'No correct deserialize json list'
    print("\njson list serialization and deserialization was successful\n")
except AssertionError as error:
    print(f'\n{error}\n')

print(f'serialize  - deserialize json dict \n{data_dict_json}:')
packed_data = SerializationJsonDict().serialize(data_dict_json)
print(f'serialize data - \n{packed_data}')
data_after = SerializationJsonDict().deserialize(packed_data)
print(f'deserialize data \n{data_after}')
try:
    assert data_dict_json == data_after, 'No correct deserialize json dict'
    print("\njson dict serialization and deserialization was successful\n")
except AssertionError as error:
    print(f'\n{error}\n')

print(f'serialize  - deserialize json set \n{data_set}:')
packed_data = SerializationJsonSet().serialize(data_set)
print(f'serialize data - \n{packed_data}')
data_after = SerializationJsonSet().deserialize(packed_data)
print(f'deserialize data \n{data_after}')
try:
    assert data_set == data_after, 'No correct deserialize json set'
    print("\njson set serialization and deserialization was successful\n")
except AssertionError as error:
    print(f'\n{error}\n')
    

print(f'serialize  - deserialize json tuple \n{data_tuple}:')
packed_data = SerializationJsonTuple().serialize(data_tuple)
print(f'serialize data - \n{packed_data}')
data_after = SerializationJsonTuple().deserialize(packed_data)
print(f'deserialize data \n{data_after}')
try:
    assert data_tuple == data_after, 'No correct deserialize json tuple'
    print("\njson tuple serialization and deserialization was successful\n")
except AssertionError as error:
    print(f'\n{error}\n')

print(f'serialize  - deserialize bin list \n{data_list}:')
packed_data = SerializationBinList().serialize(data_list)
print(f'serialize data - \n{packed_data}')
data_after = SerializationBinList().deserialize(packed_data)
print(f'deserialize data \n{data_after}')
try:
    assert data_list == data_after, 'No correct deserialize bin list'
    print("\nbin list serialization and deserialization was successful\n")
except AssertionError as error:
    print(f'\n{error}\n')

print(f'serialize  - deserialize bin dict \n{data_dict_bin}:')
packed_data = SerializationBinDict().serialize(data_dict_bin)
print(f'serialize data - \n{packed_data}')
data_after = SerializationBinDict().deserialize(packed_data)
print(f'deserialize data \n{data_after}')
try:
    assert data_dict_bin == data_after, 'No correct deserialize bin dict'
    print("\nbin dict serialization and deserialization was successful\n")
except AssertionError as error:
    print(f'\n{error}\n')

print(f'serialize  - deserialize bin set \n{data_set}:')
packed_data = SerializationBinSet().serialize(data_set)
print(f'serialize data - \n{packed_data}')
data_after = SerializationBinSet().deserialize(packed_data)
print(f'deserialize data \n{data_after}')
try:
    assert data_set == data_after, 'No correct deserialize bin set'
    print("\nbin set serialization and deserialization was successful\n")
except AssertionError as error:
    print(f'\n{error}\n')

print(f'serialize  - deserialize bin tuple v{data_tuple}:')
packed_data = SerializationBinTuple().serialize(data_tuple)
print(f'serialize data - \n{packed_data}')
data_after = SerializationBinTuple().deserialize(packed_data)
print(f'deserialize data \n{data_after}')
try:
    assert data_tuple == data_after, 'No correct deserialize bin tuple'
    print("\nbin tuple serialization and deserialization was successful\n")
except AssertionError as error:
    print(f'\n{error}\n')


