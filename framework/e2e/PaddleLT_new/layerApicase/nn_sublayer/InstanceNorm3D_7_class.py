import numpy as np
import paddle


class LayerCase(paddle.nn.Layer):
    """
    case名称: InstanceNorm3D_7
    api简介: 3维实例归一化
    """

    def __init__(self):
        super(LayerCase, self).__init__()
        self.func = paddle.nn.InstanceNorm3D(num_features=3, epsilon=1e-05, momentum=0.9, data_format='NCDHW', )

    def forward(self, data, ):
        """
        forward
        """
        out = self.func(data, )
        return out


def create_tensor_inputs():
    """
    paddle tensor
    """
    inputs = (paddle.to_tensor(-1 + (1 - -1) * np.random.random([2, 3, 5, 5, 5]).astype('float32'), dtype='float32', stop_gradient=False), )
    return inputs


def create_numpy_inputs():
    """
    numpy array
    """
    inputs = (-1 + (1 - -1) * np.random.random([2, 3, 5, 5, 5]).astype('float32'), )
    return inputs
