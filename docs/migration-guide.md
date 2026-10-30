# Migration Guide

How to move to PASVL-1.0, and how to move away from it. Both directions are legitimate.

---

## Part 1 — Moving to PASVL

### 1.1 From a permissive licence (MIT, BSD, Apache-2.0)

**Can you?** Yes for future versions, if you hold or have permission from the copyright holders.

**What stays?** The old versions remain under the old licence forever.

| Step | Action |
|---|---|
| 1 | Inventory every copyright holder |
| 2 | Check CLAs, DCO records, and employer waivers |
| 3 | Obtain consent from contributors, in writing |
| 4 | Check dependencies for incompatibility |
| 5 | Decide the version at which PASVL starts |
| 6 | Add `LICENSE`, `NOTICE`, headers, README statement |
| 7 | Update package manifests |
| 8 | Tag the last version under the old licence |
| 9 | Announce with a FAQ and a discussion thread |
| 10 | Offer grandfathering terms to existing commercial users |

**Timeline:** allow six to twelve weeks for a mature project.

**Pitfall:** relicensing without consent. It voids the licence for the affected code and can
expose you to contributor claims.

### 1.2 From GPL or AGPL

**Can you?** You can license your own future code under PASVL, but you cannot take GPL code with
you. GPL requires the combined work to remain GPL. You must either:

- rewrite the GPL-derived code;
- isolate it behind a process boundary and confirm that it does not form a single work;
- keep the affected modules under GPL and license only your original modules under PASVL, with a
  clear separation and legal advice.

**Do not** simply change the LICENSE file. That does not change the GPL obligations.

### 1.3 From proprietary

Straightforward. You are adding public visibility to an existing restricted model:

1. Publish the source.
2. Apply PASVL.
3. Convert your proprietary EULA into a LOSDA.
4. Keep your existing customers by issuing them LOSDAs at their current terms.
5. Publish the fee schedule.

### 1.4 From a source-available licence (BUSL, Elastic, PolyForm)

Usually straightforward, but check the old licence's change date and any irrevocable grants:

- BUSL converts to an open licence after its change date; you cannot undo that conversion.
- Elastic-2.0 and PolyForm have their own restrictions; confirm that a new licence does not
  conflict with grants already made.

### 1.5 From no licence

You already have the strongest possible restriction: nobody may do anything. Adding PASVL gives
people real permissions while keeping deployment gated.

---

## Part 2 — Moving away from PASVL

### 2.1 You may migrate away at any time

PASVL does not trap you. For your **own** code you may relicense future versions under any
licence. For **third-party** PASVL code in your project, you must remove or replace it, because
you cannot relicense it.

### 2.2 What survives

- Rights granted for versions already released remain.
- Active LOSDAs remain valid for their term.
- Attribution obligations for code you continue to use remain.

### 2.3 The migration

| Step | Action |
|---|---|
| 1 | Identify every PASVL component in your project |
| 2 | Decide: replace, rewrite, or keep with a LOSDA |
| 3 | If replacing, find or write an alternative |
| 4 | Remove the code and its notices |
| 5 | Update the dependency manifest |
| 6 | Remove the PASVL `LICENSE` if no PASVL code remains |
| 7 | Update the README and the website |
| 8 | Notify licensees of your work |
| 9 | Keep the old releases available under their original terms |

### 2.4 If you are a licensee migrating away

1. Check the Reliance Period (180 days by default).
2. Plan the technical migration within the period.
3. Tell the issuer — a courteous notice costs nothing and usually earns cooperation.
4. Stop using the work by the end of the period.
5. Remove the attribution once the code is removed.

### 2.5 Forking the last open version

If your project was permissively licensed before adopting PASVL, anyone may continue the last
permissive version. That is expected and permitted. Compete on quality, not on resentment.

---

## Part 3 — Version upgrade paths within PASVL

| From | To | What to do |
|---|---|---|
| PASVL-1.0 | PASVL-1.x | No action; clarifications do not change rights |
| PASVL-1.0 | PASVL-2.0 | Review the migration note; existing LOSDAs continue unless the licensee opts in |
| LOSDA-1.0 | LOSDA-1.1 | Records remain valid; new fields are optional |
| LOSDA-1.0 | LOSDA-2.0 | Records must be migrated; the schema provides a converter |

Always read the `CHANGELOG.md` before upgrading.

---

## Part 4 — Checklist

**For authors**

- [ ] Consent obtained from all copyright holders
- [ ] Dependencies checked
- [ ] Old versions preserved under old terms
- [ ] New files added
- [ ] Manifests updated
- [ ] Headers added
- [ ] Website updated
- [ ] Announcement published
- [ ] FAQ written
- [ ] Existing commercial users contacted
- [ ] First LOSDA issued under the new regime

**For deployers**

- [ ] Inventory reviewed
- [ ] LOSDA obtained or evaluation use confirmed
- [ ] Attribution implemented
- [ ] Scope recorded
- [ ] Incident contact added
- [ ] Renewal scheduled

---

## Part 5 — Getting help

- Migration questions: open a discussion in the framework repository.
- Licence-compatibility questions: [`../legal/compatibility.md`](../legal/compatibility.md).
- Community guidance: [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
