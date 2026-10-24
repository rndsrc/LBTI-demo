---
url: https://scienceops.lbto.org/lbti/ao-wfs/
title: AO & WFS
breadcrumb: AO & WFS
fetched_at: '2026-10-26T06:40:18+00:00'
sha256: 5af45841ad8cd7effab4aed54846ecfca4610ce37d5358651b3be0c068a4fa14
---

The Adaptive Optics (AO) systems at the Large Binocular Telescope (LBT) represent a distributed AO system in that the wavefront sensor (WFS) and the wavefront corrector are not co-located on the same optical bench. The AO systems can and do provide a variety of AO correction to enable different science goals. LBTI uses Natural Guide Star (NGS) on-axis correction (Single Conjugate Adaptive Optics) yielding 8.4m diffraction-limited performance and also permits Fizeau and nulling interferometry between the apertures with an unprecedented 23m baseline along one axis.

The wavefront corrector takes the form of a 672-actuator adaptive secondary mirror (ASM), also known as a deformable secondary mirror (DSM), mounted on each side of the LBT. These ASMs are permanently mounted at the M2 positions as adaptive elements for AO operations. The ASMs are controlled by the LBTI WFS’s at the 2 center bend Gregorian ports. The LBTI WFS assemblies are mounted in a fixed orientation relative to the telescope pupil and thus do not have rerotator optics.

## SOUL WFS {#TOC-SOUL-WFS}

SOUL, which stands for **S**ingle Conjugated Adaptive **O**ptics **U**pgrade for **L**BT, is an upgrade to the LBTI **F**irst **L**ight **A**daptive **O**ptics (FLAO) system that took place 2018-2019. The system uses the facility adaptive secondary mirror for wavefront corrections at rates of up to 1.7kHz. Wavefront sensing is provided by pyramid-based wavefront sensors (WFS) with up to 40 subapertures across the diameter of each telescope pupil. This upgrade increases the performance of this high performance system, specifically:

| Feature | LBTI FLAO | LBTI SOUL |
| --- | --- | --- |
| subaps | 30×30 | 40×40 |
| Read out noise | 10e-/4e- | <1e |
| Number of Modes | 400/500 | 500/650 |
| ASM rise time | <1ms | <0.7ms(0.5ms) |
| Frames rate | 1kHz | 1.7kHz |

The goals of these upgrades in to improve the overall sky coverage, wavelength range, and improve the PSF contrast allowing for observations of fainter targets to be observed, gaining ~2 magnitudes for almost all reference star brightness cases. These improvements should allow the phase to be stabilized in worse seeing.

[![](https://scienceops.lbto.org/wp-content/uploads/2021/12/SOUL.png)](https://scienceops.lbto.org/wp-content/uploads/2021/12/SOUL.png)

[LMIRcam L band image of R=3.1, I=2.2, L~0 target using SOUL WFS, Images are a stack of 10 frames each with 10 frames in the other not position subtracted for background and bias removal, integration times per frame: 0.0137 sec, 0.1099 sec, 1.0027 sec, and 10.0128 sec](https://scienceops.lbto.org/wp-content/uploads/2021/12/SOUL.png)

The SX (left) was first to be upgraded.  DX (right) was upgraded in spring of 2019.
