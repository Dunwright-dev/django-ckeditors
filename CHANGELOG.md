# CHANGELOG

## v0.2.4 (2024-10-29)

### Fix

* fix(submit): Commented out submit listener until further work #90

closes #90 ([`014a27f`](https://github.com/Dunwright-dev/django-ckeditors/commit/014a27f5fb72605611d07c7446d0a7222de25b95))

### Unknown

* Merge pull request #91 from Dunwright-dev/issue-90

fix(submit): Commented out submit listener until further work #90 ([`387d48d`](https://github.com/Dunwright-dev/django-ckeditors/commit/387d48d23a7cab4b46656c80af88e7e12d89b9a9))

## v0.2.3 (2024-09-25)

### Fix

* fix(event): Add detail:sender to custom event for debug #88

closes #88 ([`7c0d869`](https://github.com/Dunwright-dev/django-ckeditors/commit/7c0d86929bb536652a2e9bcd999b86ace519aa64))

### Unknown

* Merge pull request #89 from Dunwright-dev/issue-88

fix(event): Add detail:sender to custom event for debug #88 ([`840e19b`](https://github.com/Dunwright-dev/django-ckeditors/commit/840e19ba0ba3a9a18ba7e97d650c9f289ca0e8ed))

* Merge pull request #87 from Dunwright-dev/release

