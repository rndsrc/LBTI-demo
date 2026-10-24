---
url: https://scienceops.lbto.org/lbti/planning-observations/modes-and-strategies/nales/
title: NALES
breadcrumb: Planning Observations › Modes and Strategies › NALES
fetched_at: '2026-10-26T06:31:13+00:00'
sha256: b05dbe35923928df1e5e2cf1e86dbdaf20ca07366c917c3cc592fe2be3b27abe
---

#### The New Arizona Lenslets for Exoplanet Spectroscopy (NALES)

The NALES IFU is a PI instrument integrated into the LBTI.  In addition to contacting the LBTI team prior to proposal submission, proposers interested in using NALES need to obtain instrument PI approval from [lbtipi@lbto.org](mailto:lbtipi@lbto.org).

The Arizona Lenslets for Exoplanet Spectroscopy (ALES) is the world’s first AO-fed thermal infrared integral field spectrograph, mounted inside the LBTI. NALES is the New Arizona Lenslets for Exoplanet Spectroscopy, which upgraded the ALES optics with additional wavelength ranges, spectral resolutions, and plate scales allowing a broad suite of science that takes advantage of ALES’s unique ability to work at wavelengths >2 microns, and at the diffraction limit of the LBT’s full 23.8 meter aperture.

The available prisms for NALES science are:

| Wavelength Range  μm | Spectral  Resolution | Modes/Bands | Comments |
| --- | --- | --- | --- |
| 2.8-4.2 | ~40 | L-band |  |
| 3.0-5.0 | ~20 | L/M-band | To be commissioned, Expert/Experimental Mode only |
| 2.2-3.7 | ~40 | Ice | To be commissioned, Expert/Experimental Mode only |
| 3.1-3.5 | ~100 | PAH / CH4 | To be commissioned, Expert/Experimental Mode only |

New magnifiers enable a variety of plate scales to sample different wavelengths at the diffraction of the 8.4m mirror or 22.8m baseline.

| Magnifier | Spaxel Plate Scale | Field-of-View | Spectral Resolution |
| --- | --- | --- | --- |
| 6x |  |  |  |
| 12x | 33.76 mas/spaxel | 2”x2” | R~70 |
| 25x |  |  |  |
| 50x |  |  |  |

  Lenslet array optics:

| Spaxel Plate Scale | Field-of-View | Nyquist Samples  (Single Aperture AO) | Nyquist Samples  (Dual Aperture Interferometry) |
| --- | --- | --- | --- |
| 6×6 mas | 0.45×0.45″ | >0.5μm | >1.4.μm, Expert/Experimental Mode only |
| 12×12 mas | 0.9×0.9″ | >1.0.m | >2.8μm, Expert/Experimental Mode only |
| 25×25 mas | 1.8×1.8″ | >2.0μm |  |
| 50×50 mas | 3.6×3.6″ | >4.0μm |  |

Details about NALES optics can be found [here](https://scienceops.lbto.org/lbti/planning-observations/modes-and-strategies/nales/).

## Observing approach {#TOC-Observing-approach}

Ales utilizing the existing optics in LMIRcam. The optical alignment is optimized for each NALES configuration. Once the target is aligned on the “sweetspot” and the NALES optics are put in place, they are left in place until the observation is completed and all calibrations are taken to ensure consistency.

Wavelength calibrations are performed using narrowband filters with the ALES optics in place: magnifier, prism, and lenslet array.

Often a 3 point nod strategy is observed. The 3 point nod strategy strategy involves a pattern designed to nod between the primary, secondary, and sky.  This is particularly necessary if the secondary sources is outside the NALES limited FOV.

For self guided targets, such as calibrators or solar system objects, a two point nod sequence is  sufficient.  This nod script periodically nods from primary source to sky and back in order to track the sky background variations.

Dark frames are saved between nods, while the telescope resumes guiding.  These darks are used to monitor, track, and flag variable pixels that can complicate the reduction process.  The NOD Sequences and calibrations are all scripted to optimize use of telescope time, collecting science when the AO loops are closed and calibrations data between during moves.  The header information commonly used in reductions are automatically populated by the scripts: SCI, DRK, SKY.
