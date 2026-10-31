# The Registry Custodian

**Version:** 1.0 · **Appointed by:** the License Council · **Reports to:** the License Council

## 1. Role

The Registry Custodian is the framework's registrar. The Custodian does not decide who may
deploy; the Author does. The Custodian makes sure the world can tell whether a deployment is
permitted, right now, from a public record that cannot be quietly rewritten.

## 2. Duties

1. Record every LOSDA received from an authorized issuer within 2 business days.
2. Maintain status: expiry, suspension, revocation, supersession, withdrawal.
3. Compute and publish record hashes and the monthly Merkle root.
4. Maintain the issuer register and the public key register.
5. Process corrections and Registry disputes.
6. Publish the Enforcement Register entries supplied by enforcement authorities.
7. Operate the anonymized-listing process under the privacy policy.
8. Run quarterly access reviews and the biennial independent audit.
9. Maintain mirrors and the escrow copy.
10. Report quarterly to the License Council.

## 3. Powers

1. Refuse to record an instrument that does not meet the schema or that appears fraudulent.
2. Suspend a record pending verification (maximum 10 business days) and record the suspension.
3. Require an issuer to re-sign or clarify a defective instrument.
4. Remove confidentiality markings that conceal a term required to be public.
5. Escalate suspected fraud to the Steward and, where appropriate, to authorities.

## 4. Limits

The Custodian must not:

1. invent, alter, or delete a LOSDA;
2. change a status without a signed decision from an authorized person;
3. publish confidential annexes;
4. accept payment from a licensee to change a status;
5. disclose applicant data except as permitted;
6. act as an issuing authority for any class other than those the License allows.

## 5. Independence and conflicts

1. The Custodian may not be an employee of a major licensee.
2. The Custodian declares any relationship with an issuer or licensee.
3. Where the Custodian has a conflict, a deputy Custodian handles the matter.
4. The Custodian's decisions are appealable to the Appeals Panel.

## 6. Access control

| Control | Requirement |
|---|---|
| Authentication | Two-factor mandatory |
| Commits | Signed and reviewed by a second Custodian |
| Write access | Named individuals only; no shared accounts |
| Sessions | Re-authentication for status changes |
| Logs | Immutable, retained 7 years |
| Review | Quarterly access review; exit within 24 hours |

## 7. Service targets

| Action | Target | Consequence of breach |
|---|---|---|
| Record a LOSDA | 2 business days | Escalation to Council after 5 days |
| Reflect a revocation | 1 business day | Urgent review |
| Correct an error | 5 business days | Public notice and compensation of costs |
| Answer a Registry dispute | 10 business days | Appeal may proceed without the response |
| Publish Merkle root | Monthly, by the 5th | Annual audit finding |

## 8. Record integrity

1. The canonical repository is under signed tags.
2. A mirror is maintained at a second host.
3. A read-only escrow copy is held by a third party.
4. Merkle roots are published in the repository and in the annual report.
5. Any divergence between the canonical and mirror copy is a reportable incident.

## 9. Keys

1. The Custodian maintains a register of issuer public keys.
2. A key revocation requires the issuer's notification and a Custodian record.
3. Compromised keys are published as revoked within 24 hours of notice.
4. Records signed with a revoked key remain valid only if signed before the revocation date and
   the issuer confirms.

## 10. Anonymized listing

The Custodian decides anonymization requests under the privacy policy. The decision must:

1. be in writing, with reasons;
2. be recorded without the personal data;
3. be appealable to the Appeals Panel;
4. be reviewed annually for continued necessity.

## 11. Liability

The Custodian acts as a record-keeper. The Custodian is not liable for a deployment made in
reliance on a record that was accurate at the time, except in cases of the Custodian's own fraud
or gross negligence, and subject to the liability limits of the License.

## 12. Removal

The Custodian may be removed by the License Council for cause, after a hearing, with a
two-thirds majority. Removal requires a documented handover, key rotation, and a public notice
within 5 business days.

## 13. Deputies

At least two deputies must be named. A deputy acts whenever the Custodian is unavailable for
more than two business days, and in every conflicted matter.
