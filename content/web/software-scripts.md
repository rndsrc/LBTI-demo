---
url: https://scienceops.lbto.org/lbti/observing/software-scripts/
title: Software & Scripts
breadcrumb: Observing › Software & Scripts
fetched_at: '2026-10-26T06:28:41+00:00'
sha256: 14cdee4c94c15b94151c07795c2a8fa8a0a049f5f28e4915c6e74d67c1a31096
---

## LBTI Web {#TOC-LBTI-Web}

The LBTI Webpage is the primary interface for the user to interact with the telescope and instrument mechanisms.  There are ~3 pages/tabs that observers use regularly:

1. **The LBTO page**: This page allows the user to send telescope presets, offsets, and check on telescope and environmental parameters. This is typically the default landing page.  Tar.[![](https://scienceops.lbto.org/wp-content/uploads/2021/12/LBTOpage-1600x1049.png)](https://scienceops.lbto.org/wp-content/uploads/2021/12/LBTOpage.png)

- Environmental, telescope, and target information are summarized in the top portion and in the diagrams along the right.
- **The SCICAM page**: The users will be able to see data files streaming in real time. This page can me used for target acquisition and setup, data quality checks, and overall monitoring.    When “Camera Controls” is highlighted in green it is actively updating.
  [![](https://scienceops.lbto.org/wp-content/uploads/2022/01/SCICAMPAGE.png)](https://scienceops.lbto.org/wp-content/uploads/2022/01/SCICAMPAGE.png?attredirects=0)

1. Continuous will update the real-time display with images with the parameters set in the detector parameters section. This can be useful for target alignment, testing image quality, etc.
2. **The MOTORS page**: This page is used to reconfigure the physical instrument parameters if necessary.  This is also used for instrument alignment, troubleshooting, and verification. Many of the motor movements can be scripted, but alignments and verifications are much more efficient manually at this time.    Tweaking motions of filter wheels or other motors manually may result in incomplete header information.  Users should refer to the logs.

## Scripting {#TOC-Scripting}

Python scripts are used to send INDI commands to the instruments, configuring the instrument and taking the desired exposures. Many of the alignment procedures require manual interactions. This limits the degree of scriptability.  There are a number of template python scripts designed for each observing mode/configuration. These are designed with nod patterns, integrated darks where necessary, sky offsets where desired. The appropriate template is selected and run with an appropriate dither size and optimized exposure time.
