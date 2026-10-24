---
url: https://scienceops.lbto.org/lbti/instrument-characteristics/lmircam-filters/
title: LMIRCam Filters
breadcrumb: Instrument Characteristics › LMIRCam Filters
fetched_at: '2026-10-26T06:31:13+00:00'
sha256: 9e2371513c4f9d4abdaeadcc43b03c04dcb54667fbffd7b2456be4a1bf465280
---

## Overview {#TOC-Overview}

### Broadband filters and Spectroscopic Order Sorters {#TOC-Broadband-filters-and-Spectroscopic-Order-Sorters}

| Filter Name | Filter Wheel & Pos | λc [µm] | Range  [µm] | Comments |
| --- | --- | --- | --- | --- |
| Mauna Kea J | FW2.5, 7 | 1.25 | 1.16 – 1.34 | BeamDVT set to window, use PK50 in FW4, so as to prevent L-band light leakage |
| H | FW2.5, 2 | 1.65 | 1.50 – 1.81 | BeamDVT set to window, use PK50 in FW4, so as to prevent L-band light leakage |
| Ks | FW2.5, 3 | 2.16 | 2.00 – 2.32 | BeamDVT set to window, use PK50 in FW4, so as to prevent L-band light leakage |
| LShort | FW25, 6 | 3.31 | 3.10 – 3.51 |  |
| StdL | FW4 | 3.70 | 3.41 – 3.99 | Optimized for planets |
| L-Spec | FW2.5, 4 | 3.51 | 2.81 – 4.00 | Order sorting for L-Band Spectroscopy |
| Janos | FW2.5, 5 |  | 3.0 – 5.0 |  |
| StdM | FW4 | 4.78 | 4.60 – 4.97 | Optimized for planets |
| 2950BP1500 | FW4, 10 |  | 2.20 – 3.75 | Spectroscopic bandpass filters for ALES, optimized for pIce absorption detection at 3.1 μm |
| IWBP2250 | FW2.5, 8 |  | 2.25 – 3.81 | Spectroscopic bandpass filters for ALES, optimized for pIce absorption detection at 3.1 μm |

### Narrowband filters {#TOC-Narrowband-filters}

| Filter Name | Filter Wheel | λc [µm] | Range  [µm] | Vendor | Comments |
| --- | --- | --- | --- | --- | --- |
| Fe-II | FW2 | 1.645 | 1.63-1.66 |  |  |
| NB2925-055 | FW2 | 2.925 | 2.87-2.98 |  |  |
| H2O-Ice2 | FW4 | 3.08 | 3.01 – 3.15 | JDSU | Crystalline ice peak (sub-micron grains) |
| L-cont. 1 | FW3 | 3.16 | 3.13 – 3.20 | JDSU |  |
| NB3375-025 | FW2 | 3.375 |  | JDSU |  |
| PAH 1 | FW2 | 3.2525 | 3.2394-3.3357 |  |  |
| L-cont. 2 | FW3 | 3.47 | 3.39 – 3.54 | JDSU | Located after PAHs; matches ices filters |
| NB3555-041 | FW2 | 3.555 |  |  |  |
| L-cont. 3 | FW4 | 3.59 | 3.55 – 3.64 | JDSU |  |
| L-cont. 4 | FW4 | 3.78 | 3.68 – 3.88 | JDSU |  |
| N03946-4 | FW3 | 3.95 | 3.83-4.06 | JDSU |  |
| NB3950-035 | FW2 | 3.950 |  |  |  |
| Br-Alpha-On | FW4 | 4.06 | 4.02 – 4.09 | NDC |  |
| Br-Alpha-Off | FW4 | 4.00 | 3.97 – 4.04 | NDC |  |

Each filter wheel contain an open position.  When you request an observation with a specific filter, whether broad or narrow band, the other FW do not move to their open position by default.  Each FW must either be moved manually into position using the Motors page, or be scripted into position.

## Transmission Curves {#TOC-Transmission-Curves}

[![](https://scienceops.lbto.org/wp-content/uploads/2021/12/LMTransmissionCurves.png)](https://scienceops.lbto.org/wp-content/uploads/2021/12/LMTransmissionCurves.png)

The Barr filters were measured at 77 and 300 K, and the NDC and JDSU filters at 300 K. (The NDC and JDSU extrapolations to 77 K should be used with caution, since they were extrapolated based on the observed Barr shifts.)

## Setup {#TOC-Setup}

| Bandpass | NIC BEAMDIV | NIL DICHROIC | LMIR APERWHL | LMIR MAGWHL | LMIR FW1 | LMIR FW2 | LMIR FW25 | LMIR FW3 | LMIR FW4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Near IR Imaging  ( <=K ) | Window (NegHWLim) | NegHWLim (if imaging w NOMIC; otherwise, leave DICHROIC alone) | Open | Open | LgDual Aperture OR SX or DXAperture | Open | NIR Filter | Open | PK50 blocker |
| Thermal IR Imaging  ( > K ) | Window (NegHWLim) OR Trichroic (PosHWLim) [both OK] | NegHWLim (if imaging w NOMIC; otherwise, leave DICHROIC alone) | Open | Open | LgDual Aperture OR SX or DXAperture | sci / open | sci / open | sci / open | sci / open |
| ALES alignment | Window (NegHWLim) OR Trichroic (PosHWLim) [both OK] |  | Open | Open | SX or DXAperture | open | open | open | std_L & blank |
| ALES Science | Window (NegHWLim) OR Trichroic (PosHWLim) [both OK] |  | Lenslet Array | Refractive Magnifier | SX or DXAperture | open | Order sorting filter | IFU Prism | open |
