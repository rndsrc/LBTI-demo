---
url: https://scienceops.lbto.org/wp-content/uploads/2024/05/LBTI_user_manual_v0.11.pdf
title: LBTI User's Manual (PDF v0.11)
breadcrumb: LBTI User's Manual PDF v0.11
version: v0.11
fetched_at: '2026-10-26T06:33:47+00:00'
source_sha256: 40895eb7e8429879061a34fa1cd4aa3764e9bdc12dcaaec33a1b2845668d1ba8
sha256: 61b764b03a794cdd407f16bc8ddae708fed07f7aba0cc6c7fa6ac5ab0c181cc9
---

<!-- page: 1 -->

# LBTI user manual

Version 0.11, released: 2024-05-09 Prepared by: S. Ertel Reviewed by: TBD.

LBTI observing team in front of the instrument in February 2016.

<!-- page: 2 -->

## Revision History

|Version|Date|Prepared by|Version notes|
|---|---|---|---|
|0.1<br>0.11|2022-03-15<br>2024-05-09|S. Ertel<br>S. Ertel|Pre-release.<br>minor clarifcations regarding the use of<br>the terms chopping and nodding.|

**IMPORTANT NOTE:** This is an early release of the LBTI user manual. The information
provided here is incomplete and not always 100% reliable. The current version has not been
independently reviewed and approved. Nonetheless, the current version contains a plethora
of useful information about the LBTI that was not well documented before or scattered
across a range of publications and web pages, and often outdated. We will continue working
on this document and provide an improved version as soon as possible.

<!-- page: 3 -->

## Contents

**Revision History ii**

**1 Scope of this document 1**

**2 Introduction to the LBTI 2**
2.1 LBTI overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 LBTI availability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.3 LBTI user policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.4 Acknowledging the use of the LBTI . . . . . . . . . . . . . . . . . . . . . . . 6
2.5 Exemplary use cases of the LBTI . . . . . . . . . . . . . . . . . . . . . . . . 6
2.5.1 General requirements for LBTI observations . . . . . . . . . . . . . . 6
2.5.2 Hunt for Observable Signatures of Terrestrial planetary Systems (HOSTS) 7
2.5.3 LBTI Exozodi Exoplanet Common Hunt (LEECH) . . . . . . . . . . 8
2.5.4 A gravitationally lensed quasar . . . . . . . . . . . . . . . . . . . . . 8
2.5.5 Thermal emission from ejecta of the VY CMa supergiant . . . . . . . 8
2.5.6 Young circumstellar disks and their planets . . . . . . . . . . . . . . . 8
2.5.7 Fizeau-interferometric imaging of volcanos on the surface of Io . . . . 9
2.5.8 ALES integral-field spectroscopy of circumstellar companions and brown
dwarfs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.5.9 Non-redundant aperture masking . . . . . . . . . . . . . . . . . . . . 9

**3 LBTI characteristics 10**
3.1 LBTI wavefront sensors and AO performance . . . . . . . . . . . . . . . . . 10
3.1.1 Technical description of wavefront sensor board . . . . . . . . . . . . 11
3.1.2 General acquisition and observing procedure . . . . . . . . . . . . . . 12
3.1.3 Field rotation and considerations if the AO reference sources is not the
science target . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.2 Universal Beam Combiner use and characteristics . . . . . . . . . . . . . . . 13
3.2.1 Center bent Gregorian mount . . . . . . . . . . . . . . . . . . . . . . 13
3.2.2 UBC entrance window dichroic . . . . . . . . . . . . . . . . . . . . . 15
3.2.3 UBC image stops . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.2.4 Pupil mirrors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2.5 Pathlength correctors . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2.6 Roof mirrors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

<!-- page: 4 -->

3.2.7 Cold vs. warm UBC and link to image quality . . . . . . . . . . . . . 17
3.3 NIC optical layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.4 LMIRCam and ALES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.4.1 Observing modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.4.2 LMIRCam Detector . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.4.3 ALES principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.4.4 Filters and optics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.4.5 High-contrast imaging performance . . . . . . . . . . . . . . . . . . . 28
3.4.6 Distortion correction and astrometry . . . . . . . . . . . . . . . . . . 30
3.5 NOMIC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.5.1 Observing modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.5.2 NOMIC detector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.5.3 Filters and optics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.5.4 Distortion correction and astrometry . . . . . . . . . . . . . . . . . . 36
3.6 PhaseCam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.6.1 Optical layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.6.2 Approach to phase and tip-tilt sensing and control . . . . . . . . . . . 39
3.6.3 Limiting magnitude . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

**4 Observing planning and execution 41**
4.1 Infrared observing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.1.1 Infrared atmospheric windows . . . . . . . . . . . . . . . . . . . . . . 41
4.1.2 Impact of infrared background . . . . . . . . . . . . . . . . . . . . . . 42
4.1.3 Nodding, chopping, and connection to LBTI data . . . . . . . . . . . 43
4.2 Observing modes and strategies . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.3 Parallel use of LBTI modes and LBT instruments . . . . . . . . . . . . . . . 47
4.4 Queue execution and observing instructions . . . . . . . . . . . . . . . . . . 48
4.5 Observing scripts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.6 Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
4.7 Overheads, time request, and execution time . . . . . . . . . . . . . . . . . . 51
4.8 Data retrieval and reduction . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

**List of names and acronyms 57**

<!-- page: 5 -->

# 1 Scope of this document

This document is intended to be the primary source of information for science users of the
Large Binocular Telescope Interferometer (LBTI). It complements the support provided by
the LBTI team and contains mostly static information, as well as links to more dynamic
information that may change over time. Principal Investigators (PIs) of LBTI observing
programs (science PIs, users) should refer to this document for determining whether an observing project is feasible and for planning their observations. The basic operating principles,
technical detail, and performance of the LBTI are described. The more technical sections of
the user manual may also be of interest for researchers who are interested in the LBTI as an
instrumentation project.

The creation of a user manual is part of the LBTI’s transition from a strategic (PI) instrument to a general-use science instrument with the goal of fully integrating it into the
observatory as a facility instrument. Therefore, information on instrument characteristics
and performance that were previously not formally available need to be collected and formally documented. The user manual is the place where this documentation is happening.
Thus, this is a living document which will grow as more information are added.

In addition, the information in this document is by design incomplete: The LBTI is and
will remain an active instrumentation project that is offered to the community for exploiting
the available instrument modes and its unique capabilities. Furthermore, observations are
not executed by users but by the LBTI observing team. Thus, both high-level information
concerning actively developed aspects of the instrument and low-level details on its operations
are omitted. Users should always feel welcome to contact the LBTI’s Lead Scientist, Steve
Ertel, at [sertel@lbti.org](mailto:sertel@lbti.org) for further information that is not included in this document.

<!-- page: 6 -->

# 2 Introduction to the LBTI

In this chapter, we provide a high-level description of the LBTI, its availability, and exemplary
use cases.

## 2.1 LBTI overview

The LBTI is a strategic (PI) instrument for the Large Binocular Telescope (LBT) developed
by the LBTI team at the University of Arizona (former PI: Phil Hinz, current Lead Scientist
Steve Ertel). Primary funding for the LBTI was provided by National Aeronautics and Space
Administration (NASA)’s Exoplanet Exploration Program (ExEP) and managed by the Jet
Propulsion Laboratory (JPL) together with the University of Arizona. The purpose of the
NASA funding was the development of the instrument and the execution of it’s primary
science mission, the nulling interferometric survey for exozodiacal dust (warm dust in and
near the habitable zones of main sequence stars) through the Hunt for Observable Signatures
of Terrestrial planetary Systems (HOSTS) survey (Ertel et al. 2018, 2020a). Major additional
funding was provided by the National Science Foundation, the LBT partnership, and the
University of Arizona to leverage the initial NASA funding and make the LBTI a versatile,
general use instrument for the LBT (Hinz et al. 2016; Ertel et al. 2020b).

The instrument is designed for sensitive, high-contrast, and high-angular resolution observations in the thermal infrared (L, M, N bands) with additional wavelength coverage in
the near-infrared (J, H, K bands). The instrument can be used for Adaptive Optics (AO)
observations using the two primary apertures of the LBT separately and for nulling and
imaging interferometry combining the two apertures. LBTI’s focus is on imaging observations (including interferometric imaging) and integral field spectroscopy, but some additional
spectroscopic capabilities are also available. The use of LBT’s Adaptive Secondary Mirror (ASM) and the instrument’s design with a fully cryogenic optical path downstream of
the telescope’s tertiary mirror give the LBTI superior thermal infrared sensitivity compared
to other ground-based instruments and in particular compared to optical long-baseline interferometers.

The LBTI is located between the two 8.4 m primary mirrors of the LBT at their combined
f/15 center bent Gregorian foci (Fig. 2.1). It is directly attached to the telescope mount,
so that its orientation is fixed with respect to the telescope’s pointing direction and pupils.
The LBTI does not have an instrument rotator, so that due to the telescope’s altitudeazimuth mount the sky always rotates with respect to the orientation of the instrument (thus

<!-- page: 7 -->

**Figure 2.1:** Location of the LBTI inside the red, rectangular support structure between the two
primary mirrors of the LBT. In this picture the telescope is not configured to send light to the
LBTI.

on the science camera detectors) around the AO reference source following the Parallactic
Angle (PA).

For most observations, the LBTI uses the light from LBT’s two primary apertures and
projects it onto the same science camera detector. The two beams can be imaged individually by placing them next to each other on the detector, or combined for interferometric
observations. For the latter, there are two modes: The beams can be combined co-axially
in the pupil plane for nulling interferometry in the N band using the 14.4 m center-to-center
baseline of the two primary apertures. Alternatively, they can be combined multi-axially
in the focal plane for wide-angle Fizeau imaging interferometry or non-redundant aperture
masking (NRM) in the H to N bands using baselines up to the 22.8 m edge-to-edge separation
of the primary mirrors. A high-level sketch of the LBTI’s optical layout is shown in Fig. 2.2.

Through each of the LBT’s two primary apertures, light from the sky is sent by the
telescope’s primary mirror, ASM, and tertiary mirror to the LBTI in the center. Once the
incoming beams from the left and right telescope aperture are received by the two sides of
the Universal Beam Combiner (UBC), the light on each side is split by the wavefront sensor
dichroics into red-visible and infrared light. Red-visible light (predominantly R and I bands)
is reflected to the wavefront sensor boards where it is analyzed for AO corrections that are
sent to the telescope’s ASMs.

The wavefront sensor dichroics also serve as entrance windows that transmit the infrared
light (J to N bands) into the cryogenic UBC (temperature ∼ 80 K). The UBC, is responsible
for combining the beams, for tip-tilt and interferometric path-length correction, and pupil
alignment. It then sends the light to the Nulling and Imaging Cryostat (NIC), which is kept

<!-- page: 8 -->

**Figure 2.2:** High-level sketch of the LBTI’s optical layout. See description in Sect. 2.1.

at a temperature of ∼ 60K. Inside NIC, a selectable beam splitter transmits either the L to
M band light or the H to M band light to the LBT Mid-InfraRed Camera (LMIRCam) and
reflects either the H to K band light and the N band light, or only the N band light. The
reflected light is further separated in near-infrared and mid-infrared light. The near-infrared
light is sent to LBTI’s fringe tracking camera (PhaseCam), while the mid-infrared light is sent
to the Nulling-Optimized Mid-Infrared Camera (NOMIC). the Arizona Lenslet for Exoplanet
Spectroscopy (ALES) is a set of optics within LMIRCam that creates an integral field unit
optimized for observations in the L and M bands (Skemer et al. 2015, 2018; Hinz et al. 2018).

## 2.2 LBTI availability

The LBTI is a strategic (PI) instrument developed, maintained, and operated by the LBTI
instrument team based at Steward Observatory in collaboration with - and with significant
support from – the LBT observatory. The instrument is offered to all researchers with access
to LBT time through collaboration with the LBTI instrument and science team. Researchers
without direct access to LBT time may apply for LBT time through director’s time requests
or through collaboration with researchers who have LBT access (including the LBTI team

<!-- page: 9 -->

itself).

Teams interested in using the LBTI are encouraged to contact the LBTI team through
its Lead Scientist, Steve Ertel, at [sertel@lbti.org](mailto:sertel@lbti.org) to develop an observing project. As a
minimum, we request that interested teams obtain approval from the Lead Scientist before
submitting a proposal. This should be done by email to [lbtipi@lbto.org](mailto:lbtipi@lbto.org) approx. one week
before the relevant proposal deadline. The email should contain a description of the project
or a proposal draft, together with the amount of observing time requested. This procedure
has been put in place for ensuring that proposers receive adequate support by the LBTI team
so submitted proposals are generally feasible and well planned out given the complexity of
the instrument. The process also ensures adequate planning and allocation of resources for
the upcoming observing semester. The goal of this process is NOT to limit access to the
LBTI.

Note that LBTI’s thermal infrared integral field unit ALES is a separately funded PI
component of the instrument and its use does require collaboration with the ALES team.
The main benefit of this collaboration is that the ALES team will provide pre-reduced data
(calibrated spectral image cubes) to the science PIs, a service that the LBTI team does not
generally provide. Researchers interested in using ALES should contact Jordan Stone at
[jordan@lbti.org](mailto:jordan@lbti.org) in addition to the general request for using the LBTI to [lbtipi@lbto.org.](mailto:lbtipi@lbto.org)

## 2.3 LBTI user policy

The LBTI is a strategic (PI) instrument on the LBT. While some components such as
LMIRCam and the AO system may be considered to have a facility-like status, the instrument is developed, maintained, and operated by an independent team as a scientific and
instrumentation project. It is our policy to make the instrument as widely accessible as
possible. In return, our science PIs accept the following policy when submitting a proposal
to use the LBTI:

 - The LBTI team shall be consulted prior to proposal submission through an email to
[lbtipi@lbto.org.](mailto:lbtipi@lbto.org)

 - Team members involved in enabling or supporting a specific observation shall be given
the opportunity to be involved in the project, with the possibility of becoming a coauthor on resulting publications.

 - The use of the LBTI shall be acknowledged prominently (see below).

 - In addition to their individual user policies, the LBTI policy shall also apply to the
use of ALES and to some extent to be determined at an appropriate time to future
instrumentation making use of the LBTI architecture or procedures.

 - This policy also applies to data obtained with other LBT instruments when used in
parallel with LBTI observations during telescope time allocated to an LBTI observation. In this case, the PI of the LBTI observation is to be considered a co-owner of
these data and involved in the project accordingly.

<!-- page: 10 -->

## 2.4 Acknowledging the use of the LBTI

‘LBTI’ shall be mentioned in the title or abstract of the paper. In addition, the following
phrase shall be included in the acknowledgements:

_‘We_ _acknowledge_ _the_ _use_ _of_ _the_ _Large_ _Binocular_ _Telescope_ _Interferometer_ _(LBTI)_ _and_ _the_
_support_ _from_ _the_ _LBTI_ _team,_ _specifically_ _from_ _XX.’_

(replace ‘XX’ with a list of team members involved in enabling or supporting the observations
but not included as co-authors, please inquire with Steve Ertel at [sertel@lbti.org](mailto:sertel@lbti.org) if unsure).

## 2.5 Exemplary use cases of the LBTI

