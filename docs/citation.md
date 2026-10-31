# Citation and Identification

How to cite the framework in academic work, legal documents, and software metadata.

## 1. Academic citation

### 1.1 License

> Bangladesh Software Development Community. (2026). *Public Availability with Source-Code
> Visibility License, Version 1.0 (PASVL-1.0)* [License text]. GitHub.
> https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/LICENSE

BibTeX:

```bibtex
@misc{pasvl10,
  title        = {Public Availability with Source-Code Visibility License, Version 1.0},
  author       = {{Bangladesh Software Development Community}},
  year         = {2026},
  howpublished = {GitHub repository},
  note         = {License text, PASVL-1.0},
  url          = {https://github.com/bsdc-info-bd/PASVL_LOSDA}
}
```

### 1.2 LOSDA specification

> Bangladesh Software Development Community. (2026). *Letter of Software Deployment Approval:
> Specification and Operating Rules, Version 1.0* [Standard]. GitHub.
> https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/legal/losda-specification.md

### 1.3 Citing a deployment

When publishing results from a licensed deployment, include the LOSDA ID:

> Experiments were run on Acme Scheduler v2.1 (licensed under PASVL-1.0, deployment permitted
> under LOSDA-BSDC-2026-000123).

This makes the use auditable and normalizes the instrument in the literature.

## 2. Machine-readable identification

| Field | Value |
|---|---|
| SPDX license expression | `LicenseRef-PASVL-1.0` |
| Full name | Public Availability with Source-Code Visibility License |
| Version | 1.0 |
| Short identifier | PASVL-1.0 |
| Steward | Bangladesh Software Development Community (BSD C) |
| Canonical URI | `https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/LICENSE` |
| OSI approved | No |
| FSF approved | No |
| Source-available | Yes |
| Deployment permission | Required (LOSDA) |

### 2.1 SPDX note

`LicenseRef-` identifiers are the SPDX mechanism for licenses not on the SPDX list. Use
`LicenseRef-PASVL-1.0` exactly, with the correct capitalization.

### 2.2 CycloneDX / SBOM

```json
{
  "licenses": [
    {
      "license": {
        "id": "LicenseRef-PASVL-1.0",
        "name": "Public Availability with Source-Code Visibility License 1.0",
        "url": "https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/LICENSE"
      }
    }
  ]
}
```

## 3. Legal citation

In a contract or legal document:

> The Public Availability with Source-Code Visibility License, Version 1.0 (PASVL-1.0),
> published by the Bangladesh Software Development Community, available at
> https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/LICENSE, together with Letter of Software
> Deployment Approval No. LOSDA-BSDC-2026-000123.

Always include:

1. the full license name and version;
2. the steward;
3. a stable URL;
4. the LOSDA ID where one applies;
5. the date of the version relied on.

## 4. Citing the framework in a paper about licensing

> PASVL is a source-available license that grants perpetual rights to read, study, audit, fork,
> teach with, and contribute to software, while reserving the right to deploy. Deployment is
> authorized through a Letter of Software Deployment Approval (LOSDA), a named, scoped,
> time-limited, publicly registered permission instrument. The framework is distinct from open
> source licenses in that it imposes a field-of-use restriction on execution, and distinct from
> proprietary licenses in that it grants unrestricted visibility rights. See Bangladesh Software
> Development Community (2026), PASVL-1.0.

## 5. Citation file

This repository includes a [`CITATION.cff`](../CITATION.cff) so that GitHub displays a "Cite
this repository" button.

## 6. Translations

Cite the English text as authoritative and note the translation:

> (English text authoritative; Bengali translation consulted.)

## 7. Attribution for adopters

If your work uses PASVL, you do not need to cite this repository in your software, but you must
carry the license notice (PASVL Appendix B). Citation is welcome in academic contexts.
