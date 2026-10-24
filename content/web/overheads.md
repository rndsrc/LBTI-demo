---
url: https://scienceops.lbto.org/lbti/planning-observations/overheads/
title: Overheads
breadcrumb: Planning Observations › Overheads
fetched_at: '2026-10-26T06:31:13+00:00'
sha256: e8f9cf9ce2b9cab36b735452a1a2469703c1f8930f5f701554bb7ad324b3d270
---

Programs are typically run in queue. It is important to be aware of overheads when receiving your allocated time. The time allocated to each program is clock time and includes acquisition, calibrations, and other detector and telescope overheads.

Obtaining astronomical observations at any telescope will typically face four different sources of overhead: from the telescope, instrument, detector, and any operation that requires human interaction. The Table below summarizes these overheads.

| Source of Overhead | Action Type | Typical Time [sec] | Maximum Time [sec] |
| --- | --- | --- | --- |
| Telescope | Preset | 75 | 300 |
| Telescope | Pointing & Collimation (1st)  Pointing & Collimation | 150  30 | 900  180 |
| Telescope | AO setup | 180 | 240 |
| Telescope | Dither(AO) | 20 | 20 |
| Instrument | Camera, Pupil Alignment | 60 | 300 |
| Instrument | Filter Changes | 10 | 60 |
| Instrument | Troubleshooting | 5 | 1800 |
| Human Element | Field/Source Identification | 5 | 300 |
| Human Element | Imaging Alignment/Setup | 20 | 300 |
| Human Element | Ales Alignment/Setup | 300 | 900 |
| Human Element | NRM Alignment/Setup | 300 | 900 |
| Human Element | Nulling Alignment/Setup | 600 | 3600 |
| Human Element | Troubleshooting | 60 | 1800 |
| Source of Overhead | Action Type | LMIRCam [sec] | NOMIC [sec] |
| Detector | Fast Mode Full frame |  |  |
| Detector | Medium Mode Full frame |  |  |
| Detector | Slow Mode Full frame |  |  |

Note that Fast mode has subwindowing.  Minimum time scales linearly with vertical pixel length.

The above times are estimates and may be refined.  Detector times TBD

Twilight is used for initial AO setup and checkout, and for the initial instrument alignment. As a result, the start of night setup overheads is therefore typically not passed on to the users. Calibration frames, such as Darks, are taken during telescope transition states while waiting for the AO to reacquire as another means of increasing observing efficiency. For ALES observations, it is necessary to take the wavelength calibrations before moving any optics to ensure consistent results. It may be necessary to take these during the night, depending on the programs. These wavelength calibrations take approximately 20 minutes.
