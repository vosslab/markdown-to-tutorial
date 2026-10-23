# Voice restoration final build and calculation verification

Build date: 2026-10-22.

## Result

All 12 canonical bundles were rebuilt from the current restored Markdown with `--format all`. Each contains DOCX, PDF, XLSX, and `validation.json`; builds published successfully. The PDFs total **92 pages**. Per-tutorial page counts and all 60 source/artifact SHA-256 values are recorded below. A machine-readable copy is in ignored generated output at `tutorial_output/voice_restoration/final_build/manifest.json` (SHA-256: `4162f55fe5e19843fd5222686024da1df4bec675c07a3827938aafa2823ff9cb`).

The unchanged expectations file `tutorial_output/validation/tutorial_expectations.json` has SHA-256 `5bea9e0aa660cb6d8ccaa5ddcd17bdc9b628ed8c9952af7559d4218ee0af3543`. LibreOffice Calc 26.2.6.3 passed **13 scenarios and 254 formula comparisons**. The fresh machine report is `tutorial_output/voice_restoration/final_build/calc/run-b9omzwv6/report.json`. This is final-state formula evidence; it does not test intermediate workbook states, Google Sheets, or Google calculation.

The repository suite passed **1,545 tests** (exit status 0; 3.33 seconds). Full output is in `tutorial_output/voice_restoration/final_build/full_suite.log` (SHA-256: `447b5eaf9b5d8c08f7b8b4259f42ed487610f496c498db52c692f9d3bf65f54b`). The integrated run record is [voice final validation](voice_final_validation.md).

## Commands

The full suite ran with the repository bootstrap:

```sh
source source_me.sh && python3 -m pytest tests/ -q
```

The all-12 builds ran serially outside the sandbox using `source source_me.sh && python3 make_tutorial.py build tutorial_data/<name>.md --format all`. PDF conversion invokes LibreOffice, so the builds ran outside the sandbox as required.

Calculation validation used the existing expectations without regeneration:

```sh
source source_me.sh && python3 devel/validate_libreoffice.py tutorial_data/*.md \
  -e tutorial_output/validation/tutorial_expectations.json \
  -o tutorial_output/voice_restoration/final_build/calc
```

`devel/check_tutorial_calculations.py` was not used because it writes a new expectations file; the validation command above reads the existing one.

## Build diagnostics

Across the 12 `validation.json` files, the compiler recorded 14 `google-unmapped` notes, 70 `unavailable-input` warnings, 67 `range-overshoot` warnings, and 20 `formula-coverage` warnings. The Google notes reflect absent optional worksheet mappings. Range warnings come from authored practice formulas that reserve rows past the supplied seed data. Formula coverage warnings concern functions whose compatibility the offline checker does not assess: `INDEX`, `LINEST`, and `SUMPRODUCT`. Specific unavailable-reference diagnostics include Microbes 3 `E17`/`E18` and PETase `J13`; their Calc scenarios nevertheless passed. These diagnostics remain visible in each bundle's `validation.json` and in the generated manifest.

## Page counts and SHA-256 manifest

For each tutorial below, hashes are ordered source, DOCX, PDF, XLSX, and `validation.json`. Paths are relative to the repository root.

### `babies_1_z_test` - 6 PDF pages

```text
source     da64c65d64e160d9b7dc311b73afc7e28fefb38efdb45d9a34d9ed2704c1d5c1
docx       a0bedf727cc4bc06d87f1eeb4958998bf56bd80c63571d4b73ca2303778a9521
pdf        3e4f472da08a2312f1524e9bbb1d66a3a539d0041a498962538d24fa5210acc4
xlsx       ace84c1ced9984fa92094ef7601cd7ea965c0e0e976052d5ebd146989857d757
validation a867f5c3219444867f8cb5ce2b88c72780f6e08b9d476b2509032912cff277d9
```

### `babies_2_t_test` - 6 PDF pages

```text
source     446256332bb144cc1ecbd2d0202043dc980a484ceee4ed28db4d624a6f76e96d
docx       254f6faaa0651ad402691fb2c99dec9ef42d713e5226187d7934502e8a25f28f
pdf        161f234197910d866530b55d1ab77bf41665bc5584c825ffaa5324f9f4404b53
xlsx       3545c1caeac072021853a41eec2f2c747c57afefc5ddb554c74ebfd60476c89c
validation ed4170bc37f013f0371665114a57c1e9471eece8bb8952ed57a12a8de0e91812
```

### `babies_3_two_sample_t_test` - 5 PDF pages

```text
source     c58d36f92c826a7625f5e371c65bad5ab5dca25148301117d69ac1504217db5f
docx       4145f3c5303d9660c6818ff5a4765210064e20211028136434a3f5b45a889493
pdf        bec039792173033bda66c9395b280b21ed38b265b047220c7f9293d43907c20f
xlsx       891357795e23d5255c36c6c44cf39afeef8ee9a5aa34d11f010564c9bb805682
validation 0ad8f4fb581efd29eae0ac7b1ca8f32a74d8acec9785eebb0330e7e664837ff0
```

### `caffeine_1_descriptive_statistics` - 3 PDF pages

```text
source     744577401bf95d03521e45a3b32b606af3258301281b328824d09293f7c18cb2
docx       c357ee8115b880f89beda518146e47103fa9cccecb9eb01a7dc24284487d9ed5
pdf        b5284f2a26f3ff3cc8c18816931be6824c89555b30787ea1541317f62c4f3096
xlsx       f1b0baaf4ab5085e3de0e186eae00b31e44b1970745feb580e58f4ce26dfffc3
validation 06e8d2d8bc2f96eae421a9071b3ec1525f87bc433315800d1af5d9578f2bbe8c
```