The LBTI is designed for sensitive mid-infrared observations at high angular resolution and
high contrast. The primary science focus of the LBTI team is on exoplanet and circumstellar
disk science. The development of the LBTI was funded by NASA through ExEP to conduct
nulling interferometric observations of exozodiacal dust (warm dust in the habitable zones
of nearby stars). For this purpose, the HOSTS survey was conducted (Ertel et al. 2018,
2020a). The LBTI has also carried out the NASA funded LBT Exozodi Exoplanet Common Hunt (LEECH) AO-assisted direct imaging survey for giant exoplanets in the L band
(Stone et al. 2018). Through collaboration with science teams across the LBT partnership
and occasionally outside the partnership, the LBTI has also been used for a wide range of
Solar system, galactic, and extragalactic science. In the following, we discuss a few general
requirements for a successful LBTI observation before we describe exemplary science cases
to illustrate the LBTI’s capabilities. These examples may serve as illustrations of the typical
use cases of the instrument. More information can be found in the corresponding references.

### 2.5.1 General requirements for LBTI observations

**Adaptive optics**

The LBTI is inherently an AO instrument. As such, it requires a natural reference source
for AO correction and guiding. This can be a star or a resolved but compact object such as
a Solar system moon (Jupiter’s moon Io with an angular diameter of ∼ 1 arcsec has routinely
been used) or the core of a galaxy. The limiting magnitude for the AO system is around R
or I ∼ 18 for isolated point sources. Peak performance is reached on stars down to R or I ∼ 12.
The AO performance is reduced for resolved AO reference sources and limiting magnitudes
decrease for faint sources that are surrounded by significant diffuse emission (such as cores
of galaxies). Non-AO observations are not entirely technically impossible but generally not
done; researchers interested in this are welcome to contact the LBTI team to discuss options.

<!-- page: 11 -->

**Infrared-bright field source**

The science focus of the LBTI team is on high-contrast observations such as exoplanets and
circumstellar disks. Such observations have in common the fact that there is a relatively
bright, point-like source in the science camera field of view (FoV). The LBTI does not have
an instrument rotator and the sky rotates on the detector around the AO reference source,
so that only the AO reference source remains stationary on the detector. This field rotation
is taken advantage of, e.g., in angular differential imaging for high-contrast observations.
Typical LBTI data reduction involves centering images on a bright reference source and derotating images before stacking. Multiple images can be stacked without de rotation to locate
a faint source if it is also the AO reference source. If the reference source is not detectable
this way or is outside the science camera FoV, there needs to be at least one other bright
sources in the science camera FoV that is visible in very few, short exposures (typically of
the order of 1 s to a few seconds total integration time) to be used as reference for centering
and de-rotation of the images. Required source magnitudes are H ∼ 15, L ∼ , M ∼ , and N ∼ 4
( ∼ 1Jy) for broad band filters. If these criteria are satisfied, the LBTI can be used for
particularly sensitive observations of other, fainter sources in the field such as circumstellar
planets. Some strategies may be used to relax those constraints, but such observations need
to be considered experimental and close collaboration with the LBTI team for planning and
execution is critical for their success.

**Small FoV and need for background subtraction**

As an instrument designed for high-contrast imaging and high angular resolution, and as an
infrared instrument, the LBTI has a relatively small FoV of up to 20 arcsec and as small
as 2 arcsec for integral field spectroscopy. In addition, the LBTI uses field offsets (nodding
and/or chopping) for background subtraction and suppression of detector cosmetics and
systematics. This is typically done keeping the science target in the FoV in both offset
positions, effectively reducing it by a factor of 2. Nodding and chopping ’off chip’ is possible,
but reduces the observing efficiency as up to 50% of the integration time is spent off target.
The need for field offsets also means that there needs to be a sufficiently empty sky region
within reach of the maximum offset (nod throw ∼ 1 arcmin, chop throw ∼ 7 arcsec).

### 2.5.2 Hunt for Observable Signatures of Terrestrial planetary Systems (HOSTS)

LBTI’s core science mission, HOSTS, targeted nearby main sequence stars to search for
exozodiacal dust in their habitable zones. The survey used nulling interferometry in the
N band with NOMIC to suppress the bright star light and to spatially resolve and detect
the thermal emission from the warm dust. For nulling interferometry, the light from the
two 8.4 m apertures of the LBT is combined in the pupil plane and then re-imaged on the

<!-- page: 12 -->

detector. PhaseCam is used in K band to stabilize the interferometric phase between the
two apertures using phase-delay tracking. The survey results are described by Ertel et al.
(2018) and Ertel et al. (2020a) with references to papers describing sample selection, data
reduction, instrument performance, and modeling of the results.

### 2.5.3 LBTI Exozodi Exoplanet Common Hunt (LEECH)

LBTI’s second large science program, LEECH, used individual aperture high-contrast imaging in the L band with LMIRCam to search for giant exoplanets around nearby stars. The
thermal infrared is particularly sensitive to older planets around mature, nearby stars around
which close separations can be probed. The two apertures of the LBT were used simultaneously by placing the images from them next to each other on the detector. This way, the
two largely independent speckle patterns from the two apertures could be used to better
distinguish between companions and point spread function (PSF) subtraction residuals. The
survey results are described by Stone et al. (2018) including other pertinent references.

### 2.5.4 A gravitationally lensed quasar

Jones et al. (2019) imaged a gravitationally lensed quasar to constrain the distribution of dark
matter in the lensing galaxy. The four images of the quasar were resolved using adaptive
optics imaging. The faint limiting magnitude of LBTI’s wavefront sensors was critical to
close the AO loop on the quasar itself, enabling LBTI observations of this target. The four
images were separated from each other and LMIRCam’s sensitivity allowed for obtaining a
high signal-to-noise ratio (S/N) photometry, so that the flux ratio between the components
could be measured with high precision.

### 2.5.5 Thermal emission from ejecta of the VY CMa supergiant

Gordon et al. (2019) used NOMIC to detect for the first time the thermal emission of the
south-western clump of ejected matter from VY CMa. Observations were carried out using single-sided, AO-assisted imaging in the N band. Combined with previous LMIRCam
and HST data of the clump’s scattered light, they isolated the spectral energy distribution
of the clump from that of the star and constrained the clump’s optical depth, mass, and
temperature.

### 2.5.6 Young circumstellar disks and their planets

Wagner et al. (2019) and Wagner et al. (2020) used AO-assisted direct imaging with LMIRCam
to image protoplanetary disks in the thermal infrared, characterize their structures, and
search for candidate planets. The thermal infrared is particularly useful for this due to the
more favorable contrast between the star, disk, and possible planets and the ability to probe

<!-- page: 13 -->

deeper into the optically thick disks at these wavelengths. Observations across a range of
near-infrared and thermal-infrared observations (including spectra obtained with ALES) allow one to constrain the spectral shape of the emission and thus to distinguish between a
dust clump and a planet.

### 2.5.7 Fizeau-interferometric imaging of volcanos on the surface of Io

One of the unique capabilities of LBTI is Fizeau interferometry, which allows for obtaining
snapshot images with a relatively wide FoV (several arcsec) across the 23 m maximum interferometric baseline of the LBT. Conrad et al. (2015) used this capability to image the
volcanos on the surface of Io with an unprecedented combination of sensitivity and angular
resolution in the thermal infrared. In addition, de Kleer et al. (2017) used the snapshot
capabilities and high angular resolution of the Fizeau mode to map Io’s Loki patera during
an eclipse of Io by Jupiter’s other moon Europa. Observations of Io are carried out with the
AO loops closed on the moon itself but with the Phase loop open (‘lucky fringing’) because
fringe tracking on such an extended source is not feasible.

### 2.5.8 ALES integral-field spectroscopy of circumstellar companions and brown dwarfs

Stone et al. (2020) used ALES integral-field spectroscopy in the L band to determine the
properties of the sub-stellar companion _κ_ And b. Briesemeister et al. (2019) used ALES
to separate the two components of the benchmark binary brown dwarf HD 130948 BC from
each other and to obtain separate L band spectra of the two components.

### 2.5.9 Non-redundant aperture masking

Sallum et al. (2015) used individual-aperture NRM in with LMIRCam to detect the first
candidate planetary-mass companion inside a protoplanetary disk. In this mode the images
from the two LBT apertures are placed next to each other on the LMIRCam detector for 8.4 m
angular resolution. Sallum et al. (2017) combined the two LBT apertures for 23m-resolution
NRM to constrain the properties of the disk around the Herbig B[e] star MWC 349 A. These
observations were carried out without phase control. Finally, Sallum et al. (2021) used
phase-controlled NRM across the 23m baseline to image the disk around the Herbig Ae/Be
star MWC 297. A very short ( ∼ 10 min) science observation was sufficient to put critical
constraints on the disk structure.

<!-- page: 14 -->

# 3 LBTI characteristics

In this chapter, we describe the technical characteristics of the LBTI and its components, as
far as they are relevant for planning and carrying out a science program with the instrument.
Basic information required for planning a standard observation is provided mostly in the
pages describing the wavefront sensors and science cameras, plus PhaseCam for interferometry. We include details useful for developing non-standard observations and some technical
details of the instrument that may be useful as a starting point for researchers interested in
the LBTI as an instrumentation project.

The LBTI consists of several sub systems:

 - The wavefront sensors, one for each LBT primary aperture (Bailey et al. 2014; Pinna
et al. 2016).

 - The cryogenic Universal Beam Combiner (UBC) that combines the beams from LBT’s
two primary apertures is responsible for beam steering and interferometric pathlength
correction, and sends the beams to NIC (Hinz et al. 2016).

 - The the Nulling and Imaging Cryostat (NIC) that hosts LBTI’s science cameras and
LBTI’s fringe tracking camera (PhaseCam) (Hinz et al. 2016).

 - The the LBT Mid-InfraRed Camera (LMIRCam) for observations in the J to M bands,
including the the Arizona Lenslet for Exoplanet Spectroscopy (ALES) (Skrutskie et al.
2010; Leisenring et al. 2012; Hinz et al. 2018).

 - The the Nulling-Optimized Mid-Infrared Camera (NOMIC) for observations in the
