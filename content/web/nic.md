---
url: https://scienceops.lbto.org/lbti/nic/
title: NIC
breadcrumb: NIC
fetched_at: '2026-10-26T06:31:13+00:00'
sha256: 711a721587b7684a15a74392013a2f3f16ef3102c6872579f6a0e97ed02923f2
---

The Nulling and Imaging Camera (NIC) is composed of 2 individual camera modules: an 8-13 μm wavelength Nulling Optimized Mid-Infrared Camera (NOMIC) and a 3-5 μm imaging camera, LMIRCam.

| Camera | Wavelength  [μm] | Usable Field  [“] | Pixel Scale | Comments |
| --- | --- | --- | --- | --- |
| LMIRCAM | 1.5 – 5 | 20″ x 20″ | 10.7 mas/pixel | Regular imaging, Full readout |
| LMIRCAM | 1.5 – 5 | 2″ x 2″ | mas/pixel | NALES |
| NOMIC | 8 – 13 | 18″ x 18″ | 18 mas/pixel | Only the center 500×500 pixels are used for imaging. The outer edge of the detector is vignetted, gives a field of view of approximately 9 arcseconds tall. |

## LMIRCam Overview {#TOC-LMIRCam-Overview}

The L- and M-band Infrared Camera (LMIRcam) is a 1.5-5 μm camera and chronograph designed and built by a team at the University of Virginia, University of Minnesota, University of Arizona, and Notre Dame. LMIRCam was built to exploit the unique sensitivity and resolution of the LBT Interferometer. LMIRCam is designed for imaging at a 1:1 magnification of the combined focus provided by the LBTI beam-combiner. Re-imaging is accomplished via two biconic mirrors. This optical design of LMIRCAM creates an intermediate focal plane (useful for slits, integral field unit (IFU) optics or occulting masks) as well as an upstream and downstream pupil plane. Interchangeable cold stops and a filter wheel are placed at the first pupil plane in LMIRCam, while additional filters and a disperser are housed in additional wheels located at the second pupil plane.

LMIRCam contains various filter options spanning 1-5µm, (see Filters for details). In addition, LMIRCam has a set of germanium grisms10 (R∼300), two vector-vortex coronagraphs, a set of Apodizing Phase Plate (APP) coronagraphs, and an integral field spectrograph, all of which are outlined in the Grisms and Other section. LMIRcam is scientifically flexible in its ability to switch rapidly between its many observing modes.

Flexible readout electronics enable operating modes ranging from high frame rate broadband imaging at the longest wavelengths to low background R=400 spectroscopy at shorter wavelengths.

