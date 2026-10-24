---
url: https://scienceops.lbto.org/lbti/planning-observations/near-thermal-ir-observing/
title: Near & Thermal IR Observing
breadcrumb: Planning Observations › Near & Thermal IR Observing
fetched_at: '2026-10-26T06:31:13+00:00'
sha256: 480ba0f9374a72533ba4c46d3878f0454f40d679b97e2f37fab3a5c0b4ea7397
---

Contents

## The Atmosphere and Telescope {#TOC-The-Atmosphere-and-Telescope}

The observing approach and strategy are similar for near IR and mid IR observations but for slightly different reasons. It is important to understand the subtle differences of observing in each regime.  LBTI is designed for sensitive observations in the thermal infrared, and capable of observing in the J to N bands (wavelengths ~1.2 microns to 14 microns, with experimental Q filters).

| Regime | Wavelength Range  μm | Temp. Range  K | Comments |
| --- | --- | --- | --- |
| Near-Infrared | 1 to 5 | 740 to 3000 | Observations of: Cooler red stars Red giants. Dust is transparent. |
| Thermal-Infrared | 5 to (25-40) | (92.5-140) to 740 | AKA Mid IR. Observations of: Planets, comets and asteroids. Dust warmed by starlight. Protoplanetary disks |

Below is a table is a plot of the atmospheric transmission in the LBTI’s wavelength range:

![](http://scienceops.lbto.org/wp-content/uploads/2022/03/LBTI-Atmospheric-Transmission-1.png)

### Thermal IR observing {#TOC-Thermal-IR-observing}

In the thermal IR, the telescope and atmosphere are bright sources or radiation. Even at high altitudes, the atmosphere is relatively warm, and during observations is at the same temperature as the telescope (approximately). Therefore, like the telescope, the atmosphere will emit radiation in the thermal infrared. In fact, for most typical observations, the combination of sky background emission and telescope background emission dominate the emission from the astronomical object of interest. As well, the sky brightness changes on short timescales (over the course of a few minutes) and over small distances on the sky. Nodding on short time scales helps with the removal of sky variations.

Planets can be imaged with a more moderate planet-star contrast in the thermal infrared than in the near infrared, which is sort of what that last image was demonstrating. Here I’ve got wavelength on the x-axis and I’ve got contrast compared to a star on the y-axis. So moving down here becomes harder contrast to image something. And for every planet, every thermally every self-luminous planet, the contrast is less extreme in the L and M bands than it is that J, H, K. It takes less contrast to image it there.

### Impacts of Infrared Background {#TOC-Near-IR}

The background has 3 major effects that limit the sensitivity of observations: variable background structure, photon noise, and saturation.

1. **Variable background structure**A common challenge of infrared observations is variable, large-scale structure in the background across the images. This is removed by nodding. The frequency of nodding depends on the time scale with which this background changes. LBTI has a small FoV which limits the effect of large scale variations, the optical design of the instrument and telescope the variable telescope and instrument background is of little concern short-ward of N band.
2. **Background Photon Noise**A more critical and fundamental noise source caused be the high infrared background is photon noise. This is the Poisson noise caused by the fact that photons on an evenly illuminated detector follow a statistical distribution. The result is a random pixel-to-pixel noise with a standard deviation equal to the square-root of the counts on the detector. If the background contributes significantly to the signal on the detector, this photon noise can be the dominant noise in an image. One can compare the detector read noise in a given setup with the square-root of the expected background counts in a given filter and integration time to determine whether read noise of photon noise dominates a given observation. For high contrast imaging this noise may be negligible.
3. **Saturation**Saturation is a common factor in determining integration times in thermal infrared observations. This coincides with the regimes where the background photon noise dominates over the detector read noise, so that many short integrations do not degrade the final S/N compared to one longer integration if it was possible. Saturation of background: ~1 sec in L, 50 ms for N, etc.

## Nodding {#TOC-Nodding}

Dithering/Nodding allows for removal of instrumental signatures, thermal signature from warm optics, and sky background from RAW data. For sky removal, the largest structure you are trying to measure must be offset completely. To keep the contribution to the noise from the background down, sky subtraction is done using a number of exposures around each science image. For very extended sources, this often requires moving completely off source to obtain a separate measurement of the sky.

## Constraints {#TOC-Constraints}

Weather, water vapor, and seeing are important factors to consider. [Carrasco et. al. (2017)](http://iopscience.iop.org/article/10.1088/1538-3873/129/973/035005/meta) have an in-depth review and comparison of the site average water vapor and cloud cover.

The observing constraints should be clearly stated as constraints on all programs. Clouds act like neutral density filters only on the source flux, but the background is still collected. Clear-sky seeing does not change the source flux, but does affect the number of pixels over which you extract your data.  Poor seeing can also affect the ability to guide on the AOref and reduce efficiency.  In either case, a factor of two change in the constraint (half the source flux blocked by clouds, or an increase of the seeing from 1 to 2 arcsec) requires a factor of four change in exposure time to reach a comparable SNR as originally planned.

The opacity in the mid-infrared strongly depends on the precipitable water vapour (PWV) in the earth’s atmosphere. Measures of the site PWV can be found here. The site average is ___, but can vary from Thus it does not make any sense to observe programs when the weather or seeing constraints are not met, and it is always a good idea to have backup programs available to do in poorer conditions than needed for the primary science targets.
