.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: build-system-reference ; Index


.. _build-system-reference:

======================
Build System Reference
======================

This document provides reference information for the webpack configuration and build system used in django-ckeditors.

Package Configuration
=====================

package.json
------------

The ``package.json`` file defines the project dependencies and build scripts.

Dependencies Structure
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "dependencies": {
       "@ckeditor/ckeditor5-*": "^45.1.0"
     },
     "devDependencies": {
       "@ckeditor/ckeditor5-dev-*": "^43.0.1",
       "webpack": "^5.99.9",
       "terser-webpack-plugin": "^5.3.14"
     }
   }

**dependencies**
    CKEditor 5 runtime packages required for the editor functionality.

**devDependencies**
    Build tools and webpack configuration packages used during compilation.

Build Scripts
~~~~~~~~~~~~~

.. code-block:: json

   {
     "scripts": {
       "dev": "cross-env NODE_ENV=development webpack --mode development",
       "prod": "cross-env NODE_ENV=production webpack --mode production",
       "watch": "cross-env NODE_ENV=development webpack --watch --mode development"
     }
   }

``npm run dev``
    Builds the CKEditor bundle with development settings (unminified, with source maps).

``npm run prod``
    Builds the CKEditor bundle with production optimizations (minified, no source maps).

``npm run watch``
    Builds with development settings and watches for file changes, rebuilding automatically.

Webpack Configuration
=====================

webpack.config.mjs
------------------

The webpack configuration uses ES Module syntax and handles CKEditor-specific build requirements.

Configuration Structure
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   import { styles } from '@ckeditor/ckeditor5-dev-utils';
   import { CKEditorTranslationsPlugin } from '@ckeditor/ckeditor5-dev-translations';
   
   const isProduction = process.env.NODE_ENV === 'production';
   
   export default {
     mode: isProduction ? 'production' : 'development',
     entry: './static/django_ckeditors/app.js',
     output: {
       path: path.resolve(__dirname, 'static/django_ckeditors/dist'),
       filename: isProduction ? '[name].[contenthash].js' : '[name].js',
       chunkFilename: isProduction ? '[name].[contenthash].chunk.js' : '[name].chunk.js'
     }
   };

Entry Points
~~~~~~~~~~~~

**entry**
    ``./static/django_ckeditors/app.js`` - Main application entry point that imports and configures CKEditor.

**output.path**
    ``static/django_ckeditors/dist/`` - Output directory for compiled assets, integrated with Django's static file system.

Module Processing
~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   module: {
     rules: [
       {
         test: /\.svg$/,
         use: ['raw-loader']
       },
       {
         test: /\.css$/,
         use: [
           MiniCssExtractPlugin.loader,
           'css-loader',
           {
             loader: 'postcss-loader',
             options: {
               postcssOptions: styles.getPostCssConfig({
                 themeImporter: {
                   themePath: require.resolve('@ckeditor/ckeditor5-theme-lark')
                 },
                 minify: isProduction
               })
             }
           }
         ]
       }
     ]
   }

**SVG Processing**
    Uses ``raw-loader`` to import SVG files as strings, required for CKEditor icons.

**CSS Processing**
    Multi-stage pipeline: extracts CSS to separate files, processes with PostCSS, and applies CKEditor-specific theme configuration.

Plugins Configuration
~~~~~~~~~~~~~~~~~~~~~

CKEditorTranslationsPlugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

   new CKEditorTranslationsPlugin({
     language: 'en',
     additionalLanguages: 'all',
     buildAllTranslationsToSeparateFiles: true
   })

**language**
    Primary language built into the main bundle (default: ``'en'``).

**additionalLanguages**
    Additional languages to generate. Use ``'all'`` for all available languages or an array like ``['es', 'fr']`` for specific languages.

**buildAllTranslationsToSeparateFiles**
    When ``true``, creates separate translation files for each language instead of embedding in main bundle.

MiniCssExtractPlugin
^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

   new MiniCssExtractPlugin({
     filename: isProduction ? '[name].[contenthash].css' : '[name].css',
     chunkFilename: isProduction ? '[name].[contenthash].chunk.css' : '[name].chunk.css'
   })

Extracts CSS into separate files with content-based hashing in production for optimal caching.

Code Splitting
~~~~~~~~~~~~~~

.. code-block:: javascript

   optimization: {
     splitChunks: {
       chunks: 'all',
       cacheGroups: {
         ckeditor: {
           test: /[\\/]node_modules[\\/]@ckeditor[\\/]/,
           name: 'ckeditor',
           chunks: 'all',
           priority: 10
         },
         vendor: {
           test: /[\\/]node_modules[\\/](?!@ckeditor)/,
           name: 'vendor',
           chunks: 'all',
           priority: 5
         }
       }
     }
   }

**ckeditor chunk**
    Isolates all CKEditor packages into a separate bundle for better caching.

**vendor chunk**
    Groups other third-party dependencies separately from application code.

Production Optimizations
~~~~~~~~~~~~~~~~~~~~~~~~

TerserPlugin Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

   new TerserPlugin({
     terserOptions: {
       format: {
         comments: false,
         beautify: !isProduction
       },
       compress: {
         drop_console: isProduction,
         drop_debugger: isProduction,
         passes: isProduction ? 2 : 1
       },
       mangle: isProduction
     }
   })

**compress.drop_console**
    Removes ``console.log`` statements in production builds.

**compress.passes**
    Number of compression passes; more passes in production for better optimization.

**mangle**
    Shortens variable and function names in production for smaller file sizes.

Build Output
============

File Structure
--------------

Production builds generate the following file structure:

.. code-block:: text

   static/django_ckeditors/dist/
   ├── main.[hash].js           # Application code (6-7 KB)
   ├── main.[hash].css          # Application styles (< 1 KB)
   ├── ckeditor.[hash].js       # CKEditor library (~1.1 MB)
   ├── ckeditor.[hash].css      # CKEditor styles (~164 KB)
   ├── vendor.[hash].js         # Third-party dependencies (~38 KB)
   └── translations/
       ├── es.js                # Spanish translations
       ├── fr.js                # French translations
       └── ...                  # Additional language files

Performance Characteristics
---------------------------

**Total Bundle Size**
    Approximately 1.3 MB for complete CKEditor with all languages.

**Code Splitting Benefits**
    - Main application code: ~7 KB (fast initial load)
    - CKEditor library cached separately: ~1.1 MB
    - Vendor dependencies cached separately: ~38 KB

**Translation Files**
    Each language file: 15-27 KB, loaded dynamically when needed.

Environment Variables
=====================

NODE_ENV
--------

Controls build optimization level:

**development**
    - Unminified output
    - Source maps enabled
    - Console statements preserved
    - Faster build times

**production**
    - Minified and optimized output
    - No source maps
    - Console statements removed
    - Content-based file hashing for caching

Cross-Platform Compatibility
============================

The build system uses ``cross-env`` to ensure compatibility across operating systems:

.. code-block:: bash

   # Works on Windows, macOS, and Linux
   cross-env NODE_ENV=production webpack --mode production

This handles environment variable setting differences between Windows Command Prompt/PowerShell and Unix-like shells.
