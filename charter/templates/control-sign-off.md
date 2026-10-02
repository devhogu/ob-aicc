```yaml
id: AICC-TPL-03-EN
title: Control Sign-Off
status: active
revision: 2.3
created: 2026-10-01
revised: 2026-10-02
```

# Control Sign-Off

**Template.** The decision of a Control Function Contact: a validation, a stop, a provider check, an Exception, or the clearance of a business case, with one sign-off for each Contact where a validation involves several. It carries no figures of the Bank, no data, and no code.

| Field | Entry |
| --- | --- |
| Identifier | SGN-[nnn] |
| Type | [validation / stop / provider check / Exception / business case clearance] |
| Subject | [SOL-nnn, INI-nnn for a business case, or the provider] |
| Scope | [what the decision covers] |
| Control Function and Contact | [function, name] |
| Risk Tier confirmed | [Tier 1, 2, or 3, as assigned, or as expected in a business case; or a different Tier, with the reason (AI Policy 3.2); and whether the high-risk category was asked about] |
| Decision | [validated / validated with conditions / stopped / Exception granted / refused / cleared / not cleared / Risk Tier raised] |
| Date | [date] |
| Valid until | [date, or the change that requires a new decision; for an Exception, its expiry date (AI Policy 6.1)] |
| Risks and Issues entry | [RI-nnn, for an Exception] |
| Conditions, and what it shall not be used for | [each condition with its owner and date] |
| Based on | [references] |