N band (Hoffmann et al. 2014).

 - LBTI’s fringe tracking camera (PhaseCam), responsible for interferometric phase sensing in the H and K bands (Defr`ere et al. 2015).
The references listed above provide a general overview of the original design and performance
of the individual subsystems. The following sections contain the relevant, current information
which may deviate significantly due to instrument upgrades, further characterization, etc.

## 3.1 LBTI wavefront sensors and AO performance

LBT is equipped with Adaptive Secondary Mirrors (ASMs) in a distributed Adaptive Optics
(AO) system. This means that the two secondary mirrors of the telescope are deformable,
while the wavefront sensors are located on the LBTI’s optical bench. The telescope is in
a Gregorian configuration when configured for LBTI observations with the UBC located
at the center bent Gregorian foci between the two primary mirrors. The ASMs contribute

<!-- page: 15 -->

**Table 3.1:** Performance parameters of LBTI’s AO system.

|Wavelength range|R to I band|
|---|---|
|Acquisition camera feld of view|17 arcsec|
|Natural reference source magnitude for operation|R or I < 18|
|Natural reference source magnitude for peak performance|R or I < 12|
|Maximum loop speed|1.7 kHz|
|Maximum number of modes corrected|600|
|Wavefront sensor board patrol feld| ∼ 2 arcmin|
|Maximum number of sub-apertures|40 × 40|
|Wavefront sensor camera read noise| < 1 e-|
|ASM rise time|0.5 ms|

critically to LBTI’s excellent thermal infrared performance as they require no additional
warm reflections for AO correction compared to a seeing-limited instrument.

Each ASM has a diameter of 0.911 m and 672 actuators. The LBTI uses pyramid wavefront
sensors which provide excellent performance and limiting magnitude. This performance
has been further enhanced by the Single conjugated adaptive Optics Upgrade for the LBT
(SOUL) system currently under final commissioning and available for science observations.
LBTI requires a natural reference source for AO correction and guiding, which can be, e.g.,
a star, core of a galaxy, or a Solar system moon such as Jupiter’s Io. Table 3.1 summarizes
the performance parameters of LBTI’s AO system.

### 3.1.1 Technical description of wavefront sensor board

The wavefront sensor boards are located on each side of the LBTI’s optical bench, outside the
UBC cryostat. A sketch of their optical layout is shown in Fig. 3.1. R and I band light from
the telescope’s tertiary mirror is reflected off the UBC entrance windows (which double as
wavefront sensor dichroics to further reduce the number of warm reflections) to the wavefront
sensor board. A set of re-imaging lenses create the correct focal length. After passing an
atmospheric distortion corrector, the light hits Filter Wheel (FW) 1. This wheel contains a
set of gray beam splitters with different transmission (a window for full transmission, 10%,
1%, and 0.1% transmission gray beam splitters, and a blank for full reflection) that effectively
act as neutral density filters for the wavefront sensor and reflect to the acquisition camera
the fraction of the light that is not transmitted.

Light reflected off the beam splitter is further reflected by a fold mirror and passes another
filter wheel with an open position and a set of neutral density filters before it is imaged on the
acquisition camera detector (CCD 47). This camera has a FoV of 17 arcsec and is generally
used for basic LBTI target acquisition.

Light transmitted by FW 1 is reflected off the tip-tilt modulator used for wavefront sensing

<!-- page: 16 -->

**Figure 3.1:** High-level sketch of an LBTI wavefront sensor board. See description in Sect. 3.1.1.

and off a fold mirror. It then hits the tip of the pyramid before passing a camera lens that
re-images the four pupils from the pyramid on the wavefront sensor camera (an OCAM 2k).

The wavefront sensor boards are mounted on a x-y-z translation stages (”Bayside stages”)
which allow for movement of the board in the focal plane and perpendicular to it (in the focus
direction). This allows for relative movement of the wavefront sensor board with respect to
the telescope optical axis and thus for acquiring reference sources across the ∼ 2 arcmin patrol
field.

### 3.1.2 General acquisition and observing procedure

During presets, the Bayside stages are usually set to a ’sweet spot’ position, which means if
a star is on the tip of the pyramid it is also in a desired position on the science camera. Once
a target is identified in the 17 arcsec FoV of the CCD 47 acquisition camera, small telescope
offsets are used to move it to the nominal position on CCD 47, which coincides with the tip
of the pyramid, and the AO loop is closed. The AO loop then controls the fine guiding of
the telescope. After telescope offsets to reposition the star on the science camera (e.g., for
background subtraction), the bayside stages move accordingly to put the star back on the
tip of the pyramid and the AO loop is re-closed in this new position.

<!-- page: 17 -->

### 3.1.3 Field rotation and considerations if the AO reference sources is not the science target

Because the LBTI is directly attached to the telescope mount (i.e., the whole instrument
tips with the telescope in elevation), and has no de-rotator, the orientation of the instrument
pupil is always fixed with respect to that of the telescope pupil (always ‘pupil tracking’). Due
to the altitude-azimuth mount of the telescope, this means that the sky generally rotates with
respect to the instrument pupil and the detectors. Because fine guiding of the telescope is
performed by the AO loop, the sky always rotates around the AO reference source. This
has important consequences for AO reference sources that are not the science target itself
(off-axis reference sources): While the AO loop can in principle be closed on a source as
far as ∼ 60 arcsec away from the science target, field rotation will then move the science
target across the science detector (and possibly off the science detector if not compensated
for) at an increasing speed with increasing separation from the AO reference source. This
may put significant constraints on integration time and required source brightness of such
observations.

## 3.2 Universal Beam Combiner use and characteristics

The Universal Beam Combiner (UBC) is responsible for picking up the beams from the two
primary telescope apertures and sending them to the the Nulling and Imaging Cryostat (NIC)
where LBTI’s science cameras are located. The UBC is also responsible for beam steering
(pupil and cold stop alignment, fine tip/tilt positioning of the source on the detector), and
interferometric pathlength correction. In addition, it hosts a switch yard to divert the beams
to ancillary instruments and cameras outside NIC such as iLocater. An image of the LBTI
with the UBC well visible is shown in Fig. 3.2. A high-level sketch of the LBTI including
the UBC is shown in Fig. 3.3.

Infrared light enters the UBC from the two primary telescope apertures through the entrance window dichroics (1, 2) and is then reflected of the ellipse mirrors (3, 4) which create
a pupil plane on the pupil mirrors (5, 6). Light is then reflected off the roof mirrors (7)
and down into NIC where chromatic beamsplitters (8, 9) divert the light to LBTI’s science
and fringe tracking cameras. In the following, the user-relevant, individual components of
the UBC and their purpose and abilities are discussed in the order they are hit by incoming
light.

### 3.2.1 Center bent Gregorian mount

The UBC is located between the two primary apertures of the LBT in the center bent Gregorian position. It is directly attached to the moving telescope mount so that the orientation of
its pupil with respect to the telescope pupil is always fixed. LBTI does not have a de-rotator,

<!-- page: 18 -->

**Figure 3.2:** Picture of the LBTI
with the UBC well visible (metallic
green, T-shaped pipe structure).
Picture taken in Summer 2016; the

switch yard and iLocater structure were not yet installed. The
dark-blue box below the UBC is

NIC. Light is sent to the LBTI
by the telescope’s tertiary mirror
through the two large, round open
ings in the red telescope structure.

**Figure 3.3:** High-level sketch of the LBTI with the UBC. See description in Sect. 3.2.

so that it is always in ‘pupil tracking’ mode. This results in superb stability of the thermal
background structure from the telescope that can then be well removed from the images
using chop or nod subtraction.

<!-- page: 19 -->

**Figure 3.4:** UBC entrance window
rotator with only the LBTI window
(top) installed. See description in
Sect. 3.2.2.

### 3.2.2 UBC entrance window dichroic

Light enters the LBTI through the entrance window dichroic, i.e., an entrance window that
also serves as a dichroic for the wavefront sensor. This way, the additional warm optic of
a separate dichroic can be avoided. Light longward of ∼ 1 micron is transmitted into the
UBC while shorter wavelengths are reflected to the wavefront sensor board. The entrance
window dichroic is mounted on a rotator (similar to a filter wheel) on a hydrostatic bearing
(Fig. 3.4). This allows for switching between two windows; the original LBTI window and
one optimized for the iLocater wavelength range. Two additional slots for other dichroics
are available but currently unused.

### 3.2.3 UBC image stops

One filter wheel on each side is located inside the UBC behind the entrance window dichroic,
near the focal plane of the telescope. These filter wheels hold image stops: Each wheel
contains an open position, a cold field stop, a pinhole stop, and a pinhole grid (the latter
two for engineering purposes). The wheel can also be put in a ’closed’ position by moving
it between slots, which is generally sufficient for engineering purposes and some science
purposes. The cold field stops in the two wheels are complementary in a sense that they
block opposite sides of the FoV. This way, the images of a target from the two apertures
can be placed next to each other on a science camera detector without also overlapping the
backgrounds of the two fields, exploiting the full collecting power of the LBT for backgroundlimited observations.

<!-- page: 20 -->

**Figure 3.5:** Pupil mirror with imprinted masks.

### 3.2.4 Pupil mirrors

The pupil mirrors are flat mirrors with imprinted masks (Fig. 3.5) that block the thermal
emission from the telescope’s ASM and the hole in the corresponding primary telescope
mirror and the light from outside the primary. This significantly reduces the thermal infrared
background the LBTI receives from the telescope. Alignment of the telescope pupil with the
pupil mirrors is done through tip-tilt movements of the telescope’s tertiary mirror.

### 3.2.5 Pathlength correctors

The pupil mirrors are mounted on Fast Pathlength Correctors (FPCs). These are piezo stacks
(Fig. 3.6) for interferometric pathlength correction and fast, fine tip-tilt steering of each
mirror. They give each mirror a maximum stroke of 100 mircon in piston and the capability
to offset the beam by up to ∼ 7 arcsec on the science detectors. The FPCs can be operated
in closed-loop with PhaseCam at a frequency of up to 1 kHz for interferometric pathlength
correction. The tip-tilt capabilities of the pupil mirrors are also used for fine-centering of
a science target behind a coronagraph and for synchronized chopping with NOMIC. The
operating parameters of the pathlength correctors are listed in Table 3.2.

The the right telescope aperture (DX) (right) FPC is in addition mounted on a translation
stage, the Slow Pathlength Corrector (SPC), with a stroke of 32 mm for slow, coarse alignment
of the interferometric phase between the two primary apertures (analog to telescope delay
lines at optical long-baseline interferometers).

For closed-loop interferometric path-length correction, the two FPCs are redundant and
only one side is operated (typically the left telescope aperture (SX)). The SPC is usually

<!-- page: 21 -->

**Figure 3.6:** Fast pathlength corrector with pupil mirror (right).

**Table 3.2:** Operating parameters of the pathlength correctors.

|FPC maximum stroke|100 micron|
|---|---|
|SPC maximum stroke|32 mm|
|FPC maximum tip/tilt in arcsec on science camera| ∼ 7 arcsec|
|FPC maximum closed-loop operating frequency|1 kHz|

used only for initial phase alignment, but offloading of large phase strokes of the operated
FPC to the SPC is possible if needed.

### 3.2.6 Roof mirrors

After the pupil mirrors, the light from the two sides is reflected off the roof mirrors (Fig 3.7) to
the switch yard where it is left undisturbed and transmitted into NIC for routine LBTI operations. The roof mirrors can be moved in tip and tilt for pupil alignment and overlapping the
pupils from the two sides on NOMIC for nulling interferometry. Once the pupils are aligned
for a specific instrument setup, these mirrors are not moved throughout an observation.

### 3.2.7 Cold vs. warm UBC and link to image quality

The UBC is usually kept cold ( ∼ 80 K) during LBTI science observations. It can, however
be operated warm and at atmosphere at the cost of increased thermal background from the
additional warm reflections. Operating the UBC warm is occasionally preferred for increased
accessibility of the instrument and in particular acceptable for high-contrast observations
and other observations where the thermal background is not the dominant noise source.

<!-- page: 22 -->

**Figure 3.7:** Roof mirror
assembly inside the UBC.

Furthermore, obtaining light-weight pupil mirrors that can be used on the fast pathlength
correctors (see above), but remain flat at cryogenic temperatures has been a challenge. The
current version exhibits aberrations due to thermal stresses when the UBC is cold. While
this has been shown not to result in a critical loss of high-contrast performance, LBTI’s
image quality is currently better with a warm UBC.

## 3.3 NIC optical layout

The the Nulling and Imaging Cryostat (NIC) holds LBTI’s science cameras LMIRCam and
NOMIC and LBTI’s fringe tracking camera (PhaseCam). In addition, it holds an artificial
source (NAC source) for engineering purposes, a beam splitter to send light to the different
cameras, and a set of biconic mirrors to re-focus the light into the cameras. Fig. 3.8 shows
the optical layout of NIC and its cameras. The optical layout of the cameras is discussed in
further detail in the respective sections below.

The NIC Aperture Wheel is located at a focal plane and holds in addition to the open
position two Annular Groove Phase Mask (AGPM) coronagraphs (one for each telescope
primary aperture), a square aperture for sharp pupil imaging, two pinhole grids for internal
distortion measurements of the cameras inside NIC, and optics for imaging the NAC source.
For science observations, this wheel is most commonly put into the open position.

The NIC Beam Diverter holds two optics: (1) A trichroic is used for all thermal infrared
imaging as it sends the L and M bands to LMIRCam and the H, K, and N bands to NOMIC
and PhaseCam. (2) A window is usually only used for H or K band imaging with LMIRCam
as it sends the H to M band to this camera and only the L band to NOMIC. In the latter
configuration, PhaseCam receives no significant light and cannot be used. Whenever possible,
using the trichroic is preferred for its better optical quality compared to the window (the
latter shows a number of optical ghosts).

<!-- page: 23 -->

**Figure 3.8:** NIC and cameras optical layout. For details see Sect. 3.3. Figure from Spalding et al.
(2018) with minor modifications.

The various light paths for interferometric modes are indicated in Fig. 3.8. PhaseCam
can be used for fringe tracking irrespective of the channel used as long as the trichroic beam
diverter is used to send the H and K band light toward it.

## 3.4 LMIRCam and ALES

the LBT Mid-InfraRed Camera (LMIRCam) is one of the LBTI’s science cameras (the
other one being NOMIC), covering the near infrared and the thermal infrared up to the
M band. LMIRCam is commonly used as a sensitive, high-contrast, thermal-infrared camera. Available modes are standard imaging, coronagraphy (AGPM, vAPP coronagraphs),

<!-- page: 24 -->

non-redundant aperture masking (NRM), slit-less spectroscopy, and Fizeau imaging interferometry. NRM and Fizeau interferometry can be combined for NRM across LBT’s full 23 m
baseline and slit less spectroscopy and Fizeau interferometry can be combined for spectrointerferometry. LMIRCam also hosts the Arizona Lenslet for Exoplanet Spectroscopy (ALES),
which is a set of optical elements that allows for integral field spectroscopy. It is important
to note, that while some modes are routinely used for science observations, others are more
experimental and have not been fully commissioned.

### 3.4.1 Observing modes

**Plain AO imaging**

Standard Adaptive Optics (AO) imaging. A single side of the LBT or both sides can be
used. In the latter case, the images from the two sides are recorded next to each other on
the same detector. Cold UBC field stops can be inserted to avoid overlapping backgrounds
for exploiting the full collecting power of the LBT in the background limited regime. This
mode lready provides excellent contrast due to stable PSF and is commonly used for highcontrast imaging due to simplicity of the mode and low overheads. The main advantage of
double-sided, high-contrast imaging is that the two sides create largely uncorrelated speckle
patterns, which facilitates distinguishing faint sources from the speckle halo of nearby sources
(simultaneous confirmation observation). Currently, if both LBT apertures are used simultaneously, they still need to use the same filter, simultaneous observations in two filters are
not possible.

**Overlapped AO imaging**

A variation of plain AO imaging where the images from the two sides are overlapped on the

 √ 

detector. This improves the sensitivity in the read-noise limited regime by a factor of 2 at

n

 √ 

detector. This improves the sensitivity in the read-noise limited regime by a factor of 2 at

the cost of PSF stability and decreased observing efficiency. As the overlap is not perfect, this
is more useful for extended sources observations where contrast and image quality are less
of a concern than sensitivity. Experimental mode only with little on-sky or data reduction
experience.

**Coronagraphy**

A variation of plain AO imaging where a coronagraph is used to suppress the light from
a bright, central point source to improve the contrast-limited sensitivity to faint, nearby
sources. Both Vector Apodizing Phase Plate (Vector Apodizing Phase Plate (vAPP), 180 <sup> ◦ </sup>

and 360 <sup> ◦ </sup> dark hole) and Annular Groove Phase Mask (AGPM) coronagraphs are available. Coronagraphy is available for both single and double sided imaging. Only the 360 <sup> ◦ </sup>

vAPP coronagraph has been fully commissioned; use of the other coronagraphs is still experimental. The coronagraphs are available through external collaboration and their use

<!-- page: 25 -->

requires collaboration with the providing team (contact for AGPM: Denis Defr`ere, [de-](mailto:denis.defrere@kuleuven.be)
[nis.defrere@kuleuven.be, contact for vAPP:](mailto:denis.defrere@kuleuven.be) [Matthew Kenworthy, kenworthy@strw.leidenuniv.nl).](mailto:kenworthy@strw.leidenuniv.nl)

**Non-redundant aperture masking (NRM)**

LMIRCam is equipped with two masks for non-redundant aperture masking (NRM), a 12hole (6 holes per LBT aperture) and a 24-hole (12 holes per LBT aperture) mask. NRM
observations can be executed single- and double-sided with the two apertures imaged individually with baselines up to ∼ 8 m (routine) and with the two apertures combined for baselines
up to ∼ 23 m (experimental).

**ALES integral field spectroscopy**

ALES allows for integral field spectroscopy in the K, L, and M bands. Currently, the L band
mode (2.8-4.2 micron, R ∼ 40) is the only mode that has been fully commissioned. Additional
modes covering the K to M bands with various spectral resolutions are considered for commissioning and in part experimental. Use of ALES requires collaboration with the team that developed the system (different from the LBTI team, contact: Jordan Stone, [jordan@lbti.org).](mailto:jordan@lbti.org)
ALES can be combined with vAPP coronagraphy (routine with the 360 <sup> ◦ </sup> vAPP). Note,
however, that the vAPP has a strong absorption feature shortward of ∼ 3.3 micron.

**Wall-eyed pointing**

The two primary apertures of the LBT can point at different regions of the sky within the
LBT’s co-pointing limit (separations up to ∼ 2 arcmin have been demonstrated). LBTI’s
wall-eyed pointing mode makes use of this to project two sources onto the same detector
that are separated on sky by more than the nominal field-of-view (20 arcsec). This mode is
commissioned but not routinely used and is thus considered an experimental.

**Slit-less spectroscopy**

LMIRCam is equipped with a prism that allows for slitless spectroscopy at a spectral resolution of ∼ 100. This mode is available but only routinely used for engineering purpose. It
is thus considered an experimental mode. A slit mask for a spectral resolution of ∼ 300 is
available but no observing strategy has so far been developed for using it.

**Fizeau imaging interferometry**

This mode combines the beams from LBT’s two primary apertures interferometrically in the
focal plane for interferometric imaging. The resulting image, which can in principle utilize
LMIRCam’s full 20 arcsec FoV has a PSF equivalent to an 8.4 m telescope that is sliced
by interferometric fringes according to LBT’s the 23 m edge-to-edge baseline for improved

<!-- page: 26 -->

**Table 3.3:** Pertinent LMIRCam detector characteristics.
**Property Fast Mode Medium Mode Slow Mode**
Detector area [pix] see Table 3.4 2,048 × 2,048 2,048 × 2,048
Pixel scale [mas/pix] 10.7 10.7 10.7
Frame time [s] see Table 3.4 0.4918 1.4753
Bit/pix 12 16 16
Saturation level [ADU] 3,900 62,000 62,000
5% non-linearity [ADU] 2,900 47,500 47,500
Bias level [ADU] 500 5,000 5,000
Dark count [ADU/s] 2 18 18
Read noise [ADU] 2 35 40
Fraction of hot pixels < 1% < 1% < 1%
Fraction of dead pixels < 1% < 1% < 1%

**Notes:** Linearity curves are typically measured several times per semester (although no
significant changes have been seen over time) and can be made available to users for linearity
correction. If such data are critical for a program, users should explicitly request linearity
data when planning observation to ensure the relevant data are available.

resolution in this direction. Field rotation is exploited for reconstructing an image equivalent
to a 23 m telescope. Fringe tracking with PhaseCam can be used for sufficiently bright and
point-like sources. This mode is not fully commissioned and thus considered an experimental
mode. Can be combined with slit-less spectroscopy for spectrointerferometry (demonstrated)
and with ALES (not demonstrated).

### 3.4.2 LMIRCam Detector

The L and M band Mid-InfraRed Camera (LMIRCam) is equipped with a HAWAII-2RG
(H2RG) mercury cadmium telluride (HgCdTe) detector sensitive up to the M band. The
detector has both fast and slow readout modes enabled, as well as a ’medium’ mode which is
an over-clocked version of the slow mode. A wide range of read-out schemes are accessible,
the most common being correlated double sampling (CDS). A and ’sample up the ramp’
mode for read-noise limited observations is currently under commissioning. Table 3.3 lists
the main characteristics of the detector pertinent for planning observations.

