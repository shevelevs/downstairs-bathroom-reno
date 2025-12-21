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
   - Mounted on 10" ceiling arm
   - Square design for modern aesthetic
   - 10" size chosen as larger dimensions would be unreasonable given California GPM restrictions

2. **Fixed Wall-Mounted Shower Head** (5" × 5")
   - Square design matching overall aesthetic
   - Positioned 81" from floor (5" above the top of the slide bar)
   - Provides traditional shower experience

3. **Hand Shower with Slide Bar**
   - 25.75" slide bar length
   - 60" flexible hose
   - Adjustable height allows different people to customize position
   - Compensates for fixed positioning of the other two heads

### Valve System

**Separate Diverter and Mixer Valves:**
- Mixer valve: Controls water temperature (Delta MultiChoice Universal Valve)
- Diverter valve: Controls water flow to different shower components
- Separation allows for better availability of aesthetically pleasing trim options
- Both valves: 6.5" and 4.5" square trims respectively, matching head designs

**Diverter Valve Options:**
- Primary choice: **6-way diverter valve**
  - Supports 3 components operating individually
  - Supports 3 pairs operating simultaneously (rain + fixed, rain + hand, fixed + hand)
  - If simultaneous operation violates California flow restrictions, will use 3-way diverter instead
- Backup: **3-way diverter valve** (also ordered)
  - Only one component active at a time
  - Guaranteed to meet flow restrictions

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

5. **6-way vs 3-way Diverter:**
   - Ordered both to hedge against flow restriction uncertainty
   - 6-way preferred for flexibility (e.g., rain + hand shower simultaneously)
   - Will test actual flow rates to determine if simultaneous operation is viable
   - Can fall back to 3-way if needed

## Consequences

### Positive
- Maximum flexibility for different users and preferences
- Complies with California water regulations
- Aesthetically cohesive square design language
- Adjustable hand shower accommodates all heights
- Multiple shower experience options (spa-like rain, traditional fixed, targeted hand)

### Negative
- More complex valve system increases installation cost
- Need to verify simultaneous operation compliance (6-way diverter)
- More components means more potential maintenance points
- Ordered both diverter options, one will be unused

## Open Questions

1. Will simultaneous operation of two heads comply with California 2.0 GPM per head restriction?
2. What is the combined GPM when multiple heads operate simultaneously?
3. Should we install low-flow aerators/restrictors to ensure compliance?

## References

- [shower_faucets_wall.svg](../shower_faucets_wall.svg) - Technical layout and dimensions
- [components/rain-shower-dimensions.png](../components/rain-shower-dimensions.png) - Rain shower specifications
- [components/shower-valve-dimensions.png](../components/shower-valve-dimensions.png) - Mixer valve specifications
- [components/shower-diverter-dimensions.png](../components/shower-diverter-dimensions.png) - Diverter valve specifications
- [components/hand-shower-dimensions.png](../components/hand-shower-dimensions.png) - Hand shower and slide bar specifications

## Notes

California shower head flow regulation: Maximum 2.0 gallons per minute (GPM) per shower head at 80 psi.

The 6-way diverter valve provides the following positions:
1. Rain shower only
2. Fixed head only
3. Hand shower only
4. Rain + Fixed simultaneously
5. Rain + Hand simultaneously
6. Fixed + Hand simultaneously

If testing shows simultaneous operation exceeds flow limits, the 3-way diverter will be installed instead, allowing only one component at a time.

