.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: discussion-image-conversion-quality ; Index


.. _discussion-image-conversion-quality:

========================
Image Conversion Quality
========================

WebP Image Quality Determination
================================

**Design Pattern:** Interval Mapping with Binary Search

Motivation
----------

In the realm of web image optimization, selecting the right WebP quality level is crucial. Lower quality levels result in smaller file sizes (improving page load speed), but they can also sacrifice visual fidelity. Our goal is to automatically determine a suitable quality level for a WebP image based on its original file size, while prioritizing efficiency and adaptability.

Approach
--------

We employ an “interval mapping” strategy, augmented by Python’s bisect module for binary search, to achieve this:

**File Size Thresholds:** We maintain a list of `file size thresholds` in bytes (e.g., [500_000, 1_000_000, 2_000_000, 10_000_000]). These define the boundaries for different quality levels.

**Corresponding Qualities:** We have a parallel list of `WebP quality levels` (e.g., [30, 20, 10, 5, 3]). The quality at a given index corresponds to file sizes that fall within the interval defined by the threshold at that index and the next threshold.

**Binary Search (bisect):** Given the image’s original file size, we use bisect to efficiently locate the index where that size would fit into the thresholds list while maintaining sorted order. This effectively identifies the size interval to which the image belongs.

**Quality Lookup:** The index returned by bisect is then used to directly fetch the corresponding quality level from the qualities list.

**Code Example**

.. code-block:: python

   def _determine_quality(image_size: int) -> int:
       """Determines the optimal WebP image quality level based on file size."""
       thresholds = [500_000, 1_000_000, 2_000_000, 10_000_000]
       qualities = [30, 20, 10, 5, 3]

       index = bisect.bisect(thresholds, image_size)
       return qualities[index]

Rationale
---------

**Efficiency:** Binary search (bisect) ensures rapid lookup, even with a large number of thresholds. This is vital when dealing with many images. Maintainability: The code is simple and self-explanatory, promoting easy understanding and future adjustments.

**Adaptability:** Modifying the thresholds and qualities lists provides a straightforward way to fine-tune the quality determination logic as needed. Key Points

**Sorted Thresholds:** It’s critical that the thresholds list remains sorted in ascending order for the binary search to function correctly. Default Quality: The qualities list should contain one more element than the thresholds list to cover file sizes above the highest threshold (in the example, files larger than 10 MB receive a default quality of 3).

Example Usage
-------------

.. code-block:: python

   image_size = 1_234_567  # Example image size
   webp_quality = _determine_quality(image_size)  # This would return 20

Alternative Solutions
---------------------

While other solutions exist (e.g., linear search, explicit conditional logic), this design offers a compelling combination of efficiency, clarity, and flexibility that aligns well with best practices for maintainable code.
