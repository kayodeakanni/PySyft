from syft.generic.tensor.abstract import AbstractSyftTensor


class FixedPrecisionTensor(AbstractSyftTensor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base = 10
        self.precision_fractional = 3

        self.data = self.data * self.scaling_factor

    @property
    def scaling_factor(self):
        return self.base ** self.precision_fractional