#!/usr/bin/env python3
"""Build EEE 202 (Applied Electricity II) — optimised for a WRITTEN,
calculation-heavy exam. Every calculation question carries a full
'Given → Formula → Substitute → Answer' worked solution that can be
reproduced on paper. Theory questions cover the high-yield definitions,
laws and comparisons from the lecture notes.
Emits .eee202_out.json"""

import json

# ---------------------------------------------------------------- helpers ---
def first_sentence(exp):
    s = exp.strip()
    for i, ch in enumerate(s):
        if ch in ".!?" and i > 25:
            return s[: i + 1]
    return s[:150]

QUESTIONS = []

def calc(topic, q, opts, ans, work):
    """Calculation question with written-exam style solution."""
    sol = (
        "WORKED SOLUTION (write this out in the exam):\n" + work
        + "\n\n📘 From the EEE 202 lecture notes — this mirrors the solved exercises in "
        "the magnetism/revision notes; in the written exam, show the formula first, "
        "then the substitution, then the answer with its unit."
    )
    QUESTIONS.append(dict(topicId=topic, kind="calc", question=q, options=opts,
                          correct=ans, short=first_sentence(work), solution=sol))

def theory(topic, q, opts, ans, exp):
    sol = (
        exp
        + "\n\n📘 From the EEE 202 notes — examiners set short theory questions like "
        "this to test definitions, laws and comparisons. Learn the key phrase so you "
        "can state it in one or two sentences."
    )
    QUESTIONS.append(dict(topicId=topic, kind="theory", question=q, options=opts,
                          correct=ans, short=first_sentence(exp), solution=sol))

# ================================================================
# TOPIC 1 — Magnetism & Moving Charges
# ================================================================
T = "eee-magnetism"

theory(T, "Magnetism is best defined as:",
       ["the force produced by moving charges that attracts or repels other magnets and moving charges",
        "the force between two stationary charges",
        "the ability of a material to conduct electricity",
        "the resistance of a material to being magnetised"],
       0,
       "The notes define magnetism as the force produced by a moving charge which attracts or repels other magnets and moving charges; it is the phenomenon associated with magnetic fields, which are themselves produced by moving electric charges.")

theory(T, "For any two magnetic poles:",
       ["like poles repel each other and opposite poles attract each other",
        "like poles attract each other and opposite poles repel each other",
        "all poles attract each other",
        "poles neither attract nor repel"],
       0,
       "The notes state: like poles repel each other; opposite poles attract each other.")

theory(T, "The phenomenon of magnetism was first observed in a naturally occurring material called:",
       ["Hematite (Fe2O3)", "Magnetite (Fe3O4)", "Bauxite (Al2O3)", "Calcite (CaCO3)"],
       1,
       "The notes state that the property of magnetism was first observed in a material called magnetite (Fe₃O₄) — hence the name 'magnets' — scattered around the Earth's crust.")

theory(T, "Materials in which the electrons are arranged so that their magnetic effects do NOT cancel out are called:",
       ["diamagnetic materials", "ferromagnetic materials", "insulators", "semiconductors"],
       1,
       "In ferromagnetic materials the electron magnets do not cancel; they act as permanent magnets and attract other metallic materials naturally.")

theory(T, "Electromotive force (e.m.f.) is that which:",
       ["tends to produce an electric current in a circuit", "opposes the flow of current", "measures the resistance of a circuit", "stores charge in a capacitor"],
       0,
       "Per the notes: an electromotive force is that which tends to produce an electric current in a circuit; symbol E, unit volt (V).")

theory(T, "Which of the following is NOT listed as a principal source of e.m.f.?",
       ["Electrodes of dissimilar materials immersed in an electrolyte (cells)",
        "Relative movement of a conductor and a magnetic flux (generators)",
        "Difference of temperature between junctions of dissimilar metals (thermo-junctions)",
        "Friction between two insulators"],
       3,
       "The notes list three principal sources of e.m.f.: (1) electrodes in an electrolyte (cells/batteries), (2) relative movement of a conductor and magnetic flux (generators), and (3) temperature difference at thermo-junctions. Friction between insulators is not among them.")

theory(T, "The force on a moving charge in a magnetic field is given by:",
       ["F = q × v × B × sin θ", "F = q × v × B × cos θ", "F = qE", "F = m × B × sin θ"],
       0,
       "The notes give the magnetic force on a moving charge as F = q × v × B × sin θ, where q is the charge, v its velocity, B the magnetic field and θ the angle between the field and the velocity.")

theory(T, "Which rule is used to determine the direction of the force on a moving charge in a magnetic field?",
       ["Left-hand motor rule only", "Right-hand rule", "Ohm's rule", "Kirchhoff's rule"],
       1,
       "The notes use the right-hand rule: point the index finger along the charge's motion, rotate the middle finger (direction of B) away from it, and the thumb (perpendicular to the plane they make) gives the direction of F for a positive charge.")

theory(T, "Which of the following is NOT listed among the uses of magnets?",
       ["Magnetic compass for direction", "Speakers and electric motors/dynamos", "Maglev trains and electromagnets", "Storing electric charge in cells"],
       3,
       "The notes list compasses, speakers, electric motors and dynamos, maglev trains, construction industry and magnetic separation of objects. Magnets do not store charge in cells.")

theory(T, "The B-field and the H-field are distinguished as follows:",
       ["B-field is defined by the force it exerts on a moving charged particle; H-field is the magnetic field within a material",
        "B-field is measured in A/m and H-field in tesla",
        "H-field is defined by force on a moving charge and B-field within a material",
        "They are the same quantity with different names"],
       0,
       "Per the notes: the B-field is the magnetic field defined by the force it exerts on a moving charged particle (measured in tesla, T), while the H-field is the magnetic field within a material rather than a vacuum (measured in ampere/metre, A/m).")

theory(T, "In the CGS system, 1 tesla equals:",
       ["10,000 gauss", "1,000 gauss", "100 gauss", "10 gauss"],
       0,
       "The notes give 1 T = 10,000 G; and 1 oersted ≈ 79.577 A/m (1000/4π A/m).")

theory(T, "Which statement about magnetic field lines is FALSE?",
       ["They never cross each other",
        "They form closed loops",
        "When parallel they repel one another",
        "They originate from the south pole and end at the north pole inside the magnet"],
       3,
       "Magnetic field lines never cross, form closed loops, repel when parallel, and OUTSIDE the magnet run north to south (inside the magnet they run south to north to close the loop). The false statement is that inside the magnet they originate at the south pole and end at the north pole — inside the magnet the lines run south→north, which closes the loop.")

theory(T, "Around a straight current-carrying conductor, the magnetic field lines are:",
       ["concentric circles centred on the conductor", "straight lines parallel to the conductor", "radial lines pointing outward", "elliptical loops crossing each other"],
       0,
       "The notes state that for a straight current-carrying conductor the field lines are concentric circles; the direction follows the right-hand (thumb) rule and reverses when the current direction reverses.")

theory(T, "An electromagnet is:",
       ["a permanent magnet made of magnetite",
        "a temporary magnet, typically a coil wrapped over a soft iron core (e.g. a solenoid)",
        "a magnet that needs no current",
        "a magnet made of copper wire only"],
       1,
       "Per the notes, an electromagnet is a temporary magnet formed by current passing through a coil wrapped over a soft iron core (for example, a solenoid).")

theory(T, "Magnetic field intensity (H) is defined as:",
       ["the magnetomotive force (MMF) needed to create a flux density B inside a material per unit length of that material",
        "the force on a unit charge at rest",
        "the flux passing through a unit area",
        "the current flowing per unit area of the conductor"],
       0,
       "H denotes the strength of the magnetic field; it is the MMF needed to create a flux density B inside a material per unit length, with unit ampere/metre (A/m).")

calc(T, "A charged particle with q = 40 C travels at 5 m/s in a magnetic field of 2 T, with the field direction the SAME as the particle's path. The magnetic force on the particle is:",
     ["0 N", "400 N", "200 N", "80 N"],
     0,
     "Given: q = 40 C, v = 5 m/s, B = 2 T, and the field is along the particle's path, so θ = 0°.\nFormula: F = q × v × B × sin θ.\nSubstitute: F = 40 × 5 × 2 × sin 0° = 400 × 0 = 0 N.\nAnswer: 0 N (a charge moving PARALLEL to the field feels no magnetic force).")

