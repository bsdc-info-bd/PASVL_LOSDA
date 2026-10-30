# Why This Exists

## The problem

Two models dominate software licensing.

**Model one: permissive open source.** Publish under MIT or Apache-2.0. Anyone may read, use,
modify, and deploy — including large companies that build billion-dollar services on your work
without paying you or even telling you. It produces enormous public value and almost no
sustainable funding for the people who create it. Maintainers burn out, projects are abandoned,
security holes go unpatched, and the companies that depend on them contribute back at a rate
that would embarrass almost any other industry.

**Model two: closed source.** Keep everything private. You can sell licences, but nobody can
audit you, nobody can fix your bugs, nobody can learn from your craft, and buyers are asked to
trust a black box with their data, their money, and sometimes their safety.

Both models force a trade that many authors do not want to make: **surrender the commercial
value of your work, or surrender its transparency.**

## The observation

The two things being traded are not actually the same thing.

- **Visibility** is the ability to read, study, audit, teach, and improve. It costs the author
  almost nothing and creates enormous public value.
- **Deployment** is the ability to run the software for real — to serve customers, to operate
  infrastructure, to ship devices. It is where most of the commercial value is captured.

Open-source licences bundle these together. Proprietary licences withhold both. Almost nobody
separates them.

## The proposal

Separate them.

- Give **visibility** to everyone, permanently, unconditionally, free.
- Reserve **deployment**, and grant it individually, in writing, with scope, term, and public
  record.

That is what PASVL and the LOSDA do. The licence is the public instrument. The letter is the
private permission. The registry is the memory that makes the permission verifiable.

## Why a letter, and not a click-through

Because permission to run software in the world is a serious thing and should look like one.

A click-through is forgettable, unverifiable, and unauditable. A letter has:

- an identity and a number;
- a scope that can be read by a lawyer, an auditor, or a procurement officer;
- a signature and a hash;
- a public record that a third party can check without asking the licensee;
- a term, a revocation path, and an appeal route.

A procurement team can put a LOSDA in a contract file. They cannot do that with a checkbox.

## Why BSD C

The framework needed a steward with three properties: independence from any single vendor,
familiarity with the realities of software development outside the wealthy world, and a
commitment to publishing the rules rather than owning them.

The Bangladesh Software Development Community is a community organisation. It does not own the
licence; it publishes it. The licence is free for anyone to adopt, and its text is in this
repository for anyone to read, criticise, and improve through the RFC process.

The choice of Bangladesh as the default governing law is deliberate: it names a real
jurisdiction, it is not the default of any large technology company, and it signals that this
framework is intended for the whole world, not only for the places that already write the rules.

## What this is not

It is **not** an attempt to make open source obsolete. Open source will remain the right choice
for standards, infrastructure, libraries, and any project whose value comes from ubiquity.
PASVL is for a different case: software with real commercial value whose author wants it public
anyway.

It is **not** a way to trap users. There are no-fee classes for academia, government, research,
and public interest. There is a wind-down period. There is an appeals process. Rights cannot be
tightened retroactively. The framework is designed so that a reasonable person can comply
without a lawyer.

It is **not** a claim that this is easy. Enforcement is hard, adoption is slower, and some
communities will reject it on principle. The framework says so in the open, in
[`../legal/platform-reality.md`](../legal/platform-reality.md) and
[`../legal/risk-register.md`](../legal/risk-register.md).

## The bet

The bet is that a significant number of developers, companies, and institutions will pay a fair
price for permission to deploy software they can fully inspect — and that many more will be glad
the source is public even though they never deploy it.

If that bet is right, there is a new space between open and closed: **public, auditable, and
properly paid for.** If it is wrong, the framework will fail honestly, and the text will remain
in this repository for someone else to learn from.

## What you can do

- **As an author:** adopt it for a project where control matters, and see whether it works for
  you.
- **As a deployer:** ask for permission rather than assuming it. The process is short, and the
  authors deserve it.
- **As a critic:** say what is wrong with it. Open an RFC. The framework is designed to survive
  criticism, but not to ignore it.
- **As a translator:** help make it readable in more languages.
- **As a steward's peer:** hold BSD C to the standards in `GOVERNANCE.md`.

## A closing thought

Every licensing era began with someone refusing to accept the terms of the previous one. The
GPL began as a refusal of proprietary control. The Apache licence began as a refusal of
permissive chaos in a foundation. The Commons Clause and the Business Source Licence began as
refusals of cloud free-riding.

This framework begins as a refusal of a different trade-off: that public code must be free to
run, or that private code must be impossible to trust.

**See the source. Ask to deploy. Get it in writing.**

That is the era this repository is trying to start.
