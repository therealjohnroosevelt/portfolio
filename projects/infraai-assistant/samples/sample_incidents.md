# Sample Incidents

## 1. Entra ID Conditional Access failure
```
User reports they cannot sign in from a new location.
Azure AD sign-in logs show error AADSTS50076.
Conditional Access policy "Require MFA for all users" is enabled.
```

## 2. AWS EC2 instance unreachable
```
EC2 instance i-0abc123 in us-east-1 stopped responding.
Status checks: System reachability failed.
Security group allows 443 from 0.0.0.0/0.
No recent changes to the instance.
```

## 3. Windows Server high CPU
```
Windows Server 2022 domain controller showing 95% CPU.
Process: lsass.exe consuming majority of CPU.
Event logs show repeated Kerberos authentication failures.
```
