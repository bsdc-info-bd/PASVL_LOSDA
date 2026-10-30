# Registry Privacy Policy

**Version:** 1.0 · **Applies to:** the LOSDA Registry, the Enforcement Register, and the
licensing process operated by the Steward.

The Registry publishes who may deploy what. That purpose requires some transparency. It does
not require publishing people's lives. This policy sets the minimum data we collect, the
maximum we publish, and the way data subjects can exercise their rights.

## 1. Data we collect

| Category | Examples | Source | Why |
|---|---|---|---|
| Issuer identity | Legal name, issuer code, signing key fingerprint | Author | Verify the instrument's origin |
| Licensee identity | Legal name, registration number, country, contact person | Applicant | Identify who is licensed |
| Deployment data | Class, territory, scale band, product name | Applicant | Scope the permission |
| Verification data | Record hash, status history, timestamps | Registry | Prevent forgery; immutable audit trail |
| Enforcement data | NNCs, decisions, appeal outcomes | Enforcement process | Fair process and public accountability |
| Correspondence | Emails and letters relating to an application | Applicant, Issuer | Process the application and keep records |

We do not collect: national identity numbers, copies of passports, bank details (except where
a fee requires an invoice record held separately), health data, family data, or precise
location data.

## 2. What we publish

| Published | Not published |
|---|---|
| LOSDA ID | Personal email addresses |
| Work name and repository URL | Negotiated fee amounts |
| Class | Personal identity numbers |
| Licensee display name, or an anonymised identifier on request | Bank and payment details |
| Country | Confidential annex content |
| Effective date, term, territory, scale band | Security contact details |
| Status and status history | Investigation files before Stage 3 |
| Record hash | Individual staff names of the licensee |

## 3. Lawful basis

Where the GDPR or comparable law applies, the Steward relies on:

- **Contract** — processing necessary to issue and administer a LOSDA (Article 6(1)(b) GDPR);
- **Legal obligation** — record-keeping, sanctions screening, and tax records (6(1)(c));
- **Legitimate interests** — preventing fraud and maintaining the integrity of the Registry
  (6(1)(f)), balanced against data-subject rights;
- **Consent** — where we publish a display name that is a natural person's name, and for
  optional communications (6(1)(a)). Consent may be withdrawn; withdrawal does not affect the
  validity of the LOSDA, which can use an anonymised identifier instead.

## 4. Visibility and automated search

The Registry is a public document. Data published in it may be indexed by search engines and
copied by others. The Steward cannot recall copies made by third parties. This is why
minimisation matters at the point of collection.

**Anonymised listing.** A sole trader, a private individual, or a licensee in a vulnerable
position may request that its public listing show an anonymised identifier (for example,
`L-2026-000123 (anonymised)`) instead of a name. The request is granted where:

1. the licensee is a natural person or the disclosure would reveal a home address or a
   personal identity;
2. law enforcement or a legal process does not require publication;
3. the transparency interests of the framework are served by publishing the existence,
   class, Work, term, and status without the name.

The Registry Custodian decides within 15 business days and records the decision and reason
(without the personal data).

## 5. Retention

| Record | Retention |
|---|---|
| Registry entries and status history | Permanent (append-only) |
| Signed LOSDA letters | Permanent |
| Applications, including refusals | 5 years |
| Due-diligence material | 5 years after the end of the term |
| Enforcement files | 7 years, or until the limitation period for related litigation expires |
| Correspondence | 5 years |
| Anonymisation requests | 5 years after the request is decided |
| Keys and key histories | Permanent, annotated with revocation dates |

## 6. Security

The Steward must maintain: access control on the Registry repository; signed commits for
Registry changes; branch protection requiring review; encrypted storage for confidential
material; periodic backups at a second location; an incident response plan; and annual access
reviews. A personal-data breach is notified to affected persons and to the competent authority
without undue delay.

## 7. International transfers

The Registry is operated in Bangladesh and published globally. Where personal data is
transferred from the EEA, UK, or another jurisdiction with transfer restrictions, the Steward
relies on appropriate safeguards, including standard contractual clauses, or on an applicable
derogation. Confidential data is stored in the EEA where the data subject is in the EEA, where
practicable.

## 8. Data-subject rights

Data subjects may request:

- **Access** to the personal data held about them;
- **Rectification** of inaccurate data, including correcting a legal name in a Registry entry
  by an append-only correction referencing the original;
- **Erasure**, only to the extent compatible with the append-only integrity of the Registry
  and with legal-record obligations — in practice, erasure usually takes the form of
  anonymisation rather than deletion;
- **Restriction** of processing while a dispute is resolved;
- **Portability** of data the subject provided;
- **Objection** to processing based on legitimate interests;
- **Withdrawal of consent** where consent is the basis.

Requests go to the Registry Custodian. Response target: 30 days, extendable once by a further
60 days for complex requests with notice.

## 9. Children

The framework is not directed to children. A LOSDA is not issued to a person under 18 without
a guardian's written consent and, where the deployment is commercial, a registered entity.

## 10. Automated decision-making

The Registry does not use fully automated decision-making with legal effect. Sanctions screening
may be automated as a filter, but every refusal or suspension is reviewed by a human being.
Suspensions and revocations are always reviewed by a second human reviewer.

## 11. Cookies and analytics

The Registry is a static, publicly readable document. It sets no cookies. Any future
verification web service must publish a cookie notice and must not use non-essential cookies
without consent.

## 12. Contact and complaints

- Registry Custodian: address published in [`../GOVERNANCE.md`](../GOVERNANCE.md)
- Complaints: [`../templates/APPEAL-FORM.md`](../templates/APPEAL-FORM.md) may be used for a
  data-protection appeal
- Supervisory authority: the data subject may complain to the authority of their habitual
  residence, place of work, or place of the alleged infringement

## 13. Changes

Material changes require a 30-day public comment period and a `CHANGELOG.md` entry. Changes
never apply retroactively to data already collected for a closed matter, except where required
by law.
