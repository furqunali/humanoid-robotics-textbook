"""Numerically stable robotics helpers used by simulation and digital-twin examples."""
from __future__ import annotations

import math
from dataclasses import dataclass

Vector3 = tuple[float, float, float]

def _finite(value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("value must be finite")
    return value

def add(a: Vector3, b: Vector3) -> Vector3:
    return tuple(_finite(x + y) for x, y in zip(a, b))  # type: ignore[return-value]

def subtract(a: Vector3, b: Vector3) -> Vector3:
    return tuple(_finite(x - y) for x, y in zip(a, b))  # type: ignore[return-value]

def scale(v: Vector3, factor: float) -> Vector3:
    factor = _finite(factor)
    return tuple(_finite(x * factor) for x in v)  # type: ignore[return-value]

def dot(a: Vector3, b: Vector3) -> float:
    return _finite(sum(x * y for x, y in zip(a, b)))

def cross(a: Vector3, b: Vector3) -> Vector3:
    return (_finite(a[1]*b[2]-a[2]*b[1]), _finite(a[2]*b[0]-a[0]*b[2]), _finite(a[0]*b[1]-a[1]*b[0]))

def norm(v: Vector3) -> float:
    return math.sqrt(dot(v, v))

def normalize(v: Vector3, epsilon: float = 1e-12) -> Vector3:
    length = norm(v)
    if length <= epsilon:
        raise ValueError("cannot normalize a near-zero vector")
    return scale(v, 1.0 / length)

def clamp(value: float, lower: float, upper: float) -> float:
    value, lower, upper = map(_finite, (value, lower, upper))
    if lower > upper:
        raise ValueError("lower bound must not exceed upper bound")
    return max(lower, min(upper, value))

@dataclass(frozen=True)
class Pose:
    position: Vector3 = (0.0, 0.0, 0.0)
    yaw: float = 0.0
    pitch: float = 0.0
    roll: float = 0.0

    def validated(self) -> Pose:
        values = self.position + (self.yaw, self.pitch, self.roll)
        if not all(math.isfinite(float(v)) for v in values):
            raise ValueError("pose values must be finite")
        return self

    def translated(self, delta: Vector3) -> Pose:
        return Pose(add(self.position, delta), self.yaw, self.pitch, self.roll)

    def rotated(self, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0) -> Pose:
        return Pose(self.position, self.yaw + yaw, self.pitch + pitch, self.roll + roll).validated()

@dataclass(frozen=True)
class Twist:
    linear: Vector3 = (0.0, 0.0, 0.0)
    angular: Vector3 = (0.0, 0.0, 0.0)

    def magnitude(self) -> float:
        return math.sqrt(norm(self.linear) ** 2 + norm(self.angular) ** 2)

    def scaled(self, factor: float) -> Twist:
        return Twist(scale(self.linear, factor), scale(self.angular, factor))

def integrate_pose(pose: Pose, twist: Twist, dt: float) -> Pose:
    dt = _finite(dt)
    if dt < 0:
        raise ValueError("dt must be non-negative")
    return Pose(
        add(pose.position, scale(twist.linear, dt)),
        pose.yaw + twist.angular[2] * dt,
        pose.pitch + twist.angular[1] * dt,
        pose.roll + twist.angular[0] * dt,
    ).validated()

def distance(a: Vector3, b: Vector3) -> float:
    return norm(subtract(a, b))

def lerp(a: Vector3, b: Vector3, alpha: float) -> Vector3:
    alpha = clamp(alpha, 0.0, 1.0)
    return add(a, scale(subtract(b, a), alpha))
