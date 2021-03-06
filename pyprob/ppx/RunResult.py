# automatically generated by the FlatBuffers compiler, do not modify

# namespace: ppx

import flatbuffers

class RunResult(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRunResult(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RunResult()
        x.Init(buf, n + offset)
        return x

    # RunResult
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RunResult
    def Result(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def RunResultStart(builder): builder.StartObject(1)
def RunResultAddResult(builder, result): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(result), 0)
def RunResultEnd(builder): return builder.EndObject()
