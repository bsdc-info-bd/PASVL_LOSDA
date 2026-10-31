# Ethics Policy and Prohibited Uses

**Version:** 1.0
**Binding when:** an Author incorporates this policy by reference into the NOTICE, or a LOSDA
applies condition C14.

Ethics clauses in software licenses are controversial, and for good reasons: they can be vague,
they can make compliance unpredictable, and they can be used to discriminate. This policy is
written to be narrow, specific, reviewable, and appealable. It is modeled on the principle that
an author may refuse to be the tool of serious harm without thereby becoming the arbiter of
everyone else's morality.

## 1. Prohibited uses

An adopter that incorporates this policy must not permit its Work to be used for:

### 1.1 Weapons and targeting

- Autonomous weapons systems that select and engage targets without meaningful human control.
- Targeting systems whose purpose is to locate, identify, or attack persons.
- Development of munitions, chemical, biological, radiological, or nuclear weapons.

### 1.2 Mass surveillance and oppression

- Mass, indiscriminate surveillance of a population, including pervasive biometric
  identification of persons in public spaces.
- Social scoring systems that allocate benefits, penalties, or access to services to persons
  based on unrelated behavior.
- Systems whose primary purpose is to identify, track, or suppress political dissent, religious
  practice, or membership in a protected group.
- Predictive policing that directs enforcement action at individuals based on protected
  characteristics.

### 1.3 Coercion of individuals

- Systems that facilitate human trafficking, forced labor, or sexual exploitation.
- Systems whose purpose is to facilitate coercive control, stalking, or intimate-image abuse.
- Emotion-recognition systems used to make decisions about a person's employment, education,
  access to credit, or liberty.

### 1.4 Discrimination

- Automated decisions that deny access to housing, credit, employment, education, healthcare,
  or public services on the basis of race, ethnicity, religion, sex, gender identity, sexual
  orientation, disability, age, caste, nationality, or political opinion.

### 1.5 Serious illegality

- Fraud, ransomware, or the operation of criminal markets.
- Circumvention of safety systems where the foreseeable result is serious harm.
- Systems whose purpose is to defeat the security of another person's systems, except as
  permitted by Article 8 of the License.

### 1.6 Evasion of accountability

- Deployment designed to escape regulatory oversight or to conceal a prohibited use from
  auditors.

## 2. High-risk uses requiring review

An adopter that incorporates this policy **should** obtain an ethics review, or require the
licensee to obtain one, before permitting a Work to be used in:

| Domain | Examples of use | Review body |
|---|---|---|
| Health | Clinical decision support; diagnostic triage | Local ethics committee |
| Justice | Sentencing support; risk assessment; evidence analysis | Independent board |
| Employment | Hiring, evaluation, dismissal | Independent board |
| Education | Admission, grading, discipline | Institutional review |
| Migration | Visa, asylum, border decisions | Independent board |
| Essential services | Water, power, emergency dispatch | Sector regulator |
| Financial access | Credit, insurance, benefit decisions | Independent board |
| Children | Any product directed to minors | Institutional review |

A review is not a permission. It documents that the risks were considered. The full list of
review requirements is in `governance/ETHICS-REVIEW-BOARD.md`.

## 3. What this policy does not do

- It does not restrict lawful defense forces from using the Work for defensive, logistics,
  medical, or administrative purposes that fall outside Section 1.
- It does not restrict journalism, academic research, security research, or documentation of
  harms.
- It does not restrict the Work's use by a public authority exercising a lawful function that
  is subject to democratic oversight and judicial review.
- It does not require an Author to police a licensee's conduct beyond the express terms.
- It does not create an obligation to monitor users, and authors are not liable for uses they
  did not know of and could not reasonably have known of.

## 4. Enforcement of ethics terms

A credible allegation of a prohibited use follows the enforcement ladder (Stage 1–3), with two
special features:

1. **Urgency.** Where the harm is ongoing and serious, the issuing authority may suspend the
   LOSDA immediately and has five business days to provide the hearing (PASVL §18.10).
2. **Expert review.** The License Council may appoint two independent reviewers with subject
   expertise before a final decision. The reviewers advise; they do not decide.

A license termination for an ethics violation must state the prohibited use, the evidence, and
the reasoning. It must be appealable to the appeals panel.

## 5. Anti-discrimination in licensing

The framework prohibits refusing a LOSDA on the basis of: nationality, ethnicity, religion,
sex, gender identity, sexual orientation, disability, age, caste, political opinion, or
membership of a marginalized group, except where:

- refusal is required by sanctions or export control law;
- the applicant is a restricted party;
- the proposed use is itself prohibited under Section 1.

Refusals must be reasoned and recorded in the Registry as "refused — ground 5 (prohibited
use)" or another numbered ground from the LOSDA specification, Section 14. Aggregate refusal
statistics are published annually.

## 6. Ethics of the framework itself

The Steward commits to:

1. **Do not sell the Registry.** The Registry is not for sale, not for rent, and not for
   preferential listing.
2. **Do not sell precedence.** Fees may not be used to jump the queue except through the
   published expedited process, which is available to all.
3. **Do not sell enforcement outcomes.** No party may pay to avoid or obtain enforcement.
4. **Publish the money.** Annual financial disclosure of Registry operation costs and any
   administrative fees.
5. **No surveillance of the Registry's users.** The Registry does not track readers.
6. **No secret licenses.** No LOSDA may be issued with secret terms that contradict the
   public Register.
7. **No political endorsement.** The framework does not endorse candidates, parties, or
   campaigns, and the BSDC name must not be used in political advertising.

## 7. Reporting an ethics concern

Use [`../templates/VIOLATION-REPORT.md`](../templates/VIOLATION-REPORT.md), marking the report
"Ethics". Reports may be confidential. Retaliation is a Violation (PASVL §13.12).

## 8. Review

This policy is reviewed annually by the License Council with input from the Ethics Review
Board. Amendments follow `governance/AMENDMENT-PROCESS.md`. Any amendment that adds a
prohibited use does not apply retroactively to a LOSDA granted before the amendment unless the
licensee consents, except where the use becomes unlawful.