### `caffeine_2_linear_regression` - 10 PDF pages

```text
source     c523d926ccca192f42317977b3e2888a4f188fbf25bdf338f9671adab413980a
docx       8b1736472399c58ad9c06a9a9a2f5a43ddb49955cf88fd71bf9cb61cce30920a
pdf        f19af82f62f4ee9f2b1c4cae5515ba8ebc6b597d0acad9085121bacec2d21c4c
xlsx       7d435fb156bc8b9dc95932a7d86a97355629dc53e671c1b36a8e86e80054ead5
validation 63532032125ee49a9fd8527c0812d5b1af86049478a9897bf07e3b3c7ec157ef
```

### `caffeine_3_quadratic_regression` - 7 PDF pages

```text
source     a8736df780e128fa08cb78b8590611b2256221ab67c043aad1ebcc93bf818983
docx       4dce56aef4d94987133fb6fbe79f422c2acd71de0a2a0ebf07a4c1ea3be64ffe
pdf        2e076c3743bec887f16278322a5079b38a6c1bfb1bc312ef5cb817abda6d3fab
xlsx       80dfe167a82526de0278d8a70e15599bf5872dca4aafce550d60f7ab40f5d599
validation a4c374a96c4eb648ab73fd1a70284e7d2b273e1dcfb598d3f3836814f870d390
```

### `microbes_1_z_test` - 9 PDF pages

```text
source     f11f071cae9b664383f4e83bdaa5838004b9e48ffd61ad758c31c7fc41f150c0
docx       8732c9b3e5f35ff0be30441ec1671f95b665bc7d1880c65588d369017fe47a60
pdf        6e301211fcf5c8d07c9846e47340ccc7b3ec7ec1cac88d0a3fd9df6d546e250f
xlsx       d24844d274c0ce3ca4a9b634f9e862b8e8ffa9b46abddb25e91e8987ebb31467
validation b7fa949160643a8740ff38951e238b1638f1c2a8a89776b48d9355c28bff5129
```

### `microbes_2_t_test` - 9 PDF pages

```text
source     7e75603806f07ce2762833e1778774ea94fcd5775d02caee7fd504e7160b3d3f
docx       789d4a351c32de7bf95d79a10f99834d5113a0661852ccf414630a3bb971a8f8
pdf        c207bcb850871022d9960e7bd8031ca79743cb2ce053d28e33ea6f17b675ed5e
xlsx       7d4e357b664d1cf08250095c216850a5c931340ef09b732915975f56abbe4722
validation 7e4a5aa0c4695dd50cdaa6a0513c6d72c094e943398a76e09a3bbc8111102f61
```

### `microbes_3_two_sample_t_test` - 12 PDF pages

```text
source     86ca0cce468641ada1dce58f22239b728e46921d96b75a753be46bcbf41e49a8
docx       e2808fb57b2a7efa3e19efcf8ab0c2d0d9fead44497c6bbb8b3c7df28d46d2af
pdf        3499531ea4154667b605743d02bc8d2c1afb72e45c4c34514288a2125dceeeb5
xlsx       8701f9eed299642af87a4d085e6946986a0c77dac406eeff4282748b6b064218
validation 18ffa71ba2cc7899a9e606efd0d57db68abe5aaba9b37b56132d23aae2f0a07c
```

### `microbes_4_f_test` - 10 PDF pages

```text
source     34c3a6e2e8d608b0dd84dd78b903cdbaac68f07f1bfcd1b94cd6ddf60bf89269
docx       fb11495295adb0ec57695dcef2e56dfc016959dad6919a1b661b253a27250276
pdf        2e9447634ece3ecba80536adf2b2de1a1336b91e7f665a124f3ba9b53f3eccd0
xlsx       b2912e4f4200d1a1a6f03fc586a474dc9c75985450da84ffa410a9bd059f81d4
validation 64ab2f79ea03ecfd25ebb0572ae66a61f385520c982738d0ce59c7175071178c
```

### `microbes_5_anova` - 9 PDF pages

```text
source     9e5004a388494c8e7e28e4e9e6d2557466df9de1b90f4338caa2d4eb300fa512
docx       4fadabada44ba9bb2733688f686ece04afef0219969786f47febb14474b2a97e
pdf        158752c5ce6bf1a870bb932a84a30ae897c90dfa906267b1f1c84a143a001597
xlsx       3d39b05270116ecf27aa2dc4fe4a53d29256d64c0014d8c1766f1566f95080e3
validation 74a74135f0633cf24a7c73720fc85be53b9b9fd8f9d4ec57ff400ad2645093b6
```

### `petase_1_linear_regression` - 6 PDF pages

```text
source     1831e9d7961f770884bb9debc83d24f33ab9f33bc0d218cb5a60eabce6825469
docx       d3542c047f0757f9cd22febbc67302e4c901d49788cee2a2efdd7eebcdfd4200
pdf        5002470fd54cda0e2d0ec68f8548aff8ca4bb76dfa5816c8e593b6d3f84fb177
xlsx       46eceaa2abcc919820aa523c5a3d1c84e625b1702bfe31cb7b3e35b12fffba95
validation ccf589dab1cd22d5ae19e500e70eecac24d4c71dd3b08288e5eaaa81b1bc4156
```
