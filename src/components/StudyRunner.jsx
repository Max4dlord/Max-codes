import { useState, useEffect } from 'react'
import { useNavigate, Navigate, Link } from 'react-router-dom'
import { loadStudySession, saveStudySession } from '../progress.js'

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

// Topic-focused deep dives for AEE — each appears for any question from that topic
const TOPIC_DEEP_DIVE = {
  'welding-defects': `WELDING DEFECTS — Complete Topic Overview:
Welding defects are imperfections that weaken a weld. The 11 key defects you will see in AEE 202 are:
• Slag (flux left on surface) — low heat + slow speed → prevents flux burning off.
• Undercut (groove melted away) — high amperage + low gas + wrong angle + greasy plate.
• Porosity (holes inside) — low shielding gas + too fast + inexperience → gas trapped.
• Incomplete Fusion / Cold Weld (gap, breaks soon) — low heat + wrong angle + inexperience.
• Overlap (excess metal flowing onto base plate, 3" vs 1-2" spec, ugly/wasteful) — too long/too much weld.
• Underfill (valley from too little metal) — too fast / poor visibility / missed angle.
• Spatter (small bumps splashed, must grind, distinct sound) — low amperage + wire too long + high arc power.
• Excessive Convexity = mountain (too high/thick) vs Concavity = valley (too low) — both from heat/speed imbalance.
• Excessive Reinforcement (too tall/wide on the joint) — slow travel + wrong angle.
• Incomplete Penetration (wire doesn't reach root, weak) — electrode too short / wrong angle.
• Excessive Penetration (burn-through, weakens plate) — dwell too long in one spot.

How to tell them apart in the exam: Look for the KEY PHRASE — "holes" = Porosity, "flux on surface" = Slag, "groove" = Undercut, "gap/cold" = Fusion, "3 vs 1-2 inches" = Overlap, "valley" + not enough = Underfill, "bumps to grind + sound" = Spatter, "mountain high" = Convexity, "valley low" = Concavity, "too deep/burn through" = Excessive Penetration.`,

  'fasteners-general': `FASTENERS — Overview:
Fasteners are mechanical devices to join parts. Key families in your PDFs:
• Bolts: Carriage (round head, ribs to prevent turning), Hex (most common, 3 grades, ¼-4"), Track (elliptical head for railroads), Aircraft (D.O.D. high-strength), Lag (conical point for wood/masonry), Square, Plow, Flanged, etc.
• Heads: Washer/Flanged (no separate washer), Binding (undercut for stranded wire, electrical), Fillister (deep slot, high torque), Truss (large area, soft material), Pan, 12-point (aircraft, high torque), Flat (flush).
• Points: Cup (most common, Rockwell C45), Flat (frequent resetting), Cone (permanent, greatest holding), Oval (frequent adjustment, lowest holding), Half Dog (permanent, spotted hole).

Exam tip: Head style questions test "which eliminates washer?" → Washer/Flanged. "Which for electrical?" → Binding. "Which is twelve-sided for aircraft?" → 12-point.`,

  'fasteners-bolts': `BOLTS — Detailed:
• Carriage: round head, ribs/flats prevent turning — attractive external.
• Hex: most common, 3 grades, ¼-4", hex head = greater strength + torque + ID area.
• Track: elliptical head, prevents rotation, railroad specific.
• Aircraft: generic high-strength, but officially D.O.D. spec.
• Lag: square head, conical point, wood/masonry + expansion anchor.
• Taper pin: taper ¼" per foot, d = D - 0.02088L. Example: D=0.5, L=2 → d=0.45824".

Calculation: Always use d = D - 0.02088×L and keep units in inches.`,

  'fasteners-rivets': `RIVETS & INSERTS — Overview:
• Semitubular: hole depth ≤1.12× diameter, becomes solid when set — MOST USED.
• Full tubular: hole >1.12× diameter, can punch own holes in soft materials, lower shear.
• Bifurcated (split): prongs make own holes in fiber/wood/plastic/metal.
• Metal Piercing: greater column strength, pierces 0.15" sandwich, hardness ≤ RB50.
• Pull-mandrel blind rivet: body + mandrel, 3 types → pull-through (hollow), break (retained mandrel = plug, stronger), nonbreak (mandrel pulled in but not broken).
• Inserts: Pressed-in (easiest, hole slightly larger than OD, light loads), Self-tapping (nonferrous/plastics), Solid-bushing (mechanical locks), Molded-in (cast in place), Ultrasonic (thermoplastics, vibration melts), Wire-thread (repair, tang broken off).`,

  'hot-metal-working': `HOT METAL WORKING — Overview:
Safety: proper clothing, eye protection (#10/12 for arc, #4 for gas), hair restrained, correct tools, well ventilated, never touch hot metal, turn off heat, avoid flammables.
Melting points: Wrought iron 1540°C, Mild steel 1483°C, Cast iron 1261°C (white), Copper 1094°C, Zinc 427°C, Lead 316°C.
Heat sources: Electrical — Elect soldering 204°C/150W, Carbon arc 4982°C/150A, TIG/MIG 6427°C/200A (non-ferrous). Chemical — Propane torch 1261°C, Acetylene 3485°C (welding/cutting), Propane cutting 2873°C.
Anvil parts: Hardy hole, Pritchel hole, Face, Horn, Base, Cutting block, Body — Hardy is for cutting. Tongs: curved lip (a), flat lip (b), gad (c).`,

  'heat-treatment': `HEAT TREATMENT OF STEEL — Full topic:
Purpose: Hardening, Tempering, Annealing.
• Hardening: Heat steel (pearlite) to light cherry red → Austenite, then cool QUICKLY in warm water → Martensite (very hard).
• Tempering: Reheat hardened steel to obtain desired hardness + toughness. Stages: 93-204°C retain hardness/gain some toughness; 204-371°C moderately hard/tough; 371-538°C less hard/more tough.
  Colors: Yellow 221°C (hammers), Straw 243°C (punches/dies), Light brown 260°C (axes), Purple 277°C (rivet sets), Blue 293°C (screwdrivers/springs), Gray 371°C soft = annealing point.
• Annealing: Heat above 716°C (critical, depends on carbon) and cool SLOWLY in oven/vermiculite/sand — softens, allows bending, relieves stress.`,

  'cold-metal-safety': `COLD METAL WORKING SAFETY:
Always use eye protection, proper clothing, restrain long hair, use proper tools, keep area/tools clean. Never leave tools unattended, keep guards in place.

Arc vs Gas safety:
• Arc: #10/12 filter, clear flip-up for chipping, insulate holder/cables, keep dry (never weld wet), wool/cotton only (synthetic is flammable), secure work, metal container for stubs, turn off if electrode sticks, use pliers for hot metal, well ventilated (lead/zinc fumes toxic), no matches/lighters.
• Gas: #4 filter, same clothing, well ventilated, open acetylene ≤3/4 turn (quick close) and oxygen fully, never exceed 15 psi acetylene, tip away from body (gases saturate clothing), light with approved lighter, point flame safely, never leave lit torch, handle hot with pliers, check leaks, apron, no oil/grease + oxygen (explosive).

Tip: Arc = #10/12, Gas = #4. Acetylene ≤15 psi and ≤3/4 turn.`,

  'metal-shapes': `COMMERCIAL METAL SHAPES — How measured for purchasing:
• Hexagon / Octagon: distance across flats, 12'-20'
• I-beam: height × web thickness × flange width, to 60'
• Plate: thickness × width, to 20'
• Round: diameter, 12'-20'
• Sheet metal: thickness × width × length, to 144'
• Square / Tubing / Angle / Band / Channel: width×length or thickness×width×length or leg×leg×thickness.

Exam always asks "How is Hexagon measured?" → distance across flats. Round → diameter. I-beam → height×web×flange.`,

  'cutting-tools': `CUTTING TOOLS — Hacksaw, Files, Chisels, Hammers:
• Files selected by: length, coarseness, shape, teeth (Tang, Heel, Body, Edge, Point, Bastard/Second cut/Smooth, shapes Flat/Round/Half-round, cuts Single/Double).
• Hacksaw blades (Table 5-1): 14 TPI for 1" and over (cast iron, machine steel, brass...), 18 TPI for 1/4"-1" (annealed tool steel...), 24 TPI for 1/8"-1/4" (iron, steel...), 32 TPI for 1/8" and less.
• Three-Teeth Rule: At least 3 teeth must contact the metal (too coarse = break, too fine = inefficient).
• Broken blade: Turn over and start new blade on opposite side or finish with another old blade.
• Peen hammers: Ball peen, Straight peen, Cross peen.
• Cold chisels: Cape, Half-round nose, Diamond point.

Exam tip: For stock thickness given, pick TPI where thickness falls in the range.`,

  'drilling': `DRILLING — Key points:
• Drilling: round hole with end cutting tool (drill); Reaming: enlarge to very specific accurate size with reamer (end + side cutting).
• Procedure: Center-punch dent → lubricate → hold in vise (or V-block for round) → drill. Advantage: very fast, small accurate holes. Disadvantage: factory temperatures affect it.
• RPM Table 5-2: For High-Speed drills, e.g., 1/4" in Low Carbon Steel 1,200-1,700 RPM, in Aluminum/Brass 3,000-4,500 RPM; 1/2" in Aluminum 1,500-2,250. Reduce by ½ for carbon drills. For number/letter drills, use nearest fractional size.
• Twist drill parts: Tang, Heel, Body, etc. Shanks: tapered, straight, bit-stock, blacksmith. Sizes: Number (80-.0135 to 1-.2280), Letter (A-.2340 to Z-.4130), Fractional (1/64-.0156 to 1-.5000).
• Cutting fluids: Aluminum → kerosene/soluble oil, Brass/Bronze → soluble/mineral, Cast iron → dry/compressed air, Copper → soluble/lard/mineral, Tool steel → sulfurized oil.
• Tapping: cutting internal threads with tap (taper, plug, bottoming).`,

  'mig-welding': `MIG WELDING — Complete topic:
• Safety: correct shaded lens, well ventilated, cables straight, turn off machine + gas when done, never repair yourself.
• Equipment: Power Supply = DCRP supply + Wire feeder + Gas control; Machine adjustments = Voltage, Wire feed speed, Gas flow rate; Cable = gas line + power cable + liner + electrode; Gun = nozzle + contact tip + cooling + shielding.
• Atmosphere: N₂ 78%, O₂ 21%, Ar 0.94%, Others 0.06%.
• Shielding gases: Argon → thin sheet, Helium → thick metals, CO₂ → low/medium carbon steel, Ar+O₂ → carbon/stainless, Ar+He → thick non-ferrous.
• AWS ER 70 S 6: E=electrode, R=rod, 70=70,000 psi tensile, S=solid bare wire, 6=composition.
• Wire size vs thickness: 1/32-1/8" → 0.020/0.030/0.035; 3/16-3/8" → 0.045-1/16"; >½" → 1/8".
• Arc control: Starting = Fuse/Scratch, Stopping = Tapered current/Quick stop wire feed.
• Positions: Fig 7-21: 90° work angle top view, 15° work angle end view, 15° travel angle side view.
• Effect of gun: Perpendicular = medium bead/penetration, Backhand = narrow/deep, Forehand = wide/low.
• Metal transfer: Globular (thin metals, large globule), Short-arc/Dip (thin, 4-step short circuit: elongate → touch → short → reignite), Spray (fine spray).
• Defects: Burn-thru (hole), Crater cracks, Low penetration (surface only), Overlap (incomplete melting), Porosity (blow holes), Whiskers (short-unmelted wire).`,

  'tig-welding': `TIG WELDING — Complete topic:
• Advantages vs stick: Stronger welds, easier than stick, less spark/smoke/fumes, less distortion, less grinding, welds both ferrous and non-ferrous.
• Safety: #11 or #12 lens, well ventilated, hearing protection, never touch tungsten electrode, adjust within limits.
• Equipment: Power supply (AC, DC-straight, DC-reverse) + High frequency unit + Torch (Short cap, Torch body, Gas cup, Collet body, Collet, Electrode) + Flow meter + Hoses & leads. Flowmeter for argon/helium.
• System (Fig 68): Regulator/Flowmeter + Air/Water-cooled TIG Torch + Shielding Gas + Workpiece + Power Supply + Water cooler (optional).
• TIG uses non-consumable tungsten electrode, with separate filler rod if needed, and inert gas shielding (Ar/He).

Exam tip: Lens numbers (#11/12 for TIG vs #10/12 for MIG arc) and torch parts are frequent questions.`,

  'production-welding': `PRODUCTION WELDING — Overview:
• Definition: Joins materials (usually metals) by causing fusion; used for permanent joints.
• For high production, MIG is quickest; factories now use robotic welding (resistance spot + arc in automotive). Robotic = programmable tools that fully automate weld + handling.
• Types: Plastic/Pressure (heated to plastic, forced together — e.g., Resistance) vs Fusion/Non-Pressure (molten, solidifies — e.g., Gas, Arc).
• Classification: Gas (Oxy-acetylene, Air-acetylene, Oxy-hydrogen), Arc (Metal, Submerged, TIG, MIG, Plasma...), Resistance (Butt, Spot, Seam...), Thermit, Solid State (Friction, Ultrasonic, Diffusion, Explosive), Newer (Electron-beam, Laser), Related (Oxy-acetylene cutting, Brazing, Soldering).`,

  'gas-welding': `GAS WELDING — Detailed:
• Fusion process: heat from combustion of oxygen + fuel gas (acetylene, hydrogen, propene). Types: Oxy-Acetylene (most common), Air-Acetylene, Oxy-Hydrogen.
• Oxy-Acetylene: Intense gas flame when O₂ + acetylene in correct proportions.
• Equipment: Gas Cylinders (O₂ 125 kg/cm², Acetylene 16 kg/cm²), Regulators (working: O₂ 1 kg/cm², Acetylene 0.15 kg/cm²), Gauges, Hoses, Torch, Check valve, Non-return valve, Cylinder support, Caps, Wrench, Fusible plugs.
• Advantages: Portable/versatile, better temperature control, can weld dissimilar metals, low cost/maintenance.
• Disadvantages: Not for heavy sections, lower flame temperature, slow heating.
• Flame types determined by gas ratio: Neutral = 1:1 (50% O₂ / 50% acetylene) — hottest, blue outer, ideal; Carburizing/Reducing = excess acetylene (e.g., 70:30) — 3 zones, for Ni/Cr alloys; Oxidizing = excess oxygen — for brazing.
• Safety: Protect cylinders, separate empty/full, no oil/grease + oxygen (explosive), light acetylene first then oxygen slowly, correct goggles, never leave lit torch, check leaks, apron, ventilation.

Calculation example: Cylinder 125 vs working 1 kg/cm² = regulator reduces pressure by 125×.`,

  'arc-welding': `ARC WELDING — Detailed:
• Fusion process: heat from electric arc between base metal and electrode. Types: Metal Arc (most common), Submerged Arc, TIG, MIG.
• Equipment: Generator (D.C.) or Transformer (A.C.), 2 cables (work + electrode), Holder, Electrode, Shield, Gloves, Brush, Chipping hammer, Goggles. Metal Arc uses flux-coated consumable electrode.
• Advantages: Most efficient, lowest cost, lighter weight (better material utilization), joins all commercial metals, design flexibility.
• Disadvantages: Manually applied → high labor cost, high energy → danger, not convenient for disassembly, defects hard to detect.
• Applications: Automobile bodies, Aircraft frames, Railway wagons, Machine frames, Structural works, tanks, furniture, boilers, ship building.
• Positions: Flat, Horizontal, Vertical, Overhead (overhead is hardest). Electrode classification EXXXX: first 2 digits = tensile strength in ksi (e.g., 60 = 60,000 psi), 3rd digit = position (1=all positions, 2=flat+horizontal, 3=flat only), 4th digit = coating type. Example E6013 → 60 ksi, all positions, type 3 coating.

Study tip: For E6525 example in PDF: 65 ksi, positions 1+2, type 5 coating.`,

  'welding-classification': `WELDING CLASSIFICATION — Summary for exam:
• Arc: Carbon, Metal, MIG, TIG, Plasma, Submerged, Electro-slag
• Gas: Oxy-acetylene, Air-acetylene, Oxy-hydrogen
• Resistance: Butt, Spot, Seam, Projection, Percussion
• Thermit
• Solid State: Friction, Ultrasonic, Diffusion, Explosive
• Newer: Electron-beam, Laser
• Related: Oxy-acetylene cutting, Arc cutting, Hard facing, Brazing, Soldering

Brazing vs Soldering vs Welding: Soldering <450°C (e.g., lead-tin 183°C), Brazing >450°C but below base metal melting (e.g., silver brazing), Welding melts base metal. Soldering uses flux, filler, soldering iron, wire brush.

Exam often asks: "Which is Solid State?" → Friction/Ultrasonic. "Which is Newer?" → Electron-beam/Laser. "Which is Related?" → Brazing/Soldering.`,

  'machine-operations': `MACHINE OPERATIONS — Overview (for the PDF with Shaping, Turning, Milling, Drilling, Sawing, Robotic):
• Shaping: Cutting so part fits another, very precise down to ½ mm, small fine cuts, needs programing. Disadvantage: needs very skilled technician if tool breaks.
• Turning: Material removal to create rotational parts on lathe (workpiece rotates, cutter bit feeds). Advantage: 360° removal. Disadvantage: hard to rotate with precise accuracy.
• Milling: Multi-point rotating tool removes metal briskly. Advantage: can perform literally any operation with great accuracy — indispensable. Disadvantage: needs training, very expensive.
• Drilling: Round hole with end cutting tool (drill); Reaming enlarges to accurate size with reamer. Advantage: very fast, small accurate holes. Disadvantage: factory temperatures affect it.
• Sawing: Cut bars or shapes in plates with disks/blades/bands. Advantage: cuts very strong objects precisely. Disadvantage: very dangerous, many hand/finger accidents.
• Robotic Welding: Programmable robots fully automate weld + handling, commonly resistance spot + arc in automotive. History: robots introduced US 1960s, welding take-off 1980s. Advantages: speed + less injury. Disadvantages: very expensive, costly to fix, less precision than good human, may cause cold welds/pinholes, needs training.`,

  'advanced-manufacturing': `ADVANCED MANUFACTURING — Definition & Goals:
• Definition: Use of innovative technology (“advanced,” “innovative,” “cutting edge”) to improve products or processes; integrates new tech in both products and processes.
• Approach: Builds for immediate/nearly immediate sale, not for stock. More flexible to changing needs.
• Goal: Produce in least amount of time while minimizing waste; out-perform competitors, build faster/better.
• Characteristics: High level of design, technologically complex and superior to counterparts, cutting-edge/innovative, reliable/affordable/readily available, newer/better/exciting, solves common problems.
• Example: Toyota vs GM.
• Robotic Technology is “The way of the future.”
• Vocabulary: Innovative, Relevant, Cutting Edge, Flexible, Specifically, Approach.

Exam tip: If asked “fundamental goal” → least time + least waste. “Characteristics” → high design + complex/superior + cutting-edge + reliable/affordable.`,

  'metal-shapes': `COMMERCIAL METAL SHAPES — How measured:
• Hexagon/Octagon: distance across flats
• I-beam: height × web thickness × flange width
• Plate: thickness × width
• Round: diameter
• Sheet metal: thickness × width × length
• Square/Tubing/Angle/Band/Channel: various width×length or leg×thickness combos.
Exam always asks Hexagon → flats, Round → diameter, I-beam → height×web×flange.`,

  'cutting-tools': `CUTTING TOOLS — Hacksaw & Files:
• Files selected by: length, coarseness, shape, teeth. Hacksaw blades Table 5-1: 14 TPI for ≥1" (cast iron, machine steel, brass), 18 TPI for 1/4"-1" (annealed tool steel), 24 TPI for 1/8"-1/4" (iron, steel, drill rod), 32 TPI for ≤1/8".
• Three-Teeth Rule: At least 3 teeth must contact metal (too coarse = break, too fine = inefficient).
• Broken blade: Turn over and start new blade on opposite side or finish with another old blade.
• Peen hammers: Ball, Straight, Cross peen. Cold chisels: Cape, Half-round, Diamond point.

Use the TPI table to pick blade: thickness in range → correct TPI.`,

  'drilling': `DRILLING — Full topic:
• Procedure: Dent with center punch → Lubricate drill → Hold in vise (V-block for round) → Drill.
• RPM Table 5-2: e.g., 1/4" low carbon 1,200-1,700 RPM, 1/2" aluminum 1,500-2,250 RPM. Reduce by ½ for carbon drills. For number/letter drills, use nearest fractional size.
• Twist drill parts: Tang, Heel, Body, Edge, Point; Shanks: tapered, straight, bit-stock, blacksmith.
• Drill sizes: Number 80-.0135 to 1-.2280, Letter A-.2340 to Z-.4130, Fractional 1/64-.0156 to 1-1.0000. Example: 1/64 = 0.0156".
• Cutting fluids: Aluminum→kerosene/soluble oil, Brass/Bronze→soluble/mineral, Cast iron→dry/compressed, Tool steel→sulfurized oil.

Calculation: RPM = (SFM×4)/Diameter. Use table directly in exam.`,

  'bench-work': `BENCH WORK & FITTING — Workshop machines seen: Sheet rolling (4ft/8ft), Electronic punching (1000W), Pillar drilling (variable speed), Pedestal grinding, Bandsaw, Press, Hand shear, Lathe, Heavy duty lathe.
• Bench Work = creation by hands on bench; Fitting = assembling components.
• Hack saw teeth: alternately right/left, every 3rd/4th straight.
• Cold chisel: thick layers, clearance/rake/cutting angles. File: thin layers, slanting teeth, classified by size (100-200mm fine, 200-400mm heavy) and cut (Single 60°, Double 60°+80°).
• Filing methods: Cross filing (across), Straight filing, Draw filing (both hands).
• Marking Out: scribing lines as guide. Tools: Surface/Table, Scriber, Punch, V-block, Angle plate, Try-Square.
This topic is all theory — no calculations, focus on definitions.`,

  'workshop-safety': `WORKSHOP SAFETY — Comprehensive:
• Horseplay: Absolutely no horseplay/pranks — supervisor must boot you out.
• Clothing: Wool/cotton coveralls/lab coats/denim, good repair, proper fit, safety shoes mandatory. No rolling sleeves, no ties/watches/rings/necklace, repair torn, pack hair/scarves, safety mask/helmet/goggles/gloves.
• Hair/jewellery: Must be restrained/removed — can get caught and cause severe injury/death.
• Tools: Never use without instruction + permission, use good condition tools, report bad, never clean/adjust/lube while operating, never leave unattended, keep guards in place, keep area tidy, report all injuries.
• Arc welding safety: #10/12 filter, clear flip-up for chipping, insulate holder/cables/ground, never weld wet/damp, wool/cotton only, protect cables, secure work, metal container for stubs, turn off if electrode sticks, use pliers for hot metal, well ventilated (lead/zinc fumes toxic), no matches/lighters, clear flammables.
• Gas welding safety: #4 filter, same clothing, well ventilated, no matches/lighters, open acetylene ≤3/4 turn (quick close) and oxygen fully, never exceed 15 psi acetylene, tip away from body (gases saturate clothing), light with approved lighter, point flame safely, never leave lit torch, handle hot with pliers, check leaks, apron, no oil/grease + oxygen (explosive).`,

  'metal-joining': `METAL JOINING PROCESSES — Overview:
• Joints can be Temporary (bolting, riveting — cylindrical pin) for maintenance, or Permanent (soldering, welding, brazing) for high strength, no disassembly.
• Soldering: filler called Solder (lead-tin alloy, melts ~183°C, solidifies quickly) + flux (cleans oxides, e.g., Kline-brush), tool = soldering iron. Steps: Heat solder in flux, bring to iron until molten, fill space, clean residue. Applications: canned food (food industry), fine metals (jewelry), radiators/battery, electronics. Silver-soldering is stronger.
• Brazing: Filler metal melting point >400°C but below base metal, heated to suitable temperature, filler melts and joins. Examples: Aluminium, Silicon, Copper, Copper-zinc (kbras), gold, nickel, rare metals. Types: Furnace, Silver, Dip, Vacuum.
• Welding: Heat melts and fuses base + filler to form permanent joint. Types: Gas (oxy-acetylene) and Arc. Gas uses O₂ + acetylene, Arc uses electricity.

Exam tip: Temporary = bolts/nuts/rivets; Permanent = soldering (183°C, lead-tin) / brazing (>400°C) / welding (melts base).`,

  'gas-arc-welding': `GAS vs ARC WELDING — Detailed comparison:
• Gas Welding: Fusion process, heat from combustion of oxygen + fuel gas (acetylene, hydrogen, propene). Types: Oxy-Acetylene (most common, intense flame when O₂+acetylene in correct proportions), Air-Acetylene, Oxy-Hydrogen.
  Equipment: Gas Cylinders (O₂ 125 kg/cm², Acetylene 16 kg/cm²), Regulators (working: O₂ 1 kg/cm², Acetylene 0.15 kg/cm², varies with thickness), Gauges, Hoses, Torch, Check valve, Non-return valve, Caps, Wrench, Fusible plugs.
  Flame types by gas ratio: Neutral = 1:1 (50% O₂ / 50% acetylene) — hottest, blue outer, ideal; Carburizing/Reducing = excess acetylene (e.g., 70:30, 3 zones) — for Ni/Cr alloys; Oxidizing = excess oxygen — for brazing.
  Safety: Protect cylinders, separate empty/full, no oil/grease + oxygen (explosive), light acetylene first then oxygen slowly, correct goggles, never leave lit torch, check leaks, apron, ventilation.
• Arc Welding: Fusion process, heat from electric arc between base metal and electrode. Types: Metal Arc (most common, flux-coated), Submerged, TIG, MIG.
  Equipment: Generator (D.C.) or Transformer (A.C.), 2 cables, Holder, Electrode, Shield, Gloves, Brush, Chipping hammer, Goggles.
  Flame temps: Blue 5700°C, White inner 3200°C, Red intermediate 2500°C, Outer 1275°C.
  Advantages: Most efficient, lowest cost, lighter weight, joins all metals, design flexibility.
  Disadvantages: Manual high labor, high energy danger, not for disassembly, defects hard to detect.
  Applications: Automobile bodies, Aircraft frames, Railway wagons, Machine frames, Structural works, tanks, furniture, boilers, ship building.
  Positions: Flat, Horizontal, Vertical, Overhead (hardest). Electrode EXXXX: first 2 digits = tensile in ksi (60=60k psi), 3rd digit = position (1=all, 2=flat+horizontal, 3=flat only), 4th = coating. Example E6013 → 60 ksi, all positions, type 3.

Study tip: For any gas/arc question, first identify if it's about heat source (combustion vs arc), then equipment, then flame type by ratio, then safety.`
}

// Image mapping for AEE topics that need diagrams — prioritised for AEE
const TOPIC_IMAGES = {
  'hot-metal-working': '/images/anvil-diagram.png',
  'heat-treatment': '/images/anvil-diagram.png',
  'gas-arc-welding': '/images/flame-zones.png',
  'gas-welding': '/images/flame-zones.png',
  'arc-welding': '/images/flame-zones.png',
  'jigs-fixtures': '/images/jig-vs-fixture.png',
  'jig-fixture-design': '/images/jig-vs-fixture.png',
  'drilling': '/images/taper-pin.png',
  'cutting-tools': '/images/hacksaw-tpi.png',
  'welding-defects': '/images/welding-defects.png',
  'fasteners-bolts': '/images/taper-pin.png',
  'fasteners-rivets': '/images/jig-vs-fixture.png',
  'metal-shapes': '/images/hacksaw-tpi.png'
}

export default function StudyRunner() {
  const navigate = useNavigate()
  const [session, setSession] = useState(() => loadStudySession())
  const [index, setIndex] = useState(session?.index ?? 0)
  const [showSolution, setShowSolution] = useState(false)
  const [revealed, setRevealed] = useState({})

  if (!session) return <Navigate to="/dashboard" replace />

  const questions = session.questionSet
  const total = questions.length
  const q = questions[index]
  const deepDive = TOPIC_DEEP_DIVE[q.topicId] || `This topic covers ${q.topicId.replace(/-/g, ' ')}. Review the core definitions, formulas, and typical exam traps for this topic. Focus on understanding the *why* behind each option, not just memorizing the answer.`

  useEffect(() => {
    if (!session) return
    const next = { ...session, index }
    saveStudySession(next)
    setSession(next)
    setShowSolution(false)
  }, [index])

  function go(i) {
    if (i < 0 || i >= total) return
    setIndex(i)
  }

  function handleSeeExplanation() {
    setShowSolution(true)
    setRevealed(r => ({ ...r, [q.id]: true }))
  }

  function exitToDashboard() {
    navigate('/dashboard')
  }

  const pct = Math.round(((index + 1) / total) * 100)
  const topicImage = TOPIC_IMAGES[q.topicId]

  return (
    <div className="test-shell">
      <div className="test-topbar" style={{ background: 'linear-gradient(135deg, rgba(37,99,235,0.06), rgba(14,165,233,0.04))' }}>
        <div className="test-meta">
          <div>
            <div className="tm-title">{session.courseCode}{session.topicName ? ` · ${session.topicName}` : ' · Study Mode'} <span style={{ fontSize: 11, background: 'var(--primary)', color: '#fff', padding: '3px 8px', borderRadius: 999, marginLeft: 8, verticalAlign: 'middle' }}>STUDY MODE</span></div>
            <div className="tm-sub">Question {index + 1} of {total} · Correct answer already ticked · No timer</div>
          </div>
        </div>
        <div className="progress-wrap" style={{ minWidth: 180 }}>
          <div style={{ fontSize: 12, color: 'var(--muted)', fontWeight: 600 }}>PROGRESS</div>
          <div className="progress-bar"><div className="progress-fill" style={{ width: `${pct}%` }} /></div>
          <div style={{ fontSize: 11, color: 'var(--muted)', marginTop: 4 }}>{index + 1} / {total} · {Object.keys(revealed).length} explanations viewed</div>
        </div>
        <div className="flex gap-8">
          <button className="btn btn-ghost btn-sm" onClick={exitToDashboard}>Exit Study</button>
          <Link to="/dashboard" className="btn btn-primary btn-sm">New Study Set →</Link>
        </div>
      </div>

      <div className="test-body">
        <div className="qcard" style={{ borderLeft: '4px solid var(--primary)' }}>
          <div className="qhead">
            <span className="qindex">Study Question {index + 1} / {total}</span>
            <span className="qtopic">{q.topicId ? q.topicId.replace(/-/g, ' ') : 'Mixed topics'}</span>
          </div>
          <div className="qtext">{q.question}</div>

          {q.image && (
            <div style={{ margin: '16px 0', padding: 12, background: 'var(--bg-soft)', border: '1px solid var(--border)', borderRadius: 12, textAlign: 'center' }}>
              <img src={q.image} alt="Question diagram" style={{ maxWidth: '100%', maxHeight: 320, borderRadius: 8, border: '1px solid var(--border)' }} />
              <div style={{ fontSize: 12, color: 'var(--muted)', marginTop: 8 }}>Diagram for visual understanding — tap to zoom</div>
            </div>
          )}

          {topicImage && !q.image && (
            <div style={{ margin: '16px 0', padding: 12, background: 'var(--bg-soft)', border: '1px solid var(--border)', borderRadius: 12, textAlign: 'center', opacity: 0.9 }}>
              <div style={{ fontSize: 12, color: 'var(--muted)', marginBottom: 8, fontWeight: 600 }}>📐 Topic Diagram — {q.topicId.replace(/-/g, ' ')}</div>
              <img src={topicImage} alt={`${q.topicId} diagram`} style={{ maxWidth: '100%', maxHeight: 260, borderRadius: 8, border: '1px solid var(--border)' }} />
            </div>
          )}

          <div className="options">
            {q.options.map((opt, i) => {
              const isCorrect = i === q.correct
              return (
                <div
                  key={i}
                  className={`option ${isCorrect ? 'selected' : ''}`}
                  style={isCorrect ? { borderColor: 'var(--green)', background: 'var(--green-soft)', cursor: 'default' } : { cursor: 'default', opacity: 0.9 }}
                >
                  <span className="opt-key" style={isCorrect ? { background: 'var(--green)', color: '#fff', borderColor: 'var(--green)' } : {}}>{LETTERS[i]}</span>
                  <span style={{ flex: 1 }}>{opt}</span>
                  {isCorrect && <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--green)', background: '#fff', padding: '3px 8px', borderRadius: 999, border: '1px solid var(--green)' }}>✓ Correct</span>}
                </div>
              )
            })}
          </div>

          <div style={{ marginTop: 22, display: 'flex', gap: 12, flexWrap: 'wrap' }}>
            <button className="btn btn-primary" onClick={handleSeeExplanation} style={{ flex: 1, minWidth: 200 }}>
              {showSolution ? '✓ Explanation below — scroll down' : 'See Detailed Explanation →'}
            </button>
            <button className="btn btn-ghost" onClick={() => go(index + 1)} disabled={index === total - 1}>
              Next Question →
            </button>
          </div>

          <div className="ri-short" style={{ marginTop: 18, background: 'var(--card-2)' }}>
            <strong>Quick tip:</strong> {q.short}
          </div>

          {showSolution && (
            <div style={{ marginTop: 18, padding: 20, background: 'linear-gradient(135deg, rgba(37,99,235,0.06), rgba(14,165,233,0.04))', border: '1px solid var(--border)', borderRadius: 12 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
                <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>📖 Study Mode — Very Detailed Explanation</div>
                <span className="qtopic" style={{ background: 'var(--green-soft)', color: 'var(--green)', borderColor: 'rgba(5,150,105,0.2)' }}>Correct: {LETTERS[q.correct]}. {q.options[q.correct]}</span>
              </div>
              <div className="panel-sol" style={{ whiteSpace: 'pre-wrap', background: '#fff' }}>
                {q.solution}
                <div style={{ marginTop: 18, paddingTop: 18, borderTop: '1px dashed var(--border)' }}>
                  <div style={{ fontWeight: 700, color: 'var(--text)', marginBottom: 8 }}>📚 Deep Dive — More on {q.topicId.replace(/-/g, ' ')}:</div>
                  <div style={{ fontSize: 14, lineHeight: 1.7, color: 'var(--text)', whiteSpace: 'pre-wrap' }}>
                    {deepDive}
                  </div>
                </div>
              </div>
              {(q.image || topicImage) && (
                <div style={{ marginTop: 16, padding: 12, background: '#fff', border: '1px solid var(--border)', borderRadius: 10, textAlign: 'center' }}>
                  <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--muted)', marginBottom: 8 }}>🖼️ Visual Reference — {q.topicId.replace(/-/g, ' ')}</div>
                  <img src={q.image || topicImage} alt="Deep dive diagram" style={{ maxWidth: '100%', maxHeight: 320, borderRadius: 8 }} />
                </div>
              )}
              <div style={{ marginTop: 14, display: 'flex', gap: 10 }}>
                <button className="btn btn-ghost btn-sm" onClick={() => setShowSolution(false)}>Hide explanation</button>
                <button className="btn btn-primary btn-sm" onClick={() => go(index + 1)} disabled={index === total - 1}>Next →</button>
              </div>
            </div>
          )}

          <div className="qnav" style={{ marginTop: 24, borderTop: '1px solid var(--border)', paddingTop: 16 }}>
            <button className="btn btn-ghost" onClick={() => go(index - 1)} disabled={index === 0}>← Previous</button>
            <span style={{ fontSize: 12, color: 'var(--muted)' }}>Study Mode · No timer · Correct already ticked</span>
            {index < total - 1 ? (
              <button className="btn btn-primary" onClick={() => go(index + 1)}>Next →</button>
            ) : (
              <button className="btn btn-ghost" onClick={exitToDashboard}>Back to Dashboard</button>
            )}
          </div>
        </div>

        <div className="palette">
          <h4>Study Navigator</h4>
          <div className="palette-grid">
            {questions.map((qq, i) => {
              const cls = [
                'pcell',
                revealed[qq.id] ? 'answered' : '',
                i === index ? 'current' : ''
              ].filter(Boolean).join(' ')
              return (
                <button key={qq.id} className={cls} onClick={() => go(i)} title={`Question ${i + 1} ${revealed[qq.id] ? '(viewed)' : ''}`}>
                  {i + 1}
                </button>
              )
            })}
          </div>
          <div className="palette-legend">
            <span><span className="legend-dot" style={{ background: 'var(--green-soft)', border: '1px solid rgba(5,150,105,0.4)' }} />Viewed</span>
            <span><span className="legend-dot" style={{ background: 'var(--primary)' }} />Current</span>
          </div>
          <div style={{ marginTop: 18, padding: 12, background: 'var(--primary-soft)', borderRadius: 10, border: '1px solid rgba(37,99,235,0.12)' }}>
            <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--primary)' }}>💡 How Study Mode works</div>
            <div style={{ fontSize: 12, color: 'var(--muted)', marginTop: 6, lineHeight: 1.5 }}>
              No timer. Correct answer is pre-ticked in green. Tap <strong>See Detailed Explanation</strong> for the very long, topic-focused deep dive — longer than Test Mode — with diagrams where needed.
            </div>
          </div>
          <p className="muted" style={{ fontSize: 12, marginTop: 12, lineHeight: 1.5 }}>
            Go at your own pace. No auto-save timer, no pressure.
          </p>
        </div>
      </div>
    </div>
  )
}