calc(T, "A charged particle with q = 4 C travels at v = 20 m/s in a magnetic field B = 10 T at an angle of 30° between v and B. The magnetic force is:",
     ["400 N", "800 N", "692.8 N", "200 N"],
     0,
     "Given: q = 4 C, v = 20 m/s, B = 10 T, θ = 30°.\nFormula: F = q × v × B × sin θ.\nSubstitute: F = 4 × 20 × 10 × sin 30° = 800 × 0.5 = 400 N.\nAnswer: 400 N.")

calc(T, "A conductor of length 0.5 m carrying current i lies in a magnetic field B = 3 T at θ = 30° and experiences a force of 12 N. The current is:",
     ["16 A", "8 A", "4 A", "24 A"],
     0,
     "Given: F = 12 N, l = 0.5 m, B = 3 T, θ = 30°.\nFormula: F = B I l sin θ.\nSubstitute: 12 = I × 3 × 0.5 × sin 30° = I × 0.75 → I = 12 / 0.75 = 16 A.\nAnswer: 16 A.")

calc(T, "A straight conductor of length 2 m carries 3 A perpendicular to a magnetic field of 1.5 T. The force on the conductor is:",
     ["9 N", "4.5 N", "6 N", "0 N"],
     0,
     "Given: l = 2 m, I = 3 A, B = 1.5 T, θ = 90°.\nFormula: F = B I l sin θ.\nSubstitute: F = 1.5 × 3 × 2 × sin 90° = 9 N.\nAnswer: 9 N.")

calc(T, "A 2 m long solenoid has 2000 loops and carries 1600 A. The magnetic field strength at its centre is: (μ₀ = 4π × 10⁻⁷ T·m/A)",
     ["2.01 T", "0.31 T", "1.00 T", "4.02 T"],
     0,
     "Given: L = 2 m, N = 2000, I = 1600 A.\nFormula: B = μ₀ × n × I, with n = N/L = 2000/2 = 1000 turns/m.\nSubstitute: B = (4π × 10⁻⁷) × 1000 × 1600 = 2.0106 T ≈ 2.01 T.\nAnswer: 2.01 T.")

calc(T, "A 5 m long solenoid of 800 loops carries 1700 A. The magnetic field strength at its centre is about:",
     ["0.34 T", "0.31 T", "0.59 T", "0.68 T"],
     0,
     "Given: N = 800, L = 5 m, I = 1700 A.\nFormula: B = μ₀ × n × I, n = 800/5 = 160 turns/m.\nSubstitute: B = (4π × 10⁻⁷) × 160 × 1700 = 12.566 × 10⁻⁷ × 272 000 = 0.3418 T ≈ 0.34 T.\n(Note: the notes print 0.314 T; the exact product is 0.342 T.)\nAnswer: about 0.34 T.")

calc(T, "A 12 m long solenoid of 700 loops carries 800 A. The magnetic field strength at its centre is about:",
     ["0.0586 T", "0.586 T", "0.0293 T", "0.117 T"],
     0,
     "Given: N = 700, L = 12 m, I = 800 A.\nFormula: B = μ₀ × n × I, n = 700/12 = 58.33 turns/m.\nSubstitute: B = (4π × 10⁻⁷) × 58.33 × 800 = 0.05864 T.\nAnswer: 0.05864 T ≈ 0.0586 T.")

calc(T, "A coil of 50 turns is in a field whose flux density changes at 0.10 T/s. The induced e.m.f. is:",
     ["5 V", "0.5 V", "50 V", "0.002 V"],
     0,
     "Given: N = 50 turns, dΦ/dt = 0.10 T·m²/s.\nFormula (Faraday's 2nd law): E = N × (dΦ/dt).\nSubstitute: E = 50 × 0.10 = 5 V.\nAnswer: 5 V (the minus sign in E = −N dΦ/dt only indicates direction — Lenz's law).")

calc(T, "A single loop of wire is in a field whose flux increases at 0.02 T·m²/s. The loop's resistance is 5 Ω. The induced current is:",
     ["4 mA", "0.4 mA", "40 mA", "0.1 A"],
     0,
     "Given: N = 1, dΦ/dt = 0.02 T·m²/s, R = 5 Ω.\nStep 1: E = N × (dΦ/dt) = 1 × 0.02 = 0.02 V.\nStep 2 (Ohm's law): I = E/R = 0.02 / 5 = 0.004 A.\nAnswer: 0.004 A = 4 mA.")

calc(T, "A coil of 100 turns has its flux per turn decrease uniformly from 0.5 Wb to 0 Wb in 0.2 s. The induced e.m.f. is:",
     ["250 V", "25 V", "100 V", "2.5 V"],
     0,
     "Given: N = 100, ΔΦ = 0.5 − 0 = 0.5 Wb, Δt = 0.2 s.\nFormula: E = N × (ΔΦ/Δt).\nSubstitute: E = 100 × (0.5/0.2) = 100 × 2.5 = 250 V.\nAnswer: 250 V.")

calc(T, "A rectangular coil of 20 turns, each of area 0.1 m², sits in a field B = 0.5 T. It is rotated so the flux changes from BA to zero in 0.05 s. The average induced e.m.f. is:",
     ["20 V", "10 V", "2 V", "40 V"],
     0,
     "Given: N = 20, A = 0.1 m², B = 0.5 T, Δt = 0.05 s.\nStep 1: initial flux Φ = B A = 0.5 × 0.1 = 0.05 Wb; final flux = 0.\nStep 2: E = N × (ΔΦ/Δt) = 20 × (0.05/0.05) = 20 V.\nAnswer: 20 V.")

calc(T, "A coil of 80 turns has its flux decrease uniformly from 0.6 Wb to 0 Wb in 0.3 s. The induced e.m.f. is:",
     ["160 V", "16 V", "60 V", "26.7 V"],
     0,
     "Given: N = 80, ΔΦ = 0.6 Wb, Δt = 0.3 s.\nFormula: E = N × (ΔΦ/Δt).\nSubstitute: E = 80 × (0.6/0.3) = 80 × 2 = 160 V.\nAnswer: 160 V.")

calc(T, "A single-turn circular loop of radius 0.1 m sits perpendicular to a field of 0.8 T which is reduced to zero in 0.2 s. The induced e.m.f. is about: (π = 3.14)",
     ["0.126 V", "1.26 V", "0.063 V", "0.25 V"],
     0,
     "Given: N = 1, r = 0.1 m, B = 0.8 T, Δt = 0.2 s.\nStep 1: area A = πr² = 3.14 × 0.01 = 0.0314 m²; flux Φ = B A = 0.8 × 0.0314 = 0.02513 Wb.\nStep 2: E = N × (ΔΦ/Δt) = 1 × 0.02513/0.2 = 0.1257 V.\nAnswer: ≈ 0.126 V.")

calc(T, "A coil of 50 turns is in a field changing at 0.15 T/s and its resistance is 10 Ω. The induced current is:",
     ["0.75 A", "7.5 A", "0.075 A", "1.5 A"],
     0,
     "Given: N = 50, dΦ/dt = 0.15 T/s, R = 10 Ω.\nStep 1: E = N × (dΦ/dt) = 50 × 0.15 = 7.5 V.\nStep 2: I = E/R = 7.5/10 = 0.75 A.\nAnswer: 0.75 A.")

calc(T, "A coil of 200 turns is in a field changing at 0.05 T/s. The induced e.m.f. is:",
     ["10 V", "1 V", "100 V", "0.1 V"],
     0,
     "Formula: E = N × (dΦ/dt).\nSubstitute: E = 200 × 0.05 = 10 V.\nAnswer: 10 V.")

calc(T, "A flux density of 1.2 T passes through an area of 0.05 m². The flux is:",
     ["0.06 Wb", "0.6 Wb", "6 Wb", "0.006 Wb"],
     0,
     "Formula: Φ = B A.\nSubstitute: Φ = 1.2 × 0.05 = 0.06 Wb.\nAnswer: 0.06 Wb.")

calc(T, "A 500-turn solenoid 1 m long carries 4 A. The field at its centre is about: (μ₀ = 4π × 10⁻⁷)",
     ["2.51 mT", "25.1 mT", "0.25 mT", "5.03 mT"],
     0,
     "Formula: B = μ₀ × n × I, n = N/L = 500 turns/m.\nSubstitute: B = (4π × 10⁻⁷) × 500 × 4 = 12.566 × 10⁻⁷ × 2000 = 2.51 × 10⁻³ T.\nAnswer: 2.51 mT.")