Details about the various observing modes and setups can be found [here](https://scienceops.lbto.org/lbti/planning-observations/modes-and-strategies/).

### NALES {#TOC-NALES}

The NALES IFU is a PI instrument integrated into the LBTI.  In addition to contacting the LBTI team prior to proposal submission, proposers interested in using NALES need to obtain instrument PI approval ([lbtipi@lbto.org](mailto:lbtipi@lbto.org)).

New Arizona Lenslet for Exoplanet Spectroscopy (NALES) is a retrofit of LMIRCam instrument to enable integral field spectroscopy.  The “New” refers to the recent optics upgrade that took place in 2018-2019 which:

1. increases the original ALES field-of-view
2. added plate scales appropriate for seeing-limited, adaptive optics and interferometric observations
3. added new disperser modes with R.10-200 resolution across various bandpasses from 1.5-5 μm.

NALES is comprised of magnification optics, a lenslet array, and direct-vision prisms, all of which are included within the existing optical structure/filter wheels of LMIRcam.

[![](https://scienceops.lbto.org/wp-content/uploads/2021/12/00445_PSISDG10702_107020C_page_2_1.jpg)](https://scienceops.lbto.org/wp-content/uploads/2021/12/00445_PSISDG10702_107020C_page_2_1.jpg)

A magnifying optic increases the size of the PSF, then a lenslet array placed at the LMIRcam intermediate focal place samples the fields into an array of spots.  This array of spots is put into a disperser tunes so that the spectra interleave and do not intersect.

The recently upgraded lenselt array, installed as part of the NALES upgrade, increases the number of spaxels from 50 x 50 to 73 x 73, it increases the lenslet pitch from 360μm x 360μm to 500μm x 500μm, and it increases the length of each spectrum from 36 pixels to 80 pixels.  This upgraded version of ALES has a lenslet array that pre-corrects the field dependent astigmatism by defining a different aspheric lenslet description for each lenslet. Each lenslet pre-corrects astigmatism before it gets added back in by this biconic and going to the detector. By correcting for the astigmatism in advance, the usable field of view is increased and spectral resolution is increased. Another part of the upgrade involved implementing new reflective magnifiers. These will allow for the accommodation multiple wavelengths and plate scales.

| Magnifier | Spaxel Plate Scale | Field-of-View | Spectral Resolution |
| --- | --- | --- | --- |
| 6x |  |  |  |
| 12x | 33.76 mas/spaxel | 2”x2” | R~70 |
| 25x |  |  |  |
| 50x |  |  |  |

The prisms are zinc solenoid prisms. The available prisms for NALES science are:

| Wavelength Range  μm | Spectral  Resolution | Modes/Bands |
| --- | --- | --- |
| 2.8-4.2 | ~40 | L-band |
| 3.0-5.0 | ~20 | L/M-band |
| 2.2-3.7 | ~40 | Ice |
| 2.0-2.3 | ~150 | Ks / Brγ |
| 3.1-3.5 | ~100 | PAH / CH4 |

New magnifiers enable a variety of plate scales to sample different wavelengths at the diffraction of the 8.4m mirror or 22.8m baseline.

A magnifier is placed just after the first pupil plane, a lenslet is placed at the second  focal plane, with a prism near the second focal plane

Additional details about observing strategies and planning NALES observations can be found [here](https://scienceops.lbto.org/lbti/planning-observations/modes-and-strategies/nales/).

## NOMIC Overview {#TOC-NOMIC-Overview}

NOMIC is the longer-wavelength IR camera, sensitive to 8-13 µm camera. It is optimized for nulling interferometry but has general capability for direct imaging, low resolution spectrometry, and Fizeau interferometry. The camera uses a Raytheon 1024×1024 Si:As IBC Aquarius array with a 30 μm pitch which yields 0.018 arc-second pixels on the sky. This provides spatial resolution (λ/D) at a 10 μm wavelength of 0.27 arc-seconds for a single 8.4 meter LBT aperture, and of 0.10 arcseconds for Fizeau interferometry with the dual apertures.

The array is operated with a differential preamplifier and a version of the 16 channel array controller developed at Cornell University for the FORCAST instrument on the Sofia Observatory. With a 2.4 MHz pixel rate, the camera can achieve integration times as short as 27 milliseconds for the full array and 3 milliseconds for a partial array. The large range of integration times and two array integration well sizes allow for a wide range of background flux on the array

## PhaseCam {#TOC-PhaseCam}

PhaseCam is not a science detector but rather a tool. Phasecam is an near-IR camera using a fast-readout PICNIC detector to measure tip/tilt and phase variations between the two AO-corrected LBT apertures. This camera receives the near-infrared light from both interferometric outputs when in either the nulling or the Fizeau imaging mode.

The PHASECam optics provide a field of view of 10 arcsecs with pixels of 0.078 arcsecs wide with 1 kHz readouts (although slower readouts possible for fainter targets) of picked off 2.0-2.4 µm light from the apertures.  It can be adapted to create different setups for pathlength sensing:

1. use the relative intensity between the two interferometric outputs
2. use dispersed fringes via a low-dispersion prism, or
3. use an image of the combined pupils via a reimaging lens.

The pupil plane was chosen because the Fourier transform of the wavefront allows a clean disentangling of the tip-tilt and phase variation into the transform’s amplitude and phase, and the fact that the transform’s amplitude has a signal distinct from the zero-frequency component..

The phase sensing light is derived from the lights that goes through the nulling interferometer. In nulling mode, one output of the interferometer is reflected to the NOMIC science detector with a short pass dichroic.

For Fizeau imaging mode, both beams are intercepted before beam combination so the phase sensor is a completely different beam path from the image beam combination, so work is being done to construct a control loop which uses science detector readouts to provide control that supplements the action of Phasecam optimizing and stabilizing the OPD and di.erential tip-tilt variations.
