```yaml
id: AICC-TPL-03-EN
title: Control Sign-Off
status: active
revision: 2.0
created: 2026-10-01
revised: 2026-10-01
```

# Control Sign-Off

**Template.** The decision of a Control Function Contact: a validation, a stop, a provider check, or an Exception. It is a simple sign-off: the
decision, its date, and its scope. It carries no figures of the Bank, no data, and no code.

| Field | Entry |
| --- | --- |
| Type | [validation / stop / provider check / Exception] |
| Subject | [SOL-nnn, or the provider] |
| Scope | [what the decision covers] |
| Control Function and Contact | [function, name] |
| Decision | [validated / validated with conditions / stopped / Exception granted / refused] |
| Date | [date] |
| Valid until, or revalidate on | [date, or the change that requires it] |

## Limits and conditions

[What the subject shall not be used for, for example no output on an individual application. Any change to these limits needs a new
decision. Conditions, with owner and date.]

## For an Exception

[The expiry date and the compensating control.]

## Evidence reviewed

[References only.]
