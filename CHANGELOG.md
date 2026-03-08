All significant changes to the project will be recorded here.

## Unreleased

## 0.6.7 2026-03-08

### Breaking change

- fake.organism() renamed to fake.organism_english() so that fake.organism() can return a named tuple.

### Fixed

- Add missing return type hints across providers
- Fix taxonomy tests and bump minimum Python version to 3.9
- Lazy-load restriction enzyme data to avoid eager 437KB import on unrelated provider use
- Fix deprecated `[tool.poetry.dev-dependencies]` syntax and regenerate lock file

## 0.6.6 2026-03-08

- fix issue #23: `cds()` was ignoring its `length` parameter due to a hardcoded value in the loop condition
- fix issue #22: `protein_name_desc()` could raise an `IndexError` due to an off-by-one error in random index generation
- fix issue #21: mutable default argument in `_dict_leaves` and `_dict_all` caused results to accumulate across repeated calls

## 0.6.5 2025-06-27

 - fix issue #19 remove obsolete dependency
 - include python 3.13 in github actions test matrix
 - remove 3.7 and 3.8 from github actions test matrix

## 0.6.4 2024-02-10

 - include python 3.12 in github actions test matrix
 - dependency update

## 0.6.2

-  support wider range of core faker versions

## 0.6.1 2023-10-14

- Use random seed to produce reproducible random bioseq sequences

## 0.6.1 2023-10-14

- Use random seed to produce reproducible random bioseq sequences

## 0.6.0 2022-06-06

- amino acid named tuples - thank-you pokidovea

## 0.5.0 2022-06-03

### Added

- faker.enzyme for enzyme names and categories
- amino acid long names, 3 letter and 1 letter codes - thank-you pokidovea
- faker.organelle for subcellular organelles
