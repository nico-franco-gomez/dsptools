Changelog
=========

All notable changes to `dsptoolbox
<https://github.com/nico-franco-gomez/dsptoolbox>`_ will be documented in this file.

The format is based on `Keep a
Changelog <http://keepachangelog.com/en/1.0.0/>`__ and this project
adheres to `Semantic Versioning <http://semver.org/spec/v2.0.0.html>`_.

`To Do's for future releases`_
------------------------------

- Automated testing with pytest
- Validation of transfer functions, coherence and distances with some external tool
- Fractional time delay filter
- Beamforming module

`0.0.5`_ - 2023-01-11
---------------------

Added
~~~~~~
- stop_flag for ``stream_samples`` method of ``Signal`` class
- ``get_ir`` method for Linkwitz-Riley Filterbank class
- possibility to define a start for the RIR in the ``reverb_time`` method. Also
  the same start index is now used for all channels and bands
- sleep and output_stream to audio_io (wrappers around sounddevice's functions)
- ``min_phase_from_mag`` and ``lin_phase_from_mag`` in the special module.
- ``auditory_filters_gammatone`` filter bank.
- harmonic tone generator added in ``generators`` module
- grey noise in noise generator function
- ``find_ir_start`` in room_acoustics module
- ``Signal`` class can now handle complex time data by splitting real and imaginary
  parts in different properties (time_data and time_data_imaginary)
- ``swap_bands`` in ``MultiBandSignal`` class that allows reordering the bands
- ``swap_filters`` in ``FilterBank`` class that allows reordering the filters

Bug fixes
~~~~~~~~~~
- bug in _get_normalized_spectrum helper function
- bug in the order of the [filter] order vector in Linkwitz-Riley FliterBank class
- bug in ``Signal`` class where unwrapped phase could not be plotted correctly
- plots.general_plot can now use tight_layout() or not. Activating it could be counterproductive in cases where the legend is very large since it squishes the axes
- changed spectrum array dtype to cfloat to ensure that complex spectrum is always created

Misc
~~~~~
- changed function name ``play_stream`` to ``play_through_stream`` in audio_io module and the way it works
- extended and corrected docstrings
- ``Filter`` class can now handle complex output: a warning can be printed or not and the imaginary output is saved in the 
  ``Signal`` class' ``time_data_imaginary``. The warning is defined through ``warning_if_complex`` bool attribute
- newly improved filtering function for FIR filters that uses ``scipy.signal.convolve`` instead of ``numpy.convolve``


`0.0.4`_ - 2023-01-05
---------------------

Added
~~~~~

- added resampling using ``scipy.signal.resample_poly``
- added distance measures: snr, si-sdr
- added ``normalize`` function
- added ``get_ir`` method to ``FilterBank`` class
- added function to load pickle objects
- added changelog
- added support for ``MultiBandSignal`` input in ``reverb_time`` function
- added ``get_channel`` method in ``Signal`` class for retrieving specific channels from signal as signal objects
- introduced support for 1d-arrays in plot functions and raise error if ndim>2
- added property and specialized setter for multiple sampling rates in FilterBank and MultiBandSignal
- ``get_stream_samples`` added in ``Signal`` class for streaming purposes
- added ``fade`` method for signals

Bugfix
~~~~~~

- corrected a bug regarding filter order
- corrected documentation for ``__init__`` Filter biquad, ``find_room_modes``, 
- change assert order in merge signal function
- corrected errors in test file
- corrected copying signals in `_filter.py` functions and ``MultiBandSignal.collapse`` method
- references in pyfar functions corrected
- bug fix in normalize function
- minor bug fixes
- documentation fixed

Misc
~~~~

- dropped multichannel parameter in spectral deconvolve and get transfer function
- changed to dynamic versioning to building package with hatch
- when plotting, general plot can now take flat arrays as arguments
- readme edited
- package structure updated
- general updates to docstrings
- extended merging signals while trimming or padding in the end and in the beginning
- changed module name from `measure` to `audio_io`
- refactored ``time_vector_s`` handling in ``Signal`` class