calc(T, "A charge of 5 C moves at 4 m/s at 90° to a field of 0.3 T. The magnetic force is:",
     ["6 N", "0.6 N", "60 N", "0 N"],
     0,
     "Formula: F = q × v × B × sin θ.\nSubstitute: F = 5 × 4 × 0.3 × sin 90° = 6 N.\nAnswer: 6 N.")

calc(T, "A bar magnet moved towards a 40-turn coil increases the linked flux from 0 to 0.2 Wb in 0.05 s. With a coil resistance of 8 Ω, the induced e.m.f. and current are:",
     ["160 V and 20 A", "16 V and 2 A", "8 V and 1 A", "320 V and 40 A"],
     0,
     "Given: N = 40, ΔΦ = 0.2 Wb, Δt = 0.05 s, R = 8 Ω.\nStep 1: E = N × (ΔΦ/Δt) = 40 × (0.2/0.05) = 40 × 4 = 160 V.\nStep 2: I = E/R = 160/8 = 20 A.\nAnswer: 160 V and 20 A.")

calc(T, "A charge of 2 C moves at 10 m/s PERPENDICULAR to a magnetic field of 0.5 T. The magnetic force is:",
     ["10 N", "5 N", "20 N", "0 N"],
     0,
     "Given: q = 2 C, v = 10 m/s, B = 0.5 T, θ = 90°.\nFormula: F = q × v × B × sin θ.\nSubstitute: F = 2 × 10 × 0.5 × sin 90° = 10 N.\nAnswer: 10 N.")

theory(T, "Eddy currents (Foucault currents) are:",
       ["loops of current induced in a conductor by a changing magnetic field, opposing the change per Lenz's law",
        "the main working current of a transformer",
        "currents that only flow in superconductors",
        "currents produced by batteries"],
       0,
       "Eddy currents are loops of electric current induced in a conductor placed in a changing magnetic field; they create a field opposing the change (Lenz's law). Applications listed include AC generators, transformers and magnetic flow meters.")

theory(T, "Faraday's First Law of electromagnetic induction states that:",
       ["an e.m.f. is induced in a conductor whenever it is placed in a changing magnetic field, and a current flows if the circuit is closed",
        "the induced e.m.f. equals the rate of change of flux linkage",
        "the induced current opposes its cause",
        "a current-carrying conductor experiences a force in a magnetic field"],
       0,
       "First law: whenever a conductor is placed in a changing magnetic field, an e.m.f. is induced; if the conductor forms a closed circuit, an induced current flows. (The second law quantifies it: E = N dΦ/dt; Lenz's law gives the direction.)")

theory(T, "Faraday's Second Law states that the magnitude of the induced e.m.f. is:",
       ["equal to the rate of change of magnetic flux linked with the conductor",
        "equal to the magnetic flux itself",
        "inversely proportional to the number of turns",
        "independent of the flux change"],
       0,
       "Second law: the induced e.m.f. equals the rate of change of flux linkage, E = N × (dΦ/dt). More turns or faster flux change → larger voltage.")

theory(T, "Comparing a magnetic field and an electric field, which statement is correct?",
       ["A magnetic field is produced by moving charges or changing electric fields; an electric field is produced by static charges or changing magnetic fields",
        "Both fields do work on static charges",
        "A magnetic field interacts with static charges",
        "An electric field cannot do work on charges"],
       0,
       "Per the comparison table: magnetic fields are produced by moving charges/changing E-fields and do NOT interact with static charges or do work on them; electric fields are produced by static charges/changing magnetic fields and do work on charges.")

# ================================================================
# TOPIC 2 — AC Waveforms & Phasors
# ================================================================
T = "eee-ac-phasors"

theory(T, "Direct current (D.C.) is described as:",
       ["a uni-directional supply whose value does not change with time",
        "a bi-directional supply varying in magnitude and direction",
        "a supply that reverses every half cycle",
        "a time-varying sinusoidal supply"],
       0,
       "D.C. flows in one direction only — a fixed magnitude and definite direction (e.g. +12 V), produced by batteries, dynamos, solar cells; it stays constant unless the connections are physically reversed.")

theory(T, "An alternating (AC) waveform is defined as one that:",
       ["varies in both magnitude and direction in an even manner with respect to time",
        "flows in one direction only",
        "never changes polarity",
        "has a fixed magnitude at all times"],
       0,
       "AC varies in both magnitude and direction with time — a 'bi-directional' waveform; the most common form is the sinusoidal waveform (sine wave).")

theory(T, "The general expression of a sinusoidal AC quantity is:",
       ["A(t) = Aₘ sin(2πft)", "A(t) = Aₘ × e⁻ᵗ", "A(t) = Aₘ/t", "A(t) = Aₘ sin(t)/(2πf)"],
       0,
       "A sinusoid is defined as A(t) = Aₘ sin(2πft), where Aₘ is the amplitude and f the frequency.")

theory(T, "The Period (T) of an AC waveform is:",
       ["the time in seconds the waveform takes to repeat itself from start to finish",
        "the number of times the waveform repeats in one second",
        "the peak amplitude of the waveform",
        "half the frequency"],
       0,
       "Period T = the time for one complete cycle (also called the periodic time for sine waves, or pulse width for square waves). Frequency f = 1/T.")

theory(T, "The frequency (f) of a waveform is:",
       ["the number of times the waveform repeats itself within one second, and is the reciprocal of the period (f = 1/T)",
        "the time taken for one full cycle",
        "the amplitude divided by the period",
        "the peak-to-peak voltage"],
       0,
       "Frequency is the number of cycles per second: f = 1/T, with unit hertz (Hz).")

theory(T, "The Amplitude (A) of an AC waveform is:",
       ["the magnitude or intensity of the signal measured in volts or amps",
        "the time for one cycle",
        "the number of cycles per second",
        "the zero line of the waveform"],
       0,
       "Amplitude is the magnitude/intensity of the waveform (its peak value), measured in volts or amps. Any part above the zero axis is flow in one direction, below it in the opposite direction.")

theory(T, "The phasor method of analysing AC networks was made famous by:",
       ["Charles P. Steinmetz (General Electric, 1893)", "Thomas Edison", "Nikola Tesla", "James Maxwell"],
       0,
       "When General Electric acquired a small firm in 1893 it gained the services of Charles P. Steinmetz, whose mathematical dissertation work on the symbolic (phasor) method made him famous and revolutionised AC analysis.")

theory(T, "A phasor is best described as:",
       ["a rotating vector that represents the magnitude and phase of a sinusoidal quantity",
        "a scalar representing only the amplitude",
        "a constant equal to the r.m.s. value",
        "a unit vector along the x-axis"],
       0,
       "A phasor is a rotating vector whose length gives the magnitude and whose angle gives the phase of the sinusoid — allowing AC quantities to be added/subtracted as vectors instead of by trigonometry.")

theory(T, "Which statement about AC versus DC power systems (from the reference material) is correct?",
       ["By 1884 the DC system of Edison was established, but AC later became the world standard because its voltage can be stepped up/down with transformers",
        "DC was adopted as the world standard because it could be transformed easily",
        "AC cannot be transmitted over long distances",
        "Batteries back up AC generators better than DC"],
       0,
       "Edison's DC system dominated by 1884, but after the 1891 Frankfurt exhibition the AC system — with its transformer-based voltage transformation for efficient long-distance transmission — became the world standard.")

theory(T, "Which statement about alternating quantities is correct?",
       ["They cannot be stored in batteries or cells like DC; they are generated by alternators or waveform generators when needed",
        "They are stored in batteries",
        "They are cheaper to store than to generate",
        "They always have zero frequency"],
       0,
       "Alternating voltages/currents cannot be stored in batteries or cells; it is easier and cheaper to generate them with alternators or waveform generators when needed.")

calc(T, "A sinusoidal voltage has a period of 20 ms. Its frequency is:",
     ["50 Hz", "20 Hz", "500 Hz", "0.05 Hz"],
     0,
     "Given: T = 20 ms = 0.02 s.\nFormula: f = 1/T.\nSubstitute: f = 1/0.02 = 50 Hz.\nAnswer: 50 Hz (the domestic mains frequency).")

calc(T, "A sine wave has a frequency of 1 kHz. Its period is:",
     ["1 ms", "1 s", "0.1 ms", "10 ms"],
     0,
     "Given: f = 1000 Hz.\nFormula: T = 1/f.\nSubstitute: T = 1/1000 = 0.001 s = 1 ms.\nAnswer: 1 ms.")