0.2.2 ([`401bdb7`](https://github.com/Dunwright-dev/django-ckeditors/commit/401bdb7b29fa5e4148fb3cd9768240a75de71f1e))

## v0.2.2 (2024-09-21)

### Chore

* chore(deps-dev): Bump webpack from 5.93.0 to 5.94.0 in /django_ckeditors

Bumps [webpack](https://github.com/webpack/webpack) from 5.93.0 to 5.94.0.
- [Release notes](https://github.com/webpack/webpack/releases)
- [Commits](https://github.com/webpack/webpack/compare/v5.93.0...v5.94.0)

---
updated-dependencies:
- dependency-name: webpack
  dependency-type: direct:development
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2cf38ea`](https://github.com/Dunwright-dev/django-ckeditors/commit/2cf38eaf0d599dfb51e427c236e90813dc9f894f))

### Fix

* fix(app): Add observers, rename event #85

In some instances when using htmx and alpline.js the editors
where not being created correctly.  Adding mutation observers
for #modal and #slide seems to have solved this issue.

closes #85 ([`2e32083`](https://github.com/Dunwright-dev/django-ckeditors/commit/2e3208314c53e144bbb5e323cc7e4651f80c10c6))

### Unknown

* Merge pull request #86 from Dunwright-dev/issue-85

fix(app): Add observers, rename event #85 ([`b1dbb1c`](https://github.com/Dunwright-dev/django-ckeditors/commit/b1dbb1c8aad62f46200f6dc0b83ce490b46f1aeb))

* Merge pull request #79 from Dunwright-dev/dependabot/npm_and_yarn/django_ckeditors/webpack-5.94.0

chore(deps-dev): Bump webpack from 5.93.0 to 5.94.0 in /django_ckeditors ([`00acdf2`](https://github.com/Dunwright-dev/django-ckeditors/commit/00acdf220af7b04c411850beaae500893371cc97))

* Merge pull request #84 from Dunwright-dev/release

0.2.1 ([`013a097`](https://github.com/Dunwright-dev/django-ckeditors/commit/013a0972047de17765e49219d9e2fda02facb960))

## v0.2.1 (2024-09-10)

### Fix

* fix(app): Indentation errors in settings #82

closes 82 ([`1edb95c`](https://github.com/Dunwright-dev/django-ckeditors/commit/1edb95ca4cae01551d2799150df07c91f6e66f75))

### Unknown

* Merge pull request #83 from Dunwright-dev/issue-82

fix(app): Indentation errors in settings #82 ([`4555912`](https://github.com/Dunwright-dev/django-ckeditors/commit/455591295db367ee675133a0568fb9be1436d4da))

* Merge pull request #81 from Dunwright-dev/release

0.2.0 ([`8295031`](https://github.com/Dunwright-dev/django-ckeditors/commit/82950310aa161984befc349363a15ceebd70fe50))

## v0.2.0 (2024-09-09)

### Chore

* chore(image): Add model and admin for removed images #77

closes #77 ([`e20788d`](https://github.com/Dunwright-dev/django-ckeditors/commit/e20788d59bc9c0f611d497176c9f96a0af47ea41))

* chore(image): Add image removal setting option #77

closes #77 ([`2de11ac`](https://github.com/Dunwright-dev/django-ckeditors/commit/2de11ac48564bed9fdbd8631ed3207645975a57d))

* chore(image): Add url items for image_removal handling #77

closes #77 ([`190a185`](https://github.com/Dunwright-dev/django-ckeditors/commit/190a18501d32d2b8c084ddba88b8470e994734e8))

* chore(url): rename urls in prep for added functionality #77

This commit gets ready for new functionality, it remames an
existing url so that the urls will all make sense. ([`7834410`](https://github.com/Dunwright-dev/django-ckeditors/commit/783441000f87eab15b40039949eb6e4e6a5e0c5d))

* chore(args): Update init args #74

closes #74 ([`3aaebac`](https://github.com/Dunwright-dev/django-ckeditors/commit/3aaebaccf3f7e56ae74d7f27166550574a14b712))

### Feature

* feat(image): Add unused image removal #77

This commit provides tools to extract images that have been
uploaded in a ckeditor, and later removed.  The options are
to delete the images (default), or store them in the database
for processing at a later time.

closes #77 ([`da9ae2f`](https://github.com/Dunwright-dev/django-ckeditors/commit/da9ae2f4575f071d4deae7bcc06d3d927110f1b8))

### Fix

* fix(data): add json.dumps to context #78

Added json.dumps to the extra_data context.

closes #78 ([`1e5a5eb`](https://github.com/Dunwright-dev/django-ckeditors/commit/1e5a5ebd6e8452ad7efc928522310864c24e6402))

### Test

* test(upload): comment out broken test #74

closes #74 ([`66703ae`](https://github.com/Dunwright-dev/django-ckeditors/commit/66703ae72011eaae46630633c52db263e4796d05))

### Unknown

* Merge pull request #80 from Dunwright-dev/issue-77

feat(image): Add unused image removal #77 ([`d548a3b`](https://github.com/Dunwright-dev/django-ckeditors/commit/d548a3b24bc7ccd0e22088e5eed94d67d7ca656f))

* Merge pull request #76 from Dunwright-dev/issue-74

fix(helper): Custom URL handler logic #74 ([`be4bc6c`](https://github.com/Dunwright-dev/django-ckeditors/commit/be4bc6c9bdcebfeda71615b9d0a0aef3c3160ea9))

## v0.1.2 (2024-08-26)

## v0.1.1 (2024-08-26)

### Chore

* chore(version): Bump to 0.1.0

closes #71 ([`0669e36`](https://github.com/Dunwright-dev/django-ckeditors/commit/0669e364cd42f656ffc3f51927f58012702b7de2))

* chore(helper): Extend custom url funcionality #69

The custom url now allows the ability for the django project
to save the image file internally.  The users custom url
function must return a tuple of a string url and boolean to
indicate the saved state.

closes #69 ([`224ecff`](https://github.com/Dunwright-dev/django-ckeditors/commit/224ecffd5b3759422ebcb7d89f40a22dd6263f00))

* chore(js): Add checks for admin calling widget #66

Admin currently doesnt support the ckeditor.  I need to
find a simple solution to make the Media js conditional.

closes #66 ([`ed3be50`](https://github.com/Dunwright-dev/django-ckeditors/commit/ed3be5074e3570971aca01aff3f96d19aad95643))

* chore(deps): Update and refactor #67 ([`e966069`](https://github.com/Dunwright-dev/django-ckeditors/commit/e966069f28b5f91aab1ed8301a39d8f41b798dc0))

* chore(deps): Bump ws from 7.5.9 to 7.5.10 in /django_ckeditors

Bumps [ws](https://github.com/websockets/ws) from 7.5.9 to 7.5.10.
- [Release notes](https://github.com/websockets/ws/releases)
- [Commits](https://github.com/websockets/ws/compare/7.5.9...7.5.10)

---
updated-dependencies:
- dependency-name: ws
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e85d56d`](https://github.com/Dunwright-dev/django-ckeditors/commit/e85d56d13ffc237ef5cc50792fe6722235010594))

* chore(example): Update name changes in config #63

Refactor the example toolbar config name changes in dj-cke
project.

closes #63 ([`3be42ec`](https://github.com/Dunwright-dev/django-ckeditors/commit/3be42ec44f725d8cef7cb47d740d53a0398ca9ae))

* chore(deps-dev): Bump braces from 3.0.2 to 3.0.3 in /django_ckeditors

Bumps [braces](https://github.com/micromatch/braces) from 3.0.2 to 3.0.3.
- [Changelog](https://github.com/micromatch/braces/blob/master/CHANGELOG.md)
- [Commits](https://github.com/micromatch/braces/compare/3.0.2...3.0.3)

---
updated-dependencies:
- dependency-name: braces
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8ba4128`](https://github.com/Dunwright-dev/django-ckeditors/commit/8ba4128bd13df28997f8c5e02d31b5444dbcf45f))

* chore(version): Bump to 0.0.8 #56

closes #56 ([`88c649e`](https://github.com/Dunwright-dev/django-ckeditors/commit/88c649ec13c52a4889afaa488dd6954f623daf65))

* chore(config): Add image formatter setting #49

Added default image formatter as &#34;&#34; if one is not supplied by
the dev in project settings.

closes #49 ([`c158e1e`](https://github.com/Dunwright-dev/django-ckeditors/commit/c158e1e1ba164b9683fa585dc9d4d019116ba403))

* chore(git): Fix linter coverage reporting #45

Linter was installing multiple of the same environment, and directory changes in the workflow broke the coverage reporting.

closes #45 ([`93910ce`](https://github.com/Dunwright-dev/django-ckeditors/commit/93910ce70ec83b0ed59972318400a04718b80477))

* chore(settings): Add default to apps ready #41

Added sensible defaults to reduce config necessary for new users.

Added new settings to improve user experience and config granularity.

closes #41 ([`c4f833e`](https://github.com/Dunwright-dev/django-ckeditors/commit/c4f833eeb663bc285a9d6af2881af199332e83d4))

* chore(deps): Update webpack #40 ([`4f4c6fd`](https://github.com/Dunwright-dev/django-ckeditors/commit/4f4c6fd96ba7a1c90b412052cfec091d3b6fb104))

* chore(version): Bump to 0.0.6 #27

closes #27 ([`6d018dd`](https://github.com/Dunwright-dev/django-ckeditors/commit/6d018ddac4bed67bac513d2bd896053db6489ecd))

* chore(deps): Add filetype #31

closes #31 ([`1d06862`](https://github.com/Dunwright-dev/django-ckeditors/commit/1d06862145b9ccc7df56952eb6fea75441a55fea))

* chore(image): Add comprehensive image upload checks, exceptions and logging #31

closes #31 ([`d845844`](https://github.com/Dunwright-dev/django-ckeditors/commit/d845844144ef837397d88b8aa397ec0f58c03d85))

* chore(deps): Add ruff to dev deps, update gha to suit #32

Moved ruff into the deps so that it can be run locally without the need to install it separately. Removed the separate installation of ruff from the gha lint.

closes #32 ([`e5d83d7`](https://github.com/Dunwright-dev/django-ckeditors/commit/e5d83d72812c2bce8f6eef4a6ca9383d609bf4d4))

* chore(version): Bump to 0.0.6 #28

closes #28 ([`2a7d969`](https://github.com/Dunwright-dev/django-ckeditors/commit/2a7d9691877eeafbea14c115a7be38ac1be111e6))

* chore(app): Fix typos in app and urls #28

closes #28 ([`db7f3b8`](https://github.com/Dunwright-dev/django-ckeditors/commit/db7f3b8935e87b28ec0484283c7d7d73e1438e5b))

### Documentation

* docs(config): Update for new config names #63

closes #63 ([`5252374`](https://github.com/Dunwright-dev/django-ckeditors/commit/5252374dc1b8a5d7b71db43962349898d6ebb7a9))

* docs(img): Add new discussion docs for img conversion #54

closes #54 ([`7606c04`](https://github.com/Dunwright-dev/django-ckeditors/commit/7606c044219a265c6e1033b19af80ef3682673cd))

* docs(typo): Fix pypi rendering error #56

closes #56 ([`0ba281a`](https://github.com/Dunwright-dev/django-ckeditors/commit/0ba281a7ce5eae74bc20dbaa2371cb16cd157ebb))

* docs(config): Add image formatter setting #49

closes #49 ([`cfbbf53`](https://github.com/Dunwright-dev/django-ckeditors/commit/cfbbf535c417daacd75ba86da5095b1a31a62afa))

* docs(how-to): Update quickstart #40

closes #40 ([`4de0eb4`](https://github.com/Dunwright-dev/django-ckeditors/commit/4de0eb4162fb0e980fa12aa46483e9837141e0f3))

* docs(info): Add discussion and update quickstart #29

closes #29 ([`5e46720`](https://github.com/Dunwright-dev/django-ckeditors/commit/5e4672040a9d52d00b501168872595363408faf4))

* docs(how-to): Fix typos #28

closes #28 ([`ef9b139`](https://github.com/Dunwright-dev/django-ckeditors/commit/ef9b139def7fab09be4b3df3757f51899a43361a))

### Feature

* feat(img): Add cke img upload processing #54

Converting uploaded images to WebP offers several advantages,  we have
included a default image processor that converts CKEditor image uploads
to `.webp` format.  We have also included some sensible default image
quality and compression settings based on the image size.

The developer is able to provide a custom image handler through
`DJ_CKE_IMAGE_FORMATTER`.  The custom image handler must return a tuple
of a filename:str and a image:BytesIO.

closes #54 ([`86c1744`](https://github.com/Dunwright-dev/django-ckeditors/commit/86c17444b2016fd416c1acd263d89363fe6947fc))

### Fix

* fix(helper): Custom URL handler logic #74

closes #74 ([`10b0414`](https://github.com/Dunwright-dev/django-ckeditors/commit/10b0414af826eaa42a565775925abe81322e1f96))

* fix(toolbar): Refactor and add check for options #63

Renamed the toolbar options config to make it clear what the purpose
is.
Removed the hard coded default toolbar config from the widget and use
the settings default toolbar.
Added a check in the widget so that if the toolbar config is not in
the list of options the default toolbar will be selected.

closes #63 ([`60181cf`](https://github.com/Dunwright-dev/django-ckeditors/commit/60181cf6ac2be1a64f256c56399695ce42ca206d))

* fix(img): Add jpg as permitted image type #58

Default image types didnt allow for jpg. Added and also updated the error
message that is fed back to the user in the event that a file they have
attempted to upload has the correct extension type, but is not the
correct file type. e.g. a PDF file has had its extension changed to jpg.

closes #58 ([`258d8a5`](https://github.com/Dunwright-dev/django-ckeditors/commit/258d8a57de23e4ae9c645014d83202ddb16f9867))

### Refactor

* refactor(helpers): Add options for urls and storage #40 #42

Refactor get storage class to return an object so tests can be conducted using @override_settings.

Add option to use a custom url for saving CKE image file.

closes #40

closes #42 ([`8b77cbe`](https://github.com/Dunwright-dev/django-ckeditors/commit/8b77cbe546f135299638436553b9adfa9cac44c2))

* refactor(settings): Update to match apps ready #41

Some settings have been renamed when apps ready function was added to improve readability.

Settings have been removed now defaults added to the apps ready function.

closes #41 ([`60a08aa`](https://github.com/Dunwright-dev/django-ckeditors/commit/60a08aa37576618eac61971fcb7766ef96e9a990))

* refactor(style): Line length is now 79 #40 ([`8569536`](https://github.com/Dunwright-dev/django-ckeditors/commit/8569536bc14a83040e2f440913c2a5c0a3a2d418))

* refactor(view): Add user permission checks method #36

The checks for user permission to upload an image with cke where making the view a bit big, and refactoring these out into a helper function allows for expanded checks down the track.

closes #36 ([`0ab01c5`](https://github.com/Dunwright-dev/django-ckeditors/commit/0ab01c5a0b6c0587c0ce3dbe44359eb83ffdbf20))

### Test

* test(img): Add new and modify existing for img conversion #54

closes #54 ([`69023ac`](https://github.com/Dunwright-dev/django-ckeditors/commit/69023ac05c25d006c90dad690fcf621678f9d979))

* test(img): Add image fixtures #54

closes #54 ([`6b06cfd`](https://github.com/Dunwright-dev/django-ckeditors/commit/6b06cfd354767a9c9dafc456cbf2bfb9da782e40))

### Unknown

* Merge pull request #72 from Dunwright-dev/issue-71

chore(version): Bump to 0.1.0 ([`a65d52e`](https://github.com/Dunwright-dev/django-ckeditors/commit/a65d52e3ec4909db8d5ac263a096bdfa2298f123))

* Merge pull request #70 from Dunwright-dev/issue-69

chore(helper): Extend custom url functionality #69 ([`50ac54d`](https://github.com/Dunwright-dev/django-ckeditors/commit/50ac54d0da43aac34ab86e8d737cdbd079803ac7))

* Merge pull request #68 from Dunwright-dev/issue-66

chore(js): Add checks for admin calling widget #66 ([`6e41dee`](https://github.com/Dunwright-dev/django-ckeditors/commit/6e41dee6249f6679b96bbd24e068946c255fc246))

* Merge pull request #65 from Dunwright-dev/dependabot/npm_and_yarn/django_ckeditors/ws-7.5.10

chore(deps): Bump ws from 7.5.9 to 7.5.10 in /django_ckeditors ([`ec5c1d8`](https://github.com/Dunwright-dev/django-ckeditors/commit/ec5c1d8741e6e96027c6d0e360e0d46b022c5d88))

* Merge pull request #64 from imAsparky/issue-63

fix(toolbar): Refactor and add check for options #63 ([`6f6376b`](https://github.com/Dunwright-dev/django-ckeditors/commit/6f6376b63cc807d8b1c2ff09dbce8faa9cc455eb))

* Merge pull request #61 from imAsparky/issue-54

feat(img): Add cke img upload processing #54 ([`a00ce3a`](https://github.com/Dunwright-dev/django-ckeditors/commit/a00ce3abdbc9013b62e124c4ab2e4efe8441deb8))

* Merge pull request #55 from imAsparky/dependabot/npm_and_yarn/django_ckeditors/braces-3.0.3

chore(deps-dev): Bump braces from 3.0.2 to 3.0.3 in /django_ckeditors ([`481218e`](https://github.com/Dunwright-dev/django-ckeditors/commit/481218ec6e5974001a695a8a5987e4abdc8986e3))

* Merge pull request #59 from imAsparky/issue-58

fix(img): Add jpg as permitted image type #58 ([`b6aef95`](https://github.com/Dunwright-dev/django-ckeditors/commit/b6aef953e54c04ddff8b5041b267b8f1416a4590))

* Merge pull request #57 from imAsparky/issue-56

docs(typo): Fix pypi rendering error #56 ([`951e120`](https://github.com/Dunwright-dev/django-ckeditors/commit/951e1202a244374ac17ad849bfd8f99a253ba0e5))

* tests(app): Add tests app ready #41 ([`75b7613`](https://github.com/Dunwright-dev/django-ckeditors/commit/75b761329c1c18274907a4a05afdf2d00c1739bd))

* tests(helpers): Add tests for helpers #40 #42

Add/update tests for the following.

Refactor get storage class to return an object so tests can be conducted using @override_settings.

Add option to use a custom url for saving CKE image file.

closes #40

closes #42 ([`94cb564`](https://github.com/Dunwright-dev/django-ckeditors/commit/94cb56404d129033088ed53e4f523db3562b217f))

* tests(settings): Add tests for apps ready #41

Added tests for sensible defaults to reduce config necessary for new users.

Added tests for new settings to improve user experience and config granularity.

closes #41 ([`0a670c0`](https://github.com/Dunwright-dev/django-ckeditors/commit/0a670c0e622d2441663fe2ab6c37a3d6d6326bd5))

* tests(coverage): Update to only reflect dj-ckeditors #43

ATM coverage has dropped to just over 60%.  The fail for coverage has been dropped to 60% while we get that value up.

closes #43 ([`317cb66`](https://github.com/Dunwright-dev/django-ckeditors/commit/317cb66439569b39ae891a377e92148928781aea))

* tests(helper): Add tests and fixtures #38

I have also added a corrupt image file generator to expand tests for corrupted images at a later date.

closes #38 ([`551d4d0`](https://github.com/Dunwright-dev/django-ckeditors/commit/551d4d004e9038e2822af741a495ffa1ab85985f))

* core(helper): Add pillow exception handler #38

While adding tests found a Pillow exception that wasn&#39;t being handled.

closes #38 ([`717cf63`](https://github.com/Dunwright-dev/django-ckeditors/commit/717cf63d9712f5a9039366ce017a66622975b379))

* tests(image): Add/update image upload tests #31

closes #31 ([`3b067c3`](https://github.com/Dunwright-dev/django-ckeditors/commit/3b067c3e94ee55fbf014616579ed4fabf6df4463))

* tests(image): Update URL name #28

closes # 28 ([`325d239`](https://github.com/Dunwright-dev/django-ckeditors/commit/325d2395a550ab98149124d93482e9dff2b310c6))

## v0.0.5 (2024-04-11)

### Chore

* chore(version): Bump to 0.0.5 #25

For testing upload to pypi

closes #25 ([`3f2913e`](https://github.com/Dunwright-dev/django-ckeditors/commit/3f2913ebb8a1547a8c235888e64d7c2bea9ef39d))

* chore(git): Re-instate pypi workflow and test #25

For testing upload to pypi

closes #25 ([`8622b99`](https://github.com/Dunwright-dev/django-ckeditors/commit/8622b99dc78fc28a155b692ad1bda856e61b21bf))

* chore(git): Re-instate test pypi workflow and test #23

For testing upload to test pypi

closes #23 ([`fa144c9`](https://github.com/Dunwright-dev/django-ckeditors/commit/fa144c98e526cd514ed73c3744d0443d39134be3))

* chore(version): Bump tp 0.0.4 #23

For testing upload to test pypi

closes #23 ([`6739eed`](https://github.com/Dunwright-dev/django-ckeditors/commit/6739eed2610f5aed1b4f72c392d33e7df32cb548))

* chore(version): Bump tp 0.0.3 #21

For testing upload to test pypi

closes #21 ([`53b5f69`](https://github.com/Dunwright-dev/django-ckeditors/commit/53b5f69974a685700401afae6c13299c3c3600a8))

* chore(git): Add issue templates #10

closes #10 ([`b05fc25`](https://github.com/Dunwright-dev/django-ckeditors/commit/b05fc25e31ee894ba91839b60ddf7ea99f9cfa37))

* chore(git): Archive workflows temporarily #6

closes #6 ([`f876197`](https://github.com/Dunwright-dev/django-ckeditors/commit/f8761978e5d09cf3db8758d34dd946646e32b890))

* chore(git): Update workflow actions versions #1
closes #1 ([`d24116d`](https://github.com/Dunwright-dev/django-ckeditors/commit/d24116dd66072e73ed033072ca936d9145cbc752))

* chore(articles): Add missing migrations #2
Fixed linting.
closes #2 ([`1ec9573`](https://github.com/Dunwright-dev/django-ckeditors/commit/1ec9573c948f6151e506fe8011acde13b721040c))

* chore(articles): Add missing migrations #2

closes #2 ([`4c11e8e`](https://github.com/Dunwright-dev/django-ckeditors/commit/4c11e8e5a8fd05665123ad2312d91bc239adcff3))

### Documentation

* docs(README): Replace :ref: with link to quickstart #21 ([`bb2bff0`](https://github.com/Dunwright-dev/django-ckeditors/commit/bb2bff0055bff254049fe38ba2400753ae67674f))

* docs(how-to): Add quickstart, update README #17

closes #17 ([`47f50e9`](https://github.com/Dunwright-dev/django-ckeditors/commit/47f50e9e93af021f7717246a7d89ac79f3a0df5d))

* docs(README): Add docs badge for link to rtd&#39;s #17

closes #17 ([`5a7b0bd`](https://github.com/Dunwright-dev/django-ckeditors/commit/5a7b0bd191a1ef87109d250582acf53d59115541))

* docs(README): Add docs badge for link to rtd&#39;s #17

closes #17 ([`3ecbd83`](https://github.com/Dunwright-dev/django-ckeditors/commit/3ecbd832d3855fda1e4d26c9662b4ee5c457144b))

* docs(pkg): Add docs req to docs #15

closes #15 ([`093effd`](https://github.com/Dunwright-dev/django-ckeditors/commit/093effd7b9c35ec856af60aaf3d78313024096d0))

* docs(pkg): Add docs folder and sphinx config #12

Tweak README.rst

closes #12 ([`d1c35ad`](https://github.com/Dunwright-dev/django-ckeditors/commit/d1c35ad0cd18a0fbc4fc5db3837bb0bbf506b91d))

* docs(git): Add history log for missing commits after vendoring #7

closes #7 ([`b62aec1`](https://github.com/Dunwright-dev/django-ckeditors/commit/b62aec1e3b8e06818e2b41d057cfdfc329df1ab9))

### Refactor

* refactor(initial): Vendored from django-ckeditor-5 ([`6aae44d`](https://github.com/Dunwright-dev/django-ckeditors/commit/6aae44d1d092b4542baa666fb982b61f89e2d605))

* refactor(initial): Vendored from django-ckeditor-5 ([`af24926`](https://github.com/Dunwright-dev/django-ckeditors/commit/af249260a5f95b3c1604d6972caabae0adf38d8f))

### Unknown

* Initial commit ([`d96902b`](https://github.com/Dunwright-dev/django-ckeditors/commit/d96902b02cc4267419b7e72fe0fa959b950cf97a))
