"""Textbook ingestion and curriculum rules.

Reusable production utilities for the textbook subsystem.
"""
from __future__ import annotations

import math
import re
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class TextbookRule1:
    name: str = "rule_1"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule1:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule2:
    name: str = "rule_2"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule2:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule3:
    name: str = "rule_3"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule3:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule4:
    name: str = "rule_4"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule4:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule5:
    name: str = "rule_5"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule5:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule6:
    name: str = "rule_6"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule6:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule7:
    name: str = "rule_7"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule7:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule8:
    name: str = "rule_8"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule8:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule9:
    name: str = "rule_9"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule9:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule10:
    name: str = "rule_10"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule10:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule11:
    name: str = "rule_11"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule11:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule12:
    name: str = "rule_12"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule12:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule13:
    name: str = "rule_13"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule13:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule14:
    name: str = "rule_14"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule14:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule15:
    name: str = "rule_15"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule15:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule16:
    name: str = "rule_16"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule16:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule17:
    name: str = "rule_17"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule17:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule18:
    name: str = "rule_18"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule18:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule19:
    name: str = "rule_19"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule19:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule20:
    name: str = "rule_20"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule20:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule21:
    name: str = "rule_21"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule21:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule22:
    name: str = "rule_22"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule22:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule23:
    name: str = "rule_23"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule23:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule24:
    name: str = "rule_24"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule24:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule25:
    name: str = "rule_25"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule25:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule26:
    name: str = "rule_26"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule26:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule27:
    name: str = "rule_27"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule27:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule28:
    name: str = "rule_28"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule28:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule29:
    name: str = "rule_29"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule29:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule30:
    name: str = "rule_30"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule30:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule31:
    name: str = "rule_31"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule31:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule32:
    name: str = "rule_32"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule32:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule33:
    name: str = "rule_33"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule33:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule34:
    name: str = "rule_34"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule34:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule35:
    name: str = "rule_35"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule35:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule36:
    name: str = "rule_36"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule36:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule37:
    name: str = "rule_37"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule37:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule38:
    name: str = "rule_38"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule38:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule39:
    name: str = "rule_39"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule39:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule40:
    name: str = "rule_40"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule40:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule41:
    name: str = "rule_41"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule41:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule42:
    name: str = "rule_42"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule42:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule43:
    name: str = "rule_43"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule43:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule44:
    name: str = "rule_44"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule44:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule45:
    name: str = "rule_45"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule45:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule46:
    name: str = "rule_46"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule46:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule47:
    name: str = "rule_47"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule47:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule48:
    name: str = "rule_48"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule48:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule49:
    name: str = "rule_49"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule49:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule50:
    name: str = "rule_50"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule50:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule51:
    name: str = "rule_51"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule51:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule52:
    name: str = "rule_52"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule52:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule53:
    name: str = "rule_53"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule53:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule54:
    name: str = "rule_54"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule54:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule55:
    name: str = "rule_55"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule55:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule56:
    name: str = "rule_56"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule56:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule57:
    name: str = "rule_57"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule57:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule58:
    name: str = "rule_58"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule58:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule59:
    name: str = "rule_59"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule59:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule60:
    name: str = "rule_60"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule60:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule61:
    name: str = "rule_61"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule61:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule62:
    name: str = "rule_62"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule62:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule63:
    name: str = "rule_63"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule63:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule64:
    name: str = "rule_64"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule64:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule65:
    name: str = "rule_65"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule65:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule66:
    name: str = "rule_66"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule66:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule67:
    name: str = "rule_67"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule67:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule68:
    name: str = "rule_68"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule68:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule69:
    name: str = "rule_69"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule69:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule70:
    name: str = "rule_70"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule70:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule71:
    name: str = "rule_71"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule71:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule72:
    name: str = "rule_72"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule72:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule73:
    name: str = "rule_73"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule73:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule74:
    name: str = "rule_74"
    weight: float = 0.5
    enabled: bool = True

    def validate(self) -> TextbookRule74:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule75:
    name: str = "rule_75"
    weight: float = 0.6
    enabled: bool = True

    def validate(self) -> TextbookRule75:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule76:
    name: str = "rule_76"
    weight: float = 0.7
    enabled: bool = True

    def validate(self) -> TextbookRule76:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule77:
    name: str = "rule_77"
    weight: float = 0.1
    enabled: bool = True

    def validate(self) -> TextbookRule77:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule78:
    name: str = "rule_78"
    weight: float = 0.2
    enabled: bool = True

    def validate(self) -> TextbookRule78:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule79:
    name: str = "rule_79"
    weight: float = 0.3
    enabled: bool = True

    def validate(self) -> TextbookRule79:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass(frozen=True)
class TextbookRule80:
    name: str = "rule_80"
    weight: float = 0.4
    enabled: bool = True

    def validate(self) -> TextbookRule80:
        if not self.name.strip():
            raise ValueError("rule name must not be empty")
        if not math.isfinite(self.weight) or self.weight < 0:
            raise ValueError("rule weight must be finite and non-negative")
        return self

@dataclass
class TextbookRegistry:
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