calc(T, "A mains voltage has a peak value Vₘ = 311 V. Its r.m.s. value is about:",
     ["220 V", "311 V", "440 V", "156 V"],
     0,
     "Formula: Vᵣₘₛ = Vₘ/√2 = 0.707 × Vₘ.\nSubstitute: Vᵣₘₛ = 311 × 0.707 = 219.9 V ≈ 220 V.\nAnswer: 220 V.")

calc(T, "A supply is specified as 230 V r.m.s. Its peak value is about:",
     ["325 V", "163 V", "230 V", "460 V"],
     0,
     "Formula: Vₘ = Vᵣₘₛ × √2 = 1.414 × Vᵣₘₛ.\nSubstitute: Vₘ = 230 × 1.414 = 325.2 V.\nAnswer: ≈ 325 V.")

calc(T, "An inductor L = 0.1 H is connected across a 50 Hz supply. Its inductive reactance is: (π = 3.14)",
     ["31.4 Ω", "3.14 Ω", "62.8 Ω", "314 Ω"],
     0,
     "Formula: Xₗ = 2πfL.\nSubstitute: Xₗ = 2 × 3.14 × 50 × 0.1 = 31.4 Ω.\nAnswer: 31.4 Ω.")

calc(T, "A capacitor C = 100 µF is connected across a 50 Hz supply. Its capacitive reactance is about: (π = 3.14)",
     ["31.8 Ω", "318 Ω", "3.18 Ω", "15.9 Ω"],
     0,
     "Formula: XC = 1/(2πfC).\nSubstitute: XC = 1/(2 × 3.14 × 50 × 100 × 10⁻⁶) = 1/0.0314 = 31.85 Ω.\nAnswer: ≈ 31.8 Ω.")

calc(T, "A coil of resistance R = 3 Ω and inductive reactance Xₗ = 4 Ω is connected in series across an AC supply. The magnitude of its impedance is:",
     ["5 Ω", "7 Ω", "1 Ω", "12 Ω"],
     0,
     "Formula: Z = R + jXₗ, with magnitude |Z| = √(R² + Xₗ²).\nSubstitute: |Z| = √(3² + 4²) = √(9 + 16) = √25 = 5 Ω.\nAnswer: 5 Ω.")

calc(T, "A series circuit has R = 30 Ω and XC = 40 Ω. Its impedance magnitude is:",
     ["50 Ω", "70 Ω", "10 Ω", "35 Ω"],
     0,
     "Formula: Z = R − jXC, |Z| = √(R² + XC²).\nSubstitute: |Z| = √(30² + 40²) = √(900 + 1600) = √2500 = 50 Ω.\nAnswer: 50 Ω.")

calc(T, "A sine wave has a peak value of 100 V. Its average (mean) value over a half cycle is about:",
     ["63.7 V", "70.7 V", "100 V", "50 V"],
     0,
     "Formula: Vₐᵥₑ = 0.637 × Vₘ.\nSubstitute: Vₐᵥₑ = 0.637 × 100 = 63.7 V.\nAnswer: 63.7 V.")

calc(T, "A 50 Hz supply has an angular frequency ω of: (π = 3.14)",
     ["314 rad/s", "157 rad/s", "628 rad/s", "31.4 rad/s"],
     0,
     "Formula: ω = 2πf.\nSubstitute: ω = 2 × 3.14 × 50 = 314 rad/s.\nAnswer: 314 rad/s.")

theory(T, "In an AC circuit, the r.m.s. (effective) value of a current is:",
       ["the value of DC that would produce the same heating effect in the same resistance",
        "the peak value divided by π",
        "the average value over a full cycle",
        "always larger than the peak value"],
       0,
       "The r.m.s. value is the equivalent DC value that produces the same heating effect; for a sine wave Vᵣₘₛ = Vₘ/√2 = 0.707 × Vₘ (the average over a FULL cycle is zero, over a half cycle 0.637 × Vₘ).")

calc(T, "An inductor L = 0.2 H is connected across a 50 Hz supply. Its inductive reactance is: (π = 3.14)",
     ["62.8 Ω", "31.4 Ω", "6.28 Ω", "125.6 Ω"],
     0,
     "Formula: Xₗ = 2πfL.\nSubstitute: Xₗ = 2 × 3.14 × 50 × 0.2 = 62.8 Ω.\nAnswer: 62.8 Ω.")

calc(T, "A capacitor C = 10 µF is connected across a 50 Hz supply. Its capacitive reactance is about:",
     ["318 Ω", "31.8 Ω", "3180 Ω", "159 Ω"],
     0,
     "Formula: XC = 1/(2πfC).\nSubstitute: XC = 1/(2 × 3.14 × 50 × 10 × 10⁻⁶) = 1/0.00314 = 318.5 Ω.\nAnswer: ≈ 318 Ω.")

calc(T, "A series circuit has R = 8 Ω and XC = 6 Ω. The magnitude of its impedance is:",
     ["10 Ω", "14 Ω", "2 Ω", "48 Ω"],
     0,
     "Formula: |Z| = √(R² + XC²).\nSubstitute: |Z| = √(8² + 6²) = √(64 + 36) = √100 = 10 Ω.\nAnswer: 10 Ω.")

calc(T, "A US-style supply has Vᵣₘₛ = 110 V. Its peak value is about:",
     ["155.6 V", "77.8 V", "110 V", "220 V"],
     0,
     "Formula: Vₘ = √2 × Vᵣₘₛ = 1.414 × Vᵣₘₛ.\nSubstitute: Vₘ = 1.414 × 110 = 155.5 V.\nAnswer: ≈ 155.6 V.")

calc(T, "A waveform has a period of 2 ms. Its frequency is:",
     ["500 Hz", "200 Hz", "50 Hz", "2 kHz"],
     0,
     "Formula: f = 1/T.\nSubstitute: f = 1/(2 × 10⁻³) = 500 Hz.\nAnswer: 500 Hz.")

calc(T, "A mains sine wave has Vₘ = 311 V. Its average value over a half cycle is about:",
     ["198 V", "220 V", "311 V", "440 V"],
     0,
     "Formula: Vₐᵥₑ = 0.637 × Vₘ.\nSubstitute: Vₐᵥₑ = 0.637 × 311 = 198.1 V.\nAnswer: ≈ 198 V (while Vᵣₘₛ = 0.707 × 311 ≈ 220 V).")

# ================================================================
# TOPIC 3 — Resonance in AC Circuits
# ================================================================
T = "eee-resonance"

theory(T, "Series resonance occurs in an R-L-C series circuit when:",
       ["Xₗ = XC", "R = Xₗ", "R = XC", "the supply voltage is zero"],
       0,
       "At series resonance the inductive and capacitive reactances cancel: Xₗ = XC, leaving Z = R (minimum impedance) and maximum current.")

theory(T, "At series resonance, the impedance of the R-L-C circuit is:",
       ["minimum and equal to R", "maximum and equal to Xₗ", "equal to XC", "infinite"],
       0,
       "Since Xₗ = XC, Z = R + j(Xₗ − XC) = R — the impedance is a minimum, so the current is a maximum for a given supply voltage.")

theory(T, "The resonant frequency of a series R-L-C circuit is given by:",
       ["f₀ = 1/(2π√(LC))", "f₀ = 2π√(LC)", "f₀ = 1/(2πLC)", "f₀ = √(LC)/(2π)"],
       0,
       "Setting Xₗ = XC (2πfL = 1/(2πfC)) and solving for f gives the resonant frequency f₀ = 1/(2π√(LC)).")

theory(T, "The quality factor (Q) of a resonant circuit is a measure of:",
       ["the selectivity/sharpness of the resonance", "the power dissipated in the resistor", "the number of components", "the temperature of the coil"],
       0,
       "The Q factor measures how sharply the circuit resonates — high Q means a sharp, selective resonance with a narrow bandwidth.")

theory(T, "In a PARALLEL resonant (anti-resonant) circuit, at resonance the impedance is:",
       ["maximum", "minimum", "zero", "equal to the resistance only"],
       0,
       "Parallel resonance is the dual of series resonance: at anti-resonance the impedance of the parallel L-C combination is a MAXIMUM (so line current is a minimum).")

theory(T, "At series resonance, the power factor of the circuit is:",
       ["unity (1)", "zero", "0.5 leading", "0.707 lagging"],
       0,
       "At resonance the circuit is purely resistive (Xₗ = XC), so voltage and current are in phase and the power factor is unity.")

