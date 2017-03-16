class Binary:
    def __init__(self, value):
        assert type(value) == int and self.elementof(value).issubset(
            {'0', '1'}), 'the input accept only combinations of integers 1 and 0!'
        self.value = value

    def __str__(self):
        return 'Binary: {}'.format(self.value)

    def __repr__(self):
        return 'Binary: {}'.format(self.value)

    def elementof(self, value):
        elements = set()
        for i in str(value):
            elements.add(i)
        return elements

    def to_dec(self):
        value_str = str(self.value)
        n = Decimal(0)
        for i in reversed(range(len(value_str))):
            n.value += int(value_str[i]) * 2 ** i
        return n


class Hexadecimal:
    hex_set = set()
    for i in '1234567890ABCDEF':
        hex_set.add(i)

    def __init__(self, value):
        assert type(value) == str and self.elementof(value).issubset(self.hex_set), \
            'the input only accept strings contain one or more characters in this list "1234567890ABCDEF"!'
        self.value = value

    def __str__(self):
        return 'Hex: {}'.format(self.value)

    def __repr__(self):
        return 'Hex: {}'.format(self.value)

    def elementof(self, value):
        elements = set()
        for i in str(value):
            elements.add(i)
        return elements


class Decimal:
    def __init__(self, x):
        self.value = x

    def __str__(self):
        return 'Decimal: {}'.format(self.value)

    def __repr__(self):
        return 'Decimal: {}'.format(self.value)

    def to_bin(self):
        value_str = ''
        flag = self.value
        while flag > 0:
            value_str = value_str + str(flag % 2)
            flag = flag // 2
        _bin = Binary(int(value_str))
        return _bin