The detector plate scale is ∼ 10.7 max/pix (see astrometry section below for details) for a
theoretical full FoV of ∼ 22 arcsec squared. The useable FoV is closer to 18 arcsec squared due
to vignetting close to the edges and some significant but unexplained aberrations in the far
upper-left and upper-right corners. The FoV is significantly reduced when using the ALES
magnifiers (see Sect. 3.4.3 and Table 3.8). In Fast Mode, LMIRCam offers the ability of
horizontal striping, i.e., reducing the frame size vertically. This reduces the minimum frame

<!-- page: 27 -->

**Table 3.4:** LMIRCam readout stripes in fast mode.
**Label First row Last row Frame time [s]**
Full Image 1 2,048 27.5
Center Stripe 1024 513 1,536 13.7
Center Stripe 512 1,025 1,536 6.9
Center Stripe 256 1,025 1,280 3.4

**Notes:** Row count starts at 1, i.e., the bottom row of the full detector is row #1. All stripes
cover the whole width of the detector, from column 1 to column 2048.

**Figure 3.9:** LMIRCam dark ( _left_ ) and difference between two consecutive darks ( _right_ ) with an
integration time of ∼ 1 s (Fast Mode). Relevant features are annotated. For details see Sect. 3.4.2.

time by the fraction of the full frame that is read as well as the data rate at the cost of FoV.
Stripe parameters are listed in Table 3.4.

**Detector features and cosmetics**

A dark frame obtained with LMIRCam in fast mode (integration 1s) is shown in Fig. 3.9.
Relevant detector features are highlighted. The detector channels of LMIRCam are oriented
vertically. Bias drifts between channels are well subtracted using CDS and by subtracting
from each column its median obtained after masking significant astronomical image features
(e.g., stars). The LMIRCam detector suffers from a cluster of bad pixels to the lower-right of
the center, dubbed the ’bullet hole’. While this usually corrects well in data reduction, it is
advisable to avoid placing any scientifically relevant region of the observed field in this region

<!-- page: 28 -->

if possible. In Fast Mode, a channel close to the center of the detector shows elevated readout noise (’bad channel’). This channel should be avoided for read-noise limited observations.
Horizontal striping subtracts out without significant residuals during data reduction. The
LMIRCam detector shows the usual framing common to astronomical detectors. Persistence
of the detector is largely negligible and saturating the detector is often and routinely done
without any negative effects. There is slight cross-talk at the edges of channels from bright
sources.

**Readout and data processing time**

The exposure time is a multiple of the frame time (see Tables 3.3 and 3.4). In addition,
there is a dead time for each integration equal to one frame time for readout. Exposures
are obtained in sequences. Each sequence comes with an initial setup time of two seconds.
An exposure is transferred and processed in parallel to the following exposure in a sequence.
The exposure cadence is dictated by the detector (exposure+readout time) and exposures
are buffered before transferring, processing, and saving if the exposure time is shorter than
the processing time. Due to buffer limitations, there is a maximum number of frames in a
sequence for very short integrations (see Table **??** ). A sequence is complete if all frames are
acquired, processed, and saved, and only after that a new sequence can be started.

The processing time depends linearly on the data rate (frame size), with a processing rate of
13 ms/MB,plus a dead time of 80 ms per file. With this processing efficiency, Medium Mode
and Slow Mode exposures are always dominated by the detector cadence with processing
times being absorbed by the slow cadence of frames. Processing times do become significant,
however, for the shortest exposures possible in Fast Mode. A single Fast Mode full-frame
image has a file size of 8 MB (linear with the number of images in a file for CDS and ramps).

**Example:** We obtain a sequence of 100 images in Fast Mode, full frame, with an integration time of 55 ms (2 × the minimum frame time of 27.5 ms) per frame and CDS. Exposure+readout time per frame is then 55.0 ms + 27.5 ms = 82.5 ms. Exposures for the whole
sequence of 100 frames will then be completed 2 s + 100 × 82.5 ms = 10.25 s after triggering the sequence (start time + 100 × [exposure+readout time]). Processing time per file
is 80 ms + 13 ms × 16 MB = 288 ms or 28.8 s for the whole sequence. The sequence is thus
completed after max (10.25 s, 28.8 s) = 28.8 s and a new sequence can only be started after
this time.

This process has been implemented to avoid overfilling the file buffer during long, fast
sequences, which would produce corrupted data. As a summary, the total duration _t_ seq and
total integration time _t_ int for an LMIRCam sequence can be estimated as follows:

_t_ seq = 2 s + _n_ exp × max [ _t_ exp + _t_ frame, 80 ms + _s_ file / 1 MB × 13 ms ] (3.1)
_t_ int = _n_ exp _× t_ exp (3.2)

where _n_ exp is the number of exposures in the sequence, _t_ exp is the exposure time of each
exposure, _t_ frame is the frame time (Tables 3.3 and 3.4), and _s_ file is the file size.

<!-- page: 29 -->

**Figure 3.10:** Illustration of ALES working principle. For details see Sect. 3.4.3.

**Figure 3.11:** Sketch of LMIRCam’s optical layout. Adapted from Spalding et al. (2018).

### 3.4.3 ALES principle

The Arizona Lenslet for Exoplanet Spectroscopy (ALES) comprises a set of optics that
transform LMIRCam into an Integral Field Unit (IFU). At the heart of ALES is a photolitographically manufactured lenslet array with 75 × 75 lenslets, each with a diameter of 0.5 mm
and with optical power to correct for off-axis astigmatism. The lenslet array is located in
the LMIR Field Stop Wheel (LMIR APERWHL). The telescope PSF is first magnified using
refractive or reflective magnifiers. Light then passes the lenslet array to re-focus each spaxel.
Finally, direct-vision prisms disperse the light so that a set of spectra can be imaged on the
existing LMIRCam detector. This is illustrated in Fig. 3.10.

### 3.4.4 Filters and optics

A sketch of LMIRCam’s optical layout is shown in Fig. 3.11. Additional optics relevant
for science setups of LMIRCam or ALES but not directly part of LMIRCam are also included. The available filters and their properties are listed in Table 3.5. A list of aperture
masks, coronagraphs, and cold stops and a description are given in Table 3.6. LMIRCam
is equipped with grisms for slit-less spectroscopy. ALES has a set of prisms as dispersive
elements. Those grisms and prisms are listed in Table 3.7 with their pertinent properties.
All dispersers are located in LMIRCam’s FW 3. A set of magnifiers are used for ALES

<!-- page: 30 -->

integral field spectroscopy. These are listed in Table 3.8. Currently, only the refractive
magnifier is commissioned, which is required for adequately sampling a single-aperture PSF.
Additional, reflective magnifiers are under commissioning for different sampling and FoV,
including sampling the LBTI’s Fizeau PSF. Magnifiers are located in LMIRCam’s ALES
IFU Magnification Wheel (MagWheel). Each wheel has in addition an open position to leave
the light undisturbed.

**Table 3.5:** LMIRCam filters.
**Filter Label Filter** _λ_ c **Range Peak Counts** <sup>1</sup> **Background** <sup>2</sup>

**wheel** [ _µ_ m] [ _µ_ m] [ADU/s] [ADU/s/pix]
_Broadband_ _filters,_ _spectroscopic_ _order_ _sorters,_ _and_ _blocking_ _filters:_
MK-J (Mauna Kea J) FW2.5 1.25 1.16 - 1.34 TBD TBD
H FW2.5 1.65 1.50 - 1.81 TBD TBD
Kshort FW2.5 2.16 2.00 - 2.32 TBD TBD
Lshort FW2.5 3.31 3.10 - 3.51 TBD TBD
Std-L FW4 3.70 3.41 - 3.99 TBD TBD
2950BP1500 FW4 - 2.20 - 3.75 TBD TBD
IWBP2250 FW2.5 - 2.25 - 3.81 TBD TBD
Lspec2.8-4.0 FW2.5 - 2.81 - 4.00 TBD TBD
Janos3.0-5.0 FW2.5 - 3.0 - 5.0 TBD TBD
Std-M FW4 4.78 4.60 - 4.97 TBD TBD
PK50-Blocker FW4 - JHK bands - ND1.0-T10 FW2 - - 10% neutral density filter
ND2.0-T1 FW2 – – 1% neutral density filter
_Narrowband_ _filters:_
Fe-II FW2 1.645 1.63 - 1.66 TBD TBD
NB2925-055 FW2 2.925 2.87 - 2.98 TBD TBD
H2O-Ice2 FW4 3.08 3.01 - 3.15 TBD TBD
Lcont1 FW3 3.16 3.13 - 3.20 TBD TBD
NB3375-025 FW2 3.375 3.350 - 3.400 TBD TBD
PAH FW2 3.2525 3.2394 - 3.3357 TBD TBD
Lcont2 FW3 3.47 3.39 - 3.54 TBD TBD
NB3555-041 FW2 3.555 3.514 - 3.596 TBD TBD
Lcont3 FW4 3.59 3.55 - 3.64 TBD TBD
Lcont4 FW4 3.78 3.68 - 3.88 TBD TBD
N03946-4 FW3 3.95 3.83 - 4.06 TBD TBD
NB3950-035 FW2 3.950 3.915 - 3.985 TBD TBD
Br-Alpha-On FW4 4.06 4.02 - 4.09 TBD TBD
BR-Alpha-Of FW4 4.00 3.97 – 4.04 TBD TBD

**Notes:** <sup>**1**</sup> Approximate peak counts for a point source of brightness _m_ = 0 in this filter from
a single-aperture observation under peak AO performance. Useful for estimating saturation
levels and integration times for a star of a given brightness. **2** Approximate sky+telescope
background in typical fall ambient temperature for a single-aperture observation. Useful for
estimating maximum integration time that does not saturate the background and background
noise, as well as determining background-limited vs. read noise limited sensitivity regime.

<!-- page: 31 -->

**Table 3.6:** LMIRCam aperture masks, coronagraphs, and cold stop.

**Label Wheel Description, Purpose, Comments**
DoubleAGPM NIL NICNAC <sup>1</sup> Two AGPM coronagraphs for single- and double-sided use
PinholeGrid NIL NICNAC Pinhole grid for distortion measurements
8.5mmSquareAperture NIL NICNAC Square aperture for obtaining sharp pupil images for alignment
0.054mmSlit LMIR APERWHL <sup>2</sup> Focal plane slit, experimental
DualAperture FW1 Cold stop for dual-aperture observing
SXAperture FW1 Cold stop for SX aperture observing, blocks DX aperture
DXAperture FW1 Cold stop for DX aperture observing, blocks SX aperture
AGPMMask FW1 Dual-aperture cold stop (+ M2 swingarm mask) for AGPM imaging
NRM12 FW1 Dual-aperture NRM mask, 12 holes (6 for SX, 6 for DX aperture)
NRM24 FW1 Dual-aperture NRM mask, 24 holes (12 for SX, 12 for DX aperture)
VAPP180 FW1 vAPP coronagraph, 180 <sup> ◦ </sup> dark hole
VAPP360 FW1 vAPP coronagraph, 360 <sup> ◦ </sup> dark hole
AnnularMask FW1 Minimally redundant aperture mask
SX-Half-moon FW2 Mask for SX aperture observing, blocks DX aperture
DX-Half-moon FW2 Mask for DX aperture observing, blocks SX aperture
Blank FW4 Blocks all light for darks, etc.
UBC feldi stops UBC image stops Block opposite halves of LBTI’s FoV from LBT’s apertures

**Notes: 1** NIL NICNAC is the label on the LBTI operations interface. Corresponds to ‘NIC Aperture Wheel’ in
Fig. 3.11. **2** LMIR APERWHL is the label on the LBTI operations interface. Corresponds to ‘LMIR Field Stop
Wheel’ in Fig. 3.11.

<!-- page: 32 -->

**Table 3.7:** LMIRCam grisms and ALES prisms.

**Label Wavelength range Resolution Suggested blocking**

[ _µ_ m] _λ/_ ∆ _λ_ **filter(s)**
ALES-LM-prisms 3.0 - 5.0 ∼ 20 Janos3.0-5.0
ALES-Lspec-prisms 2.2 - 3.7 ∼ 40 Lspec2.8-4.0
ALES-Lshort-prisms 3.1 - 3.5 ∼ 100 Lshort
L-grism see Fig. 3.12 ∼ 100 ( ∼ 300) <sup>1</sup> Lspec2.8-4.0, Janos3.0-5.0
M-grism see Fig. 3.12 ∼ 100 ( ∼ 300) <sup>1</sup> Std-M, Kshort

**Notes: 1** The native spectral resolution of the grisms is ∼ 300, however for slit-less spectroscopy the spectral resolution is limited to ∼ 100 by the diffraction-limited PSF.

**Figure 3.12:** Transmission

efficiency of LMIRCam’s L
and M band grisms. Adopted
from Kuzmenko et al. (2012).

**Table 3.8:** ALES magnifiers.

**Name Magnification Resulting field of view**
Refractive Magnifier 10 × 2 × 2 arcsec
6 × Reflective Magnifier 6 × 3.3 × 3.3 arcsec
12 × Reflective Magnifier 12 × 1.7 × 1.7 arcsec
25 × Reflective Magnifier 25 × 0.8 × 0.8 arcsec

### 3.4.5 High-contrast imaging performance

LBT’s high-performance AO system in combination with LMIRCam observations predominantly being carried out in the L and M bands where the LBTI outperforms other highcontrast imagers, results in superb PSF stability which already provides excellent highcontrast performance without the use of a coronagraph. The largest high-contrast imaging

<!-- page: 33 -->

survey with the LBTI, the LEECH (Stone et al. 2018) survey has been executed in the L band
without a coronagraph. Fig. 3.13 shows the median and best contrast curve obtained by this
program. Targets were typically observed for five hours around meridian passage resulting
in high field rotation (critical for angular differential imaging). The use of ALES has been
shown not to degrade the high-contrast performance of LMIRCam (Skemer et al. 2018).

**Figure 3.13:** Median and best
contrast curves from the LEECH
survey. Adopted from Stone et al.
(2018).