calc(T, "A series circuit has L = 100 mH and C = 10 µF. Its resonant frequency is about: (π = 3.14)",
     ["159 Hz", "15.9 Hz", "1590 Hz", "50 Hz"],
     0,
     "Formula: f₀ = 1/(2π√(LC)).\nStep 1: LC = 0.1 × 10 × 10⁻⁶ = 1 × 10⁻⁶.\nStep 2: √(LC) = 1 × 10⁻³.\nStep 3: f₀ = 1/(2 × 3.14 × 10⁻³) = 1/0.00628 = 159.2 Hz.\nAnswer: ≈ 159 Hz.")

calc(T, "A series circuit has L = 20 mH and C = 20 µF. Its resonant frequency is about:",
     ["252 Hz", "25.2 Hz", "2520 Hz", "126 Hz"],
     0,
     "Formula: f₀ = 1/(2π√(LC)).\nStep 1: LC = 0.02 × 20 × 10⁻⁶ = 4 × 10⁻⁷.\nStep 2: √(LC) = 6.325 × 10⁻⁴.\nStep 3: f₀ = 1/(2 × 3.14 × 6.325 × 10⁻⁴) = 1/3.973 × 10⁻³ = 251.7 Hz.\nAnswer: ≈ 252 Hz.")

calc(T, "At resonance, a circuit has f₀ = 159 Hz and L = 100 mH. The inductive reactance Xₗ at resonance is about:",
     ["100 Ω", "1000 Ω", "10 Ω", "159 Ω"],
     0,
     "Formula: Xₗ = 2πf₀L.\nSubstitute: Xₗ = 2 × 3.14 × 159 × 0.1 = 99.9 Ω ≈ 100 Ω (and XC has the same value at resonance).\nAnswer: ≈ 100 Ω.")

calc(T, "In a series resonant circuit with R = 10 Ω and Xₗ = XC = 100 Ω at resonance, the Q factor is:",
     ["10", "100", "1", "0.1"],
     0,
     "Formula: Q = Xₗ/R = XC/R (at resonance).\nSubstitute: Q = 100/10 = 10.\nAnswer: Q = 10.")

calc(T, "A series circuit has L = 40 mH and C = 10 µF. Its resonant frequency is about: (π = 3.14)",
     ["252 Hz", "25.2 Hz", "2520 Hz", "159 Hz"],
     0,
     "Formula: f₀ = 1/(2π√(LC)).\nStep 1: LC = 0.04 × 10 × 10⁻⁶ = 4 × 10⁻⁷.\nStep 2: √(LC) = 6.32 × 10⁻⁴.\nStep 3: f₀ = 1/(2 × 3.14 × 6.32 × 10⁻⁴) = 1/3.97 × 10⁻³ = 251.9 Hz.\nAnswer: ≈ 252 Hz.")

calc(T, "A series resonant circuit has f₀ = 100 kHz and Q = 50. Its bandwidth is:",
     ["2 kHz", "5 kHz", "20 kHz", "0.5 kHz"],
     0,
     "Formula: bandwidth = f₀/Q.\nSubstitute: BW = 100 kHz / 50 = 2 kHz.\nAnswer: 2 kHz.")

calc(T, "A coil of reactance Xₗ = 100 Ω and a capacitor of reactance XC = 100 Ω are connected in PARALLEL at the resonant frequency. The impedance of the combination is:",
     ["infinite (very large) — parallel anti-resonance", "100 Ω", "50 Ω", "zero"],
     0,
     "At parallel resonance Xₗ = XC, so the L-C combination draws equal and opposite reactive currents that cancel: the combination behaves as an open circuit (infinite impedance, anti-resonance), unlike the series case which gives minimum impedance.\nAnswer: infinite (very large).")

calc(T, "A series circuit has L = 10 mH and C = 100 µF. Its resonant frequency is about:",
     ["159 Hz", "15.9 Hz", "1590 Hz", "31.8 Hz"],
     0,
     "Formula: f₀ = 1/(2π√(LC)).\nStep 1: LC = 0.01 × 100 × 10⁻⁶ = 1 × 10⁻⁶.\nStep 2: √(LC) = 1 × 10⁻³.\nStep 3: f₀ = 1/(2 × 3.14 × 10⁻³) = 159.2 Hz.\nAnswer: ≈ 159 Hz.")

# ================================================================
# TOPIC 4 — Network Theorems for AC
# ================================================================
T = "eee-network-theorems"

theory(T, "Thévenin's theorem states that any linear two-terminal network can be replaced by:",
       ["a single voltage source Vₜₕ in series with an impedance Zₜₕ",
        "a single current source in parallel with an impedance",
        "a single resistor only",
        "a capacitor and an inductor in series"],
       0,
       "Thévenin: any linear two-terminal network is equivalent to one voltage source (the open-circuit voltage Vₜₕ) in series with the equivalent impedance Zₜₕ seen at the terminals (with sources killed). For AC networks, Zₜₕ is complex (R ± jX).")

theory(T, "Norton's theorem states that any linear two-terminal network can be replaced by:",
       ["a single current source Iₙ in parallel with the same impedance Zₙ",
        "a voltage source in series with an impedance",
        "an ideal transformer",
        "a resistor and an inductor in series"],
       0,
       "Norton is the dual of Thévenin: a current source Iₙ (the short-circuit current) in parallel with Zₙ = Zₜₕ.")

theory(T, "The superposition theorem states that in a linear network with several sources, the response in any branch is:",
       ["the algebraic sum of the responses produced by each source acting alone (with the others replaced by their internal impedances)",
        "the product of the responses of all sources",
        "the response of the largest source only",
        "the average of the responses of all sources"],
       0,
       "Superposition: consider ONE source at a time (voltage sources shorted, current sources opened) and add the individual responses algebraically. It applies to linear AC networks too, using phasors.")

theory(T, "When applying Thévenin/Norton theorems to AC networks, the impedances must be treated as:",
       ["complex quantities (R ± jX) so both magnitude and phase are preserved",
        "real resistances only",
        "imaginary numbers only",
        "scalar magnitudes without phase"],
       0,
       "In AC networks the impedances are complex (e.g. 100 + j100 Ω); the theorems work exactly as in DC but with complex arithmetic, preserving magnitude AND phase.")

theory(T, "A circuit is classified as nonlinear when:",
       ["its i-v graph is not a straight line",
        "it contains only resistors",
        "its i-v graph is a straight line through the origin",
        "it contains no sources"],
       0,
       "We classify a circuit as linear or nonlinear by examining its i-v graph: a straight line → linear; any other shape → nonlinear (e.g. i = v²). Even a piecewise-linear function like |v| is nonlinear because it cannot be written as y = ax + b.")

theory(T, "A useful nonlinear circuit built with op-amps is the:",
       ["negative resistance converter, whose application is the oscillator",
        "positive resistance converter",
        "linear amplifier only",
        "full-wave rectifier only"],
       0,
       "The notes introduce the negative resistance converter as a very useful nonlinear circuit, and its key application is the oscillator (a circuit that sustains its own oscillations).")

theory(T, "About nonlinear circuit analysis, the notes say:",
       ["there are no hard and fast rules to analyse most nonlinear circuits — you have to use your brain (with systematic methods for op-amp nonlinear circuits)",
        "every nonlinear circuit can be solved with Ohm's law alone",
        "nonlinear circuits are always analysed like linear ones",
        "nonlinear circuits have no applications"],
       0,
       "The notes: most nonlinear circuits have no fixed analysis rules ('real engineering'); but systematic methods exist for analysing op-amp nonlinear circuits such as the negative resistance converter.")

calc(T, "Two impedances Z₁ = (100 + j100) Ω and Z₂ = (100 − j100) Ω are connected in series. The equivalent impedance is:",
     ["200 Ω (purely resistive)", "0 Ω", "j200 Ω", "100 Ω"],
     0,
     "Series impedances add: Z = Z₁ + Z₂.\nZ = (100 + j100) + (100 − j100) = 200 + j0 = 200 Ω.\nThe reactances cancel — the combination behaves as a pure 200 Ω resistor.\nAnswer: 200 Ω.")

calc(T, "A circuit has R = 6 Ω in series with Xₗ = 8 Ω. The magnitude of the equivalent impedance is:",
     ["10 Ω", "14 Ω", "2 Ω", "48 Ω"],
     0,
     "Formula: Z = R + jXₗ, |Z| = √(R² + Xₗ²).\nSubstitute: |Z| = √(6² + 8²) = √(36 + 64) = √100 = 10 Ω.\nAnswer: 10 Ω.")

