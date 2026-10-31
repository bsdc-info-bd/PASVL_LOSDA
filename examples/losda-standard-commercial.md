# Example LOSDA — Class S (Standard Commercial)

> This is a worked example. Names, identifiers, and hashes are fictitious. It shows what a
> complete, well-drafted Class S permission looks like.

---

# LETTER OF SOFTWARE DEPLOYMENT APPROVAL

**LOSDA ID:** `LOSDA-ACMELAB-2026-000417`
**Instrument version:** LOSDA-1.0
**License version:** PASVL-1.0
**Status on issue:** ACTIVE
**Verification URL:** `https://github.com/bsdc-info-bd/PASVL_LOSDA/blob/main/registry/losda-registry.json#LOSDA-ACMELAB-2026-000417`

---

## 1. Parties

**Issuer**

| Field | Value |
|---|---|
| Legal name | Acme Labs Ltd |
| Trading name | Acme Labs |
| Issuer code | ACMELAB |
| Country | Bangladesh |
| Identity reference | Company registration C-123456/2021 |
| Capacity to issue | Author |
| Contact | licensing@acmelabs.example |
| Signatory | R. Chowdhury, Director |

**Licensee**

| Field | Value |
|---|---|
| Legal name | Northwind Analytics Ltd |
| Registration number | UK 09876543 |
| Country | United Kingdom |
| Public display name | Northwind Analytics |
| Registry listing preference | Legal name |
| Authorized contact | legal@northwind.example |
| Compliance officer | J. Patel, Head of Engineering |
| Affiliates covered | Northwind Analytics GmbH (Germany) |

---

## 2. The Licensed Work

| Field | Value |
|---|---|
| Work name | Acme Scheduler |
| Repository URL | https://github.com/acmelabs/scheduler |
| Commit / release | v3.2.0 (tag `v3.2.0`, commit `a1b2c3d`) |
| Version range covered | 3.x |
| NOTICE | https://github.com/acmelabs/scheduler/blob/main/NOTICE |

---

## 3. Grant of permission

Subject to continuing compliance with PASVL-1.0 and the conditions in Section 6, the Issuer
grants the Licensee permission to Deploy the Licensed Work within the following scope.

### 3.1 Class

**S** — Standard Commercial

### 3.2 Deployment type

☑ Production — customer facing
☑ Production — internal (supporting the licensed product)

### 3.3 Territory

Worldwide, excluding comprehensively sanctioned territories.

### 3.4 Field of use

> Deployment as the job-scheduling backend of **Northwind Pulse**, the Licensee's customer
> analytics platform, for the Licensee's direct customers. The Work will run as an internal
> service, exposed to end users only through the Licensee's own API. The Licensee may not sell,
> resell, or provide the Work's scheduling functionality as a standalone product or API.

### 3.5 Scale limits

| Measure | Limit |
|---|---|
| End users | 25,000 |
| Named seats | 250 |
| Production instances | 12 |
| Devices distributed | 0 (not permitted) |
| Revenue threshold | Not applicable |

### 3.6 Excluded uses

1. Sublicensing, resale, or Service Bureau Use.
2. Distribution of the Work in binary or source form to customers.
3. Offering the Work's scheduling functionality as a standalone product or API.
4. Machine Learning Use.
5. Deployment outside the Field of Use.

---

## 4. Term

| Field | Value |
|---|---|
| Effective date | 2026-11-01 |
| Start date | 2026-11-01 |
| End date | 2027-10-31 |
| Perpetual | No |
| Renewal | By application, at least 30 days before expiry |
| Review date | 2027-07-31 |

---

## 5. Fees

| Field | Value |
|---|---|
| Fee | USD 18,000 |
| Basis | Annual |
| Payment schedule | 50% on signature, 50% on 2027-04-01 |
| Refund policy | Pro rata refund if the Issuer revokes without cause |
| Late payment | 1.5% per month after 30 days' notice |
| Invoice reference | INV-2026-0417 |

A fee is consideration for the permission granted by this Letter. It is not a sale of the
Licensed Work and does not transfer any ownership interest.

---

## 6. Conditions

| Code | Applied | Notes |
|---|---|---|
| C1 Preserve notices | Yes | In source and in shipped artifacts |
| C2 Display attribution | Yes | "Third-party licenses" page in Northwind Pulse |
| C3 Territory and field | Yes | |
| C4 Scale reporting | Yes | Annual, by 31 January |
| C5 No sublicensing | Yes | |
| C6 Security incident notice | Yes | Within 72 hours to security@acmelabs.example |
| C7 Registry contact current | Yes | |
| C8 Records 3 years | Yes | |
| C9 No hostile IP assertions | Yes | |
| C13 Sub-processor disclosure | Yes | AWS eu-west-1, eu-central-1 |

### 6.1 Bespoke conditions

1. The Licensee must notify the Issuer within 30 days of acquiring an entity that will deploy
   the Work.
2. The Licensee may not use the Work to build a product that directly competes with Acme
   Scheduler as a standalone offering.

---

## 7. Reliance Period

180 days, per PASVL §19.2.

---

## 8. Acknowledgments

The Licensee acknowledges that the Letter grants only the stated permissions; that the Work
remains publicly available under PASVL-1.0; that the Issuer retains all rights not granted; that
the Work is provided "as is"; that the Letter is effective only when recorded in the Registry;
and that revocation requires cause, notice, and a hearing, and is appealable.

---

## 9. Signatures

**Issuer:** R. Chowdhury — PGP detached signature over the record hash
Fingerprint: `9F2A 1C7D 44B8 0E31 D6A5  3C92 7B11 88EE 4D02 6A19`
Date: 2026-10-28

**Licensee:** J. Patel, Head of Engineering
Date: 2026-10-29

---

## 10. Registry record

| Field | Value |
|---|---|
| Recorded by | BSD C Registry Custodian |
| Recorded at | 2026-10-30T09:14:02Z |
| Record hash | `3f9c…` (full SHA-256 in the registry) |
| Previous record hash | `71ab…` |
| Registry entry reference | `LOSDA-ACMELAB-2026-000417` |
| Status | ACTIVE |

> Valid only if the Registry shows status ACTIVE and the hash matches.

---

## Why this example is well drafted

| Choice | Reason |
|---|---|
| Version range `3.x` | Avoids a new LOSDA for every patch, but blocks a surprise major change |
| Scale with headroom | 25,000 users against a current 8,000 avoids a mid-term amendment |
| Excluded uses written out | Prevents the most likely scope dispute |
| Sub-processors disclosed | Satisfies C13 and the Licensee's own procurement obligations |
| Competing-product condition | Protects the Issuer's commercial position without banning a whole market |
| Affiliate named | Prevents "our German subsidiary deployed it" disputes |
| PGP signature | Verifiable against the issuer key register |
| Reliance period stated | Removes ambiguity if the relationship ends |
