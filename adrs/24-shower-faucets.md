# ADR 24: Shower Faucets

**Status:** Accepted

**Date:** 2025-12-21

## Context

The shower requires a multi-functional system that provides flexibility for different preferences and uses while complying with California water flow regulations.

Key considerations:
- California has strict GPM (gallons per minute) restrictions on shower heads
- Different users have different height and spray preferences
- Aesthetics and design consistency matter
- Valve system needs to control multiple shower components

## Decision

Implementing a **3-component shower system**:

1. **Ceiling-Mounted Rain Shower Head** (10" × 10")
   - Mounted on 10" ceiling arm, 24" from back wall
   - Square design for modern aesthetic
   - 10" size chosen as larger dimensions would be unreasonable given California GPM restrictions

2. **Fixed Wall-Mounted Shower Head** (5" × 5")
   - Square design matching overall aesthetic
   - Positioned 81" from floor (5" above the top of the slide bar)
   - Provides traditional shower experience

3. **Hand Shower with Slide Bar**
   - 25.75" slide bar length
   - 60" flexible hose
   - Hose elbow mounted at same height as diverter switch (48" from floor) for simplified rough plumbing (straight horizontal line from diverter to elbow)
   - Adjustable height allows different people to customize position
   - Compensates for fixed positioning of the other two heads

### Valve System

**Separate Diverter and Mixer Valves:**
- Mixer valve: Controls water temperature (Delta MultiChoice Universal Valve)
- Diverter valve: Controls water flow to different shower components
- Separation allows for better availability of aesthetically pleasing trim options
- Both valves: 6.5" and 4.5" square trims respectively, matching head designs

**Diverter Valve:**
- **3-way diverter valve**
  - Only one component active at a time
  - Guaranteed to meet California flow restrictions
  - Simpler installation and operation

### Design Aesthetic

**Square-ish style** throughout:
- Rain shower head: 10" square
- Fixed shower head: 5" square
- Mixer valve trim: 6.5" square
- Diverter valve trim: 4.5" square
- Cohesive, modern aesthetic (not round fixtures)

## Rationale

1. **Three Components for Flexibility:**
   - Rain shower provides luxury spa-like experience
   - Fixed head provides traditional reliable option
   - Hand shower enables precise targeting, rinsing, and accessibility

2. **Slide Bar Adjustability:**
   - Different users have different height preferences
   - Not everyone likes fixed shower head positions
   - Slide bar allows each user to optimize hand shower position

3. **10" Rain Shower Size:**
   - Provides good coverage without being excessive
   - Larger sizes would consume too much water given California's 2.0 GPM per shower head restriction
   - Square design maximizes coverage area efficiently

4. **Separate Diverter and Mixer:**
   - More aesthetically pleasing trim options available as separate components
   - Better control granularity
   - Easier to service individual components

5. **3-way Diverter:**
   - Ensures compliance with California flow restrictions
   - Simpler operation (one component at a time)
   - Adequate flexibility given that users typically prefer one shower mode at a time

6. **Hand Shower Elbow Positioning:**
   - Mounting elbow at same height as diverter simplifies rough plumbing
   - Allows straight horizontal run from diverter to elbow
   - Reduces installation complexity and potential leak points

## Consequences

### Positive
- Maximum flexibility for different users and preferences
- Complies with California water regulations
- Aesthetically cohesive square design language
- Adjustable hand shower accommodates all heights
- Multiple shower experience options (spa-like rain, traditional fixed, targeted hand)

### Negative
- More complex valve system increases installation cost
- More components means more potential maintenance points
- Cannot operate multiple shower heads simultaneously (single-user limitation)

## Open Questions

None at this time. Using 3-way diverter ensures compliance with all flow restrictions.

## References

- [shower_faucets_wall_option2.svg](../shower_faucets_wall_option2.svg) - Technical layout and dimensions (current configuration)
- [components/rain-shower-dimensions.png](../components/shower-rain-ceiling-head-dimensions.png) - Rain shower specifications
- [components/shower-valve-dimensions.png](../components/shower-valve-dimensions.png) - Mixer valve specifications
- [components/shower-diverter-dimensions.png](../components/shower-diverter-dimensions.png) - Diverter valve specifications
- [components/hand-shower-dimensions.png](../components/shower-hand-kit-dimensions.png) - Hand shower and slide bar specifications

## Notes

California shower head flow regulation: Maximum 2.0 gallons per minute (GPM) per shower head at 80 psi.

The 3-way diverter valve provides the following positions:
1. Rain shower only
2. Fixed head only
3. Hand shower only

Plumbing layout: The hand shower elbow is positioned at 48" from floor (same height as diverter center), allowing a straight horizontal pipe run from the diverter to the elbow outlet. This simplifies rough plumbing and reduces the number of pipe fittings required.