calc(T, "Two equal impedances of (50 + j50) Ω each are connected in PARALLEL. The equivalent impedance is:",
     ["(25 + j25) Ω", "(100 + j100) Ω", "(50 − j50) Ω", "50 Ω"],
     0,
     "For two equal impedances in parallel, the equivalent is half of one: Z = (50 + j50)/2 = (25 + j25) Ω.\n(In general Zₑ = Z₁ × Z₂ / (Z₁ + Z₂); with Z₁ = Z₂ this reduces to Z/2.)\nAnswer: (25 + j25) Ω.")

calc(T, "A circuit has R = 8 Ω in series with Xₗ = 6 Ω. The magnitude of the equivalent impedance is:",
     ["10 Ω", "14 Ω", "2 Ω", "48 Ω"],
     0,
     "Formula: |Z| = √(R² + Xₗ²).\nSubstitute: |Z| = √(8² + 6²) = √(64 + 36) = √100 = 10 Ω.\nAnswer: 10 Ω.")

calc(T, "Thévenin equivalent of a network gives Vₜₕ = 20∠0° V and Zₜₕ = (10 + j0) Ω. A load of (10 + j0) Ω is connected. The load current is:",
     ["1 A", "2 A", "0.5 A", "20 A"],
     0,
     "Formula: I = Vₜₕ / (Zₜₕ + Zₗ).\nSubstitute: I = 20 / (10 + 10) = 20 / 20 = 1 A.\nAnswer: 1 A.")

# ================================================================
# TOPIC 5 — Magnetic Circuits & Transformers
# ================================================================
T = "eee-magcircuits-transformer"

theory(T, "The magnetomotive force (m.m.f.) of a coil of N turns carrying current I is:",
       ["F = NI, in amperes or ampere-turns", "F = N/I", "F = I/N", "F = NI²"],
       0,
       "Magnetomotive force F = NI (ampere-turns) — the magnetic analogue of e.m.f. It is what drives flux around a magnetic circuit.")

theory(T, "The magnetic field strength (magnetising force) in a magnetic circuit is:",
       ["H = F/L = NI/L, in amperes per metre",
        "H = FL",
        "H = F/L²",
        "H = NI L"],
       0,
       "H is the m.m.f. gradient: H = F/L = NI/L (A/m) — the m.m.f. per unit length of the magnetic path.")

theory(T, "Flux density B and magnetic field strength H are related by:",
       ["B = μH, where μ is the permeability of the material",
        "B = H/μ",
        "B = μH²",
        "B = H + μ"],
       0,
       "B = μH (teslas) — the permeability μ of the material links the field strength to the resulting flux density.")

theory(T, "The permeability of free space μ₀ equals:",
       ["4π × 10⁻⁷ H/m", "8.85 × 10⁻¹² F/m", "4π × 10⁻⁹ H/m", "1.26 H/m"],
       0,
       "μ₀ = 4π × 10⁻⁷ henrys per metre — the reference permeability of a vacuum (free space).")

theory(T, "Magnetic flux Φ, flux density B and area A are related by:",
       ["Φ = B × A, with B = Φ/A",
        "Φ = B/A",
        "Φ = A/B",
        "Φ = B + A"],
       0,
       "Flux Φ = B × A (webers); flux density B = Φ/A (teslas) — flux per unit area.")

theory(T, "The reluctance S of a magnetic circuit is:",
       ["S = l/(μA) — the magnetic analogue of resistance",
        "S = μA/l",
        "S = l μ A",
        "S = A/(μl)"],
       0,
       "Reluctance S = l/(μA), where l is the length of the magnetic path and A its cross-section — the magnetic analogue of electrical resistance (it opposes flux).")

theory(T, "The relative permeability μᵣ of a material is:",
       ["the ratio of its permeability to that of free space",
        "the permeability of free space",
        "the ratio of its resistance to its reluctance",
        "the product μ₀ × A"],
       0,
       "μᵣ = μ/μ₀ — the ratio of the material's permeability to that of free space (dimensionless); absolute permeability μ = μ₀μᵣ.")

theory(T, "Which pairing in the electrostatics ↔ electromagnetism analogy is CORRECT?",
       ["Electric field strength E ↔ Magnetic field strength H",
        "Electric flux density D ↔ Magnetomotive force F",
        "Permittivity ε ↔ Reluctance S",
        "Electric flux ↔ Magnetic flux density"],
       0,
       "From the analogy table: electric flux ↔ magnetic flux; D ↔ B (flux densities); E ↔ H (field strengths); e.m.f. ↔ m.m.f.; potential difference ↔ magnetic potential difference; permittivity ↔ permeability; ε₀ ↔ μ₀.")

theory(T, "In an IDEAL transformer, the voltage and turns ratios are related by:",
       ["V₁/V₂ = N₁/N₂ = I₂/I₁",
        "V₁/V₂ = N₂/N₁",
        "V₁/V₂ = I₁/I₂ = N₁/N₂",
        "V₁ V₂ = N₁ N₂"],
       0,
       "For an ideal transformer: V₁/V₂ = N₁/N₂ = I₂/I₁ — voltage steps with the turns ratio while current steps inversely (power in ≈ power out).")

theory(T, "A transformer that increases voltage (more secondary turns) is called:",
       ["a step-up transformer", "a step-down transformer", "an isolation transformer", "an autotransformer only"],
       0,
       "Step-up: N₂ > N₁ so V₂ > V₁; step-down: N₂ < N₁ so V₂ < V₁.")

theory(T, "Why does a transformer operate only on AC (not steady DC)?",
       ["Transformer action relies on a changing flux to induce the secondary e.m.f. per Faraday's law",
        "DC would melt the iron core",
        "DC cannot flow in copper",
        "the primary resistance blocks DC"],
       0,
       "Induction requires a changing flux (E = N dΦ/dt); a steady DC produces a constant flux, so no e.m.f. is induced in the secondary. Hence transformers are AC devices.")

theory(T, "The main losses in a practical transformer are:",
       ["copper (I²R) losses and iron losses (eddy current + hysteresis)",
        "friction and windage only",
        "capacitive losses only",
        "radiation losses only"],
       0,
       "Practical transformers have copper losses (I²R in the windings) and iron/core losses (eddy currents and hysteresis in the laminated core).")

theory(T, "Magnetic flux lines:",
       ["form closed loops, never cross, and when parallel repel one another",
        "cross each other at right angles",
        "start and end in free space",
        "are straight lines only"],
       0,
       "From the Hughes summary: flux lines form closed loops, do not cross, and parallel lines repel one another. Magnetic fields have N and S poles; like poles repel, unlike attract.")

calc(T, "A coil of 500 turns carries 2 A. Its magnetomotive force is:",
     ["1000 ampere-turns", "250 ampere-turns", "500 ampere-turns", "1000 volts"],
     0,
     "Formula: F = NI.\nSubstitute: F = 500 × 2 = 1000 ampere-turns (At).\nAnswer: 1000 At.")

calc(T, "A 1000-turn coil wound on a magnetic path 0.5 m long carries 2 A. The magnetic field strength H is:",
     ["4000 A/m", "2000 A/m", "1000 A/m", "500 A/m"],
     0,
     "Formula: H = NI/L.\nSubstitute: H = (1000 × 2)/0.5 = 4000 A/m.\nAnswer: 4000 A/m.")

calc(T, "A flux density of 0.5 T passes through an area of 0.02 m². The flux is:",
     ["0.01 Wb", "0.1 Wb", "10 Wb", "0.001 Wb"],
     0,
     "Formula: Φ = B A.\nSubstitute: Φ = 0.5 × 0.02 = 0.01 Wb.\nAnswer: 0.01 Wb.")

calc(T, "A magnetic circuit has l = 0.5 m, A = 0.001 m² and relative permeability μᵣ = 1000. Its reluctance is about: (μ₀ = 4π × 10⁻⁷)",
     ["3.98 × 10⁵ A/Wb", "3.98 × 10⁶ A/Wb", "1.26 × 10⁵ A/Wb", "7.96 × 10⁵ A/Wb"],
     0,
     "Formula: S = l/(μA) with μ = μ₀μᵣ.\nStep 1: μ = 4π × 10⁻⁷ × 1000 = 4π × 10⁻⁴.\nStep 2: S = 0.5/(4π × 10⁻⁴ × 0.001) = 0.5/(1.2566 × 10⁻⁶) = 3.98 × 10⁵ A/Wb.\nAnswer: ≈ 3.98 × 10⁵ A/Wb.")

