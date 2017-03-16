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
        exponent = 0
        for i in reversed(range(len(value_str))):
            n.value += int(value_str[i]) * 2 ** exponent
            exponent += 1
        return n

    def to_hex(self):
        return self.to_dec().to_hex()


class Hexadecimal:
    hex_set = set()
    for i in '1234567890ABCDEF':
        hex_set.add(i)

    def __init__(self, value):
        """

        :param value: String
        """
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

    def to_dec(self):
        n = Decimal(0)
        dict = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }
        hex_letter = {'A', 'B', 'C', 'D', 'E', 'F'}
        exponent = 0
        for i in reversed(range(len(self.value))):
            _ = self.value[i]
            if set(_).issubset(hex_letter):
                _ = dict[self.value[i]]
            n.value += int(_) * 16 ** exponent
            exponent += 1
        return n

    def to_bin(self):
        return self.to_dec().to_bin()


class Decimal(int):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Decimal: {}'.format(self.value)

    def __repr__(self):
        return 'Decimal: {}'.format(self.value)

    def to_bin(self):
        value_str = ''
        flag = self.value
        while flag > 0:
            value_str = str(flag % 2) + value_str
            flag = flag // 2
        _bin = Binary(int(value_str))
        return _bin

    def to_hex(self):
        value_str = ''
        flag = self.value
        dict = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'E'
        }
        while flag > 0:
            remainder = flag % 16
            if remainder > 9:
                Hex_char = dict[remainder]
                value_str = Hex_char + value_str
            else:
                value_str = str(remainder) + value_str
            flag = flag // 16
        return Hexadecimal(value_str)
