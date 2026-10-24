---
url: https://scienceops.lbto.org/lbti/instrument-characteristics/detectors/
title: Detectors
breadcrumb: Instrument Characteristics › Detectors
fetched_at: '2026-10-26T06:40:18+00:00'
sha256: d9eaa783dc1119bd1612e694e4bf9d2e0b1f5c35506972bbf8712e44f55125cf
---

## About {#TOC-About}

LMIRcam was upgraded to HAWAII-2RG (H2RG) HgCdTe detector in 2018. This detector is 2048 x 2048 pixels2.  The outer pixels are vignetted.  In Summer of 2017 LMIRcam electronics were upgraded with Teledyne’s SIDECAR electronics.

The LMIRcam plate scale is ~10.7mas/pix with a FoV 22 arcseconds squared.  Due to vignetting at the edges this FoV is closer to 18 arcseconds squared.

## Characteristics {#TOC-Characteristics}

The dark current and read noise are low, allowing for background-limited observations in most imaging and spectroscopic configurations. There is significant persistence and nonlinearity with these detectors. Detector characterization in progress.

| Parameter | LMIRCAM | LMIRCAM | LMIRCAM | NOMIC |
| --- | --- | --- | --- | --- |
| Parameter | FAST | MEDIUM | SLOW | NOMIC |
| Detector Area(pixels) | See Readout Stripes | 2048×2048 | 2048×2048 | 1024×1024 |
| Pixel Scale(mas/pixels) | 10.7 | 10.7 | 10.7 | 17.9 |
| Frame Time [s] | see Readout Stripes | 0.4918 | 1.4753 | TDB |
| Saturation Level | 3900 | 62000 | 62000 | 16000 |
| 5% non-linearity | 2900 | 47500 | 47500 | N/A |
| Bias Level | 500 | 5000 | 5000 | 1200-2500 |
| Dark Count | 2 | 18 | 18 | TDB |
| Read Noise | 2 | 35 | 40 | 15-30 |

Sub windowing is available for LMIRCAM in FAST mode only. Minimum exposure time scales linearly with the vertical pixel size.

## Readout Stripes {#TOC-Readout-Stripes}

| Label | First Row | Last Row | Frame Time [ms] |
| --- | --- | --- | --- |
| Full Image | 1 | 2048 | 27.5 |
| Center_Stripe_1024 | 513 | 1536 | 13.7 |
| Center_Stripe_512 | 1025 | 1536 | 6.9 |
| Center_Stripe_256 | 1025 | 1280 | 3.4 |

## Saturation {#TOC-Saturation}

Saturation is around 64K counts. ??% non linear at ~40K. Persistence is negligible.

## Non-Linearity {#TOC-Non-Linearity}

All near-infrared detectors are non-linear. The lmircam_linearty.py script should be run about once per run. The script takes a series of exposures intended to cover the full dynamic range of the detector and allows the users to characterize the linearization fit across the detector. If you work with high-dynamic range data or you care about doing higher precision photometry, it will be very important to linearize your data.

## Crosstalk {#TOC-Crosstalk}

At the speed the detector is read out, there is some crosstalk. For sources where the PSF core is saturated, evidence of channel crosstalk can be observed as dark spots on either side of the PSFs (approximately 64 pixels away to the left and right).
