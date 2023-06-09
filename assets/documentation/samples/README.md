# OilMetagenomesDB - Samples Column Specifications

![check_dataset paasing](https://img.shields.io/badge/check__dataset-passing-brightgreen)

This page describes columns definitions for all sample-level lists. Icons indicate columns
that are specific to specific columns.

- 🏞: oilfield environmental metagenomes
- 🦠: crude oil metagenomes

Numeric and text fields must be filled in with `None` to indicate 'value not reported'.

All column with 'defined categories' should be validated against
`assets/enums/<column>.json`. This is to ensure data consistency. E.g., all
libraries sequenced on Illumina NextSeq 500s are listed as `NextSeq 500` (as
defined in `assets/enums/instrument_models.json`). This is to ensure data
consistency.

🤝 If you wish to a new category, please make a separate pull-request with your
modification in the corresponding `assets/enums/<column>.json` file.

Samples columns are as follows:

## project_name

:heavy_check_mark: Must correspond to a `project_name` in the corresponding sample metadata
  table

- Format: `SurnameYYYY` (YYYY in numeric format)
- Due to restrictions in regex (used for validation checks), **punctuation (e.g.
  hyphens or spaces) or characters with accents cannot be used**.
  - Use the non-accented version (e.g. ã or ä become a).
  - If the first author has multiple or hyphenated surnames, write them all
    together capitalising each surname.
- If a same author/year combination already exists, please append a single lower
  case character (`b`, `c`, `d` etc.) to the key.
  - The already existing key does not need to be updated. `b` indicates the
    'second' key added.
  - e.g. SurnameYYYY (original), SurnameYYYYb (first duplicate),
    SurnameYYYYc (second duplicate) etc.

> ⚠️ [MIxS v5](https://gensc.org/mixs/) compliant field

> ⚠️ Mandatory value

## publication_year

:heavy_check_mark: Must correspond to the `publication_year` of the publication in the
  corresponding libraries metadata table!

- YYYY format.

> ⚠️ Mandatory value

## publication_doi

:heavy_check_mark: Must correspond to the `publication_doi` of the publication in the
  corresponding libraries metadata table!

- Publication DOI.

> ⚠️ Mandatory value

## site_name

- Сorresponds to the specific location where the sample was collected
- As reported in publication
- Accents are allowed
- Missing name: `None`

## latitude

- Decimal format
- Maximum three decimals
- In WGS84 projection (coordinates taken from Google Maps is recommended, range
  90 to -90)
- Can be searched in wider literature, rough location is acceptable but use
  fewer decimals
- Missing value: `None`

## longitude

- Decimal format
- Maximum three decimals
- In WGS84 projection (coordinates taken from Google Maps is recommended, range
  180 to -180)
- Can be searched in wider literature, rough location is acceptable but use
  fewer decimals
- Missing value: `None`

## geo_loc_name

- Based on modern day definitions
- Must be based on [INDSC Country list](http://www.insdc.org/country.html)
- Missing name: `None`

> ⚠️ [MIxS v5](https://gensc.org/mixs/) compliant field

Must follow categories specified in `assets/enums/<column>.json`

> ⚠️ Mandatory value

## study_primary_focus

- What area of research was the focus of the study
- These are generalised categories such as 'ecological', or 'industrial',
  with a combination of those (in that order) also allowed.

> ⚠️ this does NOT necessarily imply that the data can only be used for
> the same purposes. This column is only to facilitate faster bibliographic
> review for equivalent dataset generation

## sequence_name

- Sediment cores only
- Identifier for sequence sample was taken from, e.g. core_3, or zone_a19
- Typically cores, or quadrant/square of excavation
- Missing value: `None`

## depth

- Depth of sample from top of sequence (m)
- If reported as a range (e.g. 130-132 m), take approximate mid-point
- Use `None` if not a sequence (e.g. from surface of an open site)

## sample_name

:heavy_check_mark: Must correspond to the `sample_name` of the publication in the corresponding
  libraries metadata table.

- Unique identifier for that sample as used in publication
  - If samples are referred to by multiple names, use the most informative

> ⚠️ Mandatory value

## feature

- Description of the object, site, or immediate environment the sample was obtained from, following [Environment
  Ontology](https://www.ebi.ac.uk/ols/ontologies/envo)
  - e.g. ocean, lake, oilfield

> ⚠️ partly [MIxS v5](https://gensc.org/mixs/) compliant field, following

Must follow categories specified in `assets/enums/<column>.json`

> ⚠️ Mandatory value

## material

- Sample type DNA was extracted from
  - e.g. water, мarine sediment, soil

> ⚠️ Partly [MIxS v5](https://gensc.org/mixs/) compliant field, i.e. term
> [UBERON](https://www.ebi.ac.uk/ols/ontologies/uberon) (anatomy) or
> [ENVO](https://www.ebi.ac.uk/ols/ontologies/envo) (everything else). If you
> can't find something close enough, please write [agni-bioinformatics-lab](https://github.com/agni-bioinformatics-lab)

Must follow categories specified in `assets/enums/<column>.json`

> ⚠️ Mandatory value

## sampling_date

- Year of sampling of (sub-)sample for DNA analysis in YYYY format
- Missing value: `None`

> ⚠️ [MIxS v5](https://gensc.org/mixs/) compliant field

## archive

:heavy_check_mark: In most cases should correspond to the `archive` of the publication in the
  corresponding libraries metadata table!

- The archive the library's data is stored on.
  - Should be an established long-term stable archive.
  - Generally set up academic institutions e.g. EBI or Universities (rather than
    companies, e.g. GitHub).
- e.g. [ENA](https://www.ebi.ac.uk/ena),
  [SRA](https://www.ncbi.nlm.nih.gov/sra).
- In some cases this will vary, for example if there IS an ERS code, however
  only consensus sequences are uploaded

Must follow categories specified in `assets/enums/<column>.json`

> ⚠️ Mandatory value

## archive_project

:heavy_check_mark: Must correspond to the `archive_project` of the publication in the
  corresponding libraries metadata table!

- A project level accession code under which all samples of a project are assigned to
- Specific examples:
  - Archive: ENA/SRA/DDBJ: should be _primary_ accession code beginning with `PRJ`. [Example](https://www.ebi.ac.uk/ena/browser/view/PRJNA438985).

- Missing value: `None`

## archive_accession

:heavy_check_mark: Must correspond to the sample `archive_accession` of the publication in the
  corresponding libraries metadata table!

- Should be a single accession ID.
- For ENA/SRA: These should be **secondary** accession IDs to keep as close to
  data as possible (e.g. SRS, ERS, not SAMEA - see below)
- If non-NCBI/ENA, use as close to sample-level as possible
  - e.g. for Dryad/Figshare, use the numeric ID after 'file_steam' in the per-file download URL
- Multiple can be separated with commas
  - e.g. when different extracts of one sample incorrectly uploaded as samples

> ⚠️ Mandatory value

<details>
  <summary>Expand to show location of ERS codes on ENA</summary>
  
  ![Location of ERS
  codes](../images/tutorials/spaam-AncientMetagenomeDir_ena_ers_location.png)
  
  Select the 'secondary_sample_accesion' and 'sample_alias' columns.

</details>
<details>
  <summary>Expand to show location of SRS codes on SRA</summary>

![Location of ERS
  codes](../images/tutorials/spaam-AncientMetagenomeDir_sra_srs_location.png)

The SRS code is to the left of the SAMEA-like code under the **sample:** field

</details>