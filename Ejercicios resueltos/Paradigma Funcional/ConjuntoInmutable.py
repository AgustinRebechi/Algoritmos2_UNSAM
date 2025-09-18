from dataclasses import dataclass
@dataclass(frozen=True)
class ConjuntoInmutable:
    elementos: frozenset

    def __post_init__(self):
        elem_unicos = frozenset(self.elementos)
        tuple(self.elementos)  # Forzar la evaluación inmediata
        object.__setattr__(self, 'elementos', elem_unicos)

    def __str__(self):
        return "{" + ", ".join(str(e) for e in sorted(self.elementos)) + "}"
    
list1 = frozenset([1,2,3,4,5,5,4,3,2,1])
conj = ConjuntoInmutable(list1)
print(conj)