calc(T, "A transformer has N₁ = 500 primary turns and N₂ = 100 secondary turns. With a primary voltage of 220 V, the secondary voltage is:",
     ["44 V", "110 V", "1100 V", "22 V"],
     0,
     "Formula: V₂/V₁ = N₂/N₁.\nSubstitute: V₂ = 220 × (100/500) = 220 × 0.2 = 44 V.\nAnswer: 44 V (a step-down transformer).")

calc(T, "A step-up transformer has N₁ = 200 turns and N₂ = 1000 turns. With V₁ = 50 V, the secondary voltage is:",
     ["250 V", "10 V", "100 V", "500 V"],
     0,
     "Formula: V₂ = V₁ × (N₂/N₁).\nSubstitute: V₂ = 50 × (1000/200) = 50 × 5 = 250 V.\nAnswer: 250 V.")

calc(T, "An ideal transformer supplies a load at V₂ = 24 V, I₂ = 2 A from a primary at V₁ = 240 V. The primary current is:",
     ["0.2 A", "2 A", "20 A", "0.02 A"],
     0,
     "Formula (ideal): V₁ × I₁ = V₂ × I₂ → I₁ = V₂I₂/V₁.\nSubstitute: I₁ = (24 × 2)/240 = 48/240 = 0.2 A.\nAnswer: 0.2 A.")

calc(T, "A conductor of length 0.3 m moves at 10 m/s at right angles to a field of 0.5 T. The e.m.f. induced in it is:",
     ["1.5 V", "15 V", "0.15 V", "3 V"],
     0,
     "Formula: E = B × l × v (motional e.m.f., motion perpendicular to both B and l).\nSubstitute: E = 0.5 × 0.3 × 10 = 1.5 V.\nAnswer: 1.5 V.")

calc(T, "A transformer has N₁ = 400 primary turns and N₂ = 50 secondary turns. With V₁ = 240 V, the secondary voltage is:",
     ["30 V", "48 V", "120 V", "1920 V"],
     0,
     "Formula: V₂ = V₁ × (N₂/N₁).\nSubstitute: V₂ = 240 × (50/400) = 240 × 0.125 = 30 V.\nAnswer: 30 V (step-down).")

calc(T, "A transformer with turns ratio N₁/N₂ = 10 supplies a secondary current of 3 A. The primary current is about:",
     ["0.3 A", "3 A", "30 A", "0.03 A"],
     0,
     "Formula (ideal): I₁/I₂ = N₂/N₁ → I₁ = I₂ × (N₂/N₁).\nSubstitute: I₁ = 3 × (1/10) = 0.3 A.\nAnswer: 0.3 A.")

calc(T, "A 600-turn primary must step 240 V down to 12 V. The number of secondary turns required is:",
     ["30 turns", "120 turns", "12000 turns", "50 turns"],
     0,
     "Formula: N₂ = N₁ × (V₂/V₁).\nSubstitute: N₂ = 600 × (12/240) = 600 × 0.05 = 30 turns.\nAnswer: 30 turns.")

calc(T, "A magnetic circuit has an m.m.f. of 500 At and a reluctance of 2 × 10⁶ A/Wb. The flux produced is:",
     ["0.25 mWb", "2.5 mWb", "1 mWb", "0.025 mWb"],
     0,
     "Formula (magnetic Ohm's law): Φ = F/S.\nSubstitute: Φ = 500/(2 × 10⁶) = 2.5 × 10⁻⁴ Wb = 0.25 mWb.\nAnswer: 0.25 mWb.")

# ================================================================
# TOPIC 6 — Motors & Generators
# ================================================================
T = "eee-motors-generators"

theory(T, "The key demonstration of electromechanics in 1831 was by:",
       ["Michael Faraday — a conductor moved in a magnetic field generates current, and current in a field develops motion",
        "Thomas Edison",
        "Hans Christian Oersted",
        "Charles Steinmetz"],
       0,
       "In 1831 Faraday demonstrated both directions of electromechanical conversion: motion in a magnetic field generates current (generator), and current in a magnetic field produces motion (motor).")

theory(T, "An electric motor converts:",
       ["electrical energy into mechanical energy", "mechanical energy into electrical energy", "heat into electricity", "chemical energy into light"],
       0,
       "A motor converts electrical energy to mechanical (rotation); a generator does the reverse — mechanical energy to electrical energy, coupled through the magnetic field.")

theory(T, "A generator converts:",
       ["mechanical energy into electrical energy", "electrical energy into mechanical energy", "AC into DC", "voltage into current"],
       0,
       "A generator converts mechanical input into electrical output by electromagnetic induction (relative motion of a conductor and a magnetic flux).")

theory(T, "A battery and a generator differ in that:",
       ["a battery is a source of stored chemical energy while a generator produces e.m.f. from motion in a magnetic field",
        "both produce e.m.f. by induction",
        "a generator stores energy chemically",
        "a battery produces AC only"],
       0,
       "A battery converts stored chemical energy to e.m.f.; a generator produces e.m.f. by electromagnetic induction (relative motion of conductor and flux).")

theory(T, "The rotating part of a DC machine carrying the armature windings is called the:",
       ["armature", "field winding", "commutator brush", "stator core"],
       0,
       "The armature is the rotating part whose windings carry the generated e.m.f. (generator) or the driving current (motor); the e.m.f. appears across the armature conductors as they cut flux.")

theory(T, "In a DC machine, the function of the commutator is to:",
       ["convert the alternating e.m.f. induced in the armature into a unidirectional (DC) output",
        "generate the magnetic field",
        "cool the machine",
        "increase the speed of rotation"],
       0,
       "The commutator rectifies the AC induced in the rotating armature conductors so that the external circuit receives direct current (and it keeps the torque unidirectional in motors).")

theory(T, "Fleming's LEFT-hand rule is used for:",
       ["motors — finding the direction of force on a current-carrying conductor in a field",
        "generators — finding the direction of induced e.m.f.",
        "finding the polarity of a battery",
        "calculating transformer ratios"],
       0,
       "Left-hand rule (FBI: thumb = Force/Motion, first finger = Field, second finger = Current) is the MOTOR rule; the right-hand rule is the GENERATOR (induced e.m.f.) rule.")

theory(T, "An AC generator is also called:",
       ["an alternator", "a dynamo", "a transformer", "a rectifier"],
       0,
       "An AC generator (alternator) produces an alternating e.m.f. as the armature rotates in the field — the same principle that makes the AC waveform a product of the rotating generator.")

theory(T, "Which statement about motors vs generators is correct?",
       ["The same machine principle works both ways: motion + field → e.m.f. (generator); current + field → force (motor)",
        "Motors and generators use unrelated physical laws",
        "Only generators need a magnetic field",
        "Only motors rotate"],
       0,
       "Electromechanical energy conversion is bidirectional — the coupling through the magnetic field is the same; the direction of energy flow decides motor vs generator operation.")

calc(T, "A conductor of length 0.5 m moves at 20 m/s perpendicular to a field of 1 T. The induced e.m.f. is:",
     ["10 V", "0.1 V", "40 V", "2.5 V"],
     0,
     "Formula: E = B × l × v.\nSubstitute: E = 1 × 0.5 × 20 = 10 V.\nAnswer: 10 V.")

calc(T, "A conductor of length 0.25 m moves at 8 m/s at right angles to a field of 0.4 T. The induced e.m.f. is:",
     ["0.8 V", "8 V", "0.08 V", "1.25 V"],
     0,
     "Formula: E = B × l × v.\nSubstitute: E = 0.4 × 0.25 × 8 = 0.8 V.\nAnswer: 0.8 V.")

calc(T, "A conductor of length 0.4 m moves at 5 m/s perpendicular to a field of 0.2 T. The induced e.m.f. is:",
     ["0.4 V", "4 V", "0.04 V", "2 V"],
     0,
     "Formula: E = B × l × v.\nSubstitute: E = 0.2 × 0.4 × 5 = 0.4 V.\nAnswer: 0.4 V.")

# ================================================================
# TOPIC 7 — Instruments & Instrumentation
# ================================================================
T = "eee-instruments"

theory(T, "Instrumentation is best defined as:",
       ["the use of devices (instruments) to detect, observe, measure, control, compute, communicate and display physical quantities",
        "the repair of electrical machines",
        "the generation of electrical power",
        "the design of transformers"],
       0,
       "Per the reference material, instrumentation refers to using instruments to detect, observe, measure, control, compute, communicate and display physical quantities; all branches of experimental engineering depend on it.")

