# ADR 22: Vanity Backsplash Height and Receptacle Placement

## Status
Proposed (In Discussion)

## Context
The vanity backsplash needs to be designed considering multiple constraints:
- Material availability: 69" × 54" piece (same material as countertop)
- This piece must cover both the countertop and backsplash
- An electrical receptacle is required over the right side of the vanity (small drawers section)
- Aliona prefers a backsplash that is not "very high" (exact height preference unclear)
- The receptacle placement affects both backsplash design and mirror sizing

## Problem Statement
We need to determine the optimal backsplash height that:
1. Satisfies aesthetic preferences (not too tall)
2. Accommodates the electrical receptacle requirement
3. Works within the available material constraints
4. Allows for appropriate mirror sizing

## Options Under Consideration

### Material Constraints
- Available material: 69" × 54"
- Countertop width: 42"
- Countertop depth: 21.5"
- Must accommodate both countertop and backsplash from single piece

### Receptacle Requirements
- Location: Over right side of vanity (13.5" small drawer section)
- Preferred counter clearance: ~4" minimum from counter surface
- Receptacle dimensions: 2" × 5" (can be oriented vertically or horizontally)
- Orientation options:
  - **Vertical**: 2" wide × 5" tall (more common)
  - **Horizontal**: 5" wide × 2" tall (less common)

### Backsplash Height Options

#### Option A: Tall Backsplash with Cut-Out
- Backsplash tall enough to accommodate receptacle within it
- Cut a hole in the backsplash for the receptacle
- **Pros**: 
  - More traditional appearance
  - Protects wall better
  - Allows larger mirror
- **Cons**: 
  - May be "too tall" for Aliona's preference
  - Requires precision cutting in material
  - Receptacle interrupts backsplash surface

#### Option B: Lower Backsplash with Receptacle Above
- Backsplash height keeps receptacle above it
- Receptacle mounts on wall above backsplash
- **Pros**: 
  - Can keep backsplash shorter
  - Cleaner backsplash surface (no cut-outs)
  - Easier installation
- **Cons**: 
  - Restricts maximum mirror height
  - Limits design flexibility

### Height Examples Being Evaluated
Reference designs show various configurations:
- **8" backsplash**: Receptacle must go above (Options 4, 5)
- **10" backsplash**: Borderline for receptacle placement (Options 1, 2, 3)
- **12" backsplash**: Can accommodate receptacle within it (Option 6)

## Open Questions
1. What specific height does Aliona consider "very high"?
2. Is she comfortable with a cut-out in the backsplash, or prefer receptacle above it?
3. Which receptacle orientation is preferred (vertical vs. horizontal)?
4. What is the desired mirror size, and how does it interact with these constraints?
5. Is there flexibility on the ~4" counter clearance requirement?

## References
- Design options with dimensions: `vanity_wall_option1.svg` through `vanity_wall_option6.svg`
- Exported visualizations: `exports/vanity_wall_option*.png`
- Material size: 69" × 54"
- Vanity width: 42"
- Receptacle location: Over 13.5" right section (small drawers)
- Mirror being considered: 40" wide × 36" tall (Options 3-6) or 24" wide (Options 1-2)

## Next Steps
- [ ] Clarify Aliona's height preference for backsplash
- [ ] Decide on receptacle placement strategy (in backsplash vs. above)
- [ ] Choose receptacle orientation (vertical vs. horizontal)
- [ ] Finalize mirror dimensions based on chosen backsplash/receptacle configuration
- [ ] Verify material piece is sufficient for chosen design

## Related ADRs
- ADR 20: Sink Selection
- ADR 21: Vanity Selection

