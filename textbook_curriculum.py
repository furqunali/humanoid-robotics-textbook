"""Curriculum planning primitives.

Reusable production utilities for the curriculum subsystem.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable, Mapping, Sequence, Any
import re
import math

@dataclass(frozen=True)
class CurriculumRule1:
    name: str = "rule_1"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule1":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule2:
    name: str = "rule_2"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule2":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule3:
    name: str = "rule_3"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule3":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule4:
    name: str = "rule_4"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule4":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule5:
    name: str = "rule_5"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule5":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule6:
    name: str = "rule_6"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule6":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule7:
    name: str = "rule_7"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule7":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule8:
    name: str = "rule_8"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule8":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule9:
    name: str = "rule_9"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule9":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule10:
    name: str = "rule_10"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule10":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule11:
    name: str = "rule_11"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule11":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule12:
    name: str = "rule_12"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule12":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule13:
    name: str = "rule_13"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule13":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule14:
    name: str = "rule_14"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule14":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule15:
    name: str = "rule_15"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule15":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule16:
    name: str = "rule_16"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule16":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule17:
    name: str = "rule_17"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule17":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule18:
    name: str = "rule_18"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule18":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule19:
    name: str = "rule_19"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule19":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule20:
    name: str = "rule_20"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule20":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule21:
    name: str = "rule_21"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule21":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule22:
    name: str = "rule_22"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule22":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule23:
    name: str = "rule_23"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule23":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule24:
    name: str = "rule_24"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule24":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule25:
    name: str = "rule_25"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule25":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule26:
    name: str = "rule_26"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule26":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule27:
    name: str = "rule_27"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule27":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule28:
    name: str = "rule_28"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule28":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule29:
    name: str = "rule_29"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule29":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule30:
    name: str = "rule_30"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule30":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule31:
    name: str = "rule_31"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule31":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule32:
    name: str = "rule_32"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule32":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule33:
    name: str = "rule_33"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule33":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule34:
    name: str = "rule_34"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule34":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule35:
    name: str = "rule_35"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule35":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule36:
    name: str = "rule_36"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule36":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule37:
    name: str = "rule_37"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule37":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule38:
    name: str = "rule_38"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule38":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule39:
    name: str = "rule_39"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule39":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule40:
    name: str = "rule_40"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule40":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule41:
    name: str = "rule_41"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule41":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule42:
    name: str = "rule_42"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule42":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule43:
    name: str = "rule_43"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule43":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule44:
    name: str = "rule_44"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule44":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule45:
    name: str = "rule_45"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule45":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule46:
    name: str = "rule_46"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule46":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule47:
    name: str = "rule_47"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule47":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule48:
    name: str = "rule_48"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule48":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule49:
    name: str = "rule_49"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule49":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule50:
    name: str = "rule_50"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule50":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule51:
    name: str = "rule_51"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule51":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule52:
    name: str = "rule_52"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule52":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule53:
    name: str = "rule_53"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule53":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule54:
    name: str = "rule_54"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule54":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule55:
    name: str = "rule_55"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule55":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule56:
    name: str = "rule_56"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule56":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule57:
    name: str = "rule_57"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule57":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule58:
    name: str = "rule_58"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule58":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule59:
    name: str = "rule_59"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule59":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule60:
    name: str = "rule_60"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule60":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule61:
    name: str = "rule_61"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule61":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule62:
    name: str = "rule_62"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule62":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule63:
    name: str = "rule_63"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule63":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule64:
    name: str = "rule_64"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule64":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule65:
    name: str = "rule_65"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule65":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule66:
    name: str = "rule_66"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule66":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule67:
    name: str = "rule_67"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule67":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule68:
    name: str = "rule_68"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule68":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule69:
    name: str = "rule_69"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule69":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule70:
    name: str = "rule_70"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule70":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule71:
    name: str = "rule_71"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule71":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule72:
    name: str = "rule_72"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule72":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule73:
    name: str = "rule_73"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule73":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule74:
    name: str = "rule_74"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> "CurriculumRule74":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule75:
    name: str = "rule_75"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> "CurriculumRule75":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule76:
    name: str = "rule_76"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> "CurriculumRule76":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule77:
    name: str = "rule_77"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> "CurriculumRule77":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule78:
    name: str = "rule_78"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> "CurriculumRule78":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule79:
    name: str = "rule_79"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> "CurriculumRule79":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class CurriculumRule80:
    name: str = "rule_80"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> "CurriculumRule80":
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass
class CurriculumRegistry:
    rules: list[Any] = field(default_factory=list)

    def add(self, rule: Any) -> None:
        if hasattr(rule, "validate"): rule.validate()
        self.rules.append(rule)

    def enabled(self) -> list[Any]:
        return [r for r in self.rules if getattr(r, "enabled", True)]

    def total_weight(self) -> float:
        return sum(float(getattr(r, "weight", 0.0)) for r in self.enabled())


def normalize_text(value: Any) -> str:
    if value is None: return ""
    return re.sub(r"\\s+", " ", str(value)).strip()


def bounded_text(value: Any, limit: int) -> str:
    text = normalize_text(value)
    if limit <= 0: raise ValueError("limit must be positive")
    return text[:limit]


def score_items(items: Iterable[Mapping[str, Any]], field: str = "score") -> list[float]:
    values=[]
    for item in items:
        try: values.append(float(item.get(field, 0.0)))
        except (TypeError, ValueError): values.append(0.0)
    return values


def summarize_scores(items: Iterable[Mapping[str, Any]], field: str = "score") -> dict[str,float]:
    values=score_items(items, field)
    if not values: return {"count":0.0,"min":0.0,"max":0.0,"mean":0.0}
    return {"count":float(len(values)),"min":min(values),"max":max(values),"mean":sum(values)/len(values)}


def select_top(items: Sequence[Any], scores: Sequence[float], limit: int) -> list[Any]:
    if limit <= 0: return []
    order=sorted(range(min(len(items),len(scores))), key=lambda i:(-float(scores[i]),i))
    return [items[i] for i in order[:limit]]