theory(T, "Instruments are said to 'extend human senses' because they:",
       ["measure accurately and rapidly over a great range of distances and physical quantities",
        "replace human judgement entirely",
        "only amplify sounds",
        "are never used in engineering"],
       0,
       "The notes: instruments let humans measure accurately and quickly over a great range of quantities and distances, far beyond direct senses.")

theory(T, "Indicating instruments are used to measure:",
       ["the amount of current or voltage across a circuit — e.g. ammeters and voltmeters",
        "only temperature",
        "only frequency",
        "only resistance"],
       0,
       "Indicating instruments (ammeters, voltmeters, etc.) measure quantities like current and voltage across a circuit, displaying them on a scale/pointer or digital readout.")

theory(T, "An ammeter must be connected:",
       ["in series with the circuit and have a very LOW resistance",
        "in parallel with the circuit with a very high resistance",
        "in series with a very high resistance",
        "in parallel with a very low resistance"],
       0,
       "The ammeter measures current, so it is placed in series; its resistance must be very low so it does not disturb the circuit (ideally an ammeter reads with zero resistance).")

theory(T, "A voltmeter must be connected:",
       ["in parallel with the circuit and have a very HIGH resistance",
        "in series with the circuit with a low resistance",
        "in parallel with a low resistance",
        "in series with a high resistance"],
       0,
       "The voltmeter measures p.d., so it is placed in parallel across the component; it must have a very high resistance so it draws negligible current.")

theory(T, "The permanent-magnet moving-coil (PMMC) instrument:",
       ["works on DC only (polarity must be observed) and has a uniform scale",
        "works on AC and DC equally",
        "measures only AC power",
        "needs no magnet"],
       0,
       "The PMMC (moving-coil) instrument uses a permanent magnet and a moving coil — it deflects proportionally to DC current (deflection reverses with polarity) and gives a uniform scale.")

theory(T, "The moving-iron instrument:",
       ["works on both AC and DC and is robust, but has a non-uniform (cramped) scale",
        "works on DC only",
        "has a perfectly uniform scale",
        "is used only for frequency measurement"],
       0,
       "Moving-iron instruments deflect by repulsion/attraction of iron pieces — they respond to both AC and DC (r.m.s.) and are cheap and robust, though their scale is non-uniform.")

theory(T, "Instruments may be broadly classified as:",
       ["analog (pointer and scale) and digital (numeric display)",
        "analog only",
        "digital only",
        "mechanical only"],
       0,
       "Indicating instruments are classified as analog (continuous pointer deflection on a scale) or digital (numeric display); digital instruments give readings with no parallax error.")

theory(T, "Which of the following is a source of error/limitation in indicating instruments?",
       ["friction in the movement and parallax in reading the pointer",
        "the colour of the casing",
        "the length of the leads",
        "the room temperature of the observer"],
       0,
       "Typical instrument errors include friction in the movement (which requires a controlling/damping torque) and parallax when reading the pointer against the scale — mitigated by knife-edge pointers and mirror scales.")

calc(T, "A moving-coil meter movement has full-scale deflection at 100 µA and internal resistance Rₘ = 1 kΩ. To use it as a 10 V voltmeter, the series multiplier required is:",
     ["99 kΩ", "100 kΩ", "10 kΩ", "1 kΩ"],
     0,
     "Formula: total resistance Rₜ = V / I, where I is the full-scale deflection current; multiplier = Rₜ − Rₘ.\nStep 1: Rₜ = 10 / (1 × 10⁻⁴) = 100 kΩ.\nStep 2: multiplier = 100 kΩ − 1 kΩ = 99 kΩ.\nAnswer: 99 kΩ in series.")

calc(T, "A 1 mA movement with Rₘ = 100 Ω is to measure 1 A full scale. The shunt resistance required is about:",
     ["0.1 Ω", "1 Ω", "10 Ω", "100 Ω"],
     0,
     "Formula: Iₘ × Rₘ = (I − Iₘ) × Rₛₕ.\nStep 1: current through shunt = 1 − 0.001 = 0.999 A.\nStep 2: Rₛₕ = (0.001 × 100) / 0.999 = 0.1 / 0.999 ≈ 0.1 Ω.\nAnswer: ≈ 0.1 Ω in parallel.")

calc(T, "A moving-coil movement deflects fully at 50 µA and has Rₘ = 2 kΩ. To use it as a 5 V voltmeter, the series multiplier needed is:",
     ["98 kΩ", "100 kΩ", "50 kΩ", "10 kΩ"],
     0,
     "Formula: total resistance Rₜ = V / I, where I is the full-scale deflection current; multiplier = Rₜ − Rₘ.\nStep 1: Rₜ = 5 / (5 × 10⁻⁵) = 100 kΩ.\nStep 2: multiplier = 100 kΩ − 2 kΩ = 98 kΩ.\nAnswer: 98 kΩ.")

# ================================================================
# TOPIC 8 — Nonlinear Circuits (intro)
# ================================================================
T = "eee-nonlinear"

theory(T, "In the i-v world of circuits, a circuit is classified as linear if:",
       ["its i-v graph is a straight line",
        "it contains a diode",
        "its i-v graph is curved",
        "it contains an op-amp"],
       0,
       "Classification is by the i-v graph: straight line → linear (v = Ri); curved → nonlinear (e.g. a diode's exponential i-v).")

theory(T, "The function y = x² is:",
       ["nonlinear — its graph is a parabola, not a straight line",
        "linear — its graph is a straight line",
        "piecewise linear",
        "a constant"],
       0,
       "y = x² plots as a parabola → nonlinear. y = 2x plots as a straight line → linear.")

theory(T, "The absolute value function y = |x| is classified as:",
       ["nonlinear (piecewise linear), because it cannot be written as y = ax + b",
        "linear",
        "a parabola",
        "an exponential"],
       0,
       "Although |x| is made of two straight pieces, it is still classified as nonlinear because it cannot be written in the single form y = ax + b.")

theory(T, "Why are nonlinear circuits important in engineering?",
       ["electrical devices like amplifiers and computers are built from nonlinear components",
        "they are easier to analyse than linear circuits",
        "they have no applications",
        "all circuits are linear in practice"],
       0,
       "Amplifiers, computers and most practical devices are built from nonlinear components, so understanding nonlinear circuits is essential to designing these devices.")

theory(T, "The negative resistance converter is:",
       ["a useful nonlinear op-amp circuit whose i-v slope is negative over a region, used to build oscillators",
        "a resistor that obeys Ohm's law",
        "a transformer winding",
        "a rectifier"],
       0,
       "The negative resistance converter presents a negative slope in its i-v characteristic over some region — it delivers power instead of absorbing it, which is exactly what an oscillator needs to sustain oscillations.")

# ---------------------------------------------------------------------
# emit JSON
# ---------------------------------------------------------------------
TOPICS = [
    {"id": "eee-magnetism", "name": "Magnetism & Moving Charges"},
    {"id": "eee-ac-phasors", "name": "AC Waveforms & Phasors"},
    {"id": "eee-resonance", "name": "Resonance in AC Circuits"},
    {"id": "eee-network-theorems", "name": "Network Theorems for AC"},
    {"id": "eee-magcircuits-transformer", "name": "Magnetic Circuits & Transformers"},
    {"id": "eee-motors-generators", "name": "Electrical Motors & Generators"},
    {"id": "eee-instruments", "name": "Instruments & Instrumentation"},
    {"id": "eee-nonlinear", "name": "Nonlinear Circuits (Intro)"},
]

# assign ids
counters = {}
for q in QUESTIONS:
    c = counters.get(q["topicId"], 0) + 1
    counters[q["topicId"]] = c
    q["id"] = f"eee_{q['topicId'].replace('eee-','')}_{c:02d}"

if __name__ == "__main__":
    json.dump({"topics": TOPICS, "questions": QUESTIONS},
              open(".eee202_out.json", "w"), ensure_ascii=False, indent=2)
    by_t = {}
    kinds = {"calc": 0, "theory": 0}
    for q in QUESTIONS:
        by_t[q["topicId"]] = by_t.get(q["topicId"], 0) + 1
        kinds[q["kind"]] += 1
    print("TOTAL:", len(QUESTIONS), "| calc:", kinds["calc"], "| theory:", kinds["theory"])
    for k, v in by_t.items():
        print(" ", k, "->", v)