In addition, LMIRCam is equipped with two types of coronagraphs, vector-apodizing
phase plates (vAPPs, 180 <sup> ◦ </sup> and 360 <sup> ◦ </sup> dark holes available) and annular groove phase masks
(AGPMs). Only the 360 <sup> ◦ </sup> vAPP coronagraph has been fully commissioned; use of the other
coronagraphs is still experimental. The coronagraphs are available through external collaboration and their use requires collaboration with the providing team (contact for AGPM:
Denis Defr`ere, [denis.defrere@kuleuven.be,](mailto:denis.defrere@kuleuven.be) contact for vAPP: Matthew Kenworthy, [kenwor-](mailto:kenworthy@strw.leidenuniv.nl)
[thy@strw.leidenuniv.nl).](mailto:kenworthy@strw.leidenuniv.nl)

Coronagraphy is available for both single- and double-sided imaging. Because vAPPs
are pupil-plane coronagraphs, the observing strategy for the 360 <sup> ◦ </sup> vAPP identical to noncoronagraphic imaging, where the images of the target from the two apertures of the LBT
are placed next to each other on the detector and nodding is performed with the target in
both offset positions imaged on the detector. An additional optical alignment during the
initial instrument setup is required, but adds negligible overheads.

There are two AGPM coronagraphs available, with slightly different performance across
the L and M bands. These focal-plane coronagraphs are inserted together so that two occulting spots are visible in LMIRCam’s field-of-view. Because LMIRCam imaging typically
involves placing the two images of the target from the two LBT apertures next to each

<!-- page: 34 -->

other on the detector and nodding with the target in both offset positions imaged on the
detector for background subtraction (images of the target in four different locations on the
detector), use of the AGPM is typically only 50% efficient: Common strategies include single
sided observations where the target is offset back-and-forth between the two coronagraphs
or double-sided observations where the target images from the two apertures are nodded on
and off the coronagraph. Double-sided observations with minimal/no nodding are also an
option where background subtraction is not critical (e.g., hard contrast-limited regime or
where post-processing methods such as spatial filtering are expected to sufficiently remove
the background).

The contrast improvement for the two coronagraphs over non-coronagraphic imaging has
not been well characterized due to the wide range of parameters impacting it. In particular,
comparing observations with and without coronagraph is difficult due to the impact from
variable seeing conditions. Efforts to further characterize this are under way. Contrast curves
from some coronagraphic observations are shown in Fig. 3.14 and Fig. 3.15.

**Figure 3.14:** Contrast curves from a vAPP observation and from direct imaging observations.
Observations from three epochs are shown and are not necessarily comparable. The region where
the vAPP improves the contrast is highlighted by the gray shade in the left panel and magnified in
the right panel. Adopted from Wagner et al. (2020).

### 3.4.6 Distortion correction and astrometry

Users should be aware that the LBTI was not designed as an astrometric instrument. Thus,
the astrometric precision is limited and great care should be exercised when deriving and
using astrometric measurements from LBTI data. Maire et al. (2015) describe a procedure
to correct LMIRCam images for optical distortion and to derive a plate scale and true North
measurement of the images. A tool has been provided by Spalding et al. (2019). The required
data are part of routine instrument calibrations and are obtained at regular intervals by the

<!-- page: 35 -->

**Figure 3.15:** AGPM contrast
curve. The solid line shows the
actual contrast (including the effects of self-subtraction), while the
dotted line shows the raw contrast
(not considering self-subtraction).
Adopted from Defr`ere et al. (2014).

instrument team. Distortion corrections should generally be applied to LMIRCam images
and there are few exceptions where this does not significantly improve the data quality.
NOMIC data are typically more forgiving due to the lower angular resolution in the N band
and the rare use of the instrument for high-contrast AO imaging.

**Optical distortion correction**

LMIRCam images are subject to significant optical distortion and we highly recommend
correcting it on any images. Optical distortion is measured by imaging a pinhole grid inserted
at the NIC Aperture Wheel. The position of the pinholes in the images can be measured and
a solution can be derived that distorts the image in a way that the positions form a cartesian
grid. This is the distortion that needs to be applied to any science images to correct for the
optical distortion of the instrument. The solutions derived from previous data can be found
on the LBTI user pages [here.](https://sites.google.com/a/lbto.org/lbti/data-retrieval-reduction/distortion-correction-and-astrometric-solution)

Downstream of the pinhole grid, all optics are the same for the beams from the SX and DX
beams. Thus, there should be no significant difference between the matrices derived from
SX, DX, or double sided images. However, optics are hit at a slightly different angle and in
a slightly different position for the two sides, so that in the future matrices for the individual
sides will be provided where possible.

Users can apply the distortion matrices using their own tools or use a basic Python package
provided by our team and found on the LBTI user pages [here.](https://sites.google.com/a/lbto.org/lbti/data-retrieval-reduction/distortion-correction-and-astrometric-solution) The appropriate matrices
from the web page are simply copied into the code before running. The Python code has
been tested using Python 3.6.3 and recent versions of common libraries (as of 2020). Users
are encouraged to apply any correction to the corresponding pinhole image (also provided
on the web page) and to visually inspect the result as a verification of the procedure. The
distortion correction is typically applied to science frames after all pixel-specific corrections

<!-- page: 36 -->

(e.g., dark/bias/nod subtraction, bad pixel correction) as it distorts the original image, but
before any de-rotation or other morphing of the images as otherwise the effects of distortion
would have to be tracked through these operations.

Note that the distortion corrections have only been consistently derived for the full 2,048 × 2,048
pixel images (but they are only valid for the area of the image where pinholes are clearly
visible). The easiest way to apply the correction to subframe images is to insert the smaller
image at an appropriate position in an empty 2,048 × 2,048 image before applying the correction and then to crop again around the science image. An alternative and more efficient
method for a large number of science images may be to use the solution on a 2,048 × 2,048
image and to record the shifts for each pixel. The shifts to the relevant pixels can then be
applied to the subframes images only rather than padding each image. This option has, however, not yet been explored by the LBTI team. In the future, distortion corrections derived
for relevant subframes will be provided where possible.

Older data have the subframe information in the fits headers in the keywords starting with
‘SUBSEC’. Newer data are almost exclusively taken in full frame or the ‘center stripe’ section
of the detector which until Summer 2021 used rows 512 to 1,535 of the full-frame (where the
bottom row of the full-frame image is row 1). New subsections since Summer 2021 are listed
in Table 3.4. In case the subsection cannot be determined, please should ask your LBTI
team contact for clarification.

The described procedure corrects for distortion of all optics downstream of the pinhole grid,
but it is important to note that the typically small residual distortion from several optics
upstream of the pinhole grid will not be measured. Observations of the relatively dense
stellar field of the Trapezium cluster that is imaged for deriving an astrometric solution (see
below) can in principle also be used to derive a complete and precise distortion correction
of the full optical system. This has not yet been attempted by the LBTI team or to our
knowledge by any user. It may, however, be considered by expert users if a particularly high
level of precision is required.

**True north and plate scale**

The LBTI regularly observes the Trapezium cluster and uses the coordinates from Close et
al. (2012) to derive an astrometric solution for LMIRCam. The results are listed on the
LBTI user pages [here.](https://sites.google.com/a/lbto.org/lbti/data-retrieval-reduction/distortion-correction-and-astrometric-solution) The raw Trapezium data can be made available to our users upon
request to derive their own astrometric solutions.

## 3.5 NOMIC

The Nulling-Optimized Mid-Infrared Camera (NOMIC) is one of the LBTI’s science cameras
(the other one being LMIRCam), covering the N band. As the name states, the camera was
designed for the purpose nulling interferometry. It is, however, also used for sensitive N-band

<!-- page: 37 -->

imaging and for Fizeau interferometry. It is important to note, that while some modes are
routinely used for science observations, others are more experimental and have not been fully
commissioned.

### 3.5.1 Observing modes

**Nulling interferometry**

A high-contrast imaging mode where destructive interference between the two beams is used
to suppress the light from a bright, central point source at an angular resolution of the 14.4 m
center-to-center interferometric baseline of the LBT, while extended emission is transmitted.
The beams are combined in the pupil plane, so that the resulting image on the detector has
the resolution of an 8.4 m aperture. This is the mode that was used for the HOSTS survey
(Ertel et al., 2020). Light is sent through the nulling-interferometric channel of PhaseCam,
which was designed to minimize non-common path effects between NOMIC and the fringe
tracker for the best stability of the interferometric null.

**Plain AO imaging**

NOMIC can be used for individual aperture imaging. A single side of the LBT or both sides
can be used. In the latter case, the images from the two sides are placed next to each other
on the detector. Cold UBC field stops can be inserted to avoid overlapping backgrounds for
exploiting the full collecting power of the LBT in the background limited regime. Chopping
can be performed using the UBC’s pupil mirrors to suppress the Excess Low Frequency
Noise (ELFN) of the NOMIC detector.

**Overlapped AO imaging**

A variation of plain AO imaging where the images from the two sides are overlapped on the

 √ 

detector. This improves the sensitivity in the read-noise limited regime by a factor of 2

t

 √ 

detector. This improves the sensitivity in the read-noise limited regime by a factor of 2

at the cost of PSF stability and decreased observing efficiency. Can also be useful for faint
sources if using both LBT apertures and the whole NOMIC FoV is desired. As the overlap
is not perfect, this is more useful for extended source observations where contrast and image
quality are less of a concern than sensitivity. Experimental mode only with little on-sky or
data reduction experience.

**Fizeau imaging interferometry**

This mode combines LBT’s two primary apertures interferometrically in the focal plane for
interferometric imaging. The resulting image has a PSF equivalent to an 8.4 m telescope
that is sliced by interferometric fringes according to LBT’s 23 m edge-to-edge baseline for
improved resolution in this direction. Field rotation is exploited for reconstructing an image

<!-- page: 38 -->

equivalent to a 23 m telescope. Fringe tracking with PhaseCam can be used for sufficiently
bright and point-like sources. This mode is not fully commissioned and thus considered an
experimental mode.

### 3.5.2 NOMIC detector

NOMIC uses a Raytheon 1,024 × 1,024 pixel Si:As Impurity Band Conduction (IBC) Aquarius detector with a plate scale of 17.9 max/pix. Table 3.9 lists the main characteristics of the
detector relevant for planning observations.

**Table 3.9:** Pertinent NOMIC detector characteristics.

|Detector area [pix]|1024x1024|
|---|---|
|Pixel scale [mas/pix]|17.9|
|Minimum frame time [s]|TBD|
|Bit/pix|TBD|
|Saturation level [ADU]| ∼ 16,000|
|5% non-linearity [ADU]|N/A1|
|Bias level [ADU]|1200–25002|
|Dark count [ADU/s]|TBD|
|Read noise [ADU]|15-302|
|Fraction of hot pixels|TBD|
|Fraction of dead pixels|TBD|

**Notes: 1** NOMIC exhibits negligible non-linearity before saturation. **2** The value varies
between detector channels.

**Detector cosmetics, field-of-view, and vignetting**

The detector size and pixel scale result in a theoretical FoV of 18 arcsec squared. However,
there is some vignetting in the outer corners resulting in a circular effective field-of-view
of ∼ 15 arcsec diameter for imaging and Fizeau interferometry, which is reduced to roughly
a half-circle by additional vignetting in the nulling interferometric mode. In practice, this
vignetting is of little consequence for the nulling mode for which NOMIC was designed as
only a small FoV is required. Furthermore, the fast read-out speeds typically required for
broad N band imaging due to the high thermal background and the resulting overheads for
detector read-out and processing of the data (transfer, handling, storage) often require subframing to achieve reasonable detector duty cycles. NOMIC offers the possibility to co-add
frames on-chip and longer integration times are possible in narrower filters. Both mitigates
some of the efficiency challenges, however both limits the ability to mitigate the detector’s
ELFN (see below).

<!-- page: 39 -->

**Figure 3.16:** Sketch of NOMIC’s optical layout. For details see Sect. 3.5.3. Adapted from Spalding
et al. (2018).

Various detector and image features as well as commonly used subframes are shown in
Fig. **??** . NOMIC detector channels are oriented horizontally and read out from the center
symmetrically to the left and right. Sub-framing is achieved by reading only specific channels
(no reduction of detector duty cycle, but of overheads from handling the data) and reading
only a fraction of each channel’s length from the center (improves the duty cycle by the
fraction of the channel that is read). Detector columns from the center can also be skipped,
this does not improve the detector duty cycle, but may reduce overheads from data handling.

**Readout and data processing time**

TBD.

_TBD._ (3.3)

**Excess Low Frequency Noise (ELFN)**

NOMIC is affected by Excess Low Frequency Noise (ELFN) common to most mid-infrared
detectors. The exact source of this noise is not known. ELFN is found to be an additional,
temporal noise component that becomes significant at frequencies below ∼ 10 Hz. Thus,
integrating or adding frames over a period of time longer than 100ms results in a lower noise
improvement than the naive behavior (proportional to the square root of time). The ELFN
appears at least partially multiplicative with the light on the detector, so that the use of
narrow filters may reduce the severity of the effect.

<!-- page: 40 -->

The only well documented mitigation strategy for ELFN is fast chopping (fast movement
of the FoV between tow or more detector positions so that the ELFN can be removed by
subtracting consecutive frames). LBTI has the ability to chop with the UBC pupil mirrors
with a maximum chop throw of ∼ 7 arcsec. A 512 × 512 pixel (9 × 9 arcsec) unvignetted
FoV is used for this mode with the four quadrants of the field occupied by the images from
the two chopping positions from each of the two LBT apertures. A chopping frequency of
4.5 cycles (chop pairs) per second is used, which is optimized given the trade-off between
between high chopping frequency, high detector efficiency, and limited integration time per
frame to avoid background saturation in the Nprime filter (NOMIC’s standard filter for deep,
sensitive observations). At this frequency, the efficiency of the integrations is ∼ 76% with two
co-added frames of ∼ 42 ms integration time each per chop position and a duration of each
position of ∼ 110 ms (84 ms of integration time in 110 ms of wall-clock time).

### 3.5.3 Filters and optics

A sketch of NOMIC’s optical layout is shown in Fig. 3.16. Additional optics relevant for
science setups of NOMIC but not directly part of it are also included.

NOMIC and PhaseCam receive light from the NIC beam diverter. Put in ”Trichroic”
position, the H and K band light is sent to PhaseCam and the N band is sent to NOMIC.
Put in ”Window” position the N band is still sent to NOMIC, but PhaseCam receives no light
as the H and K band light is transmitted to LMIRCam. NOMIC has two optical channels,
one for nulling interferometry and one for imaging and Fizeau imaging interferometry. The
nulling channel goes directly through PhaseCam where the light from the two apertures is
combined in the pupil plane before the H and K band light is used for fringe tracking and the
N band light is further sent to NOMIC. This minimizes non-common path effects between
NOMIC and PhaseCam for maximum null stability. In the imaging channel, the H and
K band light still follows the same optical path and can be used in PhaseCam, but the N
band light is combined in the focal plane on the NOMIC detector. The channel is selected
using the Imaging Dichroic (in for imaging/Fizeau, out for nulling) and the Nulling Mirror
(in for nulling, out for imaging/Fizeau). The setup of the NOMIC imaging/Fizeau channel
relative to PhaseCam is analogous to that of LMIRCam.

The available filters and their properties are listed in Table 3.10. A list of aperture masks
and stops, their position in NOMIC’s optical path, and a description are given in Table 3.11.
Each wheel has in addition an open position, which is used if no filter or optic in this wheel
is required for a specific observation.

### 3.5.4 Distortion correction and astrometry

NOMIC distortion correction and astrometric calibration data are not routinely obtained.
This may, however, be requested by a PI if it is required for their program. Data for distortion
correction can be obtained in closed-dome with no cost to the PI, but the time for obtaining

<!-- page: 41 -->

**Table 3.10:** NOMIC filters.
**Filter Filter** _λ_ c **Range Peak Background**
**Label Wheel** _µ_ m _µ_ m **Counts** <sup>1</sup> **Counts** <sup>2</sup>

**[ADU/pix] [ADU/pix]**
Nprime FW1 11.11 10.22 - 12.49 TBD TBD
W08699-9 122 FW1 8.70 8.13 - 9.35 TBD TBD
W10288-8 601 FW1 10.29 8.04 - 14.02 TBD TBD
W10550-9Q 097 FW1 10.55 10.09 - 11.06 TBD TBD
N07904-9N 070 FW1 7.90 7.55 - 8.25 TBD TBD
N08909-9O 077 FW1 8.91 8.53 - 9.29 TBD TBD
N09145-9 080 FW1 9.15 8.74 - 9.55 TBD TBD
N09788-9P 091 FW1 9.79 9.33 - 10.25 TBD TBD
N11855-8R 114 FW1 11.86 11.29 - 12.42 TBD TBD
N12520-95 116 FW1 12.52 11.97 - 13.01 TBD TBD
W-10145-9 FW2 10.15 8.03 - 13.77 TBD TBD
W01641-6 <sup>3</sup> FW2 1.64 - TBD TBD
W04701-4M <sup>3</sup> FW2 4.70 4.44 - 4.99 TBD TBD
18.0 <sup>4</sup> FW2 18.0 TBD TBD TBD
24.4 <sup>4</sup> FW2 24.4 TBD TBD TBD
ZnSe-Blocker <sup>5</sup> FW2 - < 15 - BaF2-Blocker <sup>6</sup> FW2 – < 15 – –

**Notes:** <sup>**1**</sup> Approximate peak counts of Vega in this filter from a single-aperture observation
under peak AO performance. Useful for estimating saturation levels and integration times
for a star of a given brightness. **2** Approximate sky + telescope background in typical
fall ambient temperature for a single-aperture observation. Useful for estimating maximum
integration time that does not saturate the background and background noise, as well as
determining background-limited vs. read noise limited sensitivity regime. **3** Engineering
filters, use LMIRCam for science observations in those bands. May be useful for supporting
parallel LMIRCam or ALES science observations. <sup>**4**</sup> Experimental Q band filters. <sup>**5**</sup> Blocking
filter for > 10 _µ_ m filters with red leak beyond 15 _µ_ m. **6** Blocking filter for < 10 _µ_ m filters
with red leak beyond 15 _µ_ m.

astrometry data needs to be charged to a program as required on-sky calibration. NOMIC
astrometry and distortion correction are experimental as the LBTI team has little or no
experience with these data or their analysis. In principle, the process would, however be
analogous to that for LMIRCam (see details in Sect. 3.4.6) and the same tools should be
useable with minimal or no modification.

<!-- page: 42 -->

**Table 3.11:** Masks with positions and description.

**Label Wheel** Description, Purpose, Comments
Single2.3 Pupil wheel Single-aperture cold stop for nulling interferometry
or single-aperture imaging, undersized

Dual2.54 Pupil wheel Dual-aperture cold stop for imaging & Fizeau
interferometry

Dual3.05 Pupil wheel Dual-aperture cold stop for imaging & Fizeau
interferometry, oversized

SpiderAnnulus Pupil wheel Mask for minimally redundant aperture masking
Top(Right)-Half-Moon FW2 Mask for right (DX) aperture observing, blocks left
(SX) aperture

Bottom(Left)-Half-Moon FW2 Mask for left (SX) aperture observing, blocks right
(DX) aperture

SX-Half-moon FW2 Mask for left (SX) aperture observing, blocks right
(DX) aperture

DX-Half-moon FW2 Mask for right (DX) aperture observing, blocks left
(SX) aperture

Blank+Tape FW2 Blocks all light for darks, etc.

UBC field stops UBC image stops Block opposite halves of LBTI’s field-of-view for
LBT’s apertures

**Notes:** <sup>**1**</sup> NIL NICNAC is the label on the LBTI operations interface. Corresponds to ‘NIC
Aperture Wheel’ in Fig. 3.16. **2** LMIR APERWHL is the label on the LBTI operations
interface. Corresponds to ’LMIR Field Stop Wheel’ in Fig. 3.16.

**Table 3.12:** PhaseCam parameters relevant for planning an observation.

|Wavelength range|H & K bands|
|---|---|
|Limiting magnitude|H or K ∼ 4.5<br>|
|Minimum visibility for fringe tracking|_V_ 2 ∼ 0.5|
|Maximum loop speed|1 kHz|

## 3.6 PhaseCam

PhaseCam is LBTI’s interferometric fringe tracking camera, which operates in the H and
K bands. It stabilizes the phase between the wavefronts from LBT’s apertures (and tip-tilt
between the two beams) through phase-delay tracking for LBTI’s high-contrast requirements.
PhaseCam uses a fast readout PICNIC detector which, through windowing, can be operated
at a frame rate (thus phase loop speed) of up to 1 kHz. Table 3.12 lists the main parameters
of PhaseCam relevant for planning an observation.

<!-- page: 43 -->

**Figure 3.17:** Optical layout of PhaseCam. For details see Sect. 3.6.1. Adapted from Spalding
et al. (2018).

### 3.6.1 Optical layout

A sketch of PhaseCam’s optical layout is shown in Fig. 3.17. PhaseCam receives the H and
K band light from the NIC beam diverter if this is set to Dichroic (in Window, H and
K band light is sent to LMIRCam, so that PhaseCam cannot be used). The L and M band
light is always sent to LMIRCam. N band light is either sent to NOMIC by the Imaging
Dichroic for Fizeau interferometry (or non-interferometric imaging) or passed through the
PhaseCam optics and picked up by the Nulling Dichroic for nulling interferometry. In the
latter case, there is no instrumental relative Optical Path Delay (OPD) between NOMIC
and PhaseCam and non-common path aberrations between the two cameras are minimized
resulting in maximum phase stability on NOMIC when tracking the phase with PhaseCam.
In Fizeau imaging mode with LMIRCam or NOMIC, the relative instrumental OPD between
PhaseCam and the science camera needs to be minimized.

### 3.6.2 Approach to phase and tip-tilt sensing and control

The current approach to phase sensing uses the K band output pupil images. The pupil
images from the input beams from LBT’s two primary apertures are overlapped with a tilt
difference of approximately three fringes across the pupil at 2 _µ_ m. The differential phase and
tip/tilt variations can then be derived from a Fourier transform of the fringes. Fig. 3.18 shows
K band pupil images with fringes and the amplitude and phase of their Fourier transform.
The position of the peak of the Fourier amplitude measures the differential tip/tilt. There
are two peaks due to the dual-valued nature of the transform. The position is measured from
one peak to the center of the pupil image. The argument of the transform at that position
measures the phase.

<!-- page: 44 -->

**Figure 3.18:** Phasecam pupil image with fringes (left), Fourier amplitude (center), and Fourier
phase (right). For details see Sect. 3.6.2.

The phase, tip, and tilt determined by PhaseCam are compared to ‘setpoints’ for these
quantities, i.e., their desired values. These need to be determined for each observation based
on visual feedback from the science camera (LMIRCam or NOMIC). Corrections to the
piston, tip, and tilt of the wavefront from one aperture (by default the SX/left pathlength
corrector, DX/right can be used instead for redundancy in the system) are determined and
sent to the corresponding pathlength corrector which moves accordingly.

### 3.6.3 Limiting magnitude

The approach to image the wavefronts in the pupil plane results in a relatively bright limiting
magnitude for fringe tracking with the LBTI of K 4.5. This has been acceptable in the
past, because LBTI’s primary science goal was to detect exozodiacal dust using nulling
interferometry of very nearby, bright stars. This limiting magnitude is, however, severely
limiting LBTI’s ability to perform fringe-tracked Fizeau imaging interferometry on targets
such as stars in star forming regions. Thus, our team (project lead: J. Stone) is currently
working on a detector upgrade to a a linear avalanche photodiode array for astronomical
infrared applications developed by ESO and the University of Hawaii (SAPHIRA) array
and a range of other improvements to the system that are expected to extend the limiting
magnitude to K 9.5. The upgrades are currently expected to be commissioned in summer
and fall 2022.

<!-- page: 45 -->

# 4 Observing planning and execution

This chapter we describes the process of planning and executing observations with the LBTI,
including data retrieval.

The LBTI is offered by the instrument team with significant support from the LBT observatory to the LBT user community. Due to the complexity of the instrument, its continuous
development as an instrumentation project, and the limited documentation, it is highly advisable to collaborate with the instrument team when defining and planning an observing
project using the LBTI. In addition, certain instrument modes are still experimental, so that
collaboration with the LBTI team is critical for their successful use. Generally, it is advisable to consult the LBTI Lead Scientist (Steve Ertel, [sertel@lbti.org)](mailto:sertel@lbti.org) before preparing an
observing proposal. The LBTI team will be pleased to assist with planning the project and
developing the technical case of the proposal. For a full description of the LBTI’s availability
and user policy, as well as proper acknowledgement of the instrument team’s support during
publication of results, see Sects. 2.2, 2.3, and 2.4.

After a proposal is accepted, the proposing team will work with the instrument team to
prepare the observations. This typically involves completion of a README file and target
list with observability constraints. Observations are then carried out by the LBTI observing
team, which is composed of instrument team members and LBT staff observers, usually in
queue mode.

## 4.1 Infrared observing

Observing in the thermal infrared is in some ways significantly different from observing at
shorter wavelengths. We describe the main features of infrared observing in this section.

### 4.1.1 Infrared atmospheric windows

The LBTI is designed for sensitive observations in the thermal infrared and capable of observing in the J to N bands (wavelengths ∼ 1.2 _µ_ m to ∼ 14 _mu_ m with experimental Q band
filters). A plot of the atmospheric transmission in the LBTI’s wavelength range is shown
in Fig. 4.1. In addition to atmospheric transmission, thermal emission from the atmosphere
and warm telescope and infrared optics are a concern for infrared observations. This can
be approximated by a blackbody with a temperature of approx. 250-300 K (depending on
ambient temperature and sky conditions), which peaks in the N band. In clear conditions,

<!-- page: 46 -->

**Figure 4.1:** Atmospheric transmission across pertinent infrared wavelengths (and the visible because it is in the plot). The atmospheric transmission windows relevant for the LBTI are indicated.
Molecules responsible for the dominant absorption bands are listed as well. Note that in particular
the strength of water absorption bands can vary significantly depending on **PWV!** ( **PWV!** ) and
presence of clouds, which can have a major impact on the quality of LBTI some LBTI data.

the background is dominated by telescope optics (primary, secondary, and tertiary mirror),
while all LBTI optics downstream of this are cold. Clouds increase the sky opacity, which
both increases the background and reduces the sky transmission.

### 4.1.2 Impact of infrared background

The background has three effects that limit the sensitivity of observations, variable background structure, photon noise, and saturation. These effects are discussed in the following.

**Variable background structure**

A common challenge of infrared observations is variable, large-scale structure in the background across the images. Variable telescope and instrument background is commonly removed by nodding (see Sect. 4.1.3). The frequency of the nodding is then constrained by
the time scale on which the telescope background changes. Due to LBTI’s largely cryogenic
optical path and the fact that it is mounted to the telescope in such a way that the telescope
and instrument pupils remain fixed relative to each other during an observation, variable
telescope and instrument background is of little concern for LBTI observations in most conditions, at least shortward of the N band. Nodding is then mostly used for removing detector
systematics rather than variable background. Furthermore, the LBTI’s small FoV and high
angular resolution limit the effect of large-scale background variation across the image, and

<!-- page: 47 -->

in particular for high-contrast imaging any remaining structure can typically be removed
through image filtering during data reduction (if at all necessary).

**Background photon noise**

A more critical and fundamental noise source caused be the high infrared background is photon noise. This is the Poisson noise caused by the fact that photons on an evenly illuminated
detector follow a statistical distribution. The result is a random pixel-to-pixel noise with
a standard deviation equal to the square-root of the counts on the detector. If the background contributes significantly to the signal on the detector, this photon noise can be the
dominant noise in an image. One can compare the detector read noise in a given setup with
the square-root of the expected background counts in a given filter and integration time to
determine whether read noise of photon noise dominates a given observation. Pertinent data
are listed in Tables 3.3 and 3.5 for LMIRCam, and in Tables 3.9 and 3.10 for NOMIC. For
high-contrast imaging, this noise may be negligible as speckle noise from PSF subtraction
typically dominate.

**Saturation**

While at shorter wavelengths the exposure time is commonly adjusted to limit the degree of
saturation or avoid saturation altogether on the astronomical sources in the field, saturation
on the background is commonly a factor in determining integration times in thermal infrared
observations. This always coincides with the regime where the background photon noise
dominates over the detector read noise, so that many short integrations do not degrade the
final S/N compared to one longer integration if it was possible. However, the short integration
times required to avoid background saturation (e.g., ∼ 1 s for broad L band imaging, ∼ 50 ms
for broad N band imaging) can require significant minimization of overheads for reading the
detector and handling the data to achieve reasonable duty cycles.

### 4.1.3 Nodding, chopping, and connection to LBTI data

Nodding is the procedure of offsetting the telescope by a small angle (often smaller than the
camera FoV) on sky in regular intervals (for LBTI a few to few ten minutes) to obtain a
background exposure that can then be subtracted from images in the opposite nod position.
Nodding is commonly used to remove slow background variations in the image data as well
as some detector systematics (e.g., detector bias). Chopping is similar to nodding, but
commonly done with a small, internal mirror that allows for fast (often ∼ 10 Hz) cycles
with minimal overheads. Because of LBTI’s very stable background (no pupil rotation with
respect to the telescope), nodding is generally sufficient to remove most temporal background
variations. We thus use chopping only for removal of the NOMIC detector’s ELFN. Slower
chopping for background removal is in principle possible but generally not beneficial.

<!-- page: 48 -->

Raw LBTI science data are in all cases detector images. These can be actual images of
an astronomical object or field from AO imaging, images of spectra (e.g., from ALES), or
images of interferometric fringes or a nulled source from Fizeau imaging, NRM, or nulling
interferometry. In any case, images contain the following components:

 - **S** ( **x**, **p** ): The astronomical signal (image, fringes, spectra) as a function of image coordinates **x** and pointing direction **p** . For simplicity, we assume that **S** does not change
with time, although we note that due to the Alt-Az mount of the telescope and the
lack of an instrument rotator, LBTI images do slowly rotate on the detector over time
with PA.

 - **B** sky( **x**, **p** _, t_ ): The sky background as a function of image coordinates, pointing direction, and time _t_, e.g., due to clouds.

 - **B** opt( **x** _, t_ ): The background from optics (telescope and instrument) as a function of
image coordinates, pointing direction, and time, e.g., due variable temperature of optics
and moving optics in the optical path.

 - **C** ( **x** _, t_ ): The detector bias, i.e., a constant offset of pixel counts from zero even with
no light or integration. This results in a pattern on the detector as a function of image
coordinates that varies slightly with time.

 - The dark current of the detector as a function of image coordinates. For LBTI observations with common integration times of the order of one second or less, dark current
is often negligible.

 - **N** ( **x** _, t_ ): Various noise terms such as detector read noise **N** r, ELFN **N** ELFN (for the
NOMIC only), and photon noise from both the background and astronomical sources
**N** ph. We refer here to the actual representation of the noise in a specific image rather
than the magnitude of the noise. All these noise sources are a function of time either
directly (ELFN), through the counts on the detector (ELFN, photon noise, or they
vary with each read from image to image (read noise). We can only hope to remove the
ELFN from the images, while the remaining noise terms are fundamental. While the
magnitude of many noise terms such as ELFN or photon noise depends on the amount
of light on the detector, for simplicity we treat the actual representation of the noise
in each image as a pattern that is added to the image.
Most of these quantities of course depend on parameters such as integration time, which
we treat as constant across an observing sequence. For simplicity, we ignore here effects
such as vignetting, optical distortion, or bad pixels, which can be treated as largely separate
problems. Generally, an image **I** can then be expressed as:

**I** ( **x**, **p** _, t_ ) = **S** ( **x**, **p** ) + **B** sky( **x**, **p** _, t_ ) + **B** opt( **x** _, t_ ) + **C** ( **x** _, t_ ) + **N** ( **x** _, t_ ) (4.1)

**Nodding**

The goal of nodding and/or chopping is to remove as many components of an image as
possible that are not the astronomical signal **S** ( **x**, **p** ). This is achieved through small changes

<!-- page: 49 -->

of the pointing direction **p** . Components that are not affected by such small offsets and
do not significantly vary over timescales shorter than the duration of an offset cycle can be
removed by subtracting images in consecutive offset positions positions. It is thus critical
that the time scale of those pointing changes is small compared to the characteristic change
of the component that needs to be removed, e.g., for nodding with a duration _τ_ nod of a
cycle and a characteristic time scale _τ_ **B** opt of the variations of **B** opt: _τ_ nod < _τ_ **B** opt, so that
**B** opt( **x** _, t_ ) − **B** opt( **x** _, t_ + _τ_ nod) ≈ 0. Due to the Alt-Az mount of the telescope, the lack of an
instrument rotator (so the relative position and orientation of the telescope and instrument
pupils remains fixed during an observation), and due to the LBTI’s mostly cold optical path,
_τ_ **B** opt is > 30 min in the L band, > 15 min in the M band, and > 2 min in the N band.

The detector bias does vary slightly on time scales of seconds or less, but this variation is
largely constant across a detector channel. In addition to removing the dominant bias that is
constant with time through nodding, the time variation can thus be removed by subtracting
the median of a channel derived after masking any significant astronomical signal from the
value of each pixel in this channel. The time-variable component of the bias is thus ignored
throughout the rest of this section for **C** ( **x** _, t_ ) ≈ **C** ( **x** ).

The only non-astronomical component of the images that does depend on the pointing
position is **B** sky. Even in variable conditions, **B** sky manifests mostly as a time variation of
the overall background across LBTI’s FoV rather than significant variation of background
structure, so that this can be handled through other means than nodding or chopping during
data reduction (e.g., spatial filtering of the images).

The characteristic time scale of NOMIC’s ELFN is of the order of 0.1 s, so that this cannot
be removed through nodding which can only be done efficiently at time scales of ≳ 1 min.
ELFN is not an issue for LMIRCam.

For LBTI observations, nodding is commonly done by alternating between two pointing
positions with nodding intervals (half-cycles, i.e., the time spent in one position) of up to
15 min, 5 min, and 2 min in the L, M, and N bands, respectively. Longer nod intervals of up
to 30 min are acceptable with LMIRCam in the noise limited regime. For sufficiently fast
nodding, the difference of two images obtained at _t_ 1 and _t_ 2 in pointing positions **p** 1 and **p** 2
is then:

_I_ ( **x**, **p** 1 _, t_ 1) − _I_ ( **x**, **p** 2 _, t_ 2) = **S** ( **x**, **p** 1) − **S** ( **x**, **p** 2) + **N** ( **x** _, t_ 1) − **N** ( **x** _, t_ 2) (4.2)

where for LMIRCam the noise terms are only the fundamental noise and for NOMIC they
contain in addition the ELFN. In order to ensure that the astronomical signal of interest can
be retrieved from the difference image **I** ( **p** 1 _, t_ 1) − **I** ( **p** 2 _, t_ 2), it is important to use a nodding
distance (nod throw) larger than the spatial scale of that signal (e.g., for a target with a
diameter of 5 arcsec, use a nod throw of ≫ 5 arcsec. LBTI’s maximum nod throw is of the
order 2 arcmin (equivalent to the wavefront sensor patrol field).

<!-- page: 50 -->

**Chopping**

Chopping at the LBTI is done with the UBC pupil mirrors (Sect. 3.2.4). In contrast to
nodding, chopping does not move the telescope and thus does not remove the portion of
**B** opt( **x** _, t_ ) that is caused by optics upstream of the chopping mirror in the optical path
(dominated by the telescope’s primary, secondary, and tertiary mirrors). It can, however, be
performed at a high frequency and synchronized with the NOMIC science camera with an
optimized frequency of currently 4.5 cycles (chop pairs) per second. This is sufficiently fast
to remove the majority of NOMIC’s ELFN.

Chopping does move the beams from the two telescopes not only on the science camera
but also on PhaseCam. Currently, no mechanism is implemented that would prevent this
from breaking the phase loop. Re-closing the phase loop takes of the order of a few to a few
ten seconds, so that chopping to remove NOMIC’s ELFN (requiring frequencies larger than a
few Hz) is currently unavailable for continuously fringe-tracked interferometry (chopping at
a rate up to a few offsets per minute to remove background variations is possible by opening
and closing the interferometric phase loop for each offset). The maximum chop throw of the
pupil mirrors is ∼ 7 arcsec (5 arcsec is routinely used).

In addition to fast chopping to remove NOMIC’s ELFN, slow chopping is under consideration to replace nodding for some LBTI observations; those where an offset of ∼ 5 arcsec
is sufficient and where extreme precision of the background subtraction is not critical (e.g.,
short wavelengths, narrowband filters). This has the advantage of reduced overheads and improved reliability through less complexity of the process, as during chopping the AO loop can
remained closed and the telescope as a whole does not move, while for nodding a whole sequence of pausing the AO loop, moving the telescope, and resuming the AO loop is required.
This mode will be commissioned and characterized in the near future.

## 4.2 Observing modes and strategies

The observing modes available are described in Sect. 2.5 (exemplary use cases), Sect. 3.4.1
(LMIRCam), and Sect. 3.5.1 (NOMIC). Table 4.1 summarizes this information. We distinguish between routine and experimental modes. Routine modes have been demonstrated
and the instrument performance is fairly well understood through frequent use or formal
commissioning. Experimental modes are under various levels of development or commissioning so that the instrument performance in these modes is typically not well understood and
observing routines and strategies are only partly available. Observations in these modes are
generally technically feasible, but will require larger time allocation than would be needed if
the modes were fully commissioned, so that instrument readiness can be achieved, observing
strategies can be developed, and inefficiencies due to manual operation and trouble shooting
can be accommodated. Users interested in using these modes may be required to contribute
to their development. The LBTI team is, however, willing to expedite development of these

<!-- page: 51 -->

**Table 4.1:** Available LBTI instrument modes.

**Mode LMIRCam NOMIC Comments**
Plain AO imaging routine routine
8 m NRM routine unavailable
ALES integral field spec. routine unavailable Standard Lspec mode only.
vAPP coronagraphy routine unavailable 180 deg coronagraph experimental.
ALES + vAPP routine unavailable 180 deg coronagraph experimental.
Nulling interferometry unavailable routine
Slitless spectroscopy experimental unavailable
AGPM coronagraphy experimental unavailable
Overlapped AO imaging experimental experimental
Wall-eyed pointing experimental experimental
23 m NRM experimental unavailable
Fizeau interferometry experimental experimental
ALES + Fizeau unavailable unavailable Anticipated future mode.

modes within our capabilities in preparation for a significant observing program that has
received – or is anticipated to receive – telescope time. Users interested in collaborating with
our team on developing and exploiting experimental modes are invited to contact the LBTI
lead scientist (Steve Ertel) at any time at [sertel@lbti.org.](mailto:sertel@lbti.org)

## 4.3 Parallel use of LBTI modes and LBT instruments

The LBTI’s two science cameras are able to both receive light in their respective wavelength
ranges simultaneously. This is almost always the case and does not result in a performance
degradation of either camera. Thus, with added complexity of the observing process and
added overheads for instrument setup, both cameras can in principle be used simultaneously.
In the past, this has been taken advantage of for parallel AO imaging with LMIRCam and
NOMIC and parallel integral field spectroscopy with ALES and imaging with NOMIC. This
does not mean that each camera uses one side of the LBT, but depending on the instrument mode and some additional constraints, both cameras can receive light from both LBT
apertures at the same time.

To execute such parallel observations, typically one camera is dedicated as the primary
camera (usually the one that delivers the data required to address the primary science goal
of the project). The observing strategy is then governed by the use of this camera with
some consideration on optimizing the observations for parallel use. The secondary camera
then follows along during the observations, often at somewhat reduced efficiency compared to
when it is used alone. The data from the secondary camera are obtained on a best-effort basis
and are sacrificed in case of problems with the parallel observations, so that the observing
success of the primary camera are not put at risk.

<!-- page: 52 -->

Parallel use of LMIRCam and NOMIC can also be useful for using one as a technical aide
to the other. For example, a target may be relatively easily visible at LMIRCam wavelengths,
but require a very long integration on NOMIC to be detected. Or a complicated nodding
pattern off the small ALES FoV is used and NOMIC is useful to confirm pointing and avoid
losing the target position in case of offset errors. Because the FoVs of the two science cameras
are fixed with respect to each other unless they are intentionally re-aligned, one camera can
be used to indicate the position of a source on the other. This mode has to be considered
experimental.

Similarly, the use of the LBTI on one LBT aperture and a different instrument on the
other LBT aperture is in principle possible. This is currently not offered by the observatory,
but has been done in the past in collaboration between the Potsdam Echelle Polarimetric and
Spectroscopic Instrument (PEPSI) and LBTI instrument teams before PEPSI transitioned to
facility status. If such parallel observations are carried out, the same strategies as for parallel
use of the two LBTI science cameras are applied (such as assigning a primary instrument).

## 4.4 Queue execution and observing instructions

LBTI observations are executed by the LBTI observing team, which is composed of LBTI
instrument team members and trained LBT observing staff. By default, the observations
are executed in a cross-partner observing queue that is managed by the instrument team in
collaboration with the LBT observatory. This ensures execution of observations according to
factors such as weather constraints, telescope and instrument readiness, target observability,
and prioritization by partner Time Allocation Committee (TAC) and PI. A justified request
for classical observing (allocated time will be scheduled at a fixed date, typically decided while
developing the observing schedule for a given semester) can be included in the proposal.
Partner coordinators may also request classical scheduling of specific observations or all
observations from a partner for various reasons (e.g., scheduling or prioritization constraints
within the partner’s allocated projects). Programs that are scheduled classically, except
for transient events, are limited to scheduling blocks of half or full nights. Waivers of this
requirement can be requested from the LBTI Lead Scientist (Steve Ertel) at [sertel@lbti.org](mailto:sertel@lbti.org)
before submitting an observing proposal or when preparing the observations. Such requests
will only be accommodated if the additional strain on the observing team and detrimental
effects on the scheduling of other programs (including those in the observing queue) are
negligible.

When a proposal has been allocated time, the PI will be contacted by the LBTI team with
a request for pertinent information about their project. Information are compiled in form of
a README file and a target observability sheet. The README file contains information
such as target list and coordinates, time on target, sensitivity requirements, filters, etc. The
target observability sheet contains the acceptable **LST!** ( **LST!** ) range over which each target
can be observed and constraints on the observing conditions. Information in the observability

<!-- page: 53 -->

sheet are formatted in a way that allows for simple ingestion into the LBTI’s observing queue.

Once the material is received by the LBTI team, it will be ingested into the queue system.
Verification and iteration with the PI at this stage is common to ensure the instructions are
clear. At this stage it is important to ensure that the instructions are:

 - Clear, so that they are easily understood by a trained observer.

 - Accurate, so that time loss for correcting errors during execution or a failed execution
attempt can be avoided.

 - Concise, so they can be easily and quickly grasped by an observer during night time,
considering factors such as fatigue.

 - Not overly constraining, so that observations have a high probability to be scheduled
for execution under the required conditions.
A finding chart is required only if the target is relatively faint and embedded in a group of
sources within one arcminute. Often LBTI targets are obviously the brightest stars around.
It is the responsibility of the PI to provide a finding chart or to make sure that target
identification is obvious on both the AO acquisition camera (RI bands) and the science
camera in the desired filters for acquiring the target. Time lost to identifying the science
target will have to be charged to the project’s allocated time and if a target cannot be clearly
identified, an observation will be aborted in favor of executing a different observation rather
than integrating ‘in the hope we are on the correct target’.

If a finding chart is provided, it should be obtained at a red visible wavelength (e.g., R band)
and an additional finding chart, e.g., from Two-micron all-sky survey (2MASS) should be
provided if the field looks significantly different in the infrared. An FoV of ∼ 1 arcmin is the
most useful. The science target, North and East directions, size of the image (by drawing a
scale bar), and the observing band should be clearly indicated (on the image itself, not in an
email, the README, or any other auxiliary information provided).

## 4.5 Observing scripts

After a target is acquired with the AO and science camera, and the instrument is set up
according to the instructions provided by the PI, most LBTI observations consist of a sequence of integrations and sky offsets. These are executed using Python scripts that control
the instrument and telescope through sequences of Instrument Neutral Distributed Interface (INDI) commands. While most observations are executed using a few template scripts
with adjusted parameters, the Python scripting allows for maximum flexibility to execute
complex sequences with pauses for manual interaction and the ability to develop additional
functionality. For complex observations that require a certain level of automation, users
should contact the LBTI Lead Scientist (Steve Ertel) as early as possible, ideally before
submitting an observing proposal at [sertel@lbti.org.](mailto:sertel@lbti.org) The LBTI team will do their best to
accommodate complex scripting for scheduled programs, but PIs or their team members may
be required to contribute significant effort in the preparation of complex observing scripts.

<!-- page: 54 -->

**Table 4.2:** Routine calibrations obtained as part of the instrument calibration plan and not charged
to a specific program

**Calibration Interval Notes**
LMIRCam linearity 1/semester Relevant detector modes
NOMIC linearity 1/semester Relevant detector modes
LMIRCam distortion 1/observing run Relevant detector subframes
LMIRCam astrometry 1/year Map Trapezium astrometric field
NOMIC distortion 1/observing run Experimental/best-effort
LMIRCam & NOMIC darks 1/observation Relevant detector modes

**Table 4.3:** Common calibrations that need to be requested by PIs and are charged to their program

**Calibration Time required Notes**
Photometric calibrator 15 min each NOMIC & LMIRCam
Unsaturated observations 5 min each If saturation is otherwise acceptable
Telluric calibrator 15 min each ALES
PSF calibrator 15 min each LMIRCam, NOMIC, & ALES
ALES wavelength calibration 20 min ALES
NOMIC astrometry 1 h Experimental/best-effort
Flat fields – (off-sky) Common for LMIRCam in K band and shorter

The use of complex, new scripts has always to be considered experimental until the scripts
are fully tested, including an analysis of the science data produced.

At the cost of efficiency, precision, and/or repeatability, and with increased risk of human
error, the majority of commands to operate the LBTI and that happen on human time scales
can also be executed manually. This is done on a best-effort basis and is always experimental.

## 4.6 Calibration

The calibration requirements of LBTI data heavily depend on the observing mode. The
calibration data are routinely obtained by our instrument team are listed in Table 4.2. Additional calibrations required by a specific observing program need to be requested by the
PI and the sky time required for taking these data will have to be accounted for in the telescope time request for the program. Common calibrations that are not part of the routine
calibration plan are listed in Table 4.3. Calibration data are available to users as part of
their science data set or upon request.

<!-- page: 55 -->

## 4.7 Overheads, time request, and execution time

Time allocated to LBTI programs is wall clock time. Most observations are not limited by
integration time, but by constraints such as field rotation required to achieve maximum contrast or for the most effective interferometric image reconstruction. Targeted high-contrast
observations are thus commonly allocated half-nights (5 h) per target including all overheads.
More shallow high-contrast survey observations may require less time per target, as little as
2 h per target, and snapshot observations may require as little as 30 min per target if multiple
targets can be grouped together to share overheads for instrument setup.

In some cases, a more precise estimate of execution time and overheads may be desirable,
and even a time request based on field rotation benefits from a more detailed break-down
of overheads in the proposal. For this purpose, Table 4.4 lists estimates of the dominant
overheads for LBTI observations.

<!-- page: 56 -->

**Table 4.4:** List of LBTI overheads.

**Item Occurrence Time [s] Comments**
Telescope preset Each target change 75
Initial AO acquisition Each program change 600 First acquisition for a project (AO)
Further AO acquisitions Each target change 300 Additional acquisitions (e.g., for calibrators)
Alignment imaging Mode change to imaging 180 LMIRCam or NOMIC, usually parallel to AO acquisition
Alignment ALES Mode change to ALES 300 Usually parallel to AO acquisition
Alignment vAPP Mode change to vAPP 300 Usually parallel to AO acquisition
Alignment AGPM Mode change to AGPM 600 Usually parallel to AO acquisition
Alignment NRM Mode change to NRM 300 Usually parallel to AO acquisition
Alignment nulling Mode change to nulling 1200 Includes fringe search, etc., parallal to AO acq.
Alignment Fizeau interferom. Mode change to Fizeau int. 1800 Includes fringe search, etc., parallal to AO acq.
Any other alignment Any other mode change 1800 Experimental modes with limited experience
Initial science acquisition Each program change 300 First acquisition for a project
Further science acquisitions Each target change 300 Additional acquisition for a project (science camera)
AGPM acquisition Each preset for AGPM obs. 600 AGPM centering etc.
Filter change Each filter change 15
Nodding Each nod offset 5
Slow chopping Each chop offset 1
Fast chopping Each chop offset 0 NOMIC only, absorbed into camera overheads
Camera setup Each frame sequence 2 Camera setup before starting each sequence of frames
Integration LMIRCam Each LMIRCam frame Eq. 3.1
Integration NOMIC Each NOMIC frame Eq. 3.3
On-sky calibrations Depending on project Sect. 4.6 Calibrations as required by users

**Notes:** Overheads for alignment add up. For example, when combining ALES and vAPP, the alignment overhead is
300 s+300 s = 600 s, and when using ALES and NOMIC imaging in parallel, the alignment overhead is 300 s+180 s =
480 s.

<!-- page: 57 -->

An on-sky checkout of the instrument and AO system is usually done in early evening
twilight and not charged to a specific program. However, this needs to be considered when
determining the amount of twilight time that is available for science use or if the night
does not start with LBTI observations. This may limit the amount of science time that is
available during a given night. The check-out can be as short as 15 min, but may take up to
1 h depending on the amount of trouble shooting necessary.

## 4.8 Data retrieval and reduction

LBTI is currently transitioning to archiving data in the **LBTO!** ( **LBTO!** ) archive. Users will
receive an email with instructions on how to access their data until this process is complete.
Once a new, stable procedure is available, it will be described here.

The LBTI team does provide limited data reduction support on a best-effort basis. Please
contact the LBTI’s Lead Scientist, Steve Ertel, at [sertel@lbti.org](mailto:sertel@lbti.org) for further information. In
addition, the ALES team though contact Jordan Stone at [jordan@lbti.org](mailto:jordan@lbti.org) provides a basic
reduction (extraction of image cubes, wavelength and telluric calibration) for all ALES data.

Generally, the reduction of LBTI data involves common infrared imaging data reductions
such as (typically in that order) nod subtraction, correction of detector cosmetics (bad pixels, striping, etc.), distortion correction (common for LMIRCam, experimental for NOMIC),
de-rotation according to parallactic angle (LBTI does not have an instrument rotator), image
registration, and stacking. Additional reduction steps such as star-subtraction for high contrast imaging (involving angular differential imaging or reference star differential imaging and
techniques such as principle component analysis) or interferometry are required depending on
the observing technique and science goal. Photometric calibration is often performed relative
to a bright source in the field (e.g., the host star for exoplanet imaging), but photometric
standard stars can be observed as requested by the PI.

<!-- page: 58 -->

## Bibliography

Bailey, V. P., Hinz, P. M., Puglisi, A. T., et al. 2014, in Society of Photo-Optical Instrumentation

Engineers (SPIE) Conference Series, Vol. 9148, Adaptive Optics Systems IV, ed. E. Marchetti,
L. M. Close, & J.-P. Vran, 914803, doi: `[10.1117/12.2057138](http://doi.org/10.1117/12.2057138)`

Briesemeister, Z. W., Skemer, A. J., Stone, J. M., et al. 2019, AJ, 157, 244, doi: `[10.3847/](http://doi.org/10.3847/1538-3881/ab1901)`
```
 1538-3881/ab1901

```

Conrad, A., de Kleer, K., Leisenring, J., et al. 2015, AJ, 149, 175, doi: `[10.1088/0004-6256/149/](http://doi.org/10.1088/0004-6256/149/5/175)`
```
 5/175

```

de Kleer, K., Skrutskie, M., Leisenring, J., et al. 2017, Nature, 545, 199, doi: `[10.1038/nature22339](http://doi.org/10.1038/nature22339)`

Defr`ere, D., Absil, O., Hinz, P., et al. 2014, in Society of Photo-Optical Instrumentation Engineers

(SPIE) Conference Series, Vol. 9148, Adaptive Optics Systems IV, ed. E. Marchetti, L. M. Close,
& J.-P. Vran, 91483X, doi: `[10.1117/12.2057205](http://doi.org/10.1117/12.2057205)`

Defr`ere, D., Hinz, P., Downey, E., et al. 2015, arXiv e-prints, arXiv:1501.04142. `[https://arxiv.](https://arxiv.org/abs/1501.04142)`
```
 org/abs/1501.04142

```

Ertel, S., Defr`ere, D., Hinz, P., et al. 2018, AJ, 155, 194, doi: `[10.3847/1538-3881/aab717](http://doi.org/10.3847/1538-3881/aab717)`

—. 2020a, AJ, 159, 177, doi: `[10.3847/1538-3881/ab7817](http://doi.org/10.3847/1538-3881/ab7817)`

Ertel, S., Hinz, P. M., Stone, J. M., et al. 2020b, in Society of Photo-Optical Instrumentation Engi
neers (SPIE) Conference Series, Vol. 11446, Society of Photo-Optical Instrumentation Engineers
(SPIE) Conference Series, 1144607, doi: `[10.1117/12.2561849](http://doi.org/10.1117/12.2561849)`

Gordon, M. S., Jones, T. J., Humphreys, R. M., et al. 2019, AJ, 157, 57, doi: `[10.3847/1538-3881/](http://doi.org/10.3847/1538-3881/aaf5cb)`
```
 aaf5cb

```

Hinz, P. M., Skemer, A., Stone, J., Montoya, O. M., & Durney, O. 2018, in Society of Photo
Optical Instrumentation Engineers (SPIE) Conference Series, Vol. 10702, Ground-based and
Airborne Instrumentation for Astronomy VII, ed. C. J. Evans, L. Simard, & H. Takami, 107023L,
doi: `[10.1117/12.2314289](http://doi.org/10.1117/12.2314289)`

Hinz, P. M., Defr`ere, D., Skemer, A., et al. 2016, in Proc. SPIE, Vol. 9907, Optical and Infrared

Interferometry and Imaging V, 990704, doi: `[10.1117/12.2233795](http://doi.org/10.1117/12.2233795)`

Hoffmann, W. F., Hinz, P. M., Defr`ere, D., et al. 2014, in Proc. SPIE, Vol. 9147, Ground-based

and Airborne Instrumentation for Astronomy V, 91471O, doi: `[10.1117/12.2057252](http://doi.org/10.1117/12.2057252)`

<!-- page: 59 -->

Jones, T. J., Williams, L. L. R., Ertel, S., et al. 2019, AJ, 158, 237, doi: `[10.3847/1538-3881/ab5108](http://doi.org/10.3847/1538-3881/ab5108)`

Kuzmenko, P. J., Little, S. L., Little, L. M., et al. 2012, in Society of Photo-Optical Instrumentation

Engineers (SPIE) Conference Series, Vol. 8450, Modern Technologies in Space- and Ground-based
Telescopes and Instrumentation II, ed. R. Navarro, C. R. Cunningham, & E. Prieto, 84503P,
doi: `[10.1117/12.926674](http://doi.org/10.1117/12.926674)`

Leisenring, J. M., Skrutskie, M. F., Hinz, P. M., et al. 2012, in Society of Photo-Optical In
strumentation Engineers (SPIE) Conference Series, Vol. 8446, Ground-based and Airborne Instrumentation for Astronomy IV, ed. I. S. McLean, S. K. Ramsay, & H. Takami, 84464F,
doi: `[10.1117/12.924814](http://doi.org/10.1117/12.924814)`

Maire, A. L., Skemer, A. J., Hinz, P. M., et al. 2015, A&A, 576, A133, doi: `[10.1051/0004-6361/](http://doi.org/10.1051/0004-6361/201425185)`
```
 201425185

```

Pinna, E., Esposito, S., Hinz, P., et al. 2016, in Society of Photo-Optical Instrumentation Engineers

(SPIE) Conference Series, Vol. 9909, Adaptive Optics Systems V, ed. E. Marchetti, L. M. Close,
& J.-P. V´eran, 99093V, doi: `[10.1117/12.2234444](http://doi.org/10.1117/12.2234444)`

Sallum, S., Eisner, J. A., Hinz, P. M., et al. 2017, ApJ, 844, 22, doi: `[10.3847/1538-4357/aa7855](http://doi.org/10.3847/1538-4357/aa7855)`

Sallum, S., Eisner, J. A., Stone, J. M., et al. 2021, AJ, 161, 28, doi: `[10.3847/1538-3881/abc957](http://doi.org/10.3847/1538-3881/abc957)`

Sallum, S., Follette, K. B., Eisner, J. A., et al. 2015, Nature, 527, 342, doi: `[10.1038/nature15761](http://doi.org/10.1038/nature15761)`

Skemer, A. J., Hinz, P., Stone, J., et al. 2018, in Society of Photo-Optical Instrumentation En
gineers (SPIE) Conference Series, Vol. 10702, Ground-based and Airborne Instrumentation for
Astronomy VII, ed. C. J. Evans, L. Simard, & H. Takami, 107020C, doi: `[10.1117/12.2314091](http://doi.org/10.1117/12.2314091)`

Skemer, A. J., Hinz, P., Montoya, M., et al. 2015, in Society of Photo-Optical Instrumentation

Engineers (SPIE) Conference Series, Vol. 9605, Techniques and Instrumentation for Detection of
Exoplanets VII, ed. S. Shaklan, 96051D, doi: `[10.1117/12.2187284](http://doi.org/10.1117/12.2187284)`

Skrutskie, M. F., Jones, T., Hinz, P., et al. 2010, in Society of Photo-Optical Instrumentation

Engineers (SPIE) Conference Series, Vol. 7735, Ground-based and Airborne Instrumentation for
Astronomy III, ed. I. S. McLean, S. K. Ramsay, & H. Takami, 77353H, doi: `[10.1117/12.857724](http://doi.org/10.1117/12.857724)`

Spalding, E., Hinz, P., Ertel, S., Maier, E., & Stone, J. 2018, in Society of Photo-Optical Instru
mentation Engineers (SPIE) Conference Series, Vol. 10701, Proc. SPIE, 107010J, doi: `[10.1117/](http://doi.org/10.1117/12.2315498)`
```
 12.2315498

```

Spalding, E., Hinz, P., Morzinski, K., et al. 2019, arXiv e-prints, arXiv:1908.11023. `[https://](https://arxiv.org/abs/1908.11023)`
```
 arxiv.org/abs/1908.11023

```

Stone, J. M., Skemer, A. J., Hinz, P. M., et al. 2018, AJ, 156, 286, doi: `[10.3847/1538-3881/aaec00](http://doi.org/10.3847/1538-3881/aaec00)`

Stone, J. M., Barman, T., Skemer, A. J., et al. 2020, AJ, 160, 262, doi: `[10.3847/1538-3881/abbef3](http://doi.org/10.3847/1538-3881/abbef3)`

<!-- page: 60 -->

Wagner, K., Stone, J. M., Spalding, E., et al. 2019, ApJ, 882, 20, doi: `[10.3847/1538-4357/ab32ea](http://doi.org/10.3847/1538-4357/ab32ea)`

Wagner, K., Stone, J., Dong, R., et al. 2020, AJ, 159, 252, doi: `[10.3847/1538-3881/ab893f](http://doi.org/10.3847/1538-3881/ab893f)`

<!-- page: 61 -->

## List of names and acronyms

**2MASS** Two-micron all-sky survey, Skrutskie et al. paper, link

**AGPM** Annular Groove Phase Mask, a type of focal plane coronagraph

**ALES** the Arizona Lenslet for Exoplanet Spectroscopy, LBTI’s thermal infrared IFU

**AO** Adaptive Optics

**ASM** Adaptive Secondary Mirror

**CDS** correlated double sampling, a readout mode of astronomical detectors capable of non-destructive

reads

**DX** the right telescope aperture and more generally optical, mechanical, and structural elements

pertinent to it

**ELFN** Excess Low Frequency Noise, a low frequency noise component of Aquarius detectors

**ExEP** Exoplanet Exploration Program maintained by NASA

**FoV** field of view

**FPC** Fast Pathlength Corrector

**FW** Filter Wheel

**IBC** Impurity Band Conduction, a process responsible for making certain materials semiconductors

**IFU** Integral Field Unit, an optical instrument combining spectroscopic and imaging capabilities

**H2RG** HAWAII-2RG, a readout integrated circuit for visible and infrared instrumentation in ground
based and space telescope applications manufactured by Teledyne Imaging

**HgCdTe** mercury cadmium telluride, a semiconductor compound used for infrared detectors

**HOSTS** Hunt for Observable Signatures of Terrestrial planetary Systems, LBTI’s completed NASA

mission

**INDI** Instrument Neutral Distributed Interface, a distributed control system (DCS) protocol to

enable control, data acquisition and exchange among hardware devices and software front
ends, emphasizing astronomical instrumentation

**JPL** Jet Propulsion Laboratory

<!-- page: 62 -->

**LBT** Large Binocular Telescope

**LBTI** Large Binocular Telescope Interferometer

**LEECH** LBT Exozodi Exoplanet Common Hunt, a large LBTI science program

**LMIRCam** the LBT Mid-InfraRed Camera, one of LBTI’s science cameras (the other one being

NOMIC)

**NAC source** an artificial source

**NASA** National Aeronautics and Space Administration

**NIC** the Nulling and Imaging Cryostat, the cryostat holding LBTI’s science cameras

**NOMIC** the Nulling-Optimized Mid-Infrared Camera, one of LBTI’s science cameras (the other

one being LMIRCam)

**NRM** non-redundant aperture masking, an interferometric technique for high-contrast, high angu
lar resolution observations

**OPD** Optical Path Delay

**PA** Parallactic Angle

**PEPSI** Potsdam Echelle Polarimetric and Spectroscopic Instrument, a high spectral resolution

spectro-polarimeter and facility instrument at the LBT

**PhaseCam** LBTI’s fringe tracking camera

**PI** Principal Investigator

**PICNIC** a readout integrated circuit for visible and infrared instrumentation in ground-based and

space telescope applications developed by Rockwell International

**PSF** point spread function

**SAPHIRA** a linear avalanche photodiode array for astronomical infrared applications developed by

ESO and the University of Hawaii

**SOUL** Single conjugated adaptive Optics Upgrade for the LBT

**SPC** Slow Pathlength Corrector

**SX** the left telescope aperture and more generally optical, mechanical, and structural elements

pertinent to it

**S/N** signal-to-noise ratio

**TAC** Time Allocation Committee

<!-- page: 63 -->

**UBC** Universal Beam Combiner, the cryostat holding LBTI’s optics for combining the beams from

the two LBT apertures

**vAPP** Vector Apodizing Phase Plate, a type of pupil plane coronagraph
