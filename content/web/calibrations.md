---
url: https://scienceops.lbto.org/lbti/planning-observations/calibrations/
title: Calibrations
breadcrumb: Planning Observations › Calibrations
fetched_at: '2026-10-26T06:28:41+00:00'
sha256: 93239cbc00ecbfec6e47626a88065b79a9af5f52c6da0d4b68dbed62c128141a
---

- **Darks**: The alldarks.py script located in the templates/calibrations directory should be run at the end of each night. For a given dated directory, this script will take darks, inserting the blank filter into filterwheel4, for all exposure times and subframe combinations. The script will notify the user of how long it takes to run before proceeding and does require user input.
- **Linearity**: The lmircam_linearty.py script should be run about once per run. The script takes a series of exposures intended to cover the full dynamic range of the detector.
- **Dome Flats**: Taken for near IR imaging observations. These are not typically scripted, but rather just run by setting the detector parameters and motor parameters through the LBTI web pages.
- **ALES Lenslet Flats**:A lenslet flat is a flat-field that quantifies the through put of each lenslet in our lenslet array. We do not typically spend time specifically to obtain data for a lenslet flat. Instead, we use the sky-images observed while collecting science data since the background is typically bright enough and very flat across the field of view.
- **ALES Wavelength Calibrations**:Wavelength calibrations are performed using W a set of four narrow-band photometric filters in series with the ALES optics, upstream of the lenslet array: 2.9, 3.3, 3.5, and 3.9 µm. Since ALES is composed of so many moving parts, it is essential to collect wavelength calibration data before moving any of the ALES optics (to move on to a non-ALES observing program for example. Depending on the program this may require ~20 minutes of on sky time for calibrations.
- **ALES Telluric**: Typically an A or G type star with a magnitude 4
- **Imaging: Unsats**If the program allows for saturation of the source to any degree, a set of unsaturated frames should be taken.
- **Imaging: PSF Calibrator** should be nearby stars with similar magnitudes and color to the science field wavefront reference source. Fields with single PSFs appropriate for PSF calibrations can be found by searching star catalogs. PSF calibrators should not be saturated.

- **Optical distortion:**  LMIRCam optical image distortion is significant and needs to be corrected for almost all science data.  A distortion correction is derived from images of a pinhole grid.  The solutions are provided to the users.  Details can be found here [[licoeff_lmir_sx_191119nk](https://scienceops.lbto.org/wp-content/uploads/2021/12/coeff_lmir_sx_191119.dat)].
- **Astrometric solution:**  If accurate astrometry is required, the plate scale and True North direction of LMIRCam needs to be calibrated.  We regularly image the Trapezium cluster.  Data are provided to users as needed to obtain an astrometric solution.  Users should make sure the LBTI team is aware of the astrometric requirements of their program.  Details can be found here [[lincoeff_lmir_sx_191119(1)k](https://scienceops.lbto.org/wp-content/uploads/2021/12/coeff_lmir_sx_1911191.dat)].
