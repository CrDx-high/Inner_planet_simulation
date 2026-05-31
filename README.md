# Planet Simulation

A simple 2D solar system simulation built with Python and Pygame. This project uses Newtonian gravity to simulate the motion of planets orbiting the Sun.

## Features

- Realistic gravitational attraction using Newton's Law of Universal Gravitation
- Scaled astronomical distances using Astronomical Units (AU)
- Planetary motion based on velocity and acceleration
- Orbit path visualization
- Multiple planets included:
  - Mercury
  - Venus
  - Earth
  - Mars
- Real-time rendering with Pygame

## Physics

The simulation calculates gravitational forces between celestial bodies using Newton's Law of Universal Gravitation:

F = G(m₁m₂)/r²

Where:

- `G` = Gravitational Constant
- `m₁`, `m₂` = masses of the interacting bodies
- `r` = distance between the bodies

The resulting force is decomposed into x and y components and used to update each planet's velocity and position.

## Requirements

- Python 3.10+
- Pygame

Install dependencies:

```bash
pip install pygame
```

## Running the Simulation

```bash
python main.py
```

A window will open displaying the Sun and planets orbiting around it.

## Celestial Bodies

| Body    | Mass (kg)      | Initial Velocity (m/s) |
|----------|---------------|-------------------------|
| Mercury | 3.30 × 10²³   | 47,400 |
| Venus   | 4.865 × 10²⁴  | 35,027 |
| Earth   | 5.9742 × 10²⁴ | 29,783 |
| Mars    | 6.39 × 10²³   | 24,400 |
| Sun     | 1.98892 × 10³⁰| N/A |

## Scaling

Astronomical distances are scaled to fit on screen:

```python
SCALE = 250 / AU
```

Where:

- `AU` = 149.6 million kilometers
- 1 AU is mapped to approximately 250 pixels

## Implementation Details

Each simulation step:

1. Calculates gravitational forces between all planets.
2. Computes acceleration using Newton's Second Law.
3. Updates velocity.
4. Updates position.
5. Stores orbital coordinates for trajectory rendering.
6. Draws planets and orbit paths to the screen.

## Future Improvements

- Add Jupiter, Saturn, Uranus, and Neptune
- Planet labels
- Display distance from the Sun
- Zoom and camera controls
- Planet textures
- Adjustable simulation speed
- Pause and reset functionality
- More accurate numerical integration methods

## Learning Objectives

This project demonstrates:

- Object-Oriented Programming (OOP)
- Physics simulation
- Orbital mechanics
- Numerical integration
- Vector mathematics
- Real-time rendering with Pygame


