from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleorite', ('A','C','G','T'))

def test_type():
    assert True

class Gene:
    def __init__(self, gene: str) -> None:
        self.gene: str = gene

    def __str__(self) -> str:
        return self.gene

def test_gene():
    myGene: str = 'AGCGTTGCA'
    gene: Gene = Gene(myGene)
    assert gene.__str__() == myGene




class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string : int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == 'A':
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0:
                gene += 'A'
            elif bits == 1:
                gene += 'C'
            elif bits == 2:
                gene += 'G'
            else:
                gene += 'T'
        return gene[::-1]


    def __str__(self) -> str:
        return self.decompress()


def test_compressed_gene():
    myGene: str = 'AGCGTTGCA'
    gene: CompressedGene = CompressedGene(myGene)
    assert gene.__str__() == myGene