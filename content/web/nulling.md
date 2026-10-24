---
url: https://scienceops.lbto.org/lbti/planning-observations/modes-and-strategies/nulling/
title: Nulling
breadcrumb: Planning Observations › Modes and Strategies › Nulling
fetched_at: '2026-10-26T06:28:41+00:00'
sha256: c8769ece0f6cb91d7cb7f33e1bc95f8730c5b8ad04e343174d976f4474a2ed45
---

#### Nulling

NOMIC camera houses a nulling interferometer. Nulling is advantageous for suppressing the bright light from host stars and for detecting faint, extended circumstellar material inside small fields-of-view. Since the pupils are overlapped, there is a one-to-one mapping of pairs of points between the two apertures at separations of 14.4 m. Thus nulling allows the extraction of angular resolutions equivalent to the 14.4 m center-to-center mirror separation.

Nulling interferometry is implemented on the LBTI by sending each telescope beam through opposite sides of a single-pass 50% transmissive beam-splitter at near normal incidence. Fine alignment of the beams is accomplished by adjustment of two three-axis PZT tip-tilt-piston platforms.

The interferometer is tuned to null by adjusting the phase sensor setpoint, while measuring the flux at 11 µm. This process has been scripted as part of the setup procedure for nulling observations. Observations using nulling interferometry are typically carried out by acquiring many (∼1000) short (∼50 ms) exposure images per pointing.

A typical Nulling observation will consist of at least one CAL-SCI (calibrator and science target) pair. The telescope elevation should match as much as possible between Science and Calibrator.  Darks are automatically taken while setting up and adjusting the phase sensor set point. The observing script will take several nulled nodded pairs, followed by photometric and background frames.
