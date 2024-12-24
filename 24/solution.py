import re
from dataclasses import dataclass


@dataclass
class Wire:
    name: str
    value: int = None
    gate = None

    def compute_value(self):
        if self.value is None and self.gate is not None:
            return int(self.gate.compute())
        return self.value

    def __repr__(self):
        if self.gate:
            return f'<{self.name}: {self.gate}>'
        else:
            return f'<{self.name}>'

    def __and__(self, other):
        assert isinstance(other, Wire)
        return AndGate(self, other)

    def __or__(self, other):
        assert isinstance(other, Wire)
        return OrGate(self, other)

    def __xor__(self, other):
        assert isinstance(other, Wire)
        return XorGate(self, other)


@dataclass
class Gate:
    input_a: Wire
    input_b: Wire

    def has_input(self, wire):
        return self.input_a is wire or self.input_b is wire

    def has_inputs(self, wire1, wire2):
        return ((self.input_a is wire1 and self.input_b is wire2) or
                (self.input_a is wire2 and self.input_b is wire1))

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return ((self.input_a is other.input_a and self.input_b is other.input_b) or
                (self.input_a is other.input_b and self.input_b is other.input_a))

    def __hash__(self):
        return hash(type(self)) ^ hash(self.input_a.name) ^ hash(self.input_b.name)


class AndGate(Gate):
    def compute(self):
        return self.input_a.compute_value() and self.input_b.compute_value()

    def __repr__(self):
        return f'({self.input_a.name} & {self.input_b.name})'


class OrGate(Gate):
    def compute(self):
        return self.input_a.compute_value() or self.input_b.compute_value()

    def __repr__(self):
        return f'({self.input_a.name} | {self.input_b.name})'


class XorGate(Gate):
    def compute(self):
        return self.input_a.compute_value() != self.input_b.compute_value()

    def __repr__(self):
        return f'({self.input_a.name} ^ {self.input_b.name})'


@dataclass
class Register:
    name: str
    wires: list

    @property
    def value(self):
        output = 0
        shift = 0
        for wire in self.wires:
            value = wire.compute_value()
            output |= value << shift
            shift += 1
        return output

    @value.setter
    def value(self, value):
        mask = 1
        for wire in self.wires:
            wire.value = int((value & mask) != 0)
            mask <<= 1


GATES = {'AND': AndGate, 'OR': OrGate, 'XOR': XorGate}


class Circuit:
    def __init__(self):
        self.wires = {}
        self.registers = {}
        self.gates = {}
        self.bad_wires = []

    def get_wire(self, name):
        wire = self.wires.get(name)
        if wire is None:
            wire = Wire(name)
            self.wires[name] = wire
        return wire

    def parse(self, lines):
        for line in lines:
            line = line.strip()
            if not line:
                continue

            m = re.match('([a-z0-9]+): ([01])', line)
            if m:
                wire = self.get_wire(m.group(1))
                wire.value = int(m.group(2))
                continue

            m = re.match(
                '([a-z0-9]+) (XOR|AND|OR) ([a-z0-9]+) -> ([a-z0-9]+)', line)
            if m:
                input_a = self.get_wire(m.group(1))
                input_b = self.get_wire(m.group(3))
                output = self.get_wire(m.group(4))
                gate_type = GATES[m.group(2)]
                gate = gate_type(input_a, input_b)
                output.gate = gate
                self.gates[gate] = output
                continue

            raise SyntaxError(line)

        for reg_name in 'xyz':
            reg = Register(reg_name, [])
            self.registers[reg_name] = reg

            for i in range(100):
                wire = self.wires.get(f'{reg_name}{i:02d}')
                if wire is not None:
                    reg.wires.append(wire)
                else:
                    break

    def compute(self, x, y):
        self.registers['x'].value = x
        self.registers['y'].value = y
        return self.registers['z'].value


circuit = Circuit()

with open("24/data.txt", "r") as file:
    circuit.parse(file)

# * Part 1

# ! IDEA: Compute the value of register 'z' after setting the values of registers 'x' and 'y'.
# ! The value of 'z' is determined by the gates and wires defined in the circuit.

x = circuit.registers['x']
y = circuit.registers['y']
z = circuit.registers['z']

res = z.value
print(res)
