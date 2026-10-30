# Dissolution and Succession

**Version:** 1.0

## 1. Why this document exists

Frameworks die when their stewards do — and when they die badly, thousands of deployments are
left without a registry, a verification route, or an authority to issue permissions. That is an
unacceptable failure mode. This document plans for it in advance.

## 2. What survives dissolution

The following survive any dissolution, transfer, or insolvency of the Steward, and cannot be
withdrawn:

1. the rights granted to the public under Article 3 of the Licence, in respect of works already
   released;
2. the rights granted under an active or perpetual LOSDA for its stated term;
3. the obligation of any party to comply with the Licence for works they already received;
4. the public's right to read, study, audit, and fork.

A dissolved steward cannot revoke a licence that has already been granted. Dissolution is not a
ground for revocation under PASVL §18.7.

## 3. Succession triggers

1. A Council resolution to transfer stewardship.
2. Insolvency, winding-up, or loss of legal capacity.
3. Failure to hold a Council meeting for 12 months.
4. Failure to appoint a Registry Custodian for 90 days.
5. A court order.

## 4. The successor

The successor must be an entity that:

- is willing and able to maintain the Registry and publish a verification route;
- accepts the Charter's duties, including non-discrimination and transparency;
- does not have a conflicting commercial interest that would compromise neutrality;
- is endorsed by at least two-thirds of the whole Council, or by the Authors' Assembly if the
  Council cannot act.

The Council maintains a **named standby successor** at all times and reviews it annually.

## 5. Transfer package

On succession, the outgoing steward must transfer:

1. the canonical Registry and its full history;
2. the issuer, key, and works registers;
3. the Enforcement Register;
4. the trademarks, or a licence to use them;
5. the domain names and verification URLs;
6. this repository, including all versions and tags;
7. the escrow copy and the Merkle root archive;
8. all contracts that relate to Registry operation.

The transfer must be public and must be recorded in the Registry itself.

## 6. Succession procedure

| Step | Action | Deadline |
|---|---|---|
| 1 | Council declares the trigger and publishes notice | 5 business days |
| 2 | Outgoing steward publishes a handover notice | 10 business days |
| 3 | Successor is confirmed and announced | 30 business days |
| 4 | Transfer package delivered | 45 business days |
| 5 | Successor confirms Registry integrity against Merkle roots | 10 business days after delivery |
| 6 | Public notice of transition in the Repository and Registry | Immediately after confirmation |

## 7. If no successor can be found

1. The Council must appoint a **trustee** — an established non-profit, university, or standards
   body — to hold the Registry in escrow and publish it read-only.
2. Existing LOSDAs remain valid for their stated terms.
3. **No new LOSDAs may be issued** by the trustee except Continuity LOSDAs, and only where an
   essential service would otherwise fail.
4. The Licence continues to govern existing works. It cannot be amended by a trustee.
5. The Registry is published as a static archive, with the Merkle roots, and permanently
   mirrored.

## 8. Escrow

1. A read-only copy of the Registry is escrowed with a third party at least quarterly.
2. The escrow agreement must permit release to the successor, the trustee, or a court.
3. The escrow agent publishes a quarterly confirmation that the copy is current.

## 9. Works and authors after dissolution

Authors keep all rights in their works and may continue to license them independently. They
may:

- continue issuing LOSDAs directly and publish them in their own repositories;
- adopt a different licence for future versions, subject to §19.5 of the Licence;
- participate in any successor framework.

The dissolution of the Steward does not terminate an author's obligations to existing licensees
for the stated term.

## 10. Records retention after dissolution

The Registry, the Enforcement Register, and the decision register must be preserved
permanently, either by the successor or by the trustee, and made publicly readable.

## 11. Audit of the final state

Before completion, an independent auditor must verify:

1. that the Registry is complete and matches the Merkle roots;
2. that no record has been deleted;
3. that the transfer package is complete;
4. that all keys are accounted for and either transferred or revoked.

The audit report is published.

## 12. Rebirth

A successor framework may be established under the same or a new name. It may not claim to be
the original Steward, and it must state clearly what it inherited and what it did not